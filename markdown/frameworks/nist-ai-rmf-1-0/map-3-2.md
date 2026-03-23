# NIST AI Risk Management Framework 1.0 - MAP 3.2

- Framework Code: NIST-AI-RMF
- Requirement Title: Potential harms to people, organizations, and ecosystems arising from the AI system's intended use - and if relevant, across the lifecycle - are understood, characterized, and documented.

## Mapping Notes

ML threat taxonomy (CTA-2114) characterizes AI-specific harms including data poisoning, model disclosure, and evasion attacks. MITRE ATT&CK mapping documents infrastructure attack surfaces and potential harms.

## SAFE-K8S Controls

### [SAFE-K8S-1003-004 - MITRE ATT&CK for Containers coverage mapping and gap analysis](../../controls/SAFE-K8S-1003-004.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.3
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation

### [SAFE-K8S-1004-001 - ML threat taxonomy per CTA-2114 mapped to Kubernetes](../../controls/SAFE-K8S-1004-001.md)

- Domain: D10 - Observability, Incident Response, and Governance
- Knowledge Area: 10.4
- Relation Type: supports
- Strength: moderate
- Applicability: required
- Strength Reason Code: framework-language-interpretation
