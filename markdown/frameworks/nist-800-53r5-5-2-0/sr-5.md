# NIST SP 800-53 Revision 5 5.2.0 - SR-5

- Framework Code: NIST-800-53R5
- Requirement Title: Acquisition Strategies, Tools, and Methods

## Mapping Notes

Acquisition strategies for AI components must address unique supply chain security needs

8.1 - Device plugin framework (GPU acquisition/provisioning); 6.1 - Base image selection (image acquisition strategy)

## SAFE-K8S Controls

### [SAFE-K8S-0601-007 - AI GPU and ML framework base image validation](../../controls/SAFE-K8S-0601-007.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0601-015 - Inference image minimal composition with GPU runtime-only dependencies](../../controls/SAFE-K8S-0601-015.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0801-001 - GPU device plugin security configuration and hardening](../../controls/SAFE-K8S-0801-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0801-002 - MIG partitioning for hardware-enforced GPU isolation](../../controls/SAFE-K8S-0801-002.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0801-004 - vGPU virtualization security controls](../../controls/SAFE-K8S-0801-004.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0801-006 - GPU memory clearing between workload transitions](../../controls/SAFE-K8S-0801-006.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
