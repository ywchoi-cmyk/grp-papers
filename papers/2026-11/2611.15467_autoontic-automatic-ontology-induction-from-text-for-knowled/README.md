# AutoOntic: Automatic Ontology Induction from Text for Knowledge Graph Construction

- arXiv: https://arxiv.org/abs/2611.15467  (v1, submitted 2026-11-11, updated 2026-11-11)
- Authors: Alla Chepurova, Aydar Bulatov, Mikhail Burtsev, Yuri Kuratov
- Categories: cs.CL, cs.AI, cs.LG
- Collected: 2026-11-16 (KST)

## Abstract

Graph-based retrieval-augmented generation depends on the quality of the knowledge graph (KG) it retrieves over, yet schema-free LLM-based extraction pipelines typically produce flat graphs: deduplicated entities and relations with no type hierarchy and no domain/range constraints. We present AutoOntic, a pipeline that automatically constructs an ontology from text by canonicalizing open-vocabulary entity types and relations, inducing a hierarchy over the canonicalized types, and mining relation-level domain and range constraints. Its hierarchy induction procedure prioritizes types using corpus-derived relation-argument profiles and places them through local, LLM-adjudicated parent/child checks, allowing newly inserted types to trigger reassignment of existing parent-child links. The resulting hierarchy constrains entity deduplication and supports the induction of relation-level domain/range constraints. For intrinsic evaluation, we introduce a reference-based protocol that classifies induced ontology types as exact, broader, narrower, or unrelated to reference domain and range classes. On the Wikidata-TekGen and DBpedia-WebNLG subsets of Text2KGBench, over 90% of AutoOntic's induced endpoint types are semantically aligned with the reference classes across two LLM backbones: about half match exactly, while most remaining differences concern granularity. On MINE, knowledge graphs organized using an ontology built by AutoOntic achieve 88% retrieval accuracy. AutoOntic is available at https://github.com/screemix/AutoOntic.

## Figure 1

![Figure 1](fig1.png)

Figure 1: The AutoOntic pipeline. A schema-free LLM extractor (§2.1) produces a collection G of raw triplets g = (s, ts, r, o, to, Q). Their relation and type labels are canonicalized into a relation vocabulary R∗(§2.2) and a type vocabulary T ∗(§2.3) organized into a single- parent is-a hierarchy H∗(§2.4). Entity mentions are then deduplicated using that hierarchy as a symbolic gate (§2.5), and domain/range constraints are mined by re-resolving G against R∗, T ∗, and H∗(§2.6). Colored dashed arrows mark additional direct inputs beyond the sequential chain.
