# EU AI Act 2024/1689 - Annex-XI:XI(1)(c)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

Information on the resources used during the development of the model, including information on the type and amount of computational resources used, the training time, and other relevant information related to how the model was trained.

SAFE-K8S GPU resource tracking (D8), Kubernetes resource quota management, job scheduling records, and training pipeline telemetry (D9/D10) directly capture computational resource usage, training duration, and infrastructure configuration.

## SAFE-K8S Controls

### [SAFE-K8S-0801-001 - GPU device plugin security configuration and hardening](../../controls/SAFE-K8S-0801-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0805-001 - GPU telemetry collection and anomaly detection](../../controls/SAFE-K8S-0805-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0805-002 - GPU allocation audit trail and workload identity tracking](../../controls/SAFE-K8S-0805-002.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0901-006 - Gang scheduling security (Volcano, Kueue)](../../controls/SAFE-K8S-0901-006.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
