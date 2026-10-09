# Traveling with a Map: Reducing the Search Space of Link Traversal Queries Using RDF Shapes

- arXiv: https://arxiv.org/abs/2610.11701  (v1, submitted 2026-10-08, updated 2026-10-08)
- Authors: Bryan-Elliott Tam, Joanna Van Herwegen, Pieter Colpaert, Ruben Verborgh, Ruben Taelman
- Categories: cs.DB
- Collected: 2026-10-09 (KST)

## Abstract

The centralization of web information raises legal and ethical concerns, particularly in social, healthcare, and education applications. Decentralized architectures offer a promising alternative by keeping data closer to its source, yet efficient query processing remains a significant challenge. Link Traversal Query Processing (LTQP) enables querying across decentralized networks but often suffers from long execution times and high data transfer costs due to the large number of HTTP requests involved. Many queries are highly selective with respect to the data model objects distributed across the network. For example, in a social media application where users store heterogeneous data, a query may target only users' posts and comments, ignoring their other information. We refer to such queries as data-model selective. We propose a shape-based pruning approach that relies on shape indexes and a query-shape subsumption algorithm to reduce the search space and thus the number of HTTP requests. We formalize this approach as a link pruning mechanism for LTQP and evaluate it on social media queries from the SolidBench benchmark across multiple metrics. Our results show that shape-based pruning substantially improves query execution time, first-result arrival time, diefficiency, and network usage for data-model selective queries, while having a negligible impact on non-selective data-model queries. These gains cost only a minor increase in triples per shape-index instance. Our approach is also resilient, retaining its benefits even when some data providers do not supply shape indexes. This work demonstrates that shape-based metadata can significantly optimize LTQP in decentralized knowledge graphs for an important class of queries. By exposing such metadata, data providers not only enhance data quality and interoperability but also improve the efficiency of traversal-based query processing.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
