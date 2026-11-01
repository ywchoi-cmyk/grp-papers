# Beyond Similarity Search: Knowledge Graph Metadata Enrichment for Enterprise Retrieval-Augmented Generation

- arXiv: https://arxiv.org/abs/2610.37728  (v1, submitted 2026-10-27, updated 2026-10-27)
- Authors: Fakabbir Amin
- Categories: cs.IR, cs.AI, cs.LG
- Collected: 2026-11-02 (KST)

## Abstract

A key challenge of RAG systems is retrieving information from enterprise documents created by multiple teams over time, where it is not possible to enrich the information using the latest information and metadata available outside the scope of organizational documentation responsibility. We investigated whether using a knowledge graph to store metadata and frequently changing information would improve upon knowledge retrieval over similarity search over embeddings. To perform the experiment, we created a snapshot of the SEC EDGAR dataset for a quarter, comprising 167,050 filings from 10,511 companies and 508,714 embedded chunks of risk-factor text. To simulate the enrichment, we created a knowledge graph of 430,257 nodes and 561,144 edges carrying an accession number on every edge. To evaluate the gain obtained via a graph-based design, we evaluated three architectures: text-to-SQL over typed columns, dense-vector RAG with HNSW cosine search, and a two-stage GraphRAG design. All architectures share the same model and temperature to allow comparison. Results are scored programmatically by an LLM as judge over 20 questions divided across four categories, each question asked three times. GraphRAG solved 16 of 20 questions on all three attempts, compared to 10 for text-to-SQL and 3 for vector RAG. GraphRAG lost on structured aggregation queries. Vector RAG lost the single-document category it was expected to win, passing 3 of 15 where GraphRAG passed 15 of 15, because company attribution is not recoverable from cosine similarity at this scale. All six confident falsehoods in the benchmark were text-to-SQL conflating distinct people who share a surname, the failure that resolving identity to an identifier before reading any text prevents structurally; GraphRAG made none. We claim no advantage beyond this corpus, this model and this question set.

## Figure 1

![Figure 1](fig1.png)

Figure 1: The three facts a multi-hop question needs live in three different containers. Item 1A is narrative prose and is the only section embedded; EX-21 is a structured list attached to the same filing; insider roles are in a separate filing type entirely. Every projected edge carries the accession number of the filing that asserts it.
