# NIST AI Risk Management Framework 1.0 - MEASURE 1.2

- Framework Code: NIST-AI-RMF
- Requirement Title: Appropriateness of AI metrics and effectiveness of existing measures are regularly assessed and updated, including measures of accuracy, fairness and bias, data quality, security, explainability, and privacy.

## Mapping Notes

Metrics endpoint security ensures telemetry integrity and availability. GPU telemetry collection supports hardware-level measurement validation. Security posture management drives continuous metric reassessment.

## SAFE-K8S Controls

### [SAFE-K8S-0805-001 - GPU telemetry collection and anomaly detection](../../controls/SAFE-K8S-0805-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
- Relation Type: partial
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-1002-001 - Metric endpoint authentication](../../controls/SAFE-K8S-1002-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-1007-004 - Continuous security posture management for AI clusters](../../controls/SAFE-K8S-1007-004.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.7
- Relation Type: partial
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
