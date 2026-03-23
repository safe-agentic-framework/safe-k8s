# NIST SP 800-53 Revision 5 5.2.0 - SC-4

- Framework Code: NIST-800-53R5
- Requirement Title: Information in Shared System Resources

## Mapping Notes

Preventing information leakage in shared agent resources (memory, context) is critical

8.1 - GPU memory isolation (cross-tenant data remnant prevention); 8.5 - GPU memory scraping prevention

## SAFE-K8S Controls

### [SAFE-K8S-0801-001 - GPU device plugin security configuration and hardening](../../controls/SAFE-K8S-0801-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0801-002 - MIG partitioning for hardware-enforced GPU isolation](../../controls/SAFE-K8S-0801-002.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0801-004 - vGPU virtualization security controls](../../controls/SAFE-K8S-0801-004.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0801-006 - GPU memory clearing between workload transitions](../../controls/SAFE-K8S-0801-006.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0805-001 - GPU telemetry collection and anomaly detection](../../controls/SAFE-K8S-0805-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0805-002 - GPU allocation audit trail and workload identity tracking](../../controls/SAFE-K8S-0805-002.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0805-003 - GPU-based attack detection for cryptomining and memory scraping](../../controls/SAFE-K8S-0805-003.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0805-004 - GPU side-channel attack awareness and mitigation](../../controls/SAFE-K8S-0805-004.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
