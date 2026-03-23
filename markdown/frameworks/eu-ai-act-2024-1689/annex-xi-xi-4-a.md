# EU AI Act 2024/1689 - Annex-XI:XI(4)(a)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

A description of the processes used for the evaluation and testing of the model, including the results thereof and any measures taken to address any identified risk.

SAFE-K8S CI/CD pipeline controls (D6) enforce security testing gates, vulnerability scanning, and automated evaluation pipelines. However, model evaluation processes (accuracy, fairness, robustness testing) go beyond security scanning and require application-layer test design and analysis.

## SAFE-K8S Controls

### [SAFE-K8S-0601-008 - CI/CD build-time container image vulnerability scanning](../../controls/SAFE-K8S-0601-008.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0606-011 - CI build-time security gate enforcement](../../controls/SAFE-K8S-0606-011.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
