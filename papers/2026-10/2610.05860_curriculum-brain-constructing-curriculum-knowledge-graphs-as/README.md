# Curriculum Brain: Constructing Curriculum Knowledge Graphs as a Substrate for Cognitive Diagnosis

- arXiv: https://arxiv.org/abs/2610.05860  (v1, submitted 2026-10-05, updated 2026-10-05)
- Authors: Shrideep Tamboli, Chiranjeevi Maddala, Eshal Minhaj
- Categories: cs.CY, cs.AI
- Collected: 2026-10-07 (KST)

## Abstract

Cognitive Diagnostic Models (CDMs) identify which specific skills a student has and has not mastered, the signal a personalized learning path needs and a single aggregate score cannot give. Yet they are rarely deployed. The obstacle is their precondition: the Q-matrix, a mapping from every assessment item to the skills it requires, historically authored by hand. We separate the task into two stages: first construct the curriculum's own knowledge graph, the full space of concepts and skills it contains, independent of any item; then map items against that graph on demand. This paper addresses the first stage only. The item-mapping stage is designed but not implemented here, so the claim that this shifts judgment cost from once per item to once per curriculum is a design rationale rather than a finding. We present Curriculum Brain, a two-repository system pairing a version-controlled knowledge base with an agentic pipeline of eleven single-responsibility agents under a thin deterministic orchestrator. It generates candidate concept-skill mappings from official curriculum documents, checks them against accumulated rules, and compares them with a concept-skill map extracted independently from the textbook, repairing its own failures and escalating to a human only when it cannot resolve a case itself. Across 241 chapter runs (168 distinct chapters), 41.5% produced a Generator output passing both checks without a patch, and 67.6% resolved without escalation. Both are measured against criteria the system itself produced, so both describe internal consistency rather than agreement with an external standard, and both pool two pipeline configurations separated by a single change at run 77; after it the figures are 57.0% and 91.5%. Observed spend was $1.19 per chapter, API spend only, excluding human review. We release both the framework and the resulting curriculum dataset.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
