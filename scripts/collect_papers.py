#!/usr/bin/env python3
"""Collect recent ontology / knowledge-graph papers from arXiv into papers/.

Usage: collect_papers.py [--days N] [--max N] [--dry-run]
"""
import argparse
import datetime as dt
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
INDEX = ROOT / "index.md"
API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}
KST = dt.timezone(dt.timedelta(hours=9))

CATS = "(cat:cs.AI OR cat:cs.CL OR cat:cs.DB OR cat:cs.IR OR cat:cs.LG)"
QUERIES = [
    'abs:"knowledge graph"',
    "ti:ontology",
    'abs:"ontology learning"',
    'abs:"ontology engineering"',
    "abs:GraphRAG",
    'abs:"knowledge graph completion"',
    'abs:"entity alignment"',
    "abs:KGQA",
    'abs:"knowledge graph question answering"',
    "abs:SPARQL",
    'abs:"RDF graph"',
    'abs:"semantic web"',
    'abs:"knowledge base construction"',
    'abs:"temporal knowledge graph"',
    'abs:"knowledge graph embedding"',
    'abs:"text-to-cypher"',
    'abs:"text-to-SPARQL"',
    'abs:"OWL ontology"',
    'abs:"knowledge graph construction"',
]

# Strong signals that the paper is actually about KG / ontology (not a passing mention)
CORE = re.compile(
    r"knowledge[- ]graph|ontolog|graphrag|sparql|\browl\b|\brdf\b|semantic web|"
    r"entity alignment|link prediction|knowledge base|kgqa|cypher|triple store|"
    r"knowledge graph embedding|taxonom",
    re.I,
)
EXCLUDE = re.compile(r"gene ontology|\bGO terms?\b", re.I)


def fetch(url, retries=4, binary=False):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "grp-papers-collector/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            return data if binary else data.decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(3 * (i + 1))
    raise RuntimeError(f"fetch failed: {url}: {last}")


def search(query, cutoff, max_results=100):
    q = urllib.parse.quote(f"({query}) AND {CATS}")
    url = f"{API}?search_query={q}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={max_results}"
    root = ET.fromstring(fetch(url))
    out = []
    for e in root.findall("a:entry", NS):
        aid_full = e.find("a:id", NS).text.rsplit("/", 1)[-1]
        aid = re.sub(r"v\d+$", "", aid_full)
        published = dt.datetime.fromisoformat(e.find("a:published", NS).text.replace("Z", "+00:00"))
        updated = dt.datetime.fromisoformat(e.find("a:updated", NS).text.replace("Z", "+00:00"))
        if published < cutoff and updated < cutoff:
            break
        out.append(
            {
                "id": aid,
                "version": aid_full,
                "title": " ".join(e.find("a:title", NS).text.split()),
                "summary": " ".join(e.find("a:summary", NS).text.split()),
                "authors": [a.find("a:name", NS).text for a in e.findall("a:author", NS)],
                "categories": [c.get("term") for c in e.findall("a:category", NS)],
                "published": published,
                "updated": updated,
            }
        )
    return out


def relevance(p):
    text = f"{p['title']} {p['summary']}"
    if EXCLUDE.search(text) and not re.search(r"knowledge graph", text, re.I):
        return 0
    title_hits = len(CORE.findall(p["title"]))
    abs_hits = len(CORE.findall(p["summary"]))
    return title_hits * 3 + abs_hits


def existing_ids():
    ids = set()
    if PAPERS.exists():
        for d in PAPERS.glob("*/*"):
            m = re.match(r"(\d{4}\.\d{4,5})_", d.name)
            if m:
                ids.add(m.group(1))
    if INDEX.exists():
        ids.update(re.findall(r"\|\s*(\d{4}\.\d{4,5})\s*\|", INDEX.read_text()))
    return ids


def slugify(title, n=60):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:n].rstrip("-")


def find_caption(page):
    """Return bbox of the 'Figure 1' / 'Fig. 1' caption block on this page, or None."""
    for b in page.get_text("blocks"):
        txt = b[4].strip()
        if re.match(r"^(Figure|Fig\.?)\s*1\b[:.\s]", txt, re.I):
            return pymupdf.Rect(b[:4]), txt
    return None


def extract_fig1(pdf_bytes, out_path):
    """Save Figure 1 as PNG. Returns (ok, caption)."""
    doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
    cap_text = ""
    for pno in range(min(5, len(doc))):
        page = doc[pno]
        hit = find_caption(page)
        if not hit:
            continue
        cap, cap_text = hit
        pw, ph = page.rect.width, page.rect.height
        # Candidate region: everything above the caption, within the caption's column span
        region = pymupdf.Rect(cap.x0 - 10, max(0, cap.y0 - ph * 0.55), cap.x1 + 10, cap.y0 - 2)
        # Prefer the union of image / drawing blocks that sit inside the region
        boxes = []
        for info in page.get_image_info():
            r = pymupdf.Rect(info["bbox"])
            if r.intersects(region) and r.height > 20 and r.width > 20:
                boxes.append(r)
        for d in page.get_drawings():
            r = d.get("rect")
            if r and r.intersects(region) and r.height > 5 and r.width > 5:
                boxes.append(r)
        if boxes:
            clip = boxes[0]
            for r in boxes[1:]:
                clip |= r
            clip = clip & pymupdf.Rect(0, 0, pw, cap.y0)
            # Trim obvious text lines that crept in above the figure
            if clip.height < 30 or clip.width < 30:
                clip = region
        else:
            clip = region
        clip = clip & page.rect
        pix = page.get_pixmap(dpi=200, clip=clip)
        pix.save(out_path)
        return True, cap_text
    # Fallback: largest embedded image on the first two pages
    best = None
    for pno in range(min(2, len(doc))):
        for info in doc[pno].get_image_info(xrefs=True):
            r = pymupdf.Rect(info["bbox"])
            if best is None or r.get_area() > best[1].get_area():
                best = (pno, r)
    if best and best[1].get_area() > 5000:
        doc[best[0]].get_pixmap(dpi=200, clip=best[1]).save(out_path)
        return True, ""
    return False, ""


