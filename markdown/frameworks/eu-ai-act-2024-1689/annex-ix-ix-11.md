# EU AI Act 2024/1689 - Annex-IX:IX(11)

- Framework Code: EU-AI-ACT
- Requirement Title: Information to be Submitted Upon Registration for Testing in Real World Conditions in Accordance with Article 60

## Mapping Notes

The address of the place where the test data collected in the course of the real world testing is held and will be available in the event of an inspection.

SAFE-K8S storage controls (D7) manage the infrastructure where test data is stored, including persistent volumes, backup policies, and access controls. However, providing the address/location information for regulatory registration purposes is an organizational obligation.

## SAFE-K8S Controls

### [SAFE-K8S-0701-001 - PersistentVolume and PersistentVolumeClaim access mode enforcement](../../controls/SAFE-K8S-0701-001.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-0701-003 - Encryption at rest for persistent volumes](../../controls/SAFE-K8S-0701-003.md)

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Knowledge Area: 7.1
- Relation Type: partial
- Strength: moderate
- Applicability: required
- Strength Reason Code: n/a
