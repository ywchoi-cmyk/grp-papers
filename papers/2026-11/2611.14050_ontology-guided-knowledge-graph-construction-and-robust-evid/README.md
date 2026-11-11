# Ontology-Guided Knowledge Graph Construction and Robust Evidence Retrieval for Indian Knowledge Systems

- arXiv: https://arxiv.org/abs/2611.14050  (v1, submitted 2026-11-10, updated 2026-11-10)
- Authors: Anand Kaniyaar Sriranga Prasad, Avinash Holenarasipur Nagendra, Mohan Raghavan
- Categories: cs.IR
- Collected: 2026-11-12 (KST)

## Abstract

Retrieving evidence from Indian Knowledge Systems is complicated by transliteration variants, ambiguous names, and relations distributed across passages. We present an ontology-guided knowledge graph (KG) pipeline that links typed entities and relations extracted with Qwen3-32B to original textual evidence. Retrieval combines sense-aware grounding, bounded graph traversal, lexical anchors, relationship-vector search, and passage reranking. We evaluate KG alone, single-vector retrieval (SV), and KG unions with SV and Entity Notes on 320 questions from Dhara Bench, matching the per-question candidate count across internal systems under BGE and Qwen rerankers. Standalone KG has the highest Precision@5 under both rerankers and the highest MRR@20 in Counting, Composite, and Multi-hop among the evaluated internal configurations. With Qwen, KG achieves Multi-hop MRR@20 of 0.8722, compared with 0.7622 for the fully reranked KG + SV union. The KG + SV + Entity Notes union instead provides the highest overall Recall@20 (0.5134), compared with 0.4347 for KG. On the 15 Multi-hop questions, Qwen KG achieves complete-evidence MRR@20 of 0.4651 versus 0.3372 for SV, while both full unions complete ten questions within twenty results compared with nine for KG. Gemini 3.7 Flash, evaluated through manually reviewed source mappings, re mains stronger on overall MRR and nDCG, while internal systems have category-specific advantages. All comparisons are descriptive. A separate deployment timing study measures mean retrieval times of 20.374 s for KG and 0.646 s for SV. The findings support selecting KG or its unions according to the required balance of early relevance, evidence completeness, and retrieval cost.

## Figure 1

![Figure 1](fig1.png)

Fig. 1. Construction and retrieval pipeline used by the recorded Qwen3-32B generation and KG retrieval runs. Ontologies condition extraction; graph-derived evidence is projected to original corpus chunks before reranking. External SV and mapped EN candidates are combined with KG candidates only in the union configurations; KG-alone uses only graph-derived candidates.
