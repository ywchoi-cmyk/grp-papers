# Similarity-Constrained Reweighting for Complex Query Answering on Knowledge Graphs

- arXiv: https://arxiv.org/abs/2611.29596  (v1, submitted 2026-11-22, updated 2026-11-22)
- Authors: Daniel Daza, Alberto Bernardi, Luca Costabello, Christophe Gueret, Michael Cochez, Martijn Schut
- Categories: cs.AI, cs.LG
- Collected: 2026-11-24 (KST)

## Abstract

Machine learning models for Complex Query Answering (CQA) on knowledge graphs estimate the likelihood of answers that are not reachable via direct traversal. Recent work has proposed extending such queries with soft entity constraints, which require the target variable to be similar or dissimilar to specified sets of entities. We study a more general formulation where similarity constraints are specified on an arbitrary variable in a query, and introduce SCORE: a computationally efficient and interpretable method for incorporating similarity constraints on an arbitrary variable of a query. SCORE is based on a lightweight and interpretable score adjustment function that only requires tuning two hyperparameters on a validation set. Our experiments show that SCORE effectively incorporates preferences while maintaining strong query answering performance. It significantly improves ranking quality when constraints apply to the target variable and performs effectively in the more general case involving constraints on intermediate variables, and its performance remains robust when applied to several existing methods for CQA. Our implementation is available at https://github.com/dfdazac/score.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Illustration of three approaches for query answering on knowledge graphs, with vectors indicating entity scores at different steps. Left: a traditional query with purely logical constraints. Middle: incorporating similarity constraints in NQR [10], which supports only the target variable via uncalibrated score adjustments (shown in red and blue). Right: SCORE, which supports similarity constraints on arbitrary variables through normalized similarity scores.
