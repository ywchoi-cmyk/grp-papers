# Foresight-over-Graph: Reasoning Beyond Local Horizons for Knowledge Base Question Answering

- arXiv: https://arxiv.org/abs/2610.08388  (v1, submitted 2026-10-06, updated 2026-10-06)
- Authors: Yang Hong, Yajun Yang, Xin Wang, Liping Jing, Qinghua Hu
- Categories: cs.CL, cs.AI
- Collected: 2026-10-09 (KST)

## Abstract

Large language models (LLMs) have demonstrated strong capabilities in question answering, yet they still frequently suffer from hallucinations on knowledge-intensive tasks. Knowledge graphs (KGs) provide LLMs with structured, interpretable, and updatable factual grounding, making them a promising external knowledge source for reliable reasoning. However, existing LLM-guided graph reasoning methods typically rely on hop-wise greedy or beam-style pruning during evidence retrieval. Such local decision processes are inherently myopic: evidence that appears weak near the source may become crucial only after deeper graph context is explored, causing answer-critical branches to be discarded prematurely and making the reasoning chain difficult to recover. To address this limitation, we propose Foresight-over-Graph (FoG), a foresight-aware evidence retrieval framework for knowledge base question answering (KBQA). FoG iteratively constructs a question-relevant evidence subgraph and uses far-to-near feedback to guide path exploration, and maintains a compact memory subgraph to support continued exploration. Extensive experiments on widely used KBQA benchmarks demonstrate that FoG achieves state-of-the-art performance, with a particularly large improvement of 16.58% in Hit on CWQ, while also reducing LLM calls and token usage. Our code is available at https://github.com/yhong7/FoG .

## Figure 1

![Figure 1](fig1.png)

Figure 1: Limitations of short-sighted hop-by- hop KG traversal and the intuition behind FoG.
