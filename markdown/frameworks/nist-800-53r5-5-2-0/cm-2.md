# NIST SP 800-53 Revision 5 5.2.0 - CM-2

- Framework Code: NIST-800-53R5
- Requirement Title: Baseline Configuration

## Mapping Notes

Agent system baseline configs

1.4 - Apply CIS benchmarks (baseline configuration); 3.2 - AI workload security context patterns as baseline

## SAFE-K8S Controls

### [SAFE-K8S-0104-005 - Control plane configuration file permissions](../../controls/SAFE-K8S-0104-005.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0302-001 - Pod and container security context enforcement](../../controls/SAFE-K8S-0302-001.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0302-002 - Linux capability drop-all and least-privilege add-back](../../controls/SAFE-K8S-0302-002.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0302-004 - Host namespace isolation enforcement](../../controls/SAFE-K8S-0302-004.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0302-005 - AI workload security context hardening profiles](../../controls/SAFE-K8S-0302-005.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
