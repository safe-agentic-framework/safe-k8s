# NIST SP 800-53 Revision 5 5.2.0 - SC-3

- Framework Code: NIST-800-53R5
- Requirement Title: Security Function Isolation

## Mapping Notes

Isolating security functions in agent systems prevents compromise of authorization and audit

1.3 - Control plane component isolation; 2.2 - Sandboxed runtimes (security function isolation)

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

### [SAFE-K8S-0202-002 - RuntimeClass configuration for workload-appropriate isolation](../../controls/SAFE-K8S-0202-002.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0202-003 - Container runtime patching and version management](../../controls/SAFE-K8S-0202-003.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0202-004 - Runtime socket mount prevention](../../controls/SAFE-K8S-0202-004.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
