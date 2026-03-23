# NIST AI Risk Management Framework 1.0 - MANAGE 2.4

- Framework Code: NIST-AI-RMF
- Requirement Title: Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

## Mapping Notes

Change management and decommissioning controls enable safe AI workload deactivation. Containment strategies define mechanisms for isolating or suspending AI workloads (node draining, namespace isolation, inference service quarantine, pipeline suspension).

## SAFE-K8S Controls

### [SAFE-K8S-1007-005 - Change management for production AI model deployments](../../controls/SAFE-K8S-1007-005.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.7
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: depends-on-adjacent-control
