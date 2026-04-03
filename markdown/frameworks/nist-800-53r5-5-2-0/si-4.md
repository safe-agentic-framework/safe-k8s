# NIST SP 800-53 Revision 5 5.2.0 - SI-4

- Framework Code: NIST-800-53R5
- Requirement Title: System Monitoring

## Mapping Notes

System monitoring of agent behavior, resource usage, and communications detects anomalies

10.1 - Logging and Audit (comprehensive system monitoring); 2.4 - Runtime security tools

## SAFE-K8S Controls

### [SAFE-K8S-0204-001 - Runtime security tool deployment for syscall and network monitoring](../../controls/SAFE-K8S-0204-001.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0204-002 - Kubernetes-specific runtime detection rules](../../controls/SAFE-K8S-0204-002.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0204-003 - Container filesystem drift detection](../../controls/SAFE-K8S-0204-003.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0204-004 - Forensic capture capabilities for container incident investigation](../../controls/SAFE-K8S-0204-004.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-035 - Automatic canary rollback on error-rate and latency degradation](../../controls/SAFE-K8S-0905-035.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-036 - Automated AI workload circuit-breaker threshold enforcement](../../controls/SAFE-K8S-0905-036.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-004 - Federated learning cross-cluster coordination security](../../controls/SAFE-K8S-0910-004.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-032 - Cross-cluster traffic anomaly monitoring for distributed AI workloads](../../controls/SAFE-K8S-0910-032.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-004 - Audit volume management for AI workloads](../../controls/SAFE-K8S-1001-004.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-007 - Supplemental application-level telemetry for AI workload events](../../controls/SAFE-K8S-1001-007.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-008 - Permitted responses to audit findings](../../controls/SAFE-K8S-1001-008.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
