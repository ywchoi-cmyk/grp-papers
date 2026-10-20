# How Benchmark Graph Construction Shapes Multi-Hop KG Navigation: A Controlled Audit of PathQuestion and PathQuestion-Large

- arXiv: https://arxiv.org/abs/2610.26399  (v1, submitted 2026-10-19, updated 2026-10-19)
- Authors: Eduin E. Hernandez, Sergio A. Diaz, Luis F. Garcia, Nurassyl Askar, Stefano Rini
- Categories: cs.CL
- Collected: 2026-10-21 (KST)

## Abstract

Multi-hop knowledge-graph question answering (KGQA) benchmarks are often treated as fixed language-and-reasoning tasks, but for navigation-based methods, difficulty also depends on the graph in which those tasks are instantiated. This makes graph construction a consequential but often entangled part of the navigation task. To isolate this effect, we audit PathQuestion (PQ) and PathQuestion-Large (PQL) as graph-navigation benchmarks under a controlled intervention: we hold questions, topic entities, released answers, released path annotations, and family-level splits fixed while replacing each released task-filtered graph with the larger source KG distributed with the benchmark. Source restoration expands the effective navigation search space and graph-consistent answer and path multiplicity while sharply reducing unguided reachability to released answers. We evaluate whether these structural changes persist across navigation policies using structural references, frozen small-language-model navigation policies, and trained MINERVA policies. Across both frozen and trained policies, restoration substantially reduces released-answer accuracy and trajectory fidelity, while graph-consistent evaluation recovers only part of the loss. These results show that benchmark graph construction is part of the navigation task specification rather than merely an implementation detail and can materially shape measured behavior even when the released QA task is held fixed.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
