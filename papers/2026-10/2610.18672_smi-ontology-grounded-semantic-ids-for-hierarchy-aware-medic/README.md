# SMI: Ontology-Grounded Semantic IDs for Hierarchy-Aware Medical Concept Representation

- arXiv: https://arxiv.org/abs/2610.18672  (v1, submitted 2026-10-13, updated 2026-10-13)
- Authors: Ziyang Song, Lia Shen, Yixuan Li, Qincheng Lu, Weihao Li, Haoran Xu, He Zhu, Xinyu Wang, Yue Li
- Categories: cs.CL, cs.AI
- Collected: 2026-10-15 (KST)

## Abstract

Biomedical language models (LMs) provide strong representations for clinical tasks, but they often fail to capture the hierarchical structure among medical concepts. This limitation is especially pronounced for rare and fine-grained clinical codes in long-tailed vocabularies, where hierarchy-agnostic LM representations become less informative as concept frequency decreases. We introduce Semantic Medical Identifier (SMI), a training-free framework for constructing ontology-grounded Semantic IDs and hierarchy-aware medical concept representations. For each diagnosis, procedure, or medication concept, SMI defines its Semantic ID as the coarse-to-fine path through an expert-defined medical ontology. SMI then aggregates frozen biomedical LM embeddings across the corresponding ontology levels to form hierarchy-aware medical concept representations that preserve coarse-to-fine clinical semantics. The base SMI uses uniform aggregation across ontology levels, while a level-weighted variant selects global level weights on validation data. Our theoretical analysis shows that SMI yields more informative medical concept representations than hierarchy-agnostic LM embeddings, particularly for rare and fine-grained clinical concepts. Experiments show that SMI captures meaningful hierarchical structure and improves clinical relation prediction. On MIMIC-IV, SMI improves mortality prediction, readmission prediction, drug recommendation, and rare drug prediction. On eICU, SMI yields more robust patient representations under cross-hospital distribution shift.

## Figure 1

![Figure 1](fig1.png)

Figure 1: SMI better distinguishes hierarchical relations than BioBERT on ICD 1-hop predic- tion. (a) SMI consistently improves hierarchical relation prediction across levels, with the largest gains at finer ICD granularities. (b) SMI maintains stronger and more stable performance than BioBERT across concept-frequency bins, suggesting that medical ontology structure helps mitigate representation degradation for long-tailed clinical codes.
