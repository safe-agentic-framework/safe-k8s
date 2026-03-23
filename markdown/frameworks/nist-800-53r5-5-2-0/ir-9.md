# NIST SP 800-53 Revision 5 5.2.0 - IR-9

- Framework Code: NIST-800-53R5
- Requirement Title: Information Spillage Response

## Mapping Notes

Responding when agents leak sensitive data

4.3 - Secret leakage prevention; 9.7 - PII handling (information spillage response for AI training data)

## SAFE-K8S Controls

### [SAFE-K8S-0403-002 - External secrets management integration](../../controls/SAFE-K8S-0403-002.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0403-004 - Secret rotation and expiration enforcement](../../controls/SAFE-K8S-0403-004.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0403-005 - AI pipeline secret leakage prevention](../../controls/SAFE-K8S-0403-005.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0403-006 - Per-workload credential scoping for AI jobs](../../controls/SAFE-K8S-0403-006.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0907-002 - Training data privacy controls](../../controls/SAFE-K8S-0907-002.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.7
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
