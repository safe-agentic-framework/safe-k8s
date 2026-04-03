# NIST SP 800-53 Revision 5 5.2.0 - SC-8

- Framework Code: NIST-800-53R5
- Requirement Title: Transmission Confidentiality and Integrity

## Mapping Notes

Agent communications must be protected for confidentiality and integrity in transit

5.2 - Pod-to-pod encryption; 5.4 - mTLS (transmission confidentiality and integrity)

## SAFE-K8S Controls

### [SAFE-K8S-0502-001 - CNI plugin security selection criteria](../../controls/SAFE-K8S-0502-001.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0502-002 - Pod-to-pod traffic encryption](../../controls/SAFE-K8S-0502-002.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0502-004 - CNI plugin hardening and lifecycle management](../../controls/SAFE-K8S-0502-004.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0502-005 - AI workload data path encryption in transit](../../controls/SAFE-K8S-0502-005.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0504-001 - Zero trust networking principles for Kubernetes](../../controls/SAFE-K8S-0504-001.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0504-002 - Service mesh mTLS and authorization policies](../../controls/SAFE-K8S-0504-002.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0504-005 - Service mesh tuning for AI workloads](../../controls/SAFE-K8S-0504-005.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-004 - Federated learning cross-cluster coordination security](../../controls/SAFE-K8S-0910-004.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-020 - Cross-cluster transport encryption for distributed AI traffic](../../controls/SAFE-K8S-0910-020.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-030 - Cross-cluster registry replication channel mutual authentication](../../controls/SAFE-K8S-0910-030.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
