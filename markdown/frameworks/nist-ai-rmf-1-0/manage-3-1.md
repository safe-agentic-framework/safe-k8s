# NIST AI Risk Management Framework 1.0 - MANAGE 3.1

- Framework Code: NIST-AI-RMF
- Requirement Title: AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

## Mapping Notes

Dependency tracking with SLSA build provenance monitors third-party component risks. Vulnerability prioritization for AI workloads provides ongoing risk assessment. Restricted use policies govern external AI service consumption.

## SAFE-K8S Controls

### [SAFE-K8S-0604-009 - AI workload vulnerability prioritization and remediation SLAs](../../controls/SAFE-K8S-0604-009.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: compound-control-split-required

### [SAFE-K8S-0704-005 - Restricted use policies for non-organizationally owned systems and external AI services](../../controls/SAFE-K8S-0704-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.4
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0905-052 - Approved external model source allowlist definition and maintenance](../../controls/SAFE-K8S-0905-052.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-053 - Approved external model source periodic review and allowlist update governance](../../controls/SAFE-K8S-0905-053.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-057 - External model trust-signal assessment and approval review](../../controls/SAFE-K8S-0905-057.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
