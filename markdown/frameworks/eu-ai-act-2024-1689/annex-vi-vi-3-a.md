# EU AI Act 2024/1689 - Annex-VI:VI(3)(a)

- Framework Code: EU-AI-ACT
- Requirement Title: Conformity Assessment Procedure Based on Internal Control Referred to in Article 43(2)

## Mapping Notes

The provider examines the information and documentation collected in accordance with Annex IV to assess the compliance of the AI system with the relevant essential requirements.

SAFE-K8S generates much of the technical documentation referenced in Annex IV: system architecture records, cybersecurity controls documentation, logging configurations, change tracking artifacts, and post-market monitoring infrastructure evidence. However, the act of examining documentation for compliance is an organizational activity.

## SAFE-K8S Controls

### [SAFE-K8S-0604-001 - SBOM generation for container and AI artifacts](../../controls/SAFE-K8S-0604-001.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-016 - Audit policy coverage for AI-specific resource and workflow events](../../controls/SAFE-K8S-1001-016.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-1007-005 - Change management for production AI model deployments](../../controls/SAFE-K8S-1007-005.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.7
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
