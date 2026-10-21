# Automated Brick Schema Knowledge Graph Completion Across Buildings

- arXiv: https://arxiv.org/abs/2610.27339  (v1, submitted 2026-10-19, updated 2026-10-19)
- Authors: Daniel Ma, Jalil Huseynov, Xinyi Pan, Shaked Shalev, Zhang Chi, Ai Yamamoto, Sohei Arisaka
- Categories: cs.LG
- Collected: 2026-10-22 (KST)

## Abstract

The Brick schema represents building equipment, sensors, spaces, and the relationships between them as typed, multi-relational graphs, providing machine-readable metadata that supports generalizable control applications. Current methods for producing complete Brick models require extensive manual examination of building schematics and point lists. We observe that as Brick models are knowledge graphs, inferring missing relations is naturally posed as a knowledge graph completion problem. To the best of our knowledge, this is the first application of knowledge graph completion to Brick model generation. We compare three methods, gradient-boosted trees, Pairwise Brick Relation Ranking, and CompGCN, on the relations feeds, hasPart, and hasPoint, which account for the majority of the schematic-reading work in building a Brick model by hand. Models are evaluated on held-out MORTAR buildings and out-of-distribution Kaggle and Building Time Series data. Although CompGCN is the strongest performer on held-out buildings under metrics resistant to class imbalance, leading macro-F1 and AUPRC, no method generalizes uniformly across datasets or relations.

## Figure 1

![Figure 1](fig1.png)

Figure 1: A two-hop Brick graph fragment. Our completion targets are the typed, directed relations feeds, hasPart, and hasPoint.
