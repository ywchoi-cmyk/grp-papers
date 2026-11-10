# Lightfoot: Graph Retrieval-Augmented Generation with Exact, Model-Free Document Deletion

- arXiv: https://arxiv.org/abs/2611.11010  (v1, submitted 2026-11-07, updated 2026-11-07)
- Authors: Uday Allu
- Categories: cs.AI, cs.CL, cs.IR
- Collected: 2026-11-11 (KST)

## Abstract

Graph-based retrieval-augmented generation (GraphRAG) improves multi-hop question answering, but deployed systems face two costs that research comparisons rarely measure: building the graph, and removing documents from it. We present Lightfoot, a GraphRAG system in which every entity, link, fact and synonym edge is a deterministic function of per-passage extractions carrying chunk-level provenance. Indexing makes one language-model call per passage, retrieval makes none, and deleting a document is a database operation with no model calls. On the full 11,402-passage MuSiQue corpus we verify that, after deleting 10% of the documents, the graph is identical to a fresh index of the surviving documents. We compare Lightfoot with HippoRAG 2, LightRAG and fast-graphrag under identical extraction, answer and embedding models on MuSiQue, 2WikiMultiHopQA and HotpotQA. Lightfoot builds the cheapest index on all three datasets, 26-31% below HippoRAG 2 and 3-6x below LightRAG and fast-graphrag. Against HippoRAG 2 it is significantly better on MuSiQue retrieval (+2.8 points recall@5 and +4.3 recall@10 on a held-out split) and on HotpotQA answers (+7.7 points exact match), and significantly worse on 2WikiMultiHopQA (-3.9 recall@2, -8.4 F1). Deleting the same documents took LightRAG 2,187 model calls and 3.7 hours; fast-graphrag has no deletion path. Code and per-question results: https://github.com/udayallu-ml/Lightfoot-GraphRAG

## Figure 1

![Figure 1](fig1.png)

Figure 1: Recall@5 against normalised index cost for each dataset. Points nearer the top left are better.
