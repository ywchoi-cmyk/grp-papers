# TACO-Graph: Automated Construction of Text-Atributed Graphs

- arXiv: https://arxiv.org/abs/2610.36650  (v1, submitted 2026-10-27, updated 2026-10-27)
- Authors: Amiri Hayes, Kristina Wicke
- Categories: cs.LG
- Collected: 2026-10-29 (KST)

## Abstract

Graph-structured representations of text data have become foundational across machine learning, yet it remains unclear how to systematically construct a graph from a given dataset for a target task. Choices about which entities become nodes, which relationships become edges, and what text each node contains can substantially affect downstream performance. In practice, finding optimal constructions often requires expert knowledge or manual trial and error. We introduce TACO-Graph, a decision tree framework for learning which graph construction choices are most effective for a given dataset and task. Specifically, we focus on text-attributed graphs (TAGs) constructed from multi-attribute tabular data. TACO-Graph enumerates valid TAG representations, scores each using fast proxy evaluation on small representative subsets, and trains an interpretable decision tree on those scores. Across five datasets spanning citation networks, product reviews, and bibliographic relationships, our decision trees predict construction quality on separately drawn evaluation samples with mean Spearman $ρ$ above $0.9$ for node classification and above $0.8$ for GraphRAG retrieval. Our trees systematically identify which constructions perform better across both GNN and GraphRAG tasks, and the full pipeline is released as an open-source library to support evaluation on new tasks and datasets at https://github.com/AmiriHayes/text_attributed_graphs. TACO-Graph provides a systematic and interpretable guide for determining how to convert tabular data to text-attributed graphs for downstream tasks.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Overview of TACO-Graph. (1) A relational dataset’s columns are mapped to a gen- eralized schema and characterized using automated statistical and validity checks. These dataset level properties are stored for each dataset, and train/test subsets are sampled. (2) For a speci- fied downstream task, TACO-Graph enumerates the space of potential TAG constructions (vari- ants) by defining node, edge, and text-fidelity choices. (3) Each construction is evaluated on rep- resentative subsamples by scoring (via lightweight GNN or small-sample GraphRAG), yielding Score(variant, subsample). (4) A decision tree is fit to variant construction scores and validated on separately drawn data using Spearman correlation and tree edit distance. (5) The interpretable ranking from the tree reveals optimal and suboptimal graph construction choices, informing the practitioner.
