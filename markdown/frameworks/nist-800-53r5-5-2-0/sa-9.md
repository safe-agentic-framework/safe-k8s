# NIST SP 800-53 Revision 5 5.2.0 - SA-9

- Framework Code: NIST-800-53R5
- Requirement Title: External System Services

## Mapping Notes

Agents rely heavily on external services (APIs, models, tools) requiring security controls

7.4 - Cloud provider security (managing external K8s services: EKS, GKE, AKS)

## SAFE-K8S Controls

### [SAFE-K8S-0704-002 - VPC and security group integration with Kubernetes network policies](../../controls/SAFE-K8S-0704-002.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0704-005 - Restricted use policies for non-organizationally owned systems and external AI services](../../controls/SAFE-K8S-0704-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
