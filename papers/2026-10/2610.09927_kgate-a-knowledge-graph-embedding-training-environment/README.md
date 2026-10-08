# KGATE : a Knowledge Graph Embedding Training Environment

- arXiv: https://arxiv.org/abs/2610.09927  (v1, submitted 2026-10-07, updated 2026-10-07)
- Authors: Benjamin Loire, Galadriel Brière, Célia Brahimi, Antoine Toffano, Anaïs Baudot
- Categories: cs.LG, cs.AI
- Collected: 2026-10-08 (KST)

## Abstract

Knowledge graph embedding (KGE) models encode the entities and relations of a knowledge graph into a low-dimensional latent space, enabling tasks such as classification or link prediction. Most KGE models follow an autoencoder architecture, in which an encoder projects the knowledge graph into the latent space and a decoder reconstruct it. Combining both encoder and decoder components is increasingly needed, yet existing libraries rarely support complete autoencoders, are often unmaintained, rely on undocumented default hyperparameters, and produce results that cannot be compared across libraries. Here we present KGATE (Knowledge Graph Autoencoder Training Environment), a modular Python library built on PyTorch Geometric and TorchKGE. KGATE lets users assemble initializers, encoders, decoders, losses, negative samplers, and evaluation metrics as building blocks, or plug in their own block. KGATE includes a preprocessing procedure that controls data leakage, a builtin training pipeline, and reproducibility by design. Benchmarks against six existing KGE libraries show that KGATE training time is comparable with the fastest libraries while offering a broader set of features.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
