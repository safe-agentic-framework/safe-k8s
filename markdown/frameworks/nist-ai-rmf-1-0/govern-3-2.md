# NIST AI Risk Management Framework 1.0 - GOVERN 3.2

- Framework Code: NIST-AI-RMF
- Requirement Title: Policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight of AI systems.

## Mapping Notes

AI system classification assigns control profiles based on risk tier, implicitly defining human oversight requirements. Model promotion gates enforce approval workflows requiring human review before deployment.

## SAFE-K8S Controls

### [SAFE-K8S-0905-001 - AI system lifecycle classification](../../controls/SAFE-K8S-0905-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-0905-005 - Automated model promotion gates](../../controls/SAFE-K8S-0905-005.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-0905-015 - AI system control profile enforcement](../../controls/SAFE-K8S-0905-015.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-045 - Sandboxed external model behavioral vetting and disposition review](../../controls/SAFE-K8S-0905-045.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-050 - Authenticated reviewer identity validation for model promotion approvals](../../controls/SAFE-K8S-0905-050.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-057 - External model trust-signal assessment and approval review](../../controls/SAFE-K8S-0905-057.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
