# EU AI Act 2024/1689 - Annex-VI:VI(3)

- Framework Code: EU-AI-ACT
- Requirement Title: Conformity Assessment Procedure Based on Internal Control Referred to in Article 43(2)

## Mapping Notes

The provider verifies that the AI system is in conformity with the relevant essential requirements set out in Chapter III, Section 2.

SAFE-K8S controls map to several Chapter III Section 2 requirements (cybersecurity per Article 15, logging per Article 12, risk management infrastructure per Article 9). SAFE-K8S provides technical evidence of conformity for platform-layer requirements.

## SAFE-K8S Controls

### [SAFE-K8S-0401-001 - RBAC least-privilege design](../../controls/SAFE-K8S-0401-001.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-001 - Default deny ingress and egress network policies](../../controls/SAFE-K8S-0501-001.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
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

### [SAFE-K8S-1006-001 - Regulatory compliance mapping for Kubernetes AI platforms](../../controls/SAFE-K8S-1006-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.6
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
