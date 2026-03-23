# NIST SP 800-53 Revision 5 5.2.0 - SR-9

- Framework Code: NIST-800-53R5
- Requirement Title: Tamper Resistance and Detection

## Mapping Notes

Tamper resistance and detection for AI models and agent components prevents manipulation

8.2 - GPU firmware integrity (tamper detection); 6.2 - Image integrity (tamper detection via signing)

## SAFE-K8S Controls

### [SAFE-K8S-0602-001 - Sigstore/cosign keyless signing and Rekor transparency logging](../../controls/SAFE-K8S-0602-001.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0802-001 - GPU driver lifecycle and vulnerability management](../../controls/SAFE-K8S-0802-001.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0802-002 - CUDA library and container toolkit security](../../controls/SAFE-K8S-0802-002.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0802-004 - GPU firmware integrity monitoring](../../controls/SAFE-K8S-0802-004.md)

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Knowledge Area: 8.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
