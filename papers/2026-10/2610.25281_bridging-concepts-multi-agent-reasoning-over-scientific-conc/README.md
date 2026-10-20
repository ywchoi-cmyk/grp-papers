# Bridging Concepts: Multi-Agent Reasoning over Scientific Concept Graphs for High-Impact Research Prediction

- arXiv: https://arxiv.org/abs/2610.25281  (v1, submitted 2026-10-18, updated 2026-10-18)
- Authors: Donggyu Yoon, Minsung Hwang, Juneha Baek, Donghyuk Shin, Joyce Jiyoung Whang
- Categories: cs.AI, cs.IR, cs.LG
- Collected: 2026-10-21 (KST)

## Abstract

Within a research community, new topics often emerge when previously unconnected concepts are first studied together. We construct scientific concept graphs (SCGs)--domain knowledge graphs whose nodes are fine-grained research concepts extracted from paper text by LLMs and whose edges capture their co-occurrence in papers--and study the task of forecasting high-impact concept pairs, i.e., discovering concept pairs that are currently unconnected but will have high impact when connected. To this end, we introduce new benchmark datasets constructed from CIKM, KDD, and SIGIR conference papers, with varied prediction settings, including impact forecasting for emerging concepts unseen during training. We propose MiroGraph, a Multi-agent reasoning framework with scientific concept Graphs, in which a feature designer agent designs predictive features for a given concept pair from structural, semantic, and trend perspectives, and then three LLM agents compute the actual feature values from the enclosing subgraph of the concept pair. Using these feature values, a classifier designer agent constructs a classifier that predicts the final impact labels. MiroGraph outperforms various impact forecasting and temporal link prediction methods.

## Figure 1

![Figure 1](fig1.png)

Figure 1: Overview of MiroGraph. MiroGraph extracts an enclosing subgraph and employs a feature designer agent to determine predictive feature types based on statistics of the SCG. Three LLM agents compute feature values from structural, semantic, and trend perspectives. A classifier designer agent constructs classifiers to predict the final impact label based on the feature values.
