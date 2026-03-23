# NIST AI Risk Management Framework 1.0 - MANAGE 1.3

- Framework Code: NIST-AI-RMF
- Requirement Title: Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

## Mapping Notes

IR lifecycle playbooks define response procedures for AI-specific incidents (compromised training, model poisoning, GPU cryptomining). Containment strategies document specific mitigation actions.

## SAFE-K8S Controls

### [SAFE-K8S-1005-001 - Kubernetes incident response lifecycle](../../controls/SAFE-K8S-1005-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: depends-on-adjacent-control

### [SAFE-K8S-1005-008 - AI-specific incident response playbooks for Kubernetes](../../controls/SAFE-K8S-1005-008.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: framework-language-interpretation
