# NIST AI Risk Management Framework 1.0 - MEASURE 1.1

- Framework Code: NIST-AI-RMF
- Requirement Title: Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or outcomes that cannot be measured through quantitative means are addressed qualitatively.

## Mapping Notes

AI workload telemetry and metrics endpoint security provide the measurement infrastructure. Distributed tracing enables quantitative measurement of AI pipeline behavior.

## SAFE-K8S Controls

### [SAFE-K8S-1002-001 - Metric endpoint authentication](../../controls/SAFE-K8S-1002-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-1002-002 - Distributed tracing for ML pipelines](../../controls/SAFE-K8S-1002-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: partial
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
