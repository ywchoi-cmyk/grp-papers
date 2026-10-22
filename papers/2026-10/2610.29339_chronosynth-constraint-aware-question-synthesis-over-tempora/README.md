# ChronoSynth: Constraint-Aware Question Synthesis over Temporal Knowledge Graphs

- arXiv: https://arxiv.org/abs/2610.29339  (v1, submitted 2026-10-21, updated 2026-10-21)
- Authors: Feng Liang, Weixin Zeng, Runhao Zhao, Mingjun Zhou, Shaoshi Yang, Xiang Zhao
- Categories: cs.CL, cs.AI
- Collected: 2026-10-23 (KST)

## Abstract

Knowledge graph question generation (KGQG) generates natural-language questions from structured graph evidence and a target answer. When the input graph is temporal, a valid question must also preserve the answer field, time condition, reference event, and temporal order that determine the answer set. Existing KGQG methods and prompting baselines can produce fluent questions that alter these conditions, causing temporal semantic drift. This paper studies temporal KGQG as a constraint-preserving graph-to-question problem and proposes ChronoSynth, a memory-augmented and constraint-aware generation framework. ChronoSynth first constructs a Temporal Intent State to make the intended question semantics explicit. It then retrieves compatible typed question patterns from an indexed pattern memory, adapts them to the input graph, and validates the generated question. Validation feedback guides revisions when a supported inconsistency is detected. Experiments on CRONQUESTIONS and MultiTQ demonstrate state-of-the-art generation performance, with ablations supporting the contributions of its components.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Motivating examples of temporal semantic drift. The prompting baselines are fluent but change the time condition, reference event, answer field, or order cue.
