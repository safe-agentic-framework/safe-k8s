# EU AI Act 2024/1689 - Annex-VI:VI(3)(b)

- Framework Code: EU-AI-ACT
- Requirement Title: Conformity Assessment Procedure Based on Internal Control Referred to in Article 43(2)

## Mapping Notes

The provider also examines whether the design, design control and development process of the AI system and the post-market monitoring thereof have been applied consistently and in compliance with the technical documentation.

SAFE-K8S GitOps controls (D6) enforce consistent application of design and development processes through policy-as-code, admission controllers, and automated compliance checks. Post-market monitoring consistency is verified through observability stack configuration management (D10).

## SAFE-K8S Controls

### [SAFE-K8S-1002-003 - AI workload telemetry integration into cluster monitoring](../../controls/SAFE-K8S-1002-003.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
