# NIST AI Risk Management Framework 1.0 - MANAGE 1.1

- Framework Code: NIST-AI-RMF
- Requirement Title: A determination is made as to whether the AI system achieves its intended purposes and stated objectives and whether its development or deployment should proceed.

## Mapping Notes

AI system classification defines expected control profiles. Model promotion gates enforce go/no-go decisions before production deployment based on validation criteria.

## SAFE-K8S Controls

### [SAFE-K8S-0905-001 - AI system lifecycle classification](../../controls/SAFE-K8S-0905-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: compound-control-split-required

### [SAFE-K8S-0905-005 - Automated model promotion gates](../../controls/SAFE-K8S-0905-005.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-coverage
