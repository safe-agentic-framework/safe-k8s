# NIST AI Risk Management Framework 1.0 - MAP 5.1

- Framework Code: NIST-AI-RMF
- Requirement Title: Likelihood and severity of each identified impact of the AI system's use, misuse, or failure - including effects on impacted communities - are assessed and documented.

## Mapping Notes

OCTAVE risk assessment includes impact severity scoring and prioritization based on organizational risk tolerance. ML threat taxonomy documents failure modes and their impacts.

## SAFE-K8S Controls

### [SAFE-K8S-1003-002 - OCTAVE risk-based threat assessment for Kubernetes AI environments](../../controls/SAFE-K8S-1003-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-1004-001 - ML threat taxonomy per CTA-2114 mapped to Kubernetes](../../controls/SAFE-K8S-1004-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage
