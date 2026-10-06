# To Learn is to Wander: Learning Across Graphs and Tasks with Random Walks

- arXiv: https://arxiv.org/abs/2610.06694  (v1, submitted 2026-10-05, updated 2026-10-05)
- Authors: Louis Tichelman, Xingyue Huang, Jinwoo Kim, İsmail İlkan Ceylan
- Categories: cs.LG
- Collected: 2026-10-07 (KST)

## Abstract

Graph foundation models aim to transfer across graphs, feature spaces, relational schemas, and prediction tasks, yet existing approaches typically generalize only within particular graph modalities or tasks. We propose Wander, a graph foundation model designed to operate across these settings within a single pretrained checkpoint. Following the prior-predictive perspective, we formulate graph learning as completion of a partially observed graph. We realize this task-general view through a common interface based on random walks, allowing the same model to operate across homogeneous and multi-relational graphs with varying features, labels, and relational schemas. Wander can increase its structural context at inference time without changing its learned parameters and, under suitable assumptions, universally approximates the corresponding Bayes-optimal predictor on bounded connected graphs. Empirically, a single pretrained checkpoint achieves state-of-the-art or highly competitive results across node classification, homogeneous link prediction, and knowledge-graph link prediction. Moreover, joint pretraining across graph modalities and tasks preserves performance in specialized settings while enabling positive transfer and the composition of separately learned capabilities at inference time.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
