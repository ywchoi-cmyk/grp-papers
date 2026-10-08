# Uncertainty in Representation Learning on Knowledge Graphs

- arXiv: https://arxiv.org/abs/2610.06974  (v1, submitted 2026-10-03, updated 2026-10-03)
- Authors: Yuqicheng Zhu
- Categories: cs.LG
- Collected: 2026-10-08 (KST)

## Abstract

Knowledge graph embedding (KGE) methods represent entities and predicates in continuous vector spaces to infer missing knowledge. Despite strong benchmark performance, their predictions often lack principled reliability guarantees, limiting their use in high-stakes applications. Moreover, uncertainty arises throughout the KGE pipeline, from incomplete or probabilistic input knowledge to stochastic training and prediction. This thesis systematically investigates three sources of uncertainty in KGE: knowledge uncertainty, arising from incomplete, noisy, or probabilistic input knowledge; algorithmic uncertainty, induced by randomness in model training; and predictive uncertainty, concerning the reliability of model outputs. To address algorithmic uncertainty, the thesis demonstrates that models trained under identical settings can produce substantially different predictions and introduces a voting-based aggregation framework to mitigate this instability. To quantify predictive uncertainty, it adapts conformal prediction to KGE, constructing answer sets with distribution-free coverage guarantees and extending them to provide predicate-conditional reliability guarantees. To support reasoning under knowledge uncertainty, it develops statistically valid prediction intervals for confidence-scored triples and an embedding-based approach to approximate probabilistic reasoning over statistical ontologies with formal soundness guarantees. Together, these complementary, model-agnostic methods provide a practical and theoretically grounded approach to uncertainty in KGE, advancing beyond predictive accuracy toward reliable and uncertainty-aware knowledge graph reasoning.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
