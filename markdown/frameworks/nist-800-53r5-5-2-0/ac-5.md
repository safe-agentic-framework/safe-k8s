# NIST SP 800-53 Revision 5 5.2.0 - AC-5

- Framework Code: NIST-800-53R5
- Requirement Title: Separation of Duties

## Mapping Notes

Separating agent roles (executor vs. approver)

4.1 - Design and enforce RBAC (separation of duties between ML engineers, platform engineers, security teams)

## SAFE-K8S Controls

### [SAFE-K8S-0401-001 - RBAC least-privilege design](../../controls/SAFE-K8S-0401-001.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0401-002 - RBAC permission audit and analysis](../../controls/SAFE-K8S-0401-002.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0401-003 - Aggregated ClusterRole governance](../../controls/SAFE-K8S-0401-003.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0401-004 - RBAC for AI operator custom resources](../../controls/SAFE-K8S-0401-004.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0401-006 - Organizational role separation for ML, platform, and security functions](../../controls/SAFE-K8S-0401-006.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0905-025 - Separation of duties enforcement for model promotion approvals](../../controls/SAFE-K8S-0905-025.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
