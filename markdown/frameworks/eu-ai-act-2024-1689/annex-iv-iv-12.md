# EU AI Act 2024/1689 - Annex-IV:IV(12)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

Information about the training methodologies and techniques, the key design choices and assumptions, the optimisation approaches and parameters, the data requirements and the outcome of the training and validation, including information about the validation data sets used and the testing methodology.

SAFE-K8S captures training job configurations, resource allocations, hyperparameter tracking via experiment management integration, and validation pipeline results. Methodology documentation is application-layer, but SAFE-K8S provides infrastructure for reproducible training and validation artifact management.

## SAFE-K8S Controls

### [SAFE-K8S-0604-002 - ML-BOM (ML Bill of Materials) generation](../../controls/SAFE-K8S-0604-002.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-0901-003 - Checkpoint security](../../controls/SAFE-K8S-0901-003.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
