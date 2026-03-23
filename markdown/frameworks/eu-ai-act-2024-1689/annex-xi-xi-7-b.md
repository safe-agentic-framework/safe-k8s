# EU AI Act 2024/1689 - Annex-XI:XI(7)(b)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

For general-purpose AI models with systemic risk, a description of the safety and security evaluations conducted.

SAFE-K8S provides security evaluation infrastructure (vulnerability scanning, penetration testing support, security gate enforcement) through D6 and D10 controls. Safety evaluation methodology and documentation are application-layer concerns.

## SAFE-K8S Controls

### [SAFE-K8S-0601-008 - CI/CD build-time container image vulnerability scanning](../../controls/SAFE-K8S-0601-008.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0606-011 - CI build-time security gate enforcement](../../controls/SAFE-K8S-0606-011.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1003-001 - STRIDE threat modeling for Kubernetes AI systems](../../controls/SAFE-K8S-1003-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
