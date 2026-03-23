# NIST AI Risk Management Framework 1.0 - MAP 2.1

- Framework Code: NIST-AI-RMF
- Requirement Title: The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders).

## Mapping Notes

AI system classification requires documenting system type (training, serving, pipeline) and assigning appropriate control profiles. Label standards classify workloads by type.

## SAFE-K8S Controls

### [SAFE-K8S-0702-005 - Label and annotation schema definition for AI workload classification](../../controls/SAFE-K8S-0702-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-0905-001 - AI system lifecycle classification](../../controls/SAFE-K8S-0905-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
