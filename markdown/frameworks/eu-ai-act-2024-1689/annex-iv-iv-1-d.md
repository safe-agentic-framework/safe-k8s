# EU AI Act 2024/1689 - Annex-IV:IV(1)(d)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

A description of the system architecture explaining how software components build on or feed into each other and of the computational resources used to develop, train, test and validate the AI system.

SAFE-K8S directly captures system architecture through Kubernetes deployment manifests, service topologies, resource quotas, GPU allocations (D8), and pipeline DAG definitions (D9). Computational resource tracking is native to Kubernetes scheduling.

## SAFE-K8S Controls

### [SAFE-K8S-0702-005 - Label and annotation schema definition for AI workload classification](../../controls/SAFE-K8S-0702-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0801-001 - GPU device plugin security configuration and hardening](../../controls/SAFE-K8S-0801-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0904-001 - Pipeline orchestrator hardening](../../controls/SAFE-K8S-0904-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
