# Beyond Reachability: A Relation-Semantic Reasoning Framework for Biomedical Multi-hop QA

- arXiv: https://arxiv.org/abs/2610.19754  (v1, submitted 2026-10-14, updated 2026-10-14)
- Authors: Ziyang Ling, Ziyi Chen, Ronald X. Xu, Mingzhai Sun
- Categories: cs.CL
- Collected: 2026-10-16 (KST)

## Abstract

Biomedical multi-hop reasoning over knowledge graphs requires identifying a semantically valid relation sequence that supports the answer. Existing methods can retrieve correct answers, yet often rank them poorly within a large pool of seemingly relevant candidates. Even when a correct answer is retrieved, its associated evidence and reasoning path may fail to support the relation composition required by the question. We term this disconnect between answer reachability and evidential validity the reachable-but-invalid problem. We present ReSemReason, which shares a question-induced distribution over typed, directed relation schemas between candidate discovery and evidence selection. Schema compatibility guides graph search; ReSemAttn then uses relation-conditioned key/value projections and an uncertainty-weighted path prior to attend to candidate-specific evidence. A separate absolute-support score complements normalized attention when all retrieved paths are weak. The reported experiments on BioHopR, PrimeKGQA, and MedReason show improvements in answer ranking and answer-set quality. Path-discrimination analyses examine the distinction between endpoint correctness and evidential support. We also specify matched controls for search, attention, and schema uncertainty.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
