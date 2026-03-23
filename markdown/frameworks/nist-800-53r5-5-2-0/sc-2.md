# NIST SP 800-53 Revision 5 5.2.0 - SC-2

- Framework Code: NIST-800-53R5
- Requirement Title: Separation of System and User Functionality

## Mapping Notes

Separating agent system functions from user-facing interfaces prevents privilege escalation

7.2 - Namespace isolation (system vs user workload separation); 1.3 - Control plane component isolation

## SAFE-K8S Controls

### [SAFE-K8S-0103-001 - Controller-manager service account token hardening](../../controls/SAFE-K8S-0103-001.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0103-005 - Pod garbage collection threshold configuration](../../controls/SAFE-K8S-0103-005.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0103-006 - Profiling endpoint disablement for controller-manager and scheduler](../../controls/SAFE-K8S-0103-006.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0702-003 - LimitRange enforcement for containers and pods](../../controls/SAFE-K8S-0702-003.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0702-005 - Label and annotation schema definition for AI workload classification](../../controls/SAFE-K8S-0702-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0702-018 - Namespace tenant boundary model and isolation limitation documentation](../../controls/SAFE-K8S-0702-018.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
