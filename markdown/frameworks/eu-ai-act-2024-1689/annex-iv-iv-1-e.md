# EU AI Act 2024/1689 - Annex-IV:IV(1)(e)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

Where relevant, the data requirements in terms of datasheets describing the training methodologies and techniques and the training data sets used, including a general description of these data sets, information about their provenance, scope and main characteristics; how the data was obtained and selected; labelling procedures and data-cleaning methodologies.

SAFE-K8S D9 controls cover training data integrity, data pipeline provenance, and storage access controls for datasets. Dataset documentation (datasheets) is an application-layer responsibility, but SAFE-K8S enforces access controls and audit trails on data stores.

## SAFE-K8S Controls

### [SAFE-K8S-0906-002 - Large-scale data integrity verification](../../controls/SAFE-K8S-0906-002.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.6
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
