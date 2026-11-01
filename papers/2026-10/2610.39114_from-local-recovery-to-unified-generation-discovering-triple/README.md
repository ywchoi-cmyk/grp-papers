# From Local Recovery to Unified Generation: Discovering Triple Set in Knowledge Graphs via Observation-Anchored Latent Diffusion

- arXiv: https://arxiv.org/abs/2610.39114  (v1, submitted 2026-10-29, updated 2026-10-29)
- Authors: Jiaqi Wang, Yisen Gao, Huayang Shi, Junhao Hou, Wengen Li, Jihong Guan, Yichao Zhang, Shuigeng Zhou, Yangqiu Song, Hong Cheng
- Categories: cs.LG, cs.AI
- Collected: 2026-11-02 (KST)

## Abstract

Triple set prediction (TSP) is to recover missing relational triples in a knowledge graph by predicting the triple set instead of isolated links. Existing approaches predominantly rely on the subgraph-based completion paradigm, where the original graph is first partitioned into local subgraphs which are then independently completed. Such a paradigm suffers from fragmented structural reasoning, limited cross subgraph dependency modeling, and missing predictions across subgraphs. This paper proposes LatentDiff, a novel unified latent generative framework for TSP, which reformulates knowledge graph completion as latent space graph generation. LatentDiff first learns a compact latent representation using a relation-aware residual-quantized knowledge graph autoencoder, which encodes the whole graph into relation-aware latent embeddings, quantizes them with chunked residual codebooks, and reconstructs triples through a factorized decoder. On top of this latent space, we introduce an observation-anchored latent graph diffusion model, where the target latent graph representation is perturbed toward the observed latent. The reverse process recovers missing triples through progressive latent denoising. Experiments on three benchmark datasets show that LatentDiff outperforms the SOTA in terms of F_{tsp} by 5.4 percentage points on average. Code: https://anonymous.4open.science/r/LKGDiff-44A5.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
