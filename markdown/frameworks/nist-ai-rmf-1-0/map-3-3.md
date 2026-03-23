# NIST AI Risk Management Framework 1.0 - MAP 3.3

- Framework Code: NIST-AI-RMF
- Requirement Title: Representativeness and relevance of the AI system's training, testing, and evaluation data is analyzed and documented.

## Mapping Notes

Training data provenance and pipeline integrity controls establish data lineage. Data poisoning and label attack detection identifies data quality issues that may affect representativeness.

## SAFE-K8S Controls

### [SAFE-K8S-0906-004 - Statistical drift, outlier, and input validation for training data poisoning detection](../../controls/SAFE-K8S-0906-004.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.6
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
