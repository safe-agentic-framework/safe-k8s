# NIST AI Risk Management Framework 1.0 - MAP 3.4

- Framework Code: NIST-AI-RMF
- Requirement Title: Risks and benefits of all datasets used for training, testing, and operation of the AI system are mapped, including those provided by third parties.

## Mapping Notes

Training data provenance tracks dataset origin and integrity. Large-scale data integrity verification validates dataset completeness. Data type classification labels categorize data flowing through pipelines.

## SAFE-K8S Controls

### [SAFE-K8S-0403-006 - Per-workload credential scoping for AI jobs](../../controls/SAFE-K8S-0403-006.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.3
- Relation Type: supports
- Strength: weak
- Applicability: required
- Strength Reason Code: semantic-mismatch-candidate

### [SAFE-K8S-0906-002 - Large-scale data integrity verification](../../controls/SAFE-K8S-0906-002.md)

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Knowledge Area: 9.6
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match
