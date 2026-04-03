# NIST SP 800-53 Revision 5 5.2.0 - CM-6

- Framework Code: NIST-800-53R5
- Requirement Title: Configuration Settings

## Mapping Notes

Secure config settings for agent systems

1.4 - CIS benchmark application (configuration settings baseline); 1.3 - Controller-manager pod GC threshold; 2.1 - Kubelet hardening flags

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

### [SAFE-K8S-0104-005 - Control plane configuration file permissions](../../controls/SAFE-K8S-0104-005.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0201-005 - Kubelet hostname override governance](../../controls/SAFE-K8S-0201-005.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0201-008 - Kubelet configuration and credential file ownership and permissions](../../controls/SAFE-K8S-0201-008.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0201-014 - Kubelet serving certificate trust and expiry enforcement](../../controls/SAFE-K8S-0201-014.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0606-020 - Helm values override restriction and dependency integrity governance](../../controls/SAFE-K8S-0606-020.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-018 - Security-aware target-cluster posture verification before multi-cluster placement](../../controls/SAFE-K8S-0910-018.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-026 - Multi-cluster security policy baseline federation](../../controls/SAFE-K8S-0910-026.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
