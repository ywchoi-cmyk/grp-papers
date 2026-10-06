# Ontology Concept Overlap as a Training Signal: Knowledge-Grounded Reinforcement Learning for Clinical Question Answering

- arXiv: https://arxiv.org/abs/2610.06360  (v1, submitted 2026-10-05, updated 2026-10-05)
- Authors: Aditya Tanna, Abhishek Jindal
- Categories: cs.CL, cs.LG
- Collected: 2026-10-07 (KST)

## Abstract

Reinforcement learning post-training for language models relies on two reward designs: human preferences (RLHF, DPO) and binary verifiers (RLVR). Clinical question answering fits neither. Near-correct answers differ by a single substituted entity, and no executable check decides clinical correctness. We instantiate a soft verifier from a maintained controlled vocabulary: UMLS Concept Unique Identifier overlap (via scispaCy, set-level F1) gives a graded, externally specified reward computed without a model in the loop. We combine it inside GRPO with an entropy-normalised LLM judge, which covers the safety and evidence axes overlap cannot see, and a small consistency penalty on padding and repetition that keeps early-training samples scorable. This three-term composite improves over SFT on Phi-3-mini (3.8B) over MedQA by 2.9% on EM (0.700 vs 0.680) and 39% on Token-F1 (0.202 vs 0.145); on Llama-3.2-3B the corresponding gains are 14% on EM and 35% on Token-F1. We report Token-F1 as the primary metric because it credits partially-correct clinical content that EM discards at this open-generation scale. Main-table results are means over 3 seeds with standard deviations below 0.005. The method transfers to PubMedQA, where training on the PubMedQA train set with the same composite reward improves Token-F1 over SFT by 22% on Phi-3-mini and 17% on Llama-3.2-3B without retuning. A reward ablation on Phi-3, varying the judge-ontology split at a fixed consistency weight, attributes 3 EM points to the ontology term, the contribution that catches entity substitutions the judge cannot. Three negative findings constrain the design: DPO under random negatives underperforms SFT for strong-prior models but helps the weakest-prior one; PPO under a sparse neural reward diverges; GRPO with KL-in-loss collapses at 7B.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Composite-reward GRPO. The policy samples 𝐺=4 responses per question; each is scored by the frozen LLM judge, by UMLS CUI overlap against the reference, and by a consistency penalty on padding and repetition. The three terms are combined as in Eq. 1 (𝛼=0.6, 𝛽=0.3, 𝛾=0.1). Group-normalised advantages update the LoRA adapter. Reference and judge remain frozen throughout training.
