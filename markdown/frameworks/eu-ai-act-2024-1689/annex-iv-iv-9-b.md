# EU AI Act 2024/1689 - Annex-IV:IV(9)(b)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

The degree to which the logging enables adequate tracing of the AI system's functioning throughout its lifecycle.

SAFE-K8S provides tracing infrastructure through distributed tracing, deployment history, pipeline execution records, and model versioning. However, ensuring adequate tracing of AI system functioning requires application-layer instrumentation (inference logging, decision auditing) beyond platform-level tracing.

## SAFE-K8S Controls

### [SAFE-K8S-0905-006 - Model artifact lifecycle management](../../controls/SAFE-K8S-0905-006.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-1001-007 - Supplemental application-level telemetry for AI workload events](../../controls/SAFE-K8S-1001-007.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1002-002 - Distributed tracing for ML pipelines](../../controls/SAFE-K8S-1002-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
