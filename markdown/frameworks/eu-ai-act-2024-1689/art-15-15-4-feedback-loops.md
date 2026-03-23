# EU AI Act 2024/1689 - Art-15:15(4)-feedback-loops

- Framework Code: EU-AI-ACT
- Requirement Title: Accuracy, Robustness and Cybersecurity

## Mapping Notes

High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops), and as to ensure that any such feedback loops are duly addressed with appropriate mitigation measures.

Feedback loop mitigation is primarily an application-layer concern (model design). However, SAFE-K8S pipeline integrity controls (D9 KA 9.4, 9.6) and data governance controls can enforce separation between training and inference data paths at the infrastructure level.

## SAFE-K8S Controls

### [SAFE-K8S-0906-002 - Large-scale data integrity verification](../../controls/SAFE-K8S-0906-002.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.6
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
