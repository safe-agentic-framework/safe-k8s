# EU AI Act 2024/1689 - Art-15:15(5)-ai-specific-attacks

- Framework Code: EU-AI-ACT
- Requirement Title: Accuracy, Robustness and Cybersecurity

## Mapping Notes

The technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

Directly maps to SAFE-K8S D9 controls: data poisoning defense (KA 9.6), model supply chain integrity (KA 9.5), adversarial input defense (KA 9.3), model extraction prevention (KA 9.8), and inference request validation (KA 9.2).

## SAFE-K8S Controls

### [SAFE-K8S-0902-003 - Inference request validation and input sanitization](../../controls/SAFE-K8S-0902-003.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0903-001 - Adversarial example defenses at the serving layer](../../controls/SAFE-K8S-0903-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0906-004 - Statistical drift, outlier, and input validation for training data poisoning detection](../../controls/SAFE-K8S-0906-004.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0908-001 - Oracle attack prevention](../../controls/SAFE-K8S-0908-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.8
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0908-002 - Inference API information exposure controls](../../controls/SAFE-K8S-0908-002.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.8
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
