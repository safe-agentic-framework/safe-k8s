# EU AI Act 2024/1689 - Annex-XI:XI(7)(a)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

For general-purpose AI models with systemic risk, information about the computational resources used for training the model, the amount of training data, and the total compute used.

SAFE-K8S GPU tracking (D8), resource quota management, and training pipeline telemetry (D9/D10) directly capture compute resources, training data volumes, and total FLOPS consumed during training on Kubernetes infrastructure.

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
