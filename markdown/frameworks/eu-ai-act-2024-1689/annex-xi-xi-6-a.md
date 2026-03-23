# EU AI Act 2024/1689 - Annex-XI:XI(6)(a)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

A model card providing information necessary for the downstream providers to comply with their obligations under this Regulation.

SAFE-K8S ML-BOM controls (D6) support model card generation through structured metadata capture: model provenance, training data lineage, resource requirements, and version tracking. However, a complete model card requires substantial application-layer content (intended use descriptions, ethical considerations, bias analysis, per-group performance data) beyond what SAFE-K8S metadata captures.

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
