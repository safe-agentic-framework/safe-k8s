# EU AI Act 2024/1689 - Annex-XI:XI(3)(b)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

A description of the measures taken to address the limitations referred to in point (a), including information on the safety measures put in place.

SAFE-K8S provides infrastructure-level safety measures: workload isolation (D3), resource limits (D8), network segmentation (D5), and monitoring (D10). Application-layer safety measures (guardrails, content filtering) are outside SAFE-K8S scope but run on SAFE-K8S-managed infrastructure.

## SAFE-K8S Controls

### [SAFE-K8S-0302-001 - Pod and container security context enforcement](../../controls/SAFE-K8S-0302-001.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0304-011 - Namespace LimitRange and ResourceQuota enforcement](../../controls/SAFE-K8S-0304-011.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.4
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
