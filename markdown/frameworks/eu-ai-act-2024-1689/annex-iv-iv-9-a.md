# EU AI Act 2024/1689 - Annex-IV:IV(9)(a)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

Logging capabilities in accordance with Article 12, including information on the type and nature of events logged and the format of such logging.

SAFE-K8S audit logging controls (D10) provide comprehensive logging infrastructure including Kubernetes audit logs, workload logs, GPU utilization logs, and AI pipeline execution logs with structured formats.

## SAFE-K8S Controls

### [SAFE-K8S-0805-002 - GPU allocation audit trail and workload identity tracking](../../controls/SAFE-K8S-0805-002.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
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
