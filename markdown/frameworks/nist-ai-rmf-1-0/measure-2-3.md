# NIST AI Risk Management Framework 1.0 - MEASURE 2.3

- Framework Code: NIST-AI-RMF
- Requirement Title: AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment conditions. Measurement results regarding AI system trustworthiness in deployment conditions and across the AI lifecycle are documented.

## Mapping Notes

AI workload telemetry measures performance in production conditions. Distributed tracing tracks behavior across ML pipeline stages from training through serving.

## SAFE-K8S Controls

### [SAFE-K8S-0805-001 - GPU telemetry collection and anomaly detection](../../controls/SAFE-K8S-0805-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-1002-001 - Metric endpoint authentication](../../controls/SAFE-K8S-1002-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: semantic-mismatch-candidate

### [SAFE-K8S-1002-002 - Distributed tracing for ML pipelines](../../controls/SAFE-K8S-1002-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: partial
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
