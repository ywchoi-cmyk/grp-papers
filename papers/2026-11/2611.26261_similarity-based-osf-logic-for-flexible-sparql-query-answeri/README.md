# Similarity-based OSF Logic for Flexible SPARQL Query Answering

- arXiv: https://arxiv.org/abs/2611.26261  (v1, submitted 2026-11-19, updated 2026-11-19)
- Authors: Gian Carlo Milanese, Gabriella Pasi
- Categories: cs.AI, cs.DB, cs.LO
- Collected: 2026-11-23 (KST)

## Abstract

We present an updated version of fosf, a reasoner for fuzzy order-sorted feature (OSF) logic, with support for flexible SPARQL query answering over RDF knowledge graphs. Fuzzy OSF logic is a knowledge representation and reasoning language where feature symbols denote functions and sort symbols denote fuzzy sets. Sorts are organized in a fuzzy subsumption relation that extends to OSF terms, record-like structures representing classes of entities. The unification algorithm for these structures provides a calculus of fuzzy type subsumption. The latest release of fosf introduces support for similarity-based reasoning by extending the OSF language with a similarity relation among sorts, alongside a translation engine for compiling OSF terms into standard SPARQL. Queries expressed as OSF terms undergo fuzzy ontology-aware rewriting prior to translation. This process incorporates an OSF theory of sort definitions, feature domain and range declarations, and fuzzy subsumption and similarity relations through fuzzy OSF constraint normalization. This rewriting enables flexible query answering by returning approximate solutions, allowing queries that would otherwise be inconsistent with the underlying ontology to yield relevant results.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Example of how a sort subsumption ⪯(black edges) and a sort similarity ∼(dotted green edges) are parsed in fosf, and their graphical representation (where ⊥is omitted). After parsing, the two relations are combined into a single fuzzy subsumption ⪯· (black edges and dashed red edges).
