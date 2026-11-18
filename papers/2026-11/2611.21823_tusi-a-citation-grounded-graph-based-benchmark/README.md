# TUSI: A Citation-Grounded Graph-Based Benchmark

- arXiv: https://arxiv.org/abs/2611.21823  (v1, submitted 2026-11-16, updated 2026-11-16)
- Authors: Marzieh Karimi, Mehran Safayani, Alireza Basiri
- Categories: cs.CL, cs.AI
- Collected: 2026-11-18 (KST)

## Abstract

Evaluating retrieval-augmented generation (RAG) systems in Persian law remains challenging because benchmarks lack realism, grounding, and coverage of legal reasoning. Existing resources are either synthetically generated from statutory texts, lacking natural information needs, or derived from informal legal question--answer sources without explicit linkage to authoritative legal documents, making them unsuitable for rigorous evaluation of grounded legal reasoning. To address this gap, we introduce TUSI-Bench, a structured Persian legal benchmark designed for the evaluation of RAG-based systems. TUSI-Bench is built upon a multi-layered legal knowledge framework containing 7,261 legal articles and integrating codified statutes, legal commentaries, doctrinal writings, and Supreme Court unification rulings. We also construct a legal knowledge graph linking articles and concepts for structure-aware retrieval. Based on this foundation, TUSI-Bench provides two complementary evaluation tasks: (i) TUSI-QA, an open-ended question answering benchmark containing 1,999 questions that requires grounded responses with explicit legal citations, and (ii) TUSI-Bar, a multiple-choice benchmark containing approximately 500 four-option questions derived from Iranian Bar examination questions. Furthermore, we propose a graph-based retrieval baseline that leverages relational structure within the legal knowledge graph. Experimental results demonstrate that incorporating graph-based relations improves retrieval recall by up to 8 percentage points compared to standard baselines, highlighting the importance of structured legal representations for RAG systems. The proposed benchmark provides a standardized resource for evaluating grounded legal reasoning in Persian and enables future research on structured legal intelligence.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
