# EU AI Act 2024/1689 - Annex-IV:IV(4)

- Framework Code: EU-AI-ACT
- Requirement Title: Technical Documentation Referred to in Article 11(1)

## Mapping Notes

A description of the appropriateness and adequacy of the cybersecurity measures referred to in Article 15, including a description of any known limitation and the residual risks, and, as appropriate, a description of measures taken to address the identified risks.

SAFE-K8S is directly scoped to provide comprehensive cybersecurity controls for AI workloads on Kubernetes. All 10 SAFE-K8S domains collectively address Article 15 cybersecurity requirements including network security (D5), access control (D4), workload isolation (D3), supply chain integrity (D6), and incident response (D10).

## SAFE-K8S Controls

### [SAFE-K8S-0302-001 - Pod and container security context enforcement](../../controls/SAFE-K8S-0302-001.md)

- Domain: D03 - Workload and Pod Security
- Knowledge Area: 3.2
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0401-001 - RBAC least-privilege design](../../controls/SAFE-K8S-0401-001.md)

- Domain: D04 - Identity, Access, and Secrets Management
- Knowledge Area: 4.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0501-001 - Default deny ingress and egress network policies](../../controls/SAFE-K8S-0501-001.md)

- Domain: D05 - Network Security and Communication
- Knowledge Area: 5.1
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-0604-001 - SBOM generation for container and AI artifacts](../../controls/SAFE-K8S-0604-001.md)

- Domain: D06 - Supply Chain, Images, and Admission Control
- Knowledge Area: 6.4
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1003-001 - STRIDE threat modeling for Kubernetes AI systems](../../controls/SAFE-K8S-1003-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a

### [SAFE-K8S-1005-001 - Kubernetes incident response lifecycle](../../controls/SAFE-K8S-1005-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.5
- Relation Type: direct
- Strength: strong
- Applicability: required
- Strength Reason Code: n/a
