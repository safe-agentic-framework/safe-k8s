# EU AI Act 2024/1689 - Art-9:9(5)(a)

- Framework Code: EU-AI-ACT
- Requirement Title: Risk Management System

## Mapping Notes

Risk management measures shall ensure elimination or reduction of risks in as far as technically feasible through adequate design and development of the high-risk AI system.

SAFE-K8S controls implement risk reduction through secure design: minimal base images, least-privilege access, default-deny networking, supply chain integrity, and runtime hardening.

## SAFE-K8S Controls

### [SAFE-K8S-0302-001 - Pod and container security context enforcement](../../controls/SAFE-K8S-0302-001.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0401-001 - RBAC least-privilege design](../../controls/SAFE-K8S-0401-001.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-001 - Default deny ingress and egress network policies](../../controls/SAFE-K8S-0501-001.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0601-014 - Container image runtime hardening with non-root and read-only filesystem](../../controls/SAFE-K8S-0601-014.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
