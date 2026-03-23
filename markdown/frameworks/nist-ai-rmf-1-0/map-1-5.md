# NIST AI Risk Management Framework 1.0 - MAP 1.5

- Framework Code: NIST-AI-RMF
- Requirement Title: Organizational risk tolerances are determined and documented.

## Mapping Notes

OCTAVE risk assessment explicitly captures organizational risk tolerance and prioritizes treatment based on business impact. AI system classification assigns control profiles proportionate to risk tier.

## SAFE-K8S Controls

### [SAFE-K8S-0905-001 - AI system lifecycle classification](../../controls/SAFE-K8S-0905-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-1003-002 - OCTAVE risk-based threat assessment for Kubernetes AI environments](../../controls/SAFE-K8S-1003-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
