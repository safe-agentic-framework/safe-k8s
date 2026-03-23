# EU AI Act 2024/1689 - Annex-IV:IV(2)(b)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

Information about the monitoring, functioning and control of the AI system, in particular with regard to its capabilities and limitations in performance, the degrees of accuracy for specific persons or groups of persons on which the system is intended to be used and the overall expected level of accuracy in relation to its intended purpose, the foreseeable unintended outcomes and sources of risks to health and safety, fundamental rights and discrimination.

SAFE-K8S observability controls (D10) provide monitoring infrastructure, performance metrics collection, and anomaly detection. Accuracy measurement, bias assessment, and risk documentation are application-layer concerns, though SAFE-K8S supplies the telemetry pipeline.

## SAFE-K8S Controls

### [SAFE-K8S-0805-001 - GPU telemetry collection and anomaly detection](../../controls/SAFE-K8S-0805-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
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

### [SAFE-K8S-1002-003 - AI workload telemetry integration into cluster monitoring](../../controls/SAFE-K8S-1002-003.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
