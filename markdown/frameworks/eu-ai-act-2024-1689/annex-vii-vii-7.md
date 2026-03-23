# EU AI Act 2024/1689 - Annex-VII:VII(7)

- Framework Code: EU-AI-ACT
- Requirement Title: Conformity Based on Assessment of Quality Management System and Assessment of Technical Documentation

## Mapping Notes

The provider shall allow the notified body to carry out surveillance audits at reasonable intervals.

SAFE-K8S audit logging (D10) and RBAC (D4) can provide read-only auditor access to platform evidence. Granting physical or organizational access for surveillance is outside SAFE-K8S scope.

## SAFE-K8S Controls

### [SAFE-K8S-0401-001 - RBAC least-privilege design](../../controls/SAFE-K8S-0401-001.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-017 - Audit capture of admission, authorization, and privileged API decisions for AI workloads](../../controls/SAFE-K8S-1001-017.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-1006-004 - Automated audit readiness for Kubernetes AI platforms](../../controls/SAFE-K8S-1006-004.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.6
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
