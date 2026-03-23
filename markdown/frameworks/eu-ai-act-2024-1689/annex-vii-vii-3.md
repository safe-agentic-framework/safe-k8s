# EU AI Act 2024/1689 - Annex-VII:VII(3)

- Framework Code: EU-AI-ACT
- Requirement Title: Conformity Based on Assessment of Quality Management System and Assessment of Technical Documentation

## Mapping Notes

The application shall include all relevant information, including the documentation of the quality management system and the technical documentation of the AI system referred to in Annex IV.

SAFE-K8S generates technical documentation artifacts referenced in Annex IV (architecture records, cybersecurity controls, logging configurations, change tracking). These form a subset of the information package submitted with the application.

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

### [SAFE-K8S-1001-016 - Audit policy coverage for AI-specific resource and workflow events](../../controls/SAFE-K8S-1001-016.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
