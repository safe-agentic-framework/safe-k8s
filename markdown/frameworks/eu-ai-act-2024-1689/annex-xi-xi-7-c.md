# EU AI Act 2024/1689 - Annex-XI:XI(7)(c)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation for Providers of General-Purpose AI Models Referred to in Article 53(1)(a)

## Mapping Notes

For general-purpose AI models with systemic risk, the results of any red-teaming or adversarial testing conducted to identify and address systemic risks, including information on any measures taken to mitigate the risks identified.

SAFE-K8S provides infrastructure for running adversarial tests: workload isolation for test environments, network controls for test boundaries, and D9 adversarial defense controls (KA 9.3). The testing methodology, results analysis, and mitigation strategy are application-layer and organizational concerns.

## SAFE-K8S Controls

### [SAFE-K8S-0903-001 - Adversarial example defenses at the serving layer](../../controls/SAFE-K8S-0903-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.3
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
