# EU AI Act 2024/1689 - Annex-XI:XI(2)(c)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

Where applicable, a description of the fine-tuning procedures that were applied, including the fine-tuning data used and how the fine-tuning affected the model's performance on the specific tasks.

SAFE-K8S tracks fine-tuning job execution, resource consumption, and model versioning through ML-BOM lineage. Fine-tuning methodology documentation is application-layer, but SAFE-K8S provides the infrastructure audit trail.

## SAFE-K8S Controls

### [SAFE-K8S-0604-002 - ML-BOM (ML Bill of Materials) generation](../../controls/SAFE-K8S-0604-002.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-0905-006 - Model artifact lifecycle management](../../controls/SAFE-K8S-0905-006.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
