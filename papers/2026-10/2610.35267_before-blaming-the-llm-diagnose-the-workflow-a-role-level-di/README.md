# Before Blaming the LLM, Diagnose the Workflow: A Role-Level Difficulty Profile for Translating Natural Language into Ontology-Grounded Statements

- arXiv: https://arxiv.org/abs/2610.35267  (v1, submitted 2026-10-26, updated 2026-10-26)
- Authors: Liang Zhang, Benoît Daireaux, Sergey Alyaev
- Categories: cs.AI
- Collected: 2026-10-28 (KST)

## Abstract

Natural-language-to-domain-specific-language (NL-to-DSL) semantic parsing systems increasingly translate informal user descriptions into structured artifacts such as Structured Query Language (SQL) queries, Application Programming Interface (API) calls, workflows, formal specifications, and ontology-grounded domain-specific language (DSL) statements. This paper focuses on ontology-grounded Assertion Box (ABox) DSL generation: the translation of natural language domain descriptions into assertion-level DSL statements grounded in a pre-existing ontology vocabulary. In this setting, syntactic validity is often easier to achieve than semantic adequacy. Failures are frequently attributed to weak generator models, but recurring sources of difficulty are also structural: insufficient input, weak domain grounding, output template and vocabulary gaps, weak validation, and non-local repair. We propose a role-level difficulty profile for diagnosing difficulty in ontology-grounded NL-to-DSL semantic parsing at the workflow level. The profile organizes diagnostic variables across five recurring workflow roles: Input, Generator, Output, Validator, and Repairer. The seven variables are input sufficiency, context availability, grounding complexity, template fit, vocabulary coverage, validation strength, and error observability. Practitioners construct the difficulty profile through qualitative judgment over available evidence. This experience-informed, non-exhaustive difficulty profile is intended to support workflow diagnosis and guide redesign or human-in-the-loop intervention.

## Figure 1

![Figure 1](fig1.png)

Fig. 1. Typical workflow and recurring roles in LLM-based ontology-grounded semantic parsing.
