# Enhancing Legal Reasoning in Pre-trained Language Models via Knowledge Graph-Guided Multi-Task Pre-training

- arXiv: https://arxiv.org/abs/2610.13722  (v1, submitted 2026-10-09, updated 2026-10-09)
- Authors: Ibrahim Siddig, Munir Georges
- Categories: cs.CL
- Collected: 2026-10-13 (KST)

## Abstract

Legal language understanding requires reasoning over semi-structured regulatory documents, yet standard pre-training objectives do not explicitly target this structural capability. Because current legal language models rely solely on masked language modeling, they treat statutory text as flat token sequences and ignore the underlying hierarchical constraints. To bridge this gap, we present a multi-task pre-training approach for German traffic law (StVO). Our approach combines three complementary objectives: Next Sentence Prediction (NSP), Knowledge Graph (KG) Guided Clustering (CLU), and Knowledge Graph (KG) Aware Paragraph Classification (CLS). This approach explicitly encodes structured legal knowledge directly into the model weights. This encoding enables zero-shot legal reasoning at inference time and removes the need for discrete graph traversal. We evaluate our approach across nine Transformer-based encoders and 324 experimental runs. On synthetic StVO question answering, our models demonstrate consistent relative improvements between 10.3% and 155.0% over baselines. Furthermore, relative to the established LexGLUE baselines (Chalkidis et al., 2022), our models improve over prior results on four of seven legal benchmarks. It also achieves consistent zero-shot transfer gains between 3.4% and 15.8% on Austrian driving regulations. These experimental results indicate that our training approach generalizes successfully beyond the initial training legal domain.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Architecture of the proposed KG-guided multi-task pre-training pipeline. German StVO legal text is parsed, translated via an LLM translator, and structurally aligned with a corresponding English-based knowledge graph to inject explicit relational constraints into model reasoning. A detailed visualization of the generated graph topology is provided in Appendix A.
