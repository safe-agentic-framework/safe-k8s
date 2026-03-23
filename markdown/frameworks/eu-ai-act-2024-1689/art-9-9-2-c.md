# EU AI Act 2024/1689 - Art-9:9(2)(c)

- Framework Code: EU-AI-ACT
- Requirement Title: Risk Management System

## Mapping Notes

The risk management system shall comprise the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system referred to in Article 72.

SAFE-K8S observability and monitoring controls (D10) collect the operational data that feeds risk evaluation: inference telemetry, anomaly detection, and audit trail analysis. However, the risk evaluation itself -- determining whether new risks have emerged from post-market findings -- is an organizational activity.

## SAFE-K8S Controls

### [SAFE-K8S-1001-016 - Audit policy coverage for AI-specific resource and workflow events](../../controls/SAFE-K8S-1001-016.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-1002-002 - Distributed tracing for ML pipelines](../../controls/SAFE-K8S-1002-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1002-003 - AI workload telemetry integration into cluster monitoring](../../controls/SAFE-K8S-1002-003.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
