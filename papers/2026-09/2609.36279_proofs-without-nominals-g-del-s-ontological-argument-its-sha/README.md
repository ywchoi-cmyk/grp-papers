# Proofs Without Nominals: Gödel's Ontological Argument, its Shallow Embedding, and the Open Questions of the Monatshefte Notes

- arXiv: https://arxiv.org/abs/2609.36279  (v2, submitted 2026-09-28, updated 2026-10-01)
- Authors: Christoph Benzmüller
- Categories: cs.LO, cs.AI, math.LO
- Collected: 2026-10-06 (KST)

## Abstract

The shallow embedding of higher-order modal logic in classical higher-order logic, used in Benzmüller and Scott's Notes on Gödel's and Scott's variants of the ontological argument (2025), reaches beyond the modal object language of the arguments: its property quantifiers range over terms that may also express nominals and satisfaction operators of hybrid logic, and a proof using one proves a theorem of the embedding that need not be one of the modal logic. That the framework affords this is not new, and whether a result is one of the modal logic can be settled in two ways: by replaying it in an explicit proof calculus, done by hand for chosen theorems, or by analysing the proofs the embedding itself produces, done here mechanically, for every result at once. Every statement the Notes prove has a proof inside the object language: 294 written out by hand and machine-checked, none using a nominal. The proofs the Notes themselves give instantiate no nominal either; what the detector flags there are terms a prover substituted. The three questions the Notes leave open are settled too, without nominals, but the conjunction axiom has to be emended: generalised in the Notes to Gödel's "any number of summands", it covers the conjunction of no properties, and of one; the empty one alone settles all three, and the two together yield what a separate axiom of Gödel's is for. This article restricts the conjunction axiom to at least two different conjuncts, the reading Gödel's footnote suggests, and the questions are settled again, by proofs that turn on the argument rather than a degenerate instance. The restriction holds of the object language only: with a nominal the axioms make the accessibility relation the identity and the readings coincide. Every theorem is verified in Isabelle/HOL and independently in Lean 4; the countermodels are Nitpick's, certified by the build.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
