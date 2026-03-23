# NIST AI Risk Management Framework 1.0 - MEASURE 3.1

- Framework Code: NIST-AI-RMF
- Requirement Title: Approaches, personnel, and documentation are in place to regularly identify and track existing, unanticipated, and emergent AI risks based on factors such as intended and actual performance in deployed contexts.

## Mapping Notes

Threat intelligence integration consumes CVE feeds, runtime threat intelligence, and adversarial ML attack pattern libraries. Security posture management provides continuous risk assessment with drift detection.

## SAFE-K8S Controls

### [SAFE-K8S-1004-004 - Kubernetes AI threat intelligence feed ingestion and detection enrichment](../../controls/SAFE-K8S-1004-004.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.4
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: compound-control-split-required

### [SAFE-K8S-1007-004 - Continuous security posture management for AI clusters](../../controls/SAFE-K8S-1007-004.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.7
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: semantic-mismatch-candidate
