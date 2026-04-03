# NIST AI Risk Management Framework 1.0 - GOVERN 4.1

- Framework Code: NIST-AI-RMF
- Requirement Title: Organizational policies and practices are in place to foster a critical thinking and safety-first mindset in the design, development, deployment, and uses of AI systems to minimize potential negative impacts.

## Mapping Notes

AI system classification enforces risk-proportionate controls. Model promotion gates require validation before deployment, embedding a safety-first workflow in the AI lifecycle.

## SAFE-K8S Controls

### [SAFE-K8S-0905-001 - AI system lifecycle classification](../../controls/SAFE-K8S-0905-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-0905-005 - Automated model promotion gates](../../controls/SAFE-K8S-0905-005.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-0905-015 - AI system control profile enforcement](../../controls/SAFE-K8S-0905-015.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-045 - Sandboxed external model behavioral vetting and disposition review](../../controls/SAFE-K8S-0905-045.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
