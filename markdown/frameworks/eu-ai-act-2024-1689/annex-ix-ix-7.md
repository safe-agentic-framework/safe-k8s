# EU AI Act 2024/1689 - Annex-IX:IX(7)

- Framework Code: EU-AI-ACT
- Requirement Title: Information to be Submitted Upon Registration for Testing in Real World Conditions in Accordance with Article 60

## Mapping Notes

A description of the safeguards and risk mitigation measures put in place, including the measures taken to protect the fundamental rights and personal data of the subjects of the testing.

SAFE-K8S provides technical safeguards relevant to real-world testing: workload isolation (D3), network segmentation (D5), access controls (D4), and data protection controls (D7). Fundamental rights protections and organizational safeguards are outside SAFE-K8S scope.

## SAFE-K8S Controls

### [SAFE-K8S-0302-001 - Pod and container security context enforcement](../../controls/SAFE-K8S-0302-001.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

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

### [SAFE-K8S-0701-003 - Encryption at rest for persistent volumes](../../controls/SAFE-K8S-0701-003.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
