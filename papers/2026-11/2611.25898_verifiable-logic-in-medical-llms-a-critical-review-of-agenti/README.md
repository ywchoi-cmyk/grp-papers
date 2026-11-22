# Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding

- arXiv: https://arxiv.org/abs/2611.25898  (v1, submitted 2026-11-19, updated 2026-11-19)
- Authors: Youssef ElNahas, Adel Ammar, Soumaya Chaffar, Wadii Boulila
- Categories: cs.CL, cs.AI, cs.CY, cs.LG
- Collected: 2026-11-23 (KST)

## Abstract

Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demographic shortcuts can pass conventional evaluation. This critical review covers four paradigms in turn: how clinical hallucination arises and why static metrics miss it; the agentic hallucination cascade, in which multi-agent and tool-augmented systems propagate and amplify early reasoning errors; process reward modeling as step-level supervision; and neuro-symbolic grounding, in which formal logic engines, ontology reasoners, and knowledge graphs place verifiable constraints on neural output. Within their encoded domains, systems with symbolic veto layers offer guarantees that hold relative to their encoded knowledge, and they report large gains on the safety measures they use. These results come from single studies, mostly in simulated or small-sample settings, and are not directly comparable with neural baselines. Process reward models remain bounded by the statistics of their training data. We propose a conceptual framework that maps each agentic failure mode to a symbolic intervention point, and we argue that clinical AI safety depends substantially on system architecture. Because current regulation emphasizes performance and does not require verification of reasoning steps, we argue that responsible certification should also audit reasoning trajectories alongside accuracy on static benchmarks.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Study selection flow, presented in the format of the PRISMA-ScR flow diagram [24] for transparency. Records were retrieved through structured prompt-based searches with five AI-assisted retrieval tools and verified by hand against indexed sources; counts start from the verified records logged for charting. The included studies are all primary studies and are listed in Supplementary Table S1; prior surveys, precursor works and regulatory or background sources are cited separately. Exclusion reasons correspond to the eligibility criteria and temporal scope described in this section.
