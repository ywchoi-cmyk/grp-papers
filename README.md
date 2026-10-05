# grp-papers

온톨로지 · 지식그래프 분야 arXiv 논문 팔로업 저장소.

- `papers/YYYY-MM/<arxivID>_<slug>/README.md` — 제목, 저자, 링크, abstract
- `papers/YYYY-MM/<arxivID>_<slug>/fig1.png` — 논문의 Figure 1
- `index.md` — 수집 목록 (최신순)

## 수집 방식

`.github/workflows/collect.yml`이 평일 06:30 KST에 `scripts/collect_papers.py`를 실행한다.
arXiv API(cs.AI / cs.CL / cs.DB / cs.IR / cs.LG)에서 최근 3일(월요일은 4일)에 제출·갱신된
온톨로지·지식그래프 논문을 찾아 저장하고, 이미 있는 arXiv ID는 건너뛴다.

백필 또는 수동 실행: Actions 탭 → *Collect KG/Ontology papers* → **Run workflow** → `days` 입력 (예: 14).

로컬 실행: `pip install pymupdf && python scripts/collect_papers.py --days 14`
