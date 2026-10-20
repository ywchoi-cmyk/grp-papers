# Reranking Answers of Large Language Models with Knowledge Graphs

- arXiv: https://arxiv.org/abs/2610.25185  (v1, submitted 2026-10-18, updated 2026-10-18)
- Authors: Mikhail Salnikov, Hai Le, Olga Tsymboi, Ivan Lazichny, Dmitrii Iarosh, Egor Cheremiskin, Andrey Savchenko, Dmitry Simakov, Alexander Panchenko
- Categories: cs.CL, cs.AI
- Collected: 2026-10-21 (KST)

## Abstract

Answering natural language questions over knowledge graph data is challenging due to the vast number of facts, which can be difficult to process and navigate. One potential solution for this issue is to use mined subgraphs related to the query, although this process still requires extracting these subgraphs. This research presents a solution for extracting subgraphs related to entity candidates from a question-and-answer set, which can be obtained by inferring a large language model by calculating the shortest paths between entities. The proposed approaches detail various features that can be extracted from the subgraphs and reranking models to select the most probable answers from a list of candidates. Experiments were conducted on Wikidata to evaluate the effectiveness of the proposed approaches. This involved enumerating all the main feature types that can be extracted from mined subgraphs and a detailed analysis of the proposed features and reranking method combinations. In addition, a public web application that provides a useful web tool for studying the graph space between question and answer entities has been developed to work with subgraphs. This includes visualization of the extracted subgraph and automatic generation of natural language text to describe it.

## Figure 1

![Figure 1](fig1.png)

Fig. 1. The motivation of our research: LLM’s top-1 QA prediction accuracy is often incorrect. However, the correct answer is often in the top 10-40 alternative generations. Thus, a better reranking, such as the one presented in this article, is required. Dependence of Hit@N metric on the size of answer pool N on Mintaka [32] full dataset and Mistral [11], Mixtral [12], T5-Large-SSM and T5-XL-SSM [26] tuned models using Diverse Beam Search [39] as an inference strategy.
