# NIST AI Risk Management Framework 1.0 - MANAGE 4.1

- Framework Code: NIST-AI-RMF
- Requirement Title: Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.

## Mapping Notes

SAFE-K8S provides comprehensive post-deployment infrastructure: audit policies for AI workload monitoring, metrics and tracing for performance evaluation, IR playbooks for incident response, ransomware response for recovery, and change management for controlled lifecycle transitions.

## SAFE-K8S Controls

### [SAFE-K8S-0101-005 - Streaming connection idle timeout enforcement](../../controls/SAFE-K8S-0101-005.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.1
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: implementation-specific

### [SAFE-K8S-0201-005 - Kubelet hostname override governance](../../controls/SAFE-K8S-0201-005.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0203-016 - Node time synchronization with authoritative time sources](../../controls/SAFE-K8S-0203-016.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.3
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-016 - Audit policy coverage for AI-specific resource and workflow events](../../controls/SAFE-K8S-1001-016.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-1002-001 - Metric endpoint authentication](../../controls/SAFE-K8S-1002-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: semantic-mismatch-candidate

### [SAFE-K8S-1005-001 - Kubernetes incident response lifecycle](../../controls/SAFE-K8S-1005-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.5
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
- Strength Reason Code: partial-control-coverage
