# NIST AI Risk Management Framework 1.0 - MEASURE 2.5

- Framework Code: NIST-AI-RMF
- Requirement Title: The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented.

## Mapping Notes

Model promotion gates enforce validation before production deployment. Model signing and provenance verification establish artifact integrity through the deployment pipeline.

## SAFE-K8S Controls

### [SAFE-K8S-0905-005 - Automated model promotion gates](../../controls/SAFE-K8S-0905-005.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: partial-control-coverage
