# NIST AI Risk Management Framework 1.0 - MAP 3.5

- Framework Code: NIST-AI-RMF
- Requirement Title: Likelihood and magnitude of each identified risk based on expected use, past uses of similar systems, public incident reports, feedback from those external to the team that developed or deployed the AI system, or other data are assessed and documented.

## Mapping Notes

OCTAVE risk assessment includes likelihood and impact scoring. Threat intelligence integration consumes external incident data and adversarial ML attack pattern libraries.

## SAFE-K8S Controls

### [SAFE-K8S-1003-002 - OCTAVE risk-based threat assessment for Kubernetes AI environments](../../controls/SAFE-K8S-1003-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-1004-005 - Adversarial ML threat taxonomy and structured classification](../../controls/SAFE-K8S-1004-005.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.4
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: compound-control-split-required
