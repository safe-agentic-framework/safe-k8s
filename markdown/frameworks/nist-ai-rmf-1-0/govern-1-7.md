# NIST AI Risk Management Framework 1.0 - GOVERN 1.7

- Framework Code: NIST-AI-RMF
- Requirement Title: Processes and procedures are in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or harms.

## Mapping Notes

SAFE-K8S requires secure decommissioning procedures including cleanup of data, artifacts, reservations, secrets, and access grants. Change management enforces approval workflows for model deployment lifecycle transitions.

## SAFE-K8S Controls

### [SAFE-K8S-0905-006 - Model artifact lifecycle management](../../controls/SAFE-K8S-0905-006.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-1007-005 - Change management for production AI model deployments](../../controls/SAFE-K8S-1007-005.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.7
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: depends-on-adjacent-control
