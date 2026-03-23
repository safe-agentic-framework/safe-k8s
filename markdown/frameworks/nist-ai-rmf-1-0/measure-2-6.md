# NIST AI Risk Management Framework 1.0 - MEASURE 2.6

- Framework Code: NIST-AI-RMF
- Requirement Title: The AI system is evaluated regularly for safety risks - as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.

## Mapping Notes

Metrics endpoint security and AI workload telemetry provide real-time safety monitoring including model performance, inference latency, and GPU health. Distributed tracing with alerting for training divergence, model staleness, and accuracy degradation supports continuous safety evaluation.

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
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: framework-language-interpretation
