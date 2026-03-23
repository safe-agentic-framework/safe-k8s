# NIST SP 800-53 Revision 5 5.2.0 - RA-2

- Framework Code: NIST-800-53R5
- Requirement Title: Security Categorization

## Mapping Notes

Security categorization of agentic AI systems drives control selection and rigor

7.2 - Label/annotation standards (security categorization of AI workloads); 9.7 - Data classification

## SAFE-K8S Controls

### [SAFE-K8S-0702-003 - LimitRange enforcement for containers and pods](../../controls/SAFE-K8S-0702-003.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0702-005 - Label and annotation schema definition for AI workload classification](../../controls/SAFE-K8S-0702-005.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
- Relation Type: supports
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0702-019 - Supplementary namespace isolation control enforcement for multi-tenant AI clusters](../../controls/SAFE-K8S-0702-019.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.2
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
