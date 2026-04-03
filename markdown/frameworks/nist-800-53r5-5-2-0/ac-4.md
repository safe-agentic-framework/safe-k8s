# NIST SP 800-53 Revision 5 5.2.0 - AC-4

- Framework Code: NIST-800-53R5
- Requirement Title: Information Flow Enforcement

## Mapping Notes

Core to agent data flow control between trust boundaries

5.1 - Implement network policies (default deny, namespace isolation, egress controls for information flow enforcement)

## SAFE-K8S Controls

### [SAFE-K8S-0501-001 - Default deny ingress and egress network policies](../../controls/SAFE-K8S-0501-001.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-002 - Namespace network isolation patterns](../../controls/SAFE-K8S-0501-002.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-003 - Workload egress controls](../../controls/SAFE-K8S-0501-003.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-004 - CNI-specific network policy extensions](../../controls/SAFE-K8S-0501-004.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-006 - Multi-cluster network segmentation for federated AI workloads](../../controls/SAFE-K8S-0501-006.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-007 - East-west AI workload traffic monitoring](../../controls/SAFE-K8S-0501-007.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-008 - AI workload type network microsegmentation](../../controls/SAFE-K8S-0501-008.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-034 - Canary and A/B candidate version isolation and traffic-splitting integrity](../../controls/SAFE-K8S-0905-034.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-022 - Cross-cluster communication authorization policy enforcement](../../controls/SAFE-K8S-0910-022.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
