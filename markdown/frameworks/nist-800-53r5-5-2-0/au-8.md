# NIST SP 800-53 Revision 5 5.2.0 - AU-8

- Framework Code: NIST-800-53R5
- Requirement Title: Time Stamps

## Mapping Notes

Accurate timestamps for agent action correlation

2.3 - Host OS and Kernel Hardening (node time synchronization with authoritative time sources, drift monitoring, and timestamp integrity); 10.1 - Audit logging (timestamps in audit records for forensic accuracy and event correlation)

## SAFE-K8S Controls

### [SAFE-K8S-0203-016 - Node time synchronization with authoritative time sources](../../controls/SAFE-K8S-0203-016.md)

- Domain: D02 - Node, Runtime, and OS Security
- Knowledge Area: 2.3
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-051 - Model promotion approval audit binding to reviewer identity and model version](../../controls/SAFE-K8S-0905-051.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-004 - Audit volume management for AI workloads](../../controls/SAFE-K8S-1001-004.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-007 - Supplemental application-level telemetry for AI workload events](../../controls/SAFE-K8S-1001-007.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1001-008 - Permitted responses to audit findings](../../controls/SAFE-K8S-1001-008.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
