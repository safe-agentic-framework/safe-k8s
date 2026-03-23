# EU AI Act 2024/1689 - Annex-VIII:VIII(14)

- Framework Code: EU-AI-ACT
- Requirement Title: Information to be Submitted Upon the Registration of High-Risk AI Systems in Accordance with Article 49

## Mapping Notes

A description of the means of identification of the AI system, such as a serial number, version number, or model identifier.

SAFE-K8S supply chain controls (D6) support identification through container image digests, model version tracking via ML-BOMs, workload labels, and cryptographic attestation. However, defining the identification scheme (serial numbers, model identifiers) for regulatory registration is an organizational decision.

## SAFE-K8S Controls

### [SAFE-K8S-0602-001 - Sigstore/cosign keyless signing and Rekor transparency logging](../../controls/SAFE-K8S-0602-001.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0604-002 - ML-BOM (ML Bill of Materials) generation](../../controls/SAFE-K8S-0604-002.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-0702-005 - Label and annotation schema definition for AI workload classification](../../controls/SAFE-K8S-0702-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
