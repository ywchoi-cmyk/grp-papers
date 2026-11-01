# Leaving the Cave by Breaking the Symmetry: Identifiable Structure Can Enable Cross-Lingual Generalization

- arXiv: https://arxiv.org/abs/2610.38509  (v1, submitted 2026-10-28, updated 2026-10-28)
- Authors: Frederick Riemenschneider, Anette Frank
- Categories: cs.CL
- Collected: 2026-11-02 (KST)

## Abstract

Why do multilingual language models generalize across languages even without shared vocabulary? The Platonic Representation Hypothesis posits that models trained on different data, objectives, and modalities converge toward a shared statistical model of reality. Extending this intuition to representations inside a single multilingual model, we propose the Relational Identifiability Hypothesis: relations in a shared world can promote entity alignment by ruling out alternative cross-lingual correspondences, making corresponding entities more likely to become directly readable without an additional transformation. We test this hypothesis in a controlled bilingual Transformer whose two token-disjoint languages describe the same modular-arithmetic world. We find that the languages can develop a shared answer subspace without aligning corresponding numbers. Cross-lingual alignment emerges selectively when the available relations constrain number correspondences: subtraction makes zero task-level identifiable, inducing selective alignment, while an order-sensitive operation produces broad alignment across numbers. These patterns predict success in zero-shot cross-lingual transfer. Together, our results show that relational structure in a shared world can promote entity alignment and enable transfer.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Modular addition produces a shared an- swer subspace without number-level alignment. Adding an order-sensitive operation broadly aligns those numbers despite disjoint vocabularies.
