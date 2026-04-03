# NIST SP 800-53 Revision 5 5.2.0 - CM-5

- Framework Code: NIST-800-53R5
- Requirement Title: Access Restrictions for Change

## Mapping Notes

Restricting who can change agent configs

6.6 - GitOps (repository access controls, branch protection for change restrictions); 1.4 - Control plane configuration file permissions; 2.1 - Kubelet hostname override governance (change control for --hostname-override)

## SAFE-K8S Controls

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

### [SAFE-K8S-0606-002 - CI/CD build environment hardening](../../controls/SAFE-K8S-0606-002.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0606-007 - CI/CD build activity monitoring](../../controls/SAFE-K8S-0606-007.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0606-009 - SSDF v1.1 alignment for secure development practices](../../controls/SAFE-K8S-0606-009.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0606-024 - Policy-as-code and runtime configuration integrity governance](../../controls/SAFE-K8S-0606-024.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
