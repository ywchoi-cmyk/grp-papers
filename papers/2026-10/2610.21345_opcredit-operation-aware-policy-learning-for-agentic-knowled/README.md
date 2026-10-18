# OpCredit: Operation-Aware Policy Learning for Agentic Knowledge Graph Question Answering

- arXiv: https://arxiv.org/abs/2610.21345  (v1, submitted 2026-10-15, updated 2026-10-15)
- Authors: Yucheng Li, Mingyuan Li, Xiaxia Wang, Gong Cheng
- Categories: cs.CL
- Collected: 2026-10-19 (KST)

## Abstract

Agentic knowledge graph question answering(KGQA) relies on sequences of executable operations, but trajectory-level rewards obscure their individual contributions. Successful trajectories may contain ineffective operations, while failed trajectories may contain useful ones. To assess individual operations, we propose OpCredit, an operationaware policy-learning framework that combines downstream outcome credit with immediate transition credit: Branch Outcome Credit (BOC) reuses ordinary rollouts to compare terminal task rewards observed after different operations under matched navigation contexts; Frontier Transition Credit (FTC) measures operation-induced changes in answer-conditioned frontier potential. The two complementary signals jointly supervise the corresponding decision spans during training, while inference uses only the learned policy and standard KG interface. Experiments on ComplexWebQuestions, WebQSP, and GrailQA across three backbones demonstrate consistent improvements in KGQA performance.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
