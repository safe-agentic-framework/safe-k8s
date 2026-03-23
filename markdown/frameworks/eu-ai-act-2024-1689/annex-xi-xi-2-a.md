# EU AI Act 2024/1689 - Annex-XI:XI(2)(a)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

A description of the training approach and methodology, including any specific training techniques used, and information on the training data used and how it was collected and processed.

SAFE-K8S captures training job configurations, pipeline DAGs, data ingestion controls, and processing infrastructure. Training methodology documentation is application-layer, but SAFE-K8S provides reproducible training infrastructure records.

## SAFE-K8S Controls

### [SAFE-K8S-0904-001 - Pipeline orchestrator hardening](../../controls/SAFE-K8S-0904-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
