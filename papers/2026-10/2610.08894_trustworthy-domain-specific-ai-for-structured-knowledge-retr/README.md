# Trustworthy Domain-Specific AI for Structured Knowledge Retrieval and Reasoning

- arXiv: https://arxiv.org/abs/2610.08894  (v1, submitted 2026-10-06, updated 2026-10-06)
- Authors: Ryan C. Barron
- Categories: cs.IR, cs.AI
- Collected: 2026-10-09 (KST)

## Abstract

This dissertation presents a scalable architecture for transforming unstructured, domain-specific text into structured knowledge for retrieval and reasoning. It integrates semi-automatic corpus curation, semantic structuring, retrieval, and inference into an interpretable pipeline. The research introduces Binary Bleed, an adapted binary search method that reduces low-rank search complexity for Non-negative Matrix Factorization (NMF), and Hierarchical NMF with automatic latent feature selection (HNMFk), a depth-adaptive topic modeling method that produces interpretable taxonomies guided by subject matter experts. These representations populate a typed Knowledge Graph and a semantically aligned Vector Store containing extracted latent features, synchronized through an event-driven substrate. Tensor-Structured Retrieval-Augmented Generation (T-SRAG) dynamically routes queries across retrieval paths. Contrastive alignment maps document and query embeddings to hierarchical topic structures to improve semantic fidelity and reduce hallucinations. Beyond retrieval, tensor-based link prediction identifies and completes missing links in the Knowledge Graph, supporting inference grounded in citation structure. Applications across cybersecurity, law, materials science, and healthcare demonstrate improvements in retrieval precision, early trend detection, hypothesis generation, and hallucination mitigation. The dissertation provides a deployable, modular foundation for trustworthy, domain-specific AI systems that retrieve and reason over structured knowledge.

## Figure 1

![Figure 1](fig1.png)
