# Narrow and Deep: An Ontology Tower as the Knowledge of an LLM Agent for an Industrial Equipment System

- arXiv: https://arxiv.org/abs/2610.11768  (v1, submitted 2026-10-08, updated 2026-10-08)
- Authors: Younghwan Joo, Sung-il Kim
- Categories: eess.SY, cs.AI
- Collected: 2026-10-12 (KST)

## Abstract

Large language model (LLM) agents are beginning to operate industrial energy equipment, and what they get right depends on what they are told about the plant. Established building ontologies name many kinds of points across many sites, whereas an industrial equipment system needs few entities with much knowledge about each. This study proposes the ontology tower, a narrow-and-deep ontology of a single equipment system whose knowledge deepens in two ways: through quantities derived from the measured points by physical relations, and through lessons from the operating journal incorporated as knowledge nodes. On a real low-humidity air-handling test plant operated daily through a programmable logic controller, agents received a text projected from its tower in a preregistered evaluation of nine tasks replayed from the plant's records, using four open-weight models from 9 to about 750 billion parameters. This knowledge raised the rate at which the agents avoided the most plausible misjudgment of each task by about 20 percentage points, and the overall task score of the 9-billion-parameter model as much as that of the largest. Operating lessons were used when incorporated into the tower or placed in the prompt as records, but seldom when left in the journal behind a search tool. In live runs through an invariant safety layer, the agents brought the controlled variable into its target band in 12 of 14 runs. An ontology narrow in entities but deep in what is known about them can thus supply the knowledge that an agent for an industrial equipment system needs.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Ontology tower of the studied system: node counts at each computed level, two dependency chains that fix the levels, and the node and edge kinds of the interchange schema.
