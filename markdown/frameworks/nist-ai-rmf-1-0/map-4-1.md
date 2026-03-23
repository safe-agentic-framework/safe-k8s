# NIST AI Risk Management Framework 1.0 - MAP 4.1

- Framework Code: NIST-AI-RMF
- Requirement Title: Approaches for mapping AI technology and legal risks of its components - including the use of third-party data or software - are in place, followed, and documented, as are risks of infringement of a third-party's intellectual property or other rights.

## Mapping Notes

SBOM and ML-BOM generation documents all software and model dependencies. ML dependency vulnerability management tracks known vulnerabilities in third-party components.

## SAFE-K8S Controls

### [SAFE-K8S-0604-001 - SBOM generation for container and AI artifacts](../../controls/SAFE-K8S-0604-001.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0604-002 - ML-BOM (ML Bill of Materials) generation](../../controls/SAFE-K8S-0604-002.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
