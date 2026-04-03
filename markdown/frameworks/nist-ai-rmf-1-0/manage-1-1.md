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

### [SAFE-K8S-0905-015 - AI system control profile enforcement](../../controls/SAFE-K8S-0905-015.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0606-017 - CNCF lifecycle phase security coverage](../../controls/SAFE-K8S-0606-017.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0606-018 - Zero-trust CI/CD handoff verification and independent evidence generation](../../controls/SAFE-K8S-0606-018.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-018 - Security-aware target-cluster posture verification before multi-cluster placement](../../controls/SAFE-K8S-0910-018.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
