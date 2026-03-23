# NIST AI Risk Management Framework 1.0 - MAP 2.2

- Framework Code: NIST-AI-RMF
- Requirement Title: Information about the AI system's knowledge limits and how system output may be utilized and overseen by humans is documented. Documentation also includes a description of the capabilities the system can and cannot support, its intended scope of operation, and conditions under which it would not be advisable to deploy the system.

## Mapping Notes

Inference request validation and response filtering enforce operational boundaries. Adversarial example defenses help define system reliability limits.

## SAFE-K8S Controls

### [SAFE-K8S-0902-003 - Inference request validation and input sanitization](../../controls/SAFE-K8S-0902-003.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.2
- Relation Type: partial
- Strength: weak
- Applicability: required
- Strength Reason Code: partial-control-coverage

### [SAFE-K8S-0903-001 - Adversarial example defenses at the serving layer](../../controls/SAFE-K8S-0903-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.3
- Relation Type: partial
- Strength: weak
- Applicability: required
- Strength Reason Code: partial-control-coverage
