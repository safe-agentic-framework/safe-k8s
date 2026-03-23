# NIST AI Risk Management Framework 1.0 - MANAGE 1.2

- Framework Code: NIST-AI-RMF
- Requirement Title: Treatment of documented AI risks is prioritized based on impact, likelihood, and available resources or methods.

## Mapping Notes

OCTAVE risk assessment prioritizes treatment by business impact and organizational risk tolerance. Vulnerability prioritization for AI workloads provides risk-ranked remediation guidance.

## SAFE-K8S Controls

### [SAFE-K8S-0604-008 - AI workload vulnerability exposure classification](../../controls/SAFE-K8S-0604-008.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: depends-on-adjacent-control

### [SAFE-K8S-1003-002 - OCTAVE risk-based threat assessment for Kubernetes AI environments](../../controls/SAFE-K8S-1003-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
