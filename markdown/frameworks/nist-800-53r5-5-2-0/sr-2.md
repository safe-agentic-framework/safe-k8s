# NIST SP 800-53 Revision 5 5.2.0 - SR-2

- Framework Code: NIST-800-53R5
- Requirement Title: Supply Chain Risk Management Plan

## Mapping Notes

SCRM plan for agentic AI addresses model provenance, tool integrity, and vendor risks

6.6 - Supply chain security (CNCF lifecycle, SLSA, SSDF); 9.4 - AI supply chain and model lifecycle

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

### [SAFE-K8S-0904-001 - Pipeline orchestrator hardening](../../controls/SAFE-K8S-0904-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0904-003 - Notebook and experimentation environment security](../../controls/SAFE-K8S-0904-003.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
