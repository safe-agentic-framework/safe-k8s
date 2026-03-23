# NIST SP 800-53 Revision 5 5.2.0 - SA-4

- Framework Code: NIST-800-53R5
- Requirement Title: Acquisition Process

## Mapping Notes

Acquisition of agentic AI components (models, tools, plugins) requires security requirements

8.2 - GPU driver/library security (acquisition controls); 9.4 - ML dependency management and acquisition

## SAFE-K8S Controls

### [SAFE-K8S-0802-001 - GPU driver lifecycle and vulnerability management](../../controls/SAFE-K8S-0802-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.2
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0802-002 - CUDA library and container toolkit security](../../controls/SAFE-K8S-0802-002.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.2
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0802-004 - GPU firmware integrity monitoring](../../controls/SAFE-K8S-0802-004.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.2
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0904-001 - Pipeline orchestrator hardening](../../controls/SAFE-K8S-0904-001.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.4
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0904-003 - Notebook and experimentation environment security](../../controls/SAFE-K8S-0904-003.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.4
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
