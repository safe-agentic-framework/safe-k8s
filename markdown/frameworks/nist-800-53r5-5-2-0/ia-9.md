# NIST SP 800-53 Revision 5 5.2.0 - IA-9

- Framework Code: NIST-800-53R5
- Requirement Title: Service Identification and Authentication

## Mapping Notes

Core -- agent service-to-service authentication

5.4 - SPIFFE/SPIRE workload identity (service-to-service identification and authentication); 4.4 - mTLS

## SAFE-K8S Controls

### [SAFE-K8S-0404-001 - cert-manager deployment and Issuer configuration](../../controls/SAFE-K8S-0404-001.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0404-002 - TLS provisioning for webhooks, API aggregation, and internal services](../../controls/SAFE-K8S-0404-002.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0404-003 - mTLS for service-to-service authentication](../../controls/SAFE-K8S-0404-003.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.4
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
