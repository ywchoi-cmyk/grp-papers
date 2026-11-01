# What Does an Ontology Catch? Curated, LLM-Generated and Data-Derived Ontologies as Checkers of LLM Agents over Knowledge Graphs

- arXiv: https://arxiv.org/abs/2610.37809  (v1, submitted 2026-10-27, updated 2026-10-27)
- Authors: Michal Orzechowski, Rund Tawfiq, Tomasz Kosciolek
- Categories: cs.AI, cs.DB
- Collected: 2026-11-02 (KST)

## Abstract

LLM agents that answer questions over Web knowledge graphs are increasingly wrapped in checks derived from the graph's ontology, on the assumption that a formal schema makes a reliable judge. Yet a checker can be wrong as well: it can miss errors, and it can flag correct answers and push the agent into "fixing" them. Whether a curated ontology is worth its cost as such a judge, and how it compares with an ontology an LLM writes or a schema mined from the data, is unknown. We make the checker itself the object of study. Across curated, LLM-generated and data-derived ontologies, used as prompt context, as a checker, or both, and across open-weight and proprietary agents on public graphs and a private graph of nearly $10^{9}$ triples, we account for what ontology-derived checks catch and what they wrongly flag. We show how each source trades caught errors against false alarms, how a curated schema used as published can contradict its own data, which errors structural checks miss, and whether combining sources or giving the agent the checker's specific feedback pays off. On UniProt, the curated ontology flags more correct answers than either an ontology derived from the data or one an LLM derives from a summary of the data with masked identifiers. On real agent answers, its flags are only marginally more precise than random flags.

## Figure 1

![Figure 1](fig1.png)

Figure 1: The setting. An LLM agent answers a question with a SPARQL query; a check derived from an ontology passes the answer or flags it, and a flag triggers one retry. The same ontology can also be the agent’s context.
