# NIST SP 800-53 Revision 5 5.2.0 - SA-3

- Framework Code: NIST-800-53R5
- Requirement Title: System Development Life Cycle

## Mapping Notes

SDLC for agentic AI must integrate security at every phase including model training and deployment

6.6 - CNCF lifecycle security (Develop-Distribute-Deploy); 10.4 - SSDF v1.1 alignment for SDLC

## SAFE-K8S Controls

### [SAFE-K8S-0606-002 - CI/CD build environment hardening](../../controls/SAFE-K8S-0606-002.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0606-007 - CI/CD build activity monitoring](../../controls/SAFE-K8S-0606-007.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0606-009 - SSDF v1.1 alignment for secure development practices](../../controls/SAFE-K8S-0606-009.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1004-001 - ML threat taxonomy per CTA-2114 mapped to Kubernetes](../../controls/SAFE-K8S-1004-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1004-002 - Software supply chain threat model per NIST SP 800-204D](../../controls/SAFE-K8S-1004-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
