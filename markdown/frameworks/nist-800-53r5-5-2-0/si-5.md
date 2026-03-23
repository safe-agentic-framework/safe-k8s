# NIST SP 800-53 Revision 5 5.2.0 - SI-5

- Framework Code: NIST-800-53R5
- Requirement Title: Security Alerts, Advisories, and Directives

## Mapping Notes

Security alerts and advisories inform operators of threats to agentic AI systems

1.4 - CVE response (monitoring security announcements); 10.2 - Threat intelligence (consuming advisories)

## SAFE-K8S Controls

### [SAFE-K8S-0104-005 - Control plane configuration file permissions](../../controls/SAFE-K8S-0104-005.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-0104-018 - Kubernetes security advisory and provider bulletin monitoring](../../controls/SAFE-K8S-0104-018.md)

- Domain: D01 - Control Plane and Cluster Hardening
- Knowledge Area: 1.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1002-001 - Metric endpoint authentication](../../controls/SAFE-K8S-1002-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: exact-text-match

### [SAFE-K8S-1002-002 - Distributed tracing for ML pipelines](../../controls/SAFE-K8S-1002-002.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1002-003 - AI workload telemetry integration into cluster monitoring](../../controls/SAFE-K8S-1002-003.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1002-004 - AI-specific alerting and failure mode detection](../../controls/SAFE-K8S-1002-004.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
