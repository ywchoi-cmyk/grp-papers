# Reflective Compositional Grounding for Natural-Language-to-SPARQL

- arXiv: https://arxiv.org/abs/2610.21796  (v1, submitted 2026-10-15, updated 2026-10-15)
- Authors: Isabelle Mohr, John Dujany, Andre Freitas
- Categories: cs.DB
- Collected: 2026-10-19 (KST)

## Abstract

Natural-language query generation over large knowledge graphs embodies the classical vocabulary problem in human-systems communication. Questions express concepts through wording and compositions that can differ substantially from the target schema, while limited model context requires selective access to schema information. We present an NL2SPARQL framework that places conceptual compositionality at the center of query interpretation and connects it to the relational composition required for binding and query construction. A fixed concept encoder represents compound expressions jointly, and schema candidates are ranked using semantic similarity, type compatibility, and hierarchy proximity. Reflective refinement critically examines how the grounded meanings are realized through argument bindings, joins, and operator scope. Diagnosed semantic discrepancies guide revisions to the responsible stage. We formalise a monotone refinement discipline that accumulates scoped interpretation requirements and establish conditions under which changes to the composed process preserve previously validated interpretations. Across five benchmark/knowledge-graph targets, mean schema recall@10 increases from 0.712 to 0.837. With retrieval held fixed, reflective prompt rewriting adds 2.27-3.33 answer-F1 points. These experiments evaluate the grounding and refinement mechanisms, while the formal analysis specifies the stronger requirements for conservative adaptation across queries.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Reflective refinement and restricted symbolic construction extend the staged query process. Ground ranks schema candidates by c(s, e) using the fixed encoder Eθ; Bind and Construct carry them into an executable query, with an optional restricted symbolic mode checked against the graph before the default LLM mode. On a diagnosed violation, Reflect attributes it to one stage a⋆and extends only that stage’s requirement set Γa⋆(the figure’s targeted-update guarantee); specification monotonicity is proven in Appendix B.3.
