# NIST SP 800-53 Revision 5 5.2.0 - IA-5

- Framework Code: NIST-800-53R5
- Requirement Title: Authenticator Management

## Mapping Notes

Managing agent credentials/tokens/keys

4.3 - Manage secrets (authenticator lifecycle: rotation policies, expiration, revocation, leak detection; per-workload credential scoping SAFE-K8S-0403-006; credential inventory and sprawl governance SAFE-K8S-0403-008)

## SAFE-K8S Controls

### [SAFE-K8S-0403-002 - External secrets management integration](../../controls/SAFE-K8S-0403-002.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0403-004 - Secret rotation and expiration enforcement](../../controls/SAFE-K8S-0403-004.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0403-005 - AI pipeline secret leakage prevention](../../controls/SAFE-K8S-0403-005.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0403-006 - Per-workload credential scoping for AI jobs](../../controls/SAFE-K8S-0403-006.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
