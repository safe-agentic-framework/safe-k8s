# EU AI Act 2024/1689 - Art-15:15(4)-resilience

- Framework Code: EU-AI-ACT
- Requirement Title: Accuracy, Robustness and Cybersecurity

## Mapping Notes

High-risk AI systems shall be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken in this regard.

Platform resilience measures include pod disruption budgets, health checks, resource limits, fault-tolerant scheduling, checkpoint security, and infrastructure redundancy -- all governed by SAFE-K8S controls.

## SAFE-K8S Controls

### [SAFE-K8S-0304-011 - Namespace LimitRange and ResourceQuota enforcement](../../controls/SAFE-K8S-0304-011.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0703-002 - Pod Disruption Budgets for workload availability](../../controls/SAFE-K8S-0703-002.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0703-005 - AI workload resource exhaustion guardrails](../../controls/SAFE-K8S-0703-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0901-003 - Checkpoint security](../../controls/SAFE-K8S-0901-003.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0901-004 - Training fault tolerance and security](../../controls/SAFE-K8S-0901-004.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
