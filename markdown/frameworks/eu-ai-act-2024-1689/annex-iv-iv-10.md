# EU AI Act 2024/1689 - Annex-IV:IV(10)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

For high-risk AI systems that are components of products, a description of how the AI system is integrated in or interacts with the product.

SAFE-K8S captures service mesh topology, API gateway configurations, and workload interconnection patterns for AI systems deployed on Kubernetes. Full product-level integration documentation is an organizational responsibility.

## SAFE-K8S Controls

### [SAFE-K8S-0504-002 - Service mesh mTLS and authorization policies](../../controls/SAFE-K8S-0504-002.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0702-005 - Label and annotation schema definition for AI workload classification](../../controls/SAFE-K8S-0702-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
