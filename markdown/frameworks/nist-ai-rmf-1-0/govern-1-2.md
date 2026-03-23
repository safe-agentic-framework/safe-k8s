# NIST AI Risk Management Framework 1.0 - GOVERN 1.2

- Framework Code: NIST-AI-RMF
- Requirement Title: The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices.

## Mapping Notes

Policy-as-code engines enforce trustworthiness requirements (image provenance, resource limits, security contexts) as admission-time policies. Compliance mapping documents link organizational AI policies to infrastructure enforcement points.

## SAFE-K8S Controls

### [SAFE-K8S-0605-001 - OPA/Gatekeeper policies for Kubernetes and AI workloads](../../controls/SAFE-K8S-0605-001.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-1006-001 - Regulatory compliance mapping for Kubernetes AI platforms](../../controls/SAFE-K8S-1006-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.6
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-1006-005 - Policy-as-code enforcement for AI workload compliance](../../controls/SAFE-K8S-1006-005.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.6
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
