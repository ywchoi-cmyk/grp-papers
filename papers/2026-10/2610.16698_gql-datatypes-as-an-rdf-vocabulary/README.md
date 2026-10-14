# GQL Datatypes as an RDF Vocabulary

- arXiv: https://arxiv.org/abs/2610.16698  (v1, submitted 2026-10-12, updated 2026-10-12)
- Authors: Dominik Tomaszuk, Daniel Szałaj
- Categories: cs.DB
- Collected: 2026-10-15 (KST)

## Abstract

The ISO GQL standard introduces a rich value-type system for property graphs, including scalar, temporal, byte-string, list, record, and dynamic union datatypes. The vocabulary presented here additionally covers a vector extension. At the same time, RDF-based knowledge graph systems identify literal datatypes by IRIs and interpret typed literals through value spaces, lexical spaces, and lexical-to-value mappings. This paper presents the GQL Datatypes RDF Vocabulary, a lightweight RDF vocabulary that represents selected GQL datatypes and the vector extension as RDF datatype IRIs and describes their hierarchy, aliases, and selected constraints using RDF, RDFS, OWL, and XML Schema Datatypes vocabulary terms. The vocabulary is intended to support interoperability between GQL-oriented property graph systems and RDF-based knowledge graph systems. We describe its namespace and datatype model, summarize its datatype coverage, and show how the accompanying generator and validator use the vocabulary. In the reference implementation, RDF literals retain GQL datatype IRIs; XSD mappings declared in the vocabulary support scalar validation, while lists, records, and vectors are encoded directly as JSON lexical forms of vocabulary-typed literals.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