def write_paper(p, now_kst, dry):
    month = p["published"].strftime("%Y-%m")
    folder = PAPERS / month / f"{p['id']}_{slugify(p['title'])}"
    if dry:
        print(f"[dry] {folder.relative_to(ROOT)}")
        return folder, False
    folder.mkdir(parents=True, exist_ok=True)
    fig_ok, caption = False, ""
    try:
        pdf = fetch(f"https://arxiv.org/pdf/{p['version']}", binary=True)
        fig_ok, caption = extract_fig1(pdf, str(folder / "fig1.png"))
    except Exception as e:  # noqa: BLE001
        print(f"  fig1 failed for {p['id']}: {e}", file=sys.stderr)
    fig_section = "![Figure 1](fig1.png)\n" + (f"\n{caption}\n" if caption else "") if fig_ok \
        else "Figure 1: 추출 실패 (PDF 참조)\n"
    readme = (
        f"# {p['title']}\n\n"
        f"- arXiv: https://arxiv.org/abs/{p['id']}  ({p['version'][len(p['id']):] or 'v1'}, "
        f"submitted {p['published'].strftime('%Y-%m-%d')}, updated {p['updated'].strftime('%Y-%m-%d')})\n"
        f"- Authors: {', '.join(p['authors'])}\n"
        f"- Categories: {', '.join(p['categories'])}\n"
        f"- Collected: {now_kst.strftime('%Y-%m-%d')} (KST)\n\n"
        f"## Abstract\n\n{p['summary']}\n\n"
        f"## Figure 1\n\n{fig_section}"
    )
    (folder / "README.md").write_text(readme, encoding="utf-8")
    return folder, fig_ok


def update_index(rows):
    header = "# Ontology / Knowledge Graph Papers\n\n| Collected | arXiv ID | Title | Categories | Folder |\n|---|---|---|---|---|\n"
    body = ""
    if INDEX.exists():
        old = INDEX.read_text(encoding="utf-8")
        body = old.split("|---|---|---|---|---|\n", 1)[1] if "|---|---|---|---|---|\n" in old else ""
    INDEX.write_text(header + "".join(rows) + body, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=3)
    ap.add_argument("--max", type=int, default=15)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    now = dt.datetime.now(dt.timezone.utc)
    now_kst = now.astimezone(KST)
    cutoff = now - dt.timedelta(days=args.days)
    known = existing_ids()

    cands = {}
    for q in QUERIES:
        try:
            hits = search(q, cutoff)
            for p in hits:
                cands.setdefault(p["id"], p)
            print(f"query ok: {q}: {len(hits)} within window")
        except Exception as e:  # noqa: BLE001
            print(f"query failed: {q}: {e}", file=sys.stderr)
        time.sleep(3)  # arXiv API etiquette

    skipped = [p for p in cands.values() if p["id"] in known]
    fresh = [p for p in cands.values() if p["id"] not in known]
    scored = [(relevance(p), p) for p in fresh]
    scored = [(s, p) for s, p in scored if s >= 2]
    scored.sort(key=lambda t: (-t[0], -t[1]["published"].timestamp()))
    picked = [p for _, p in scored[: args.max]]
    print(f"candidates={len(cands)} known={len(skipped)} relevant_new={len(scored)} picked={len(picked)}")

    rows, summary = [], []
    for p in sorted(picked, key=lambda p: p["published"], reverse=True):
        folder, fig_ok = write_paper(p, now_kst, args.dry_run)
        rel = folder.relative_to(ROOT).as_posix()
        rows.append(
            f"| {now_kst.strftime('%Y-%m-%d')} | {p['id']} | {p['title'].replace('|', '/')} | "
            f"{', '.join(p['categories'][:3])} | [{folder.name}]({rel}) |\n"
        )
        summary.append({"id": p["id"], "title": p["title"], "fig1": fig_ok, "folder": rel})
        print(f"  + {p['id']} {'[fig1]' if fig_ok else '[no fig1]'} {p['title']}")
    if rows and not args.dry_run:
        update_index(rows)
    (ROOT / ".last_run.json").write_text(
        json.dumps({"date": now_kst.strftime("%Y-%m-%d"), "added": summary, "skipped": len(skipped)}, ensure_ascii=False, indent=1)
    )


if __name__ == "__main__":
    main()
