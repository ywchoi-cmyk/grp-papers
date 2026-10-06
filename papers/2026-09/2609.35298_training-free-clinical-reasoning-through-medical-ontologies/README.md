# Training-Free Clinical Reasoning through Medical Ontologies and Cognitive Mapping: A Symbolic-Probabilistic Knowledge Graph Framework

- arXiv: https://arxiv.org/abs/2609.35298  (v1, submitted 2026-09-28, updated 2026-09-28)
- Authors: Surajit Das
- Categories: cs.AI
- Collected: 2026-10-06 (KST)

## Abstract

Most clinical prediction systems learn patient-variable-outcome associations; we investigate a training-free diagnostic paradigm mapping patient observations to explicit medical knowledge. CKG Reasoner integrates candidate-specific Evidence Feature Nodes, patient-reference matching, a bounded Information Gate, knowledge-weighted evidence accumulation, disease similarity, and decisive clinical rules. Missing-aware normalization and coverage auditing distinguish absent from unavailable evidence. Candidate ranking is separate from outcome-label-independent K-means clustering, which uses four derived evidence coordinates (evidence strength, relative magnitude, directional similarity, and evidence completeness), not raw predictors or targets, to derive cohort-level assignments. Across six retrospective cohorts - four dengue (N = 1000, 1523, 989, 1018), malaria (N = 2190), and influenza (N = 4569) - a uniform, label-free, cohort-fitted K = 2 protocol yielded positive-class F1 scores of 0.996, 0.634, 0.936, 0.917, 0.695, and 0.842, and all-record accuracies of 0.996, 0.558, 0.914, 0.893, 0.707, and 0.906, respectively, with full partition-decision coverage using the frozen package and disease-specific knowledge representations. Neither scoring nor clustering uses outcome labels. Logistic regression provides a supervised baseline. Influenza incorporates confirmatory molecular PCR and is not independent pre-test prediction. Results characterize knowledge-grounded evidence separation, auditability, and sensitivity, not prospective clinical validity or comparative superiority. FOL/LLM-based clinical explanation remains unevaluated.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
