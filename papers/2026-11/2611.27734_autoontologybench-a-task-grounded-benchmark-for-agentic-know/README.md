# AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering

- arXiv: https://arxiv.org/abs/2611.27734  (v1, submitted 2026-11-20, updated 2026-11-20)
- Authors: Minye Shao, Chenghao Xiao, Xingyue Zhao, Yang Long
- Categories: cs.CL
- Collected: 2026-11-24 (KST)

## Abstract

Foundation-model agents are increasingly extending beyond software engineering (SWE) into autonomous scientific research, where acquiring and integrating domain knowledge remains a critical challenge. Recent industrial advances have increasingly adopted knowledge graphs and ontology-based semantic layers to organize heterogeneous knowledge into reusable representations. We ask: Can autonomous agents construct ontologies that help them solve real tasks, and do they offer measurable benefits over alternative knowledge representations? Existing benchmarks evaluate ontology correctness or agent task success in isolation, leaving the value of autonomously acquired knowledge unresolved. We therefore introduce AutoOntologyBench, a task-grounded benchmark comprising 19,947 audited tasks grounded in 18 real-world knowledge sources across 7 domains, with source-native verification. Spanning Application, Repair, Organization, and Construction, AutoOntologyBench compares nine frontier-model agents under matched knowledge representations. Layered on retrieval, agent-built ontologies add 6.1 points of task success, yet trail an expert-derived reference by 13.0, identifying autonomous knowledge acquisition as the bottleneck to scalable scientific research. Code and resources are available at https://github.com/VinyehShaw/AutoOntologyBench.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Overview of AutoOntologyBench, illustrated with one Gatekeeper task. Left: the audited bank, 19,947 tasks in 16 lanes, with seven domains (inner ring) and pinned sources (outer ring). Right: (1) a pinned source, here a Kubernetes policy rule that every namespace needs an owner label; (2) the task factory fetches and pins the source, builds a task and its private oracle by solving it natively with the Open Policy Agent (OPA) The Open Policy Agent Authors (2026), and qualifies it through native verification; (3) the task’s regime, here Repair, and the public task the agent sees; (4) the knowledge representation the agent builds, here an ontology, with Direct, RAG, and a native DSL as the alternatives; (5) execution with the same native tools in every condition; (6) the native verifier checks the final state against the private oracle, and we report task success and valid task success.
