# OntoAR-HAR: Ontology-Guided Agentic RAG with Personalized Memory for Human Activity Recognition

- arXiv: https://arxiv.org/abs/2610.15292  (v1, submitted 2026-10-11, updated 2026-10-11)
- Authors: Xiangqing Lu, Tao Zhu, Liang Yu, Shuangjian Li, Lulu Ban, Furong Duan, Mingxing Nie, Liming Chen, Yaping Wan
- Categories: cs.AI
- Collected: 2026-10-15 (KST)

## Abstract

LLMs increasingly support sensor-based human activity recognition (HAR) by linking motion signals with activity semantics and physical knowledge. Retrieval-augmented generation (RAG) grounds decisions in sensor examples and domain features, enabling training-free target-user inference with less dependence on raw numerical arrays. However, existing LLM/RAG-based HAR typically searches single-level activity spaces using static population knowledge. Consequently, they compare many unrelated candidates using the same static population evidence and overlook personalized motion patterns. We propose OntoAR-HAR, an ontology-guided agentic RAG framework combining static population and personalized knowledge. Its tree-structured activity ontology decomposes classification into local decisions among semantically related activities. The static store supplies node-constrained examples, while offline-discovered executable signal features provide numerical evidence for local distinctions. During inference, the personalized store collects selected user observations, which the LLM integrates with static knowledge and signal features while traversing the ontology to an activity label. Cross-subject and heterogeneous-sensing experiments show complementary gains from hierarchical retrieval and personalized memory across multiple LLM backbones, achieving state-of-the-art performance. By explicitly modeling hierarchical relations across activity granularities, OntoAR-HAR also addresses the long-overlooked semantic inclusion problem and avoids treating related labels as independent categories.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
