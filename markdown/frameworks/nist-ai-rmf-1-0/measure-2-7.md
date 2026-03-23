# NIST AI Risk Management Framework 1.0 - MEASURE 2.7

- Framework Code: NIST-AI-RMF
- Requirement Title: AI system security and resilience - as identified in the MAP function - are evaluated and documented.

## Mapping Notes

STRIDE threat modeling evaluates security posture across six threat categories. MITRE ATT&CK mapping evaluates defense coverage across attack tactics. ML threat taxonomy evaluates AI-specific attack resilience. Runtime security tools continuously evaluate system security.

## SAFE-K8S Controls

### [SAFE-K8S-0101-005 - Streaming connection idle timeout enforcement](../../controls/SAFE-K8S-0101-005.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.1
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: semantic-mismatch-candidate

### [SAFE-K8S-0103-006 - Profiling endpoint disablement for controller-manager and scheduler](../../controls/SAFE-K8S-0103-006.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.3
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: semantic-mismatch-candidate

### [SAFE-K8S-0201-005 - Kubelet hostname override governance](../../controls/SAFE-K8S-0201-005.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.1
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: implementation-specific

### [SAFE-K8S-0204-001 - Runtime security tool deployment for syscall and network monitoring](../../controls/SAFE-K8S-0204-001.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-coverage

### [SAFE-K8S-0403-006 - Per-workload credential scoping for AI jobs](../../controls/SAFE-K8S-0403-006.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: semantic-mismatch-candidate

### [SAFE-K8S-1003-001 - STRIDE threat modeling for Kubernetes AI systems](../../controls/SAFE-K8S-1003-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-1003-005 - Technique-aligned detection engineering for Kubernetes AI attack scenarios](../../controls/SAFE-K8S-1003-005.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: compound-control-split-required

### [SAFE-K8S-1004-001 - ML threat taxonomy per CTA-2114 mapped to Kubernetes](../../controls/SAFE-K8S-1004-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.4
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: compound-control-split-required
