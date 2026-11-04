# Knowledge Graph Lakehouse: A Cloud-Native Architecture for Managing Enterprise Knowledge Graphs at Scale

- arXiv: https://arxiv.org/abs/2611.04899  (v1, submitted 2026-11-03, updated 2026-11-03)
- Authors: Bashar Ahmad, Christoph G. Schuetz, Loris Bozzato
- Categories: cs.DB
- Collected: 2026-11-05 (KST)

## Abstract

Modern data architectures for integrating heterogeneous data sources to discover actionable knowledge include the data warehouse, the data lake, and the data lakehouse, which combines the flexibility of the data lake with the structured data management capabilities of the data warehouse through metadata, indexes, and caching. Enterprise knowledge graphs (KGs) offer an alternative approach to such integration for the purposes of data analysis, but handling them at scale must address the Three Vs of big data: volume, velocity, and variety. Contextualized KGs (CKGs) meet part of that challenge by enriching facts with contextual information, yet many applications require only a context-specific subset of that knowledge. We propose the Knowledge Graph Lakehouse (KG Lakehouse), a cloud-native microservice architecture that adapts the data lakehouse paradigm for management of CKGs at scale. The KG Lakehouse indexes incoming source documents along configurable context dimensions and stores these documents in a data lake, from which application-specific CKGs are constructed on demand instead of maintaining a single, monolithic KG. We realize the proposed architecture as a proof of concept, with independently deployable services built from established cloud technology; context dimensions and format-specific document handling enter as configuration, leaving the architecture independent of the application domain. We evaluate the implemented system in experiments on a distributed cluster deployment.

## Figure 1

Figure 1: 추출 실패 (PDF 참조)
