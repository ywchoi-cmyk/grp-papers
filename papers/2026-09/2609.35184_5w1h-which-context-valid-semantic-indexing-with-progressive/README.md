# 5W1H+Which: Context-Valid Semantic Indexing with Progressive Ontology Binding

- arXiv: https://arxiv.org/abs/2609.35184  (v1, submitted 2026-09-28, updated 2026-09-28)
- Authors: Yaxiao Liu, Pengbo Liu, Yiwen Liu, Yihua Guan, Jiaxing Song
- Categories: cs.AI, cs.CL, cs.IR
- Collected: 2026-10-06 (KST)

## Abstract

Transforming raw data into queryable knowledge requires both early extraction of reusable information and explicit types, relations, and applicability conditions for particular tasks. If indexing selects content too early around a single business schema, later tasks may be unable to use information that was omitted. If the index retains only open-ended text, however, rule-based reasoning lacks checkable premises. We propose 5W1H+Which, a semantic indexing design that separates content extraction from ontology binding. The 5W1H questions organize source-grounded content units; Which points to versioned ontology elements and records mapping relations, scope, and validation status. Time, location, system environment, and participant roles are not merely retrieval labels: together, they constrain the contexts in which facts, bindings, and rules apply. Unbound content remains searchable, while bound content enters a formal reasoning path only after premise checks. The method further distinguishes business valid time, system knowledge time, and operational traces, and uses dependency records to support binding revalidation and the maintenance of derived conclusions. A worked example of migration from an on-premises server to a cloud environment illustrates the different treatment of world-state changes, ontology-version changes, and changes in rule applicability. We formulate three groups of falsifiable hypotheses concerning cross-task evidence coverage, control of contextual misuse, and incremental update cost. The planned evaluation includes a strong typed fact-graph baseline with the same evidence, temporal information, and budget, to test whether benefits arise from 5W1H organization, deferred binding, or additional information and engineering effort. The contribution is a testable indexing mechanism, not a claim to a new universal ontology or a demonstrated performance advantage.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
