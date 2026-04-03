# NIST SP 800-53 Revision 5 5.2.0 - SR-4

- Framework Code: NIST-800-53R5
- Requirement Title: Provenance

## Mapping Notes

Provenance tracking for AI models, training data, and agent tools verifies origin and integrity

6.3 - SLSA provenance, in-toto attestations; 9.5 - Model signing and provenance; 6.6 - Build attestation per NIST SP 800-204D

## SAFE-K8S Controls

### [SAFE-K8S-0603-004 - Cryptographic agility and post-quantum readiness](../../controls/SAFE-K8S-0603-004.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0603-005 - FIPS 140 cryptographic module validation](../../controls/SAFE-K8S-0603-005.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0603-006 - TUF-based secure software update systems](../../controls/SAFE-K8S-0603-006.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

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

### [SAFE-K8S-0606-018 - Zero-trust CI/CD handoff verification and independent evidence generation](../../controls/SAFE-K8S-0606-018.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-001 - AI system lifecycle classification](../../controls/SAFE-K8S-0905-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0905-005 - Automated model promotion gates](../../controls/SAFE-K8S-0905-005.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-006 - Model artifact lifecycle management](../../controls/SAFE-K8S-0905-006.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0905-009 - Model provenance verification at deployment](../../controls/SAFE-K8S-0905-009.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-012 - Development-to-production environment separation for AI workloads](../../controls/SAFE-K8S-0905-012.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-047 - Training pipeline attestation generation for ML artifacts](../../controls/SAFE-K8S-0905-047.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-056 - External model publisher identity and provenance metadata verification](../../controls/SAFE-K8S-0905-056.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0910-024 - Cross-cluster model provenance chain-of-custody preservation](../../controls/SAFE-K8S-0910-024.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.10
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
