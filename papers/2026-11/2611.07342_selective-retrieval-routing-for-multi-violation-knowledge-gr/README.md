# Selective Retrieval Routing for Multi-Violation Knowledge Graph Repair

- arXiv: https://arxiv.org/abs/2611.07342  (v1, submitted 2026-11-05, updated 2026-11-05)
- Authors: Tung-Wei Lin, Gabe Fierro, Han Li, Tianzhen Hong, Pierluigi Nuzzo, Alberto Sangiovanni-Vinentelli
- Categories: cs.DB, cs.AI
- Collected: 2026-11-09 (KST)

## Abstract

Knowledge graphs often contain missing or inconsistent facts that undermine the applications built on them. Schema validation detects such violations but does not identify which of several valid repairs recovers the intended graph. External corpora can supply the evidence needed to identify the intended repair, but retrieving from them is costly and not always successful. We propose a framework for selective retrieval in iterative graph repair. An LLM repair agent explores and edits the graph, while a router controls its access to a researcher agent that retrieves external evidence. We extend a violation-injection framework to generate cases with multiple compatible violations and known reference repairs. The agent's repair outcomes on these cases provide supervision for training the deployment-specific router. On two building-automation datasets, researcher access improves repairs for some violations and degrades them for others, with effects differing across deployments. The router uses fewer repair-time tokens than always enabling access in all six evaluation suites. It achieves higher repair $F_1$ than always disabling access in five of six suites.

## Figure 1

![Figure 1](fig1.png)

Figure 1: The illustrated shape requires each HVAC zone to reach exactly one air-handling unit through one or more cnx edges (cnx+). Adding one edge between the existing outlet and inlet connection points satisfies this requirement. However, the equipment schedule identifies an intermediate variable air volume (VAV) box on the supply path. Recovering this documented path requires adding the VAV box and its connection points, yielding a larger (but correct) repair.
