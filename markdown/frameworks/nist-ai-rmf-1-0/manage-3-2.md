# NIST AI Risk Management Framework 1.0 - MANAGE 3.2

- Framework Code: NIST-AI-RMF
- Requirement Title: Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.

## Mapping Notes

Model signing and provenance verification ensures pre-trained model integrity. Model registry hardening protects stored models. ML dependency vulnerability management tracks vulnerabilities in model dependencies.

## SAFE-K8S Controls

### [SAFE-K8S-0905-056 - External model publisher identity and provenance metadata verification](../../controls/SAFE-K8S-0905-056.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
