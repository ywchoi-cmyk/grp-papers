# FIRME: Registry-Anchored Memory Graphs for Evolving, Heterogeneous Investor Knowledge

- arXiv: https://arxiv.org/abs/2610.40482  (v1, submitted 2026-10-29, updated 2026-10-29)
- Authors: Yunbai Zhang, Yunyi Gao, Han-Tai Shiao
- Categories: cs.AI, cs.CL
- Collected: 2026-11-02 (KST)

## Abstract

Financial AI workflows that reuse investor knowledge need persistent memory that integrates observations across sources and periods without losing identity or provenance. In a knowledge graph, recurring observations may use different surface forms, fragmenting relationship histories and preventing evidence from accumulating. We introduce Fusion and Identity Registry for Memory Evolution (FIRME), a registry-anchored memory graph that reconciles incoming observations to persistent canonical relationships and retains their source, time, and context. Within periods, rule-based fusion links investor-call discussions to portfolio cash-flow signals, directly or through a fixed product-topic ontology. Across periods, canonical identities and persistent aliases direct recurring observations to the same relationship history; deterministic updates summarize reinforcement, inactivity, and reactivation. We evaluate FIRME on proprietary investor-call and cash-flow records and on S&P 500 earnings-call transcripts. Compared with a historical registry that retains canonical identities and semantic fallback but omits alias memory, FIRME increases final-period Correct Match Rate by 7.8-12.1 percentage points across four dataset-backend settings under a fixed-judge and fallback-review protocol. A blinded human audit of 200 incoming observations per setting finds Correct Match Rate gains of 9.0-16.5 points and reattachment-recall gains of 22.5-29.0 points, with higher observed merge precision in all four samples. A separate audit finds valid evidence paths for 293 of 300 outputs from full within-period fusion in the investor-call setting. Extraction-faithfulness and round-trip diagnostics assess source grounding and preservation of extractor-derived graph content.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Coupled short- and long-term fusion in FIRME across consecutive periods. Each short-term graph 𝑆𝑡= 𝐺𝑡𝑢⊕ 𝐺𝑡𝑠fuses unstructured and structured graphs. Dashed arrows show registry update from 𝑅𝑡−1 to 𝑅𝑡, conditioned on 𝑆𝑡; solid arrows to 𝑀𝑡show memory reconciliation of 𝑆𝑡, 𝑅𝑡, and 𝑀𝑡−1.
