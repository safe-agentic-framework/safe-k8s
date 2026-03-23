# NIST AI Risk Management Framework 1.0 - MEASURE 2.10

- Framework Code: NIST-AI-RMF
- Requirement Title: Privacy risk of the AI system - as identified in the MAP function - is examined and documented.

## Mapping Notes

Training data privacy controls enforce data handling policies. Differential privacy and output perturbation mitigate inference privacy risks. Centralized logging with PII redaction prevents sensitive data exposure in observability systems.

## SAFE-K8S Controls

### [SAFE-K8S-0907-002 - Training data privacy controls](../../controls/SAFE-K8S-0907-002.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.7
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: compound-control-split-required
