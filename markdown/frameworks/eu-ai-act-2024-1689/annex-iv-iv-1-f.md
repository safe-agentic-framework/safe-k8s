# EU AI Act 2024/1689 - Annex-IV:IV(1)(f)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

Where relevant, information about the use of pre-trained systems and other third-party tools integrated into the AI system, as well as information about the training data used to train those systems.

SAFE-K8S supply chain controls (D6) track model provenance via ML-BOMs and SBOMs. Container image scanning and registry controls verify third-party components. Full upstream training data documentation requires organizational effort.

## SAFE-K8S Controls

### [SAFE-K8S-0604-001 - SBOM generation for container and AI artifacts](../../controls/SAFE-K8S-0604-001.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0604-002 - ML-BOM (ML Bill of Materials) generation](../../controls/SAFE-K8S-0604-002.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
