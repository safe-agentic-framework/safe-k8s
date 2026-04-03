# NIST SP 800-53 Revision 5 5.2.0 - RA-5

- Framework Code: NIST-800-53R5
- Requirement Title: Vulnerability Monitoring and Scanning

## Mapping Notes

Vulnerability scanning of agentic AI components, dependencies, and models is essential

6.1 - Container image vulnerability scanning (CI/CD, registry, runtime); 6.4 - Vulnerability intelligence

## SAFE-K8S Controls

### [SAFE-K8S-0604-001 - SBOM generation for container and AI artifacts](../../controls/SAFE-K8S-0604-001.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0604-002 - ML-BOM (ML Bill of Materials) generation](../../controls/SAFE-K8S-0604-002.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0604-003 - SBOM storage and distribution as OCI artifacts](../../controls/SAFE-K8S-0604-003.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0604-004 - VEX (Vulnerability Exploitability eXchange) publication](../../controls/SAFE-K8S-0604-004.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0604-007 - Third-party component security requirements documentation](../../controls/SAFE-K8S-0604-007.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0604-008 - AI workload vulnerability exposure classification](../../controls/SAFE-K8S-0604-008.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-028 - ML framework and Python dependency vulnerability management](../../controls/SAFE-K8S-0905-028.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0905-029 - CUDA and GPU accelerator dependency vulnerability management](../../controls/SAFE-K8S-0905-029.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
