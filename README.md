# SAFE-K8S Public Security Control Catalog

This repository publishes the public SAFE-K8S security control catalog for Kubernetes and AI systems. It includes the public control set, knowledge area structure, and framework crosswalks under `SAFE-K8S-*` identifiers.

## Purpose

- Publish a public SAFE-K8S control catalog for external use
- Preserve traceability between controls and mapped frameworks
- Support review, reuse, and downstream publication without internal-only fields

## Contents

- YAML source files for domains, knowledge areas, controls, and crosswalks
- Generated markdown pages for controls and reverse mappings by framework

## Basic Info

- Domains: 10
- Knowledge areas: 55
- Controls: 839
- Crosswalk rows: 4724

## YAML Files

- `safe_k8s_domains.yaml`
- `safe_k8s_knowledge_areas.yaml`
- `safe_k8s_controls.yaml`
- `safe_k8s_crosswalks.yaml`

## Markdown Pages

- `markdown/controls/` contains one markdown page per control with related mappings
- `markdown/frameworks/` contains reverse-mapping pages by framework and requirement

## Framework Reverse Mappings

- [EU AI Act 2024/1689](markdown/frameworks/eu-ai-act-2024-1689/README.md)
- [NIST SP 800-53 Revision 5 5.2.0](markdown/frameworks/nist-800-53r5-5-2-0/README.md)
- [NIST AI Risk Management Framework 1.0](markdown/frameworks/nist-ai-rmf-1-0/README.md)
- [NIST SP 800-218: Secure Software Development Framework (SSDF) Version 1.1 1.1](markdown/frameworks/nist-ssdf-1-1/README.md)

## Notes

- Crosswalk pages keep `framework_mapping_notes` because they carry useful interpretive context.
- `strength_reason_note` is intentionally not published in this export.

## Controls

| Control ID | Domain | Knowledge Area | Title | Maturity | Class |
| --- | --- | --- | --- | --- | --- |
| [SAFE-K8S-0101-001](markdown/controls/SAFE-K8S-0101-001.md) | D01 | 1.1 | API server hardening flags | Foundational | baseline |
| [SAFE-K8S-0101-002](markdown/controls/SAFE-K8S-0101-002.md) | D01 | 1.1 | API server TLS configuration and certificate rotation | Foundational | baseline |
| [SAFE-K8S-0101-003](markdown/controls/SAFE-K8S-0101-003.md) | D01 | 1.1 | Encryption at rest for Secrets and sensitive API resources | Foundational | baseline |
| [SAFE-K8S-0101-004](markdown/controls/SAFE-K8S-0101-004.md) | D01 | 1.1 | API server access controls and authorization modes | Foundational | baseline |
| [SAFE-K8S-0101-005](markdown/controls/SAFE-K8S-0101-005.md) | D01 | 1.1 | Streaming connection idle timeout enforcement | Foundational | baseline |
| [SAFE-K8S-0101-006](markdown/controls/SAFE-K8S-0101-006.md) | D01 | 1.1 | API server audit logging policy and backend configuration | Foundational | baseline |
| [SAFE-K8S-0101-007](markdown/controls/SAFE-K8S-0101-007.md) | D01 | 1.1 | API server request rate limiting and API Priority and Fairness | Practitioner | ai-specific |
| [SAFE-K8S-0101-008](markdown/controls/SAFE-K8S-0101-008.md) | D01 | 1.1 | API server audit policy coverage and event detail | Foundational | baseline |
| [SAFE-K8S-0101-009](markdown/controls/SAFE-K8S-0101-009.md) | D01 | 1.1 | API server audit log backend durability and retention | Foundational | baseline |
| [SAFE-K8S-0101-010](markdown/controls/SAFE-K8S-0101-010.md) | D01 | 1.1 | API server anonymous authentication disablement and authorization mode hardening | Foundational | baseline |
| [SAFE-K8S-0101-011](markdown/controls/SAFE-K8S-0101-011.md) | D01 | 1.1 | API server profiling disablement and approved admission controller configuration | Foundational | baseline |
| [SAFE-K8S-0101-012](markdown/controls/SAFE-K8S-0101-012.md) | D01 | 1.1 | API server TLS enforcement | Foundational | baseline |
| [SAFE-K8S-0101-013](markdown/controls/SAFE-K8S-0101-013.md) | D01 | 1.1 | API server certificate rotation and validation | Foundational | baseline |
| [SAFE-K8S-0101-014](markdown/controls/SAFE-K8S-0101-014.md) | D01 | 1.1 | API server authorization mode baseline enforcement | Foundational | baseline |
| [SAFE-K8S-0101-015](markdown/controls/SAFE-K8S-0101-015.md) | D01 | 1.1 | API server webhook authorizer endpoint trust controls | Foundational | baseline |
| [SAFE-K8S-0101-016](markdown/controls/SAFE-K8S-0101-016.md) | D01 | 1.1 | API server audit log backend delivery and durable storage | Foundational | baseline |
| [SAFE-K8S-0101-017](markdown/controls/SAFE-K8S-0101-017.md) | D01 | 1.1 | API server audit log retention enforcement | Foundational | baseline |
| [SAFE-K8S-0101-018](markdown/controls/SAFE-K8S-0101-018.md) | D01 | 1.1 | API server anonymous authentication disablement | Foundational | baseline |
| [SAFE-K8S-0101-019](markdown/controls/SAFE-K8S-0101-019.md) | D01 | 1.1 | API server AlwaysAllow prohibition | Foundational | baseline |
| [SAFE-K8S-0101-020](markdown/controls/SAFE-K8S-0101-020.md) | D01 | 1.1 | API server profiling and debug exposure disablement | Foundational | baseline |
| [SAFE-K8S-0101-021](markdown/controls/SAFE-K8S-0101-021.md) | D01 | 1.1 | API server approved admission controller chain configuration | Foundational | baseline |
| [SAFE-K8S-0102-001](markdown/controls/SAFE-K8S-0102-001.md) | D01 | 1.2 | etcd storage-layer disk encryption with externally managed keys | Foundational | baseline |
| [SAFE-K8S-0102-002](markdown/controls/SAFE-K8S-0102-002.md) | D01 | 1.2 | etcd access controls and network isolation | Foundational | baseline |
| [SAFE-K8S-0102-003](markdown/controls/SAFE-K8S-0102-003.md) | D01 | 1.2 | etcd backup and restore security | Foundational | baseline |
| [SAFE-K8S-0102-004](markdown/controls/SAFE-K8S-0102-004.md) | D01 | 1.2 | etcd cluster health monitoring, compaction, and defragmentation | Foundational | baseline |
| [SAFE-K8S-0102-005](markdown/controls/SAFE-K8S-0102-005.md) | D01 | 1.2 | etcd certificate rotation and lifecycle management | Practitioner | baseline |
| [SAFE-K8S-0102-006](markdown/controls/SAFE-K8S-0102-006.md) | D01 | 1.2 | etcd encryption key rotation scheduling and verification | Foundational | baseline |
| [SAFE-K8S-0102-007](markdown/controls/SAFE-K8S-0102-007.md) | D01 | 1.2 | etcd backup storage encryption | Foundational | baseline |
| [SAFE-K8S-0102-008](markdown/controls/SAFE-K8S-0102-008.md) | D01 | 1.2 | etcd backup integrity verification and restore assurance | Foundational | baseline |
| [SAFE-K8S-0102-009](markdown/controls/SAFE-K8S-0102-009.md) | D01 | 1.2 | etcd backup storage access restriction and auditing | Foundational | baseline |
| [SAFE-K8S-0102-010](markdown/controls/SAFE-K8S-0102-010.md) | D01 | 1.2 | etcd certificate rotation execution and testing | Practitioner | baseline |
| [SAFE-K8S-0102-011](markdown/controls/SAFE-K8S-0102-011.md) | D01 | 1.2 | etcd certificate validity limits and expiration alerting | Practitioner | baseline |
| [SAFE-K8S-0102-012](markdown/controls/SAFE-K8S-0102-012.md) | D01 | 1.2 | etcd health monitoring and alerting | Foundational | baseline |
| [SAFE-K8S-0102-013](markdown/controls/SAFE-K8S-0102-013.md) | D01 | 1.2 | etcd compaction and periodic defragmentation | Foundational | baseline |
| [SAFE-K8S-0102-014](markdown/controls/SAFE-K8S-0102-014.md) | D01 | 1.2 | etcd certificate rotation coverage and execution | Practitioner | baseline |
| [SAFE-K8S-0102-015](markdown/controls/SAFE-K8S-0102-015.md) | D01 | 1.2 | etcd certificate rotation testing and recovery validation | Practitioner | baseline |
| [SAFE-K8S-0102-016](markdown/controls/SAFE-K8S-0102-016.md) | D01 | 1.2 | etcd backup repository access restriction and break-glass authorization | Foundational | baseline |
| [SAFE-K8S-0102-017](markdown/controls/SAFE-K8S-0102-017.md) | D01 | 1.2 | etcd backup repository access audit logging and review | Foundational | baseline |
| [SAFE-K8S-0102-018](markdown/controls/SAFE-K8S-0102-018.md) | D01 | 1.2 | etcd client and peer certificate authentication | Foundational | baseline |
| [SAFE-K8S-0102-019](markdown/controls/SAFE-K8S-0102-019.md) | D01 | 1.2 | etcd endpoint network isolation from worker and workload traffic | Foundational | baseline |
| [SAFE-K8S-0102-020](markdown/controls/SAFE-K8S-0102-020.md) | D01 | 1.2 | etcd certificate maximum validity period enforcement | Practitioner | baseline |
| [SAFE-K8S-0102-021](markdown/controls/SAFE-K8S-0102-021.md) | D01 | 1.2 | etcd certificate expiration monitoring and lead-time alerting | Practitioner | baseline |
| [SAFE-K8S-0102-022](markdown/controls/SAFE-K8S-0102-022.md) | D01 | 1.2 | etcd backup repository least-privilege access restriction | Foundational | baseline |
| [SAFE-K8S-0102-023](markdown/controls/SAFE-K8S-0102-023.md) | D01 | 1.2 | etcd backup break-glass authorization governance | Foundational | baseline |
| [SAFE-K8S-0102-024](markdown/controls/SAFE-K8S-0102-024.md) | D01 | 1.2 | etcd backup repository access audit logging | Foundational | baseline |
| [SAFE-K8S-0102-025](markdown/controls/SAFE-K8S-0102-025.md) | D01 | 1.2 | etcd backup repository access review and alerting | Foundational | baseline |
| [SAFE-K8S-0103-001](markdown/controls/SAFE-K8S-0103-001.md) | D01 | 1.3 | Controller-manager service account token hardening | Foundational | baseline |
| [SAFE-K8S-0103-002](markdown/controls/SAFE-K8S-0103-002.md) | D01 | 1.3 | Scheduler access restriction and extender authentication | Practitioner | baseline |
| [SAFE-K8S-0103-003](markdown/controls/SAFE-K8S-0103-003.md) | D01 | 1.3 | Cloud controller-manager isolation and credential management | Practitioner | baseline |
| [SAFE-K8S-0103-004](markdown/controls/SAFE-K8S-0103-004.md) | D01 | 1.3 | Leader election security and control-plane high availability | Practitioner | baseline |
| [SAFE-K8S-0103-005](markdown/controls/SAFE-K8S-0103-005.md) | D01 | 1.3 | Pod garbage collection threshold configuration | Foundational | ai-specific |
| [SAFE-K8S-0103-006](markdown/controls/SAFE-K8S-0103-006.md) | D01 | 1.3 | Profiling endpoint disablement for controller-manager and scheduler | Foundational | baseline |
| [SAFE-K8S-0103-007](markdown/controls/SAFE-K8S-0103-007.md) | D01 | 1.3 | Controller-manager and scheduler bind-address and port hardening | Foundational | baseline |
| [SAFE-K8S-0103-008](markdown/controls/SAFE-K8S-0103-008.md) | D01 | 1.3 | Cloud controller-manager deployment isolation | Practitioner | baseline |
| [SAFE-K8S-0103-009](markdown/controls/SAFE-K8S-0103-009.md) | D01 | 1.3 | Cloud controller-manager IAM scoping and credential rotation | Practitioner | baseline |
| [SAFE-K8S-0103-010](markdown/controls/SAFE-K8S-0103-010.md) | D01 | 1.3 | Leader election configuration and lease object RBAC | Practitioner | baseline |
| [SAFE-K8S-0103-011](markdown/controls/SAFE-K8S-0103-011.md) | D01 | 1.3 | Control-plane high availability topology and failover | Practitioner | baseline |
| [SAFE-K8S-0103-012](markdown/controls/SAFE-K8S-0103-012.md) | D01 | 1.3 | Cloud controller-manager cloud IAM least-privilege scoping | Practitioner | baseline |
| [SAFE-K8S-0103-013](markdown/controls/SAFE-K8S-0103-013.md) | D01 | 1.3 | Cloud controller-manager workload identity and credential rotation | Practitioner | baseline |
| [SAFE-K8S-0103-014](markdown/controls/SAFE-K8S-0103-014.md) | D01 | 1.3 | Scheduler API and decision endpoint access restriction | Practitioner | baseline |
| [SAFE-K8S-0103-015](markdown/controls/SAFE-K8S-0103-015.md) | D01 | 1.3 | Scheduler extender authentication and custom scheduler approval | Practitioner | baseline |
| [SAFE-K8S-0103-016](markdown/controls/SAFE-K8S-0103-016.md) | D01 | 1.3 | Controller-manager and scheduler loopback bind-address enforcement | Foundational | baseline |
| [SAFE-K8S-0103-017](markdown/controls/SAFE-K8S-0103-017.md) | D01 | 1.3 | Controller-manager and scheduler insecure-port disablement and non-public health-metrics exposure | Foundational | baseline |
| [SAFE-K8S-0103-018](markdown/controls/SAFE-K8S-0103-018.md) | D01 | 1.3 | Control-plane replica distribution and etcd quorum topology | Practitioner | baseline |
| [SAFE-K8S-0103-019](markdown/controls/SAFE-K8S-0103-019.md) | D01 | 1.3 | API server load-balancer health-check failover | Practitioner | baseline |
| [SAFE-K8S-0104-001](markdown/controls/SAFE-K8S-0104-001.md) | D01 | 1.4 | CIS Kubernetes Benchmark automated assessment and remediation | Foundational | baseline |
| [SAFE-K8S-0104-002](markdown/controls/SAFE-K8S-0104-002.md) | D01 | 1.4 | Kubernetes version lifecycle and upgrade strategy management | Foundational | baseline |
| [SAFE-K8S-0104-003](markdown/controls/SAFE-K8S-0104-003.md) | D01 | 1.4 | Kubernetes CVE monitoring, prioritization, and emergency patching | Foundational | baseline |
| [SAFE-K8S-0104-004](markdown/controls/SAFE-K8S-0104-004.md) | D01 | 1.4 | Feature gate governance and lifecycle management | Practitioner | baseline |
| [SAFE-K8S-0104-005](markdown/controls/SAFE-K8S-0104-005.md) | D01 | 1.4 | Control plane configuration file permissions | Foundational | baseline |
| [SAFE-K8S-0104-006](markdown/controls/SAFE-K8S-0104-006.md) | D01 | 1.4 | Kubernetes CVE monitoring and prioritization | Foundational | baseline |
| [SAFE-K8S-0104-007](markdown/controls/SAFE-K8S-0104-007.md) | D01 | 1.4 | Emergency Kubernetes patch deployment procedures | Foundational | baseline |
| [SAFE-K8S-0104-008](markdown/controls/SAFE-K8S-0104-008.md) | D01 | 1.4 | Production feature gate approval and risk assessment governance | Practitioner | baseline |
| [SAFE-K8S-0104-009](markdown/controls/SAFE-K8S-0104-009.md) | D01 | 1.4 | Feature gate lifecycle transition tracking across Kubernetes upgrades | Practitioner | baseline |
| [SAFE-K8S-0104-010](markdown/controls/SAFE-K8S-0104-010.md) | D01 | 1.4 | Recurring CIS Kubernetes Benchmark assessment | Foundational | baseline |
| [SAFE-K8S-0104-011](markdown/controls/SAFE-K8S-0104-011.md) | D01 | 1.4 | CIS Benchmark remediation tracking and exception governance | Foundational | baseline |
| [SAFE-K8S-0104-012](markdown/controls/SAFE-K8S-0104-012.md) | D01 | 1.4 | Kubernetes supported version window and component skew compliance | Foundational | baseline |
| [SAFE-K8S-0104-013](markdown/controls/SAFE-K8S-0104-013.md) | D01 | 1.4 | Kubernetes upgrade strategy, validation, and rollback planning | Foundational | baseline |
| [SAFE-K8S-0104-014](markdown/controls/SAFE-K8S-0104-014.md) | D01 | 1.4 | Recurring CIS Kubernetes Benchmark scan execution | Foundational | baseline |
| [SAFE-K8S-0104-015](markdown/controls/SAFE-K8S-0104-015.md) | D01 | 1.4 | CIS Benchmark result retention and posture trend reporting | Foundational | baseline |
| [SAFE-K8S-0104-016](markdown/controls/SAFE-K8S-0104-016.md) | D01 | 1.4 | CIS Benchmark remediation workflow tracking | Foundational | baseline |
| [SAFE-K8S-0104-017](markdown/controls/SAFE-K8S-0104-017.md) | D01 | 1.4 | CIS Benchmark exception approval and re-review governance | Foundational | baseline |
| [SAFE-K8S-0104-018](markdown/controls/SAFE-K8S-0104-018.md) | D01 | 1.4 | Kubernetes security advisory and provider bulletin monitoring | Foundational | baseline |
| [SAFE-K8S-0104-019](markdown/controls/SAFE-K8S-0104-019.md) | D01 | 1.4 | Kubernetes CVE risk prioritization framework | Foundational | baseline |
| [SAFE-K8S-0104-020](markdown/controls/SAFE-K8S-0104-020.md) | D01 | 1.4 | Kubernetes supported version window compliance | Foundational | baseline |
| [SAFE-K8S-0104-021](markdown/controls/SAFE-K8S-0104-021.md) | D01 | 1.4 | Kubernetes component version skew compliance | Foundational | baseline |
| [SAFE-K8S-0104-022](markdown/controls/SAFE-K8S-0104-022.md) | D01 | 1.4 | Non-default feature gate inventory for production clusters | Practitioner | baseline |
| [SAFE-K8S-0104-023](markdown/controls/SAFE-K8S-0104-023.md) | D01 | 1.4 | Stage-based approval and risk assessment for production feature gates | Practitioner | baseline |
| [SAFE-K8S-0201-001](markdown/controls/SAFE-K8S-0201-001.md) | D02 | 2.1 | Kubelet authentication, authorization, and anonymous access hardening | Foundational | baseline |
| [SAFE-K8S-0201-002](markdown/controls/SAFE-K8S-0201-002.md) | D02 | 2.1 | Kubelet certificate rotation and TLS bootstrap | Foundational | baseline |
| [SAFE-K8S-0201-003](markdown/controls/SAFE-K8S-0201-003.md) | D02 | 2.1 | Node allocatable resources and eviction thresholds | Foundational | baseline |
| [SAFE-K8S-0201-004](markdown/controls/SAFE-K8S-0201-004.md) | D02 | 2.1 | Kubelet configuration file permissions and node-level audit controls | Foundational | baseline |
| [SAFE-K8S-0201-005](markdown/controls/SAFE-K8S-0201-005.md) | D02 | 2.1 | Kubelet hostname override governance | Foundational | baseline |
| [SAFE-K8S-0201-006](markdown/controls/SAFE-K8S-0201-006.md) | D02 | 2.1 | Node system and kube reserved resource allocations | Foundational | baseline |
| [SAFE-K8S-0201-007](markdown/controls/SAFE-K8S-0201-007.md) | D02 | 2.1 | Node eviction threshold tuning for workload pressure | Foundational | baseline |
| [SAFE-K8S-0201-008](markdown/controls/SAFE-K8S-0201-008.md) | D02 | 2.1 | Kubelet configuration and credential file ownership and permissions | Foundational | baseline |
| [SAFE-K8S-0201-009](markdown/controls/SAFE-K8S-0201-009.md) | D02 | 2.1 | Kubelet systemd unit hardening | Foundational | baseline |
| [SAFE-K8S-0201-010](markdown/controls/SAFE-K8S-0201-010.md) | D02 | 2.1 | Node-level kubelet audit verification | Foundational | baseline |
| [SAFE-K8S-0201-011](markdown/controls/SAFE-K8S-0201-011.md) | D02 | 2.1 | Kubelet webhook authentication and authorization enforcement | Foundational | baseline |
| [SAFE-K8S-0201-012](markdown/controls/SAFE-K8S-0201-012.md) | D02 | 2.1 | Kubelet anonymous access and read-only port lockdown | Foundational | baseline |
| [SAFE-K8S-0201-013](markdown/controls/SAFE-K8S-0201-013.md) | D02 | 2.1 | Kubelet client certificate rotation via TLS bootstrap | Foundational | baseline |
| [SAFE-K8S-0201-014](markdown/controls/SAFE-K8S-0201-014.md) | D02 | 2.1 | Kubelet serving certificate trust and expiry enforcement | Foundational | baseline |
| [SAFE-K8S-0201-015](markdown/controls/SAFE-K8S-0201-015.md) | D02 | 2.1 | Node-level kubelet audit rule coverage | Foundational | baseline |
| [SAFE-K8S-0201-016](markdown/controls/SAFE-K8S-0201-016.md) | D02 | 2.1 | Node audit log forwarding and centralized reviewability | Foundational | baseline |
| [SAFE-K8S-0202-001](markdown/controls/SAFE-K8S-0202-001.md) | D02 | 2.2 | Container runtime configuration baselines and socket protection | Foundational | baseline |
| [SAFE-K8S-0202-002](markdown/controls/SAFE-K8S-0202-002.md) | D02 | 2.2 | RuntimeClass configuration for workload-appropriate isolation | Foundational | ai-specific |
| [SAFE-K8S-0202-003](markdown/controls/SAFE-K8S-0202-003.md) | D02 | 2.2 | Container runtime patching and version management | Foundational | baseline |
| [SAFE-K8S-0202-004](markdown/controls/SAFE-K8S-0202-004.md) | D02 | 2.2 | Runtime socket mount prevention | Foundational | baseline |
| [SAFE-K8S-0202-005](markdown/controls/SAFE-K8S-0202-005.md) | D02 | 2.2 | Container escape prevention through kernel security profiles | Foundational | baseline |
| [SAFE-K8S-0202-006](markdown/controls/SAFE-K8S-0202-006.md) | D02 | 2.2 | Node seccomp defaults and mandatory access control activation | Foundational | baseline |
| [SAFE-K8S-0202-007](markdown/controls/SAFE-K8S-0202-007.md) | D02 | 2.2 | Container runtime user namespace isolation | Foundational | baseline |
| [SAFE-K8S-0202-008](markdown/controls/SAFE-K8S-0202-008.md) | D02 | 2.2 | Container runtime socket root-only protection | Foundational | baseline |
| [SAFE-K8S-0202-009](markdown/controls/SAFE-K8S-0202-009.md) | D02 | 2.2 | Container runtime secure baseline settings and debug endpoint disablement | Foundational | baseline |
| [SAFE-K8S-0202-010](markdown/controls/SAFE-K8S-0202-010.md) | D02 | 2.2 | Node default seccomp profile enforcement | Foundational | baseline |
| [SAFE-K8S-0202-011](markdown/controls/SAFE-K8S-0202-011.md) | D02 | 2.2 | Node mandatory access control activation for container workloads | Foundational | baseline |
| [SAFE-K8S-0203-001](markdown/controls/SAFE-K8S-0203-001.md) | D02 | 2.3 | Minimal and immutable host OS configuration | Foundational | baseline |
| [SAFE-K8S-0203-002](markdown/controls/SAFE-K8S-0203-002.md) | D02 | 2.3 | Kernel parameter hardening via sysctl | Foundational | baseline |
| [SAFE-K8S-0203-003](markdown/controls/SAFE-K8S-0203-003.md) | D02 | 2.3 | Cloud metadata service protection and IMDSv2 enforcement | Foundational | baseline |
| [SAFE-K8S-0203-004](markdown/controls/SAFE-K8S-0203-004.md) | D02 | 2.3 | Secure boot and verified boot chain enforcement | Foundational | baseline |
| [SAFE-K8S-0203-005](markdown/controls/SAFE-K8S-0203-005.md) | D02 | 2.3 | Kernel module restriction and lockdown mode | Foundational | baseline |
| [SAFE-K8S-0203-006](markdown/controls/SAFE-K8S-0203-006.md) | D02 | 2.3 | Cloud instance metadata service hardening and IMDSv2 configuration | Foundational | baseline |
| [SAFE-K8S-0203-007](markdown/controls/SAFE-K8S-0203-007.md) | D02 | 2.3 | Pod metadata endpoint blocking and workload identity replacement | Foundational | baseline |
| [SAFE-K8S-0203-008](markdown/controls/SAFE-K8S-0203-008.md) | D02 | 2.3 | Pod metadata endpoint network path blocking | Foundational | baseline |
| [SAFE-K8S-0203-009](markdown/controls/SAFE-K8S-0203-009.md) | D02 | 2.3 | Workload identity replacement for cloud API access | Foundational | baseline |
| [SAFE-K8S-0203-010](markdown/controls/SAFE-K8S-0203-010.md) | D02 | 2.3 | Minimal purpose-built node OS baseline | Foundational | baseline |
| [SAFE-K8S-0203-011](markdown/controls/SAFE-K8S-0203-011.md) | D02 | 2.3 | Immutable node root filesystem enforcement | Foundational | baseline |
| [SAFE-K8S-0203-012](markdown/controls/SAFE-K8S-0203-012.md) | D02 | 2.3 | Kernel module restriction and approved module whitelisting | Foundational | baseline |
| [SAFE-K8S-0203-013](markdown/controls/SAFE-K8S-0203-013.md) | D02 | 2.3 | Kernel lockdown mode enforcement for runtime integrity | Foundational | baseline |
| [SAFE-K8S-0203-014](markdown/controls/SAFE-K8S-0203-014.md) | D02 | 2.3 | Authenticated cloud metadata service mode enforcement | Foundational | baseline |
| [SAFE-K8S-0203-015](markdown/controls/SAFE-K8S-0203-015.md) | D02 | 2.3 | Cloud metadata endpoint restriction settings | Foundational | baseline |
| [SAFE-K8S-0204-001](markdown/controls/SAFE-K8S-0204-001.md) | D02 | 2.4 | Runtime security tool deployment for syscall and network monitoring | Practitioner | baseline |
| [SAFE-K8S-0204-002](markdown/controls/SAFE-K8S-0204-002.md) | D02 | 2.4 | Kubernetes-specific runtime detection rules | Practitioner | baseline |
| [SAFE-K8S-0204-003](markdown/controls/SAFE-K8S-0204-003.md) | D02 | 2.4 | Container filesystem drift detection | Practitioner | baseline |
| [SAFE-K8S-0204-004](markdown/controls/SAFE-K8S-0204-004.md) | D02 | 2.4 | Forensic capture capabilities for container incident investigation | Practitioner | baseline |
| [SAFE-K8S-0205-001](markdown/controls/SAFE-K8S-0205-001.md) | D02 | 2.5 | kube-proxy mode selection and security hardening | Practitioner | baseline |
| [SAFE-K8S-0205-002](markdown/controls/SAFE-K8S-0205-002.md) | D02 | 2.5 | NodePort and HostPort restriction policies | Practitioner | baseline |
| [SAFE-K8S-0205-003](markdown/controls/SAFE-K8S-0205-003.md) | D02 | 2.5 | Node-level firewall and Kubernetes network policy integration | Practitioner | baseline |
| [SAFE-K8S-0205-004](markdown/controls/SAFE-K8S-0205-004.md) | D02 | 2.5 | eBPF-based kernel-level network policy enforcement | Practitioner | baseline |
| [SAFE-K8S-0205-005](markdown/controls/SAFE-K8S-0205-005.md) | D02 | 2.5 | eBPF program integrity verification and loading monitoring | Practitioner | baseline |
| [SAFE-K8S-0205-006](markdown/controls/SAFE-K8S-0205-006.md) | D02 | 2.5 | Node-level firewall rule restriction and audit | Practitioner | baseline |
| [SAFE-K8S-0205-007](markdown/controls/SAFE-K8S-0205-007.md) | D02 | 2.5 | Node firewall compatibility validation with CNI and network policy | Practitioner | baseline |
| [SAFE-K8S-0205-008](markdown/controls/SAFE-K8S-0205-008.md) | D02 | 2.5 | kube-proxy or service proxy mode selection governance | Practitioner | baseline |
| [SAFE-K8S-0205-009](markdown/controls/SAFE-K8S-0205-009.md) | D02 | 2.5 | Service proxy path hardening for kube-proxy or replacements | Practitioner | baseline |
| [SAFE-K8S-0205-010](markdown/controls/SAFE-K8S-0205-010.md) | D02 | 2.5 | Node-level firewall rule restriction for cluster communication | Practitioner | baseline |
| [SAFE-K8S-0205-011](markdown/controls/SAFE-K8S-0205-011.md) | D02 | 2.5 | Node firewall audit and change governance | Practitioner | baseline |
| [SAFE-K8S-0301-001](markdown/controls/SAFE-K8S-0301-001.md) | D03 | 3.1 | Pod Security Standards level assignment | Foundational | baseline |
| [SAFE-K8S-0301-002](markdown/controls/SAFE-K8S-0301-002.md) | D03 | 3.1 | Pod Security Admission configuration and version pinning | Foundational | baseline |
| [SAFE-K8S-0301-003](markdown/controls/SAFE-K8S-0301-003.md) | D03 | 3.1 | PodSecurityPolicy to PSA migration | Foundational | baseline |
| [SAFE-K8S-0301-004](markdown/controls/SAFE-K8S-0301-004.md) | D03 | 3.1 | PSA exemption management for privileged system and GPU workloads | Foundational | ai-specific |
| [SAFE-K8S-0301-005](markdown/controls/SAFE-K8S-0301-005.md) | D03 | 3.1 | PSA exemption register and justification tracking | Foundational | ai-specific |
| [SAFE-K8S-0301-006](markdown/controls/SAFE-K8S-0301-006.md) | D03 | 3.1 | Scoped PSA exception enforcement and compensating controls | Foundational | ai-specific |
| [SAFE-K8S-0302-001](markdown/controls/SAFE-K8S-0302-001.md) | D03 | 3.2 | Pod and container security context enforcement | Foundational | baseline |
| [SAFE-K8S-0302-002](markdown/controls/SAFE-K8S-0302-002.md) | D03 | 3.2 | Linux capability drop-all and least-privilege add-back | Foundational | ai-specific |
| [SAFE-K8S-0302-003](markdown/controls/SAFE-K8S-0302-003.md) | D03 | 3.2 | Privilege escalation prevention controls | Foundational | baseline |
| [SAFE-K8S-0302-004](markdown/controls/SAFE-K8S-0302-004.md) | D03 | 3.2 | Host namespace isolation enforcement | Foundational | baseline |
| [SAFE-K8S-0302-005](markdown/controls/SAFE-K8S-0302-005.md) | D03 | 3.2 | AI workload security context hardening profiles | Foundational | ai-specific |
| [SAFE-K8S-0302-006](markdown/controls/SAFE-K8S-0302-006.md) | D03 | 3.2 | No-new-privileges execution enforcement | Foundational | baseline |
| [SAFE-K8S-0302-007](markdown/controls/SAFE-K8S-0302-007.md) | D03 | 3.2 | Safe fsGroup and supplementalGroups volume ownership | Foundational | baseline |
| [SAFE-K8S-0303-001](markdown/controls/SAFE-K8S-0303-001.md) | D03 | 3.3 | Seccomp profile enforcement | Practitioner | baseline |
| [SAFE-K8S-0303-002](markdown/controls/SAFE-K8S-0303-002.md) | D03 | 3.3 | AppArmor profile management and enforcement | Practitioner | baseline |
| [SAFE-K8S-0303-003](markdown/controls/SAFE-K8S-0303-003.md) | D03 | 3.3 | SELinux context assignment and multi-tenancy isolation | Practitioner | baseline |
| [SAFE-K8S-0303-004](markdown/controls/SAFE-K8S-0303-004.md) | D03 | 3.3 | MAC profile generation from runtime behavior | Practitioner | baseline |
| [SAFE-K8S-0303-005](markdown/controls/SAFE-K8S-0303-005.md) | D03 | 3.3 | MAC profile pre-enforcement audit-mode validation | Practitioner | baseline |
| [SAFE-K8S-0303-006](markdown/controls/SAFE-K8S-0303-006.md) | D03 | 3.3 | MAC profile iterative refinement cycle | Practitioner | baseline |
| [SAFE-K8S-0303-007](markdown/controls/SAFE-K8S-0303-007.md) | D03 | 3.3 | AppArmor profile distribution and node readiness | Practitioner | baseline |
| [SAFE-K8S-0303-008](markdown/controls/SAFE-K8S-0303-008.md) | D03 | 3.3 | AppArmor workload profile assignment and unconfined-mode restriction | Practitioner | baseline |
| [SAFE-K8S-0304-001](markdown/controls/SAFE-K8S-0304-001.md) | D03 | 3.4 | Cloud Native 8 secure defaults enforcement | Foundational | baseline |
| [SAFE-K8S-0304-002](markdown/controls/SAFE-K8S-0304-002.md) | D03 | 3.4 | CPU, memory, and ephemeral storage resource limits | Foundational | baseline |
| [SAFE-K8S-0304-003](markdown/controls/SAFE-K8S-0304-003.md) | D03 | 3.4 | QoS class assignment for workload stability | Foundational | baseline |
| [SAFE-K8S-0304-004](markdown/controls/SAFE-K8S-0304-004.md) | D03 | 3.4 | Ephemeral container security context enforcement | Foundational | baseline |
| [SAFE-K8S-0304-005](markdown/controls/SAFE-K8S-0304-005.md) | D03 | 3.4 | Training job ephemeral storage and scratch space security | Foundational | ai-specific |
| [SAFE-K8S-0304-006](markdown/controls/SAFE-K8S-0304-006.md) | D03 | 3.4 | Host volume mount restriction | Foundational | baseline |
| [SAFE-K8S-0304-007](markdown/controls/SAFE-K8S-0304-007.md) | D03 | 3.4 | Service account token automount opt-out | Foundational | baseline |
| [SAFE-K8S-0304-008](markdown/controls/SAFE-K8S-0304-008.md) | D03 | 3.4 | Training scratch volume limits and tmpfs handling | Foundational | ai-specific |
| [SAFE-K8S-0304-009](markdown/controls/SAFE-K8S-0304-009.md) | D03 | 3.4 | Temporary checkpoint storage encryption, integrity, and access control | Foundational | ai-specific |
| [SAFE-K8S-0304-010](markdown/controls/SAFE-K8S-0304-010.md) | D03 | 3.4 | Pod resource requests and limits specification | Foundational | baseline |
| [SAFE-K8S-0304-011](markdown/controls/SAFE-K8S-0304-011.md) | D03 | 3.4 | Namespace LimitRange and ResourceQuota enforcement | Foundational | baseline |
| [SAFE-K8S-0304-012](markdown/controls/SAFE-K8S-0304-012.md) | D03 | 3.4 | Training scratch volume size limits and ephemeral-storage quotas | Foundational | baseline |
| [SAFE-K8S-0304-013](markdown/controls/SAFE-K8S-0304-013.md) | D03 | 3.4 | Tmpfs-backed handling for sensitive training intermediates | Foundational | baseline |
| [SAFE-K8S-0401-001](markdown/controls/SAFE-K8S-0401-001.md) | D04 | 4.1 | RBAC least-privilege design | Foundational | baseline |
| [SAFE-K8S-0401-002](markdown/controls/SAFE-K8S-0401-002.md) | D04 | 4.1 | RBAC permission audit and analysis | Foundational | baseline |
| [SAFE-K8S-0401-003](markdown/controls/SAFE-K8S-0401-003.md) | D04 | 4.1 | Aggregated ClusterRole governance | Foundational | baseline |
| [SAFE-K8S-0401-004](markdown/controls/SAFE-K8S-0401-004.md) | D04 | 4.1 | RBAC for AI operator custom resources | Foundational | ai-specific |
| [SAFE-K8S-0401-005](markdown/controls/SAFE-K8S-0401-005.md) | D04 | 4.1 | Separation of duties for ML, platform, and security roles | Foundational | ai-specific |
| [SAFE-K8S-0401-006](markdown/controls/SAFE-K8S-0401-006.md) | D04 | 4.1 | Organizational role separation for ML, platform, and security functions | Foundational | ai-specific |
| [SAFE-K8S-0401-007](markdown/controls/SAFE-K8S-0401-007.md) | D04 | 4.1 | GPU resource governance permission boundaries | Foundational | ai-specific |
| [SAFE-K8S-0402-001](markdown/controls/SAFE-K8S-0402-001.md) | D04 | 4.2 | Default service account restriction | Foundational | baseline |
| [SAFE-K8S-0402-002](markdown/controls/SAFE-K8S-0402-002.md) | D04 | 4.2 | Inactive service account and stale credential remediation | Practitioner | baseline |
| [SAFE-K8S-0402-003](markdown/controls/SAFE-K8S-0402-003.md) | D04 | 4.2 | Service account identifier exposure prevention | Practitioner | baseline |
| [SAFE-K8S-0402-004](markdown/controls/SAFE-K8S-0402-004.md) | D04 | 4.2 | Workload identity attribute integrity | Practitioner | baseline |
| [SAFE-K8S-0402-005](markdown/controls/SAFE-K8S-0402-005.md) | D04 | 4.2 | Projected service account token configuration | Foundational | baseline |
| [SAFE-K8S-0402-006](markdown/controls/SAFE-K8S-0402-006.md) | D04 | 4.2 | Cloud workload identity federation for AI services | Practitioner | ai-specific |
| [SAFE-K8S-0402-007](markdown/controls/SAFE-K8S-0402-007.md) | D04 | 4.2 | OIDC authentication integration | Practitioner | baseline |
| [SAFE-K8S-0402-008](markdown/controls/SAFE-K8S-0402-008.md) | D04 | 4.2 | Distinct identity assignment for AI workload types | Practitioner | ai-specific |
| [SAFE-K8S-0402-009](markdown/controls/SAFE-K8S-0402-009.md) | D04 | 4.2 | Ephemeral training job credential lifecycle management | Practitioner | ai-specific |
| [SAFE-K8S-0402-010](markdown/controls/SAFE-K8S-0402-010.md) | D04 | 4.2 | Cross-cluster and cross-cloud cryptographic identity federation | Advanced | ai-specific |
| [SAFE-K8S-0402-011](markdown/controls/SAFE-K8S-0402-011.md) | D04 | 4.2 | Cross-environment static credential prohibition | Advanced | ai-specific |
| [SAFE-K8S-0402-012](markdown/controls/SAFE-K8S-0402-012.md) | D04 | 4.2 | Ephemeral training job credential expiration | Practitioner | ai-specific |
| [SAFE-K8S-0402-013](markdown/controls/SAFE-K8S-0402-013.md) | D04 | 4.2 | Ephemeral training job credential rotation | Practitioner | ai-specific |
| [SAFE-K8S-0402-014](markdown/controls/SAFE-K8S-0402-014.md) | D04 | 4.2 | Ephemeral training job credential revocation on completion | Practitioner | ai-specific |
| [SAFE-K8S-0402-015](markdown/controls/SAFE-K8S-0402-015.md) | D04 | 4.2 | Legacy service account token secret removal | Foundational | baseline |
| [SAFE-K8S-0402-016](markdown/controls/SAFE-K8S-0402-016.md) | D04 | 4.2 | Projected service account token audience and TokenRequest enforcement | Foundational | baseline |
| [SAFE-K8S-0402-017](markdown/controls/SAFE-K8S-0402-017.md) | D04 | 4.2 | Projected token lifetime bounds and long-lived token exception governance | Foundational | baseline |
| [SAFE-K8S-0402-018](markdown/controls/SAFE-K8S-0402-018.md) | D04 | 4.2 | Default service account disablement and token automount hardening | Foundational | baseline |
| [SAFE-K8S-0402-019](markdown/controls/SAFE-K8S-0402-019.md) | D04 | 4.2 | Dedicated workload service accounts and least-privilege assignment | Foundational | baseline |
| [SAFE-K8S-0402-020](markdown/controls/SAFE-K8S-0402-020.md) | D04 | 4.2 | Projected service account token issuance path enforcement | Foundational | baseline |
| [SAFE-K8S-0402-021](markdown/controls/SAFE-K8S-0402-021.md) | D04 | 4.2 | Workload token explicit audience binding | Foundational | baseline |
| [SAFE-K8S-0402-022](markdown/controls/SAFE-K8S-0402-022.md) | D04 | 4.2 | Projected service account token lifetime bounds enforcement | Foundational | baseline |
| [SAFE-K8S-0402-023](markdown/controls/SAFE-K8S-0402-023.md) | D04 | 4.2 | Long-lived workload token exception governance and retirement tracking | Foundational | baseline |
| [SAFE-K8S-0403-001](markdown/controls/SAFE-K8S-0403-001.md) | D04 | 4.3 | Kubernetes Secrets external KMS integration and key lifecycle | Foundational | baseline |
| [SAFE-K8S-0403-002](markdown/controls/SAFE-K8S-0403-002.md) | D04 | 4.3 | External secrets management integration | Foundational | baseline |
| [SAFE-K8S-0403-003](markdown/controls/SAFE-K8S-0403-003.md) | D04 | 4.3 | Approved secret injection pattern standards | Foundational | baseline |
| [SAFE-K8S-0403-004](markdown/controls/SAFE-K8S-0403-004.md) | D04 | 4.3 | Secret rotation and expiration enforcement | Foundational | baseline |
| [SAFE-K8S-0403-005](markdown/controls/SAFE-K8S-0403-005.md) | D04 | 4.3 | AI pipeline secret leakage prevention | Foundational | ai-specific |
| [SAFE-K8S-0403-006](markdown/controls/SAFE-K8S-0403-006.md) | D04 | 4.3 | Per-workload credential scoping for AI jobs | Practitioner | ai-specific |
| [SAFE-K8S-0403-007](markdown/controls/SAFE-K8S-0403-007.md) | D04 | 4.3 | AI platform key hierarchy and KMS architecture | Advanced | ai-specific |
| [SAFE-K8S-0403-008](markdown/controls/SAFE-K8S-0403-008.md) | D04 | 4.3 | Credential inventory and sprawl governance at scale | Practitioner | ai-specific |
| [SAFE-K8S-0403-009](markdown/controls/SAFE-K8S-0403-009.md) | D04 | 4.3 | Automated secret leak detection and response | Practitioner | baseline |
| [SAFE-K8S-0403-010](markdown/controls/SAFE-K8S-0403-010.md) | D04 | 4.3 | Kubernetes Secrets external KMS integration and least-privilege key policy | Foundational | baseline |
| [SAFE-K8S-0403-011](markdown/controls/SAFE-K8S-0403-011.md) | D04 | 4.3 | Secrets KMS key rotation and re-encryption verification | Foundational | baseline |
| [SAFE-K8S-0403-012](markdown/controls/SAFE-K8S-0403-012.md) | D04 | 4.3 | Automated credential inventory and orphaned credential reconciliation | Practitioner | ai-specific |
| [SAFE-K8S-0403-013](markdown/controls/SAFE-K8S-0403-013.md) | D04 | 4.3 | Credential scope drift monitoring and lifecycle metrics governance | Practitioner | ai-specific |
| [SAFE-K8S-0403-014](markdown/controls/SAFE-K8S-0403-014.md) | D04 | 4.3 | Automated secret leak detection coverage and enforcement | Practitioner | baseline |
| [SAFE-K8S-0403-015](markdown/controls/SAFE-K8S-0403-015.md) | D04 | 4.3 | Secret leak incident response and credential revocation | Practitioner | baseline |
| [SAFE-K8S-0403-016](markdown/controls/SAFE-K8S-0403-016.md) | D04 | 4.3 | Environment variable secret injection prohibition and exception governance | Foundational | baseline |
| [SAFE-K8S-0403-017](markdown/controls/SAFE-K8S-0403-017.md) | D04 | 4.3 | AI platform key-domain hierarchy and envelope encryption architecture | Foundational | baseline |
| [SAFE-K8S-0403-018](markdown/controls/SAFE-K8S-0403-018.md) | D04 | 4.3 | AI platform cryptographic key access domain separation | Foundational | baseline |
| [SAFE-K8S-0403-019](markdown/controls/SAFE-K8S-0403-019.md) | D04 | 4.3 | Kubernetes Secrets external KMS provider integration | Foundational | baseline |
| [SAFE-K8S-0403-020](markdown/controls/SAFE-K8S-0403-020.md) | D04 | 4.3 | Kubernetes Secrets KMS key least-privilege access policy | Foundational | baseline |
| [SAFE-K8S-0403-021](markdown/controls/SAFE-K8S-0403-021.md) | D04 | 4.3 | Automated AI workload credential inventory | Practitioner | ai-specific |
| [SAFE-K8S-0403-022](markdown/controls/SAFE-K8S-0403-022.md) | D04 | 4.3 | Orphaned AI workload credential detection and remediation | Practitioner | ai-specific |
| [SAFE-K8S-0403-023](markdown/controls/SAFE-K8S-0403-023.md) | D04 | 4.3 | Credential scope drift monitoring for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0403-024](markdown/controls/SAFE-K8S-0403-024.md) | D04 | 4.3 | Credential lifecycle metrics publication and governance | Practitioner | ai-specific |
| [SAFE-K8S-0403-025](markdown/controls/SAFE-K8S-0403-025.md) | D04 | 4.3 | Automated secret leak detection coverage across development and runtime surfaces | Practitioner | baseline |
| [SAFE-K8S-0403-026](markdown/controls/SAFE-K8S-0403-026.md) | D04 | 4.3 | Secret leak prevention gate and enforcement controls | Practitioner | baseline |
| [SAFE-K8S-0403-027](markdown/controls/SAFE-K8S-0403-027.md) | D04 | 4.3 | Secret leak incident triage and containment workflow | Practitioner | baseline |
| [SAFE-K8S-0403-028](markdown/controls/SAFE-K8S-0403-028.md) | D04 | 4.3 | Exposed credential revocation and replacement execution | Practitioner | baseline |
| [SAFE-K8S-0403-029](markdown/controls/SAFE-K8S-0403-029.md) | D04 | 4.3 | Environment variable secret injection prohibition enforcement | Foundational | baseline |
| [SAFE-K8S-0403-030](markdown/controls/SAFE-K8S-0403-030.md) | D04 | 4.3 | Environment variable secret injection exception governance | Foundational | baseline |
| [SAFE-K8S-0404-001](markdown/controls/SAFE-K8S-0404-001.md) | D04 | 4.4 | cert-manager deployment and Issuer configuration | Practitioner | baseline |
| [SAFE-K8S-0404-002](markdown/controls/SAFE-K8S-0404-002.md) | D04 | 4.4 | TLS provisioning for webhooks, API aggregation, and internal services | Practitioner | baseline |
| [SAFE-K8S-0404-003](markdown/controls/SAFE-K8S-0404-003.md) | D04 | 4.4 | mTLS for service-to-service authentication | Practitioner | baseline |
| [SAFE-K8S-0404-004](markdown/controls/SAFE-K8S-0404-004.md) | D04 | 4.4 | Certificate rotation, expiry monitoring, and compromise response | Practitioner | baseline |
| [SAFE-K8S-0404-005](markdown/controls/SAFE-K8S-0404-005.md) | D04 | 4.4 | Certificate rotation execution and expiry monitoring | Practitioner | baseline |
| [SAFE-K8S-0404-006](markdown/controls/SAFE-K8S-0404-006.md) | D04 | 4.4 | Certificate compromise revocation and re-issuance response | Practitioner | baseline |
| [SAFE-K8S-0404-007](markdown/controls/SAFE-K8S-0404-007.md) | D04 | 4.4 | Automated certificate rotation before expiry | Practitioner | baseline |
| [SAFE-K8S-0404-008](markdown/controls/SAFE-K8S-0404-008.md) | D04 | 4.4 | Certificate expiry monitoring and alerting | Practitioner | baseline |
| [SAFE-K8S-0404-009](markdown/controls/SAFE-K8S-0404-009.md) | D04 | 4.4 | Compromised certificate revocation and re-issuance execution | Practitioner | baseline |
| [SAFE-K8S-0404-010](markdown/controls/SAFE-K8S-0404-010.md) | D04 | 4.4 | Post-compromise certificate recovery validation | Practitioner | baseline |
| [SAFE-K8S-0405-001](markdown/controls/SAFE-K8S-0405-001.md) | D04 | 4.5 | API impersonation restriction and auditing | Practitioner | baseline |
| [SAFE-K8S-0405-002](markdown/controls/SAFE-K8S-0405-002.md) | D04 | 4.5 | Privilege escalation detection and monitoring | Practitioner | baseline |
| [SAFE-K8S-0405-003](markdown/controls/SAFE-K8S-0405-003.md) | D04 | 4.5 | Kubeconfig security and hygiene | Practitioner | baseline |
| [SAFE-K8S-0405-004](markdown/controls/SAFE-K8S-0405-004.md) | D04 | 4.5 | Security awareness for Kubernetes and GPU administrators | Practitioner | baseline |
| [SAFE-K8S-0405-005](markdown/controls/SAFE-K8S-0405-005.md) | D04 | 4.5 | Credential management and multi-factor authentication | Practitioner | baseline |
| [SAFE-K8S-0405-006](markdown/controls/SAFE-K8S-0405-006.md) | D04 | 4.5 | Attribute-based access control for AI artifacts | Advanced | ai-specific |
| [SAFE-K8S-0405-007](markdown/controls/SAFE-K8S-0405-007.md) | D04 | 4.5 | Authentication endpoint availability and DoS protection | Practitioner | baseline |
| [SAFE-K8S-0405-008](markdown/controls/SAFE-K8S-0405-008.md) | D04 | 4.5 | Break-glass emergency access procedures | Practitioner | baseline |
| [SAFE-K8S-0405-009](markdown/controls/SAFE-K8S-0405-009.md) | D04 | 4.5 | API impersonation RBAC restriction | Practitioner | baseline |
| [SAFE-K8S-0405-010](markdown/controls/SAFE-K8S-0405-010.md) | D04 | 4.5 | API impersonation audit logging and alerting | Practitioner | baseline |
| [SAFE-K8S-0405-011](markdown/controls/SAFE-K8S-0405-011.md) | D04 | 4.5 | Credential policy and secure storage governance | Practitioner | baseline |
| [SAFE-K8S-0405-012](markdown/controls/SAFE-K8S-0405-012.md) | D04 | 4.5 | Privileged MFA enforcement for cluster administration | Practitioner | baseline |
| [SAFE-K8S-0405-013](markdown/controls/SAFE-K8S-0405-013.md) | D04 | 4.5 | Break-glass recovery procedure definition and testing | Practitioner | baseline |
| [SAFE-K8S-0405-014](markdown/controls/SAFE-K8S-0405-014.md) | D04 | 4.5 | Break-glass access auditing, dual-authorization, and automatic expiration | Practitioner | baseline |
| [SAFE-K8S-0405-015](markdown/controls/SAFE-K8S-0405-015.md) | D04 | 4.5 | Break-glass dual-authorization and tenant-scoped activation guardrails | Practitioner | baseline |
| [SAFE-K8S-0405-016](markdown/controls/SAFE-K8S-0405-016.md) | D04 | 4.5 | Break-glass access audit logging and automatic expiration | Practitioner | baseline |
| [SAFE-K8S-0405-017](markdown/controls/SAFE-K8S-0405-017.md) | D04 | 4.5 | Credential policy baseline requirements | Practitioner | baseline |
| [SAFE-K8S-0405-018](markdown/controls/SAFE-K8S-0405-018.md) | D04 | 4.5 | Secure credential storage and lifecycle governance | Practitioner | baseline |
| [SAFE-K8S-0405-019](markdown/controls/SAFE-K8S-0405-019.md) | D04 | 4.5 | Break-glass recovery procedure definition | Practitioner | baseline |
| [SAFE-K8S-0405-020](markdown/controls/SAFE-K8S-0405-020.md) | D04 | 4.5 | Break-glass recovery exercise validation | Practitioner | baseline |
| [SAFE-K8S-0405-021](markdown/controls/SAFE-K8S-0405-021.md) | D04 | 4.5 | Break-glass activation multi-party approval enforcement | Practitioner | baseline |
| [SAFE-K8S-0405-022](markdown/controls/SAFE-K8S-0405-022.md) | D04 | 4.5 | Tenant-scoped break-glass credential boundary enforcement | Practitioner | baseline |
| [SAFE-K8S-0405-023](markdown/controls/SAFE-K8S-0405-023.md) | D04 | 4.5 | Break-glass access audit logging coverage | Practitioner | baseline |
| [SAFE-K8S-0405-024](markdown/controls/SAFE-K8S-0405-024.md) | D04 | 4.5 | Break-glass credential automatic expiration and revocation enforcement | Practitioner | baseline |
| [SAFE-K8S-0501-001](markdown/controls/SAFE-K8S-0501-001.md) | D05 | 5.1 | Default deny ingress and egress network policies | Foundational | baseline |
| [SAFE-K8S-0501-002](markdown/controls/SAFE-K8S-0501-002.md) | D05 | 5.1 | Namespace network isolation patterns | Foundational | baseline |
| [SAFE-K8S-0501-003](markdown/controls/SAFE-K8S-0501-003.md) | D05 | 5.1 | Workload egress controls | Foundational | baseline |
| [SAFE-K8S-0501-004](markdown/controls/SAFE-K8S-0501-004.md) | D05 | 5.1 | CNI-specific network policy extensions | Practitioner | baseline |
| [SAFE-K8S-0501-005](markdown/controls/SAFE-K8S-0501-005.md) | D05 | 5.1 | AI workload network segmentation | Foundational | ai-specific |
| [SAFE-K8S-0501-006](markdown/controls/SAFE-K8S-0501-006.md) | D05 | 5.1 | Multi-cluster network segmentation for federated AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0501-007](markdown/controls/SAFE-K8S-0501-007.md) | D05 | 5.1 | East-west AI workload traffic monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0501-008](markdown/controls/SAFE-K8S-0501-008.md) | D05 | 5.1 | AI workload type network microsegmentation | Foundational | ai-specific |
| [SAFE-K8S-0501-009](markdown/controls/SAFE-K8S-0501-009.md) | D05 | 5.1 | Model download path isolation from training data paths | Foundational | ai-specific |
| [SAFE-K8S-0502-001](markdown/controls/SAFE-K8S-0502-001.md) | D05 | 5.2 | CNI plugin security selection criteria | Practitioner | baseline |
| [SAFE-K8S-0502-002](markdown/controls/SAFE-K8S-0502-002.md) | D05 | 5.2 | Pod-to-pod traffic encryption | Practitioner | baseline |
| [SAFE-K8S-0502-003](markdown/controls/SAFE-K8S-0502-003.md) | D05 | 5.2 | IPAM security and IP spoofing protection | Practitioner | baseline |
| [SAFE-K8S-0502-004](markdown/controls/SAFE-K8S-0502-004.md) | D05 | 5.2 | CNI plugin hardening and lifecycle management | Practitioner | baseline |
| [SAFE-K8S-0502-005](markdown/controls/SAFE-K8S-0502-005.md) | D05 | 5.2 | AI workload data path encryption in transit | Practitioner | ai-specific |
| [SAFE-K8S-0502-006](markdown/controls/SAFE-K8S-0502-006.md) | D05 | 5.2 | Kubernetes CNI IPAM capacity sizing and exhaustion monitoring | Practitioner | baseline |
| [SAFE-K8S-0502-007](markdown/controls/SAFE-K8S-0502-007.md) | D05 | 5.2 | Kubernetes pod IP anti-spoofing enforcement and validation | Practitioner | baseline |
| [SAFE-K8S-0502-008](markdown/controls/SAFE-K8S-0502-008.md) | D05 | 5.2 | Network policy design for AI-specific traffic patterns | Practitioner | ai-specific |
| [SAFE-K8S-0502-009](markdown/controls/SAFE-K8S-0502-009.md) | D05 | 5.2 | Kubernetes CNI IPAM capacity sizing | Practitioner | baseline |
| [SAFE-K8S-0502-010](markdown/controls/SAFE-K8S-0502-010.md) | D05 | 5.2 | Kubernetes CNI IP pool exhaustion monitoring and alerting | Practitioner | baseline |
| [SAFE-K8S-0503-001](markdown/controls/SAFE-K8S-0503-001.md) | D05 | 5.3 | Ingress controller hardening | Practitioner | baseline |
| [SAFE-K8S-0503-002](markdown/controls/SAFE-K8S-0503-002.md) | D05 | 5.3 | DNS infrastructure hardening | Practitioner | baseline |
| [SAFE-K8S-0503-003](markdown/controls/SAFE-K8S-0503-003.md) | D05 | 5.3 | External traffic policy and source IP preservation | Practitioner | baseline |
| [SAFE-K8S-0503-004](markdown/controls/SAFE-K8S-0503-004.md) | D05 | 5.3 | Internal load balancer annotation enforcement | Practitioner | baseline |
| [SAFE-K8S-0503-005](markdown/controls/SAFE-K8S-0503-005.md) | D05 | 5.3 | DNS exfiltration detection | Practitioner | baseline |
| [SAFE-K8S-0503-006](markdown/controls/SAFE-K8S-0503-006.md) | D05 | 5.3 | Cloud load balancer security group configuration | Practitioner | baseline |
| [SAFE-K8S-0503-007](markdown/controls/SAFE-K8S-0503-007.md) | D05 | 5.3 | Ingress TLS termination and boundary configuration hardening | Practitioner | baseline |
| [SAFE-K8S-0503-008](markdown/controls/SAFE-K8S-0503-008.md) | D05 | 5.3 | Ingress WAF integration and rate limiting | Practitioner | baseline |
| [SAFE-K8S-0503-009](markdown/controls/SAFE-K8S-0503-009.md) | D05 | 5.3 | CoreDNS and upstream resolver hardening | Practitioner | baseline |
| [SAFE-K8S-0503-010](markdown/controls/SAFE-K8S-0503-010.md) | D05 | 5.3 | DNS resolution path enforcement and namespace-scoped service discovery | Practitioner | baseline |
| [SAFE-K8S-0503-011](markdown/controls/SAFE-K8S-0503-011.md) | D05 | 5.3 | External traffic policy mode selection and tradeoff governance | Practitioner | baseline |
| [SAFE-K8S-0503-012](markdown/controls/SAFE-K8S-0503-012.md) | D05 | 5.3 | Client source IP preservation for external services | Practitioner | baseline |
| [SAFE-K8S-0503-013](markdown/controls/SAFE-K8S-0503-013.md) | D05 | 5.3 | Ingress web application firewall integration and request filtering | Practitioner | baseline |
| [SAFE-K8S-0503-014](markdown/controls/SAFE-K8S-0503-014.md) | D05 | 5.3 | Ingress rate limiting and abuse throttling | Practitioner | baseline |
| [SAFE-K8S-0503-015](markdown/controls/SAFE-K8S-0503-015.md) | D05 | 5.3 | Approved DNS resolution path enforcement | Practitioner | baseline |
| [SAFE-K8S-0503-016](markdown/controls/SAFE-K8S-0503-016.md) | D05 | 5.3 | Namespace-scoped DNS service discovery restriction | Practitioner | baseline |
| [SAFE-K8S-0504-001](markdown/controls/SAFE-K8S-0504-001.md) | D05 | 5.4 | Zero trust networking principles for Kubernetes | Practitioner | baseline |
| [SAFE-K8S-0504-002](markdown/controls/SAFE-K8S-0504-002.md) | D05 | 5.4 | Service mesh mTLS and authorization policies | Practitioner | baseline |
| [SAFE-K8S-0504-003](markdown/controls/SAFE-K8S-0504-003.md) | D05 | 5.4 | SPIFFE/SPIRE workload identity management | Advanced | baseline |
| [SAFE-K8S-0504-004](markdown/controls/SAFE-K8S-0504-004.md) | D05 | 5.4 | L7 microsegmentation and API-aware policies | Practitioner | baseline |
| [SAFE-K8S-0504-005](markdown/controls/SAFE-K8S-0504-005.md) | D05 | 5.4 | Service mesh tuning for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0504-006](markdown/controls/SAFE-K8S-0504-006.md) | D05 | 5.4 | SPIFFE/SPIRE workload identity issuance and lifecycle management | Advanced | baseline |
| [SAFE-K8S-0504-007](markdown/controls/SAFE-K8S-0504-007.md) | D05 | 5.4 | SPIFFE trust domain scoping and cross-cluster federation governance | Advanced | baseline |
| [SAFE-K8S-0504-008](markdown/controls/SAFE-K8S-0504-008.md) | D05 | 5.4 | L7 service authorization policy enforcement | Practitioner | baseline |
| [SAFE-K8S-0504-009](markdown/controls/SAFE-K8S-0504-009.md) | D05 | 5.4 | API-aware request contract validation | Practitioner | baseline |
| [SAFE-K8S-0505-001](markdown/controls/SAFE-K8S-0505-001.md) | D05 | 5.5 | API server network access restriction | Practitioner | baseline |
| [SAFE-K8S-0505-002](markdown/controls/SAFE-K8S-0505-002.md) | D05 | 5.5 | LoadBalancer, NodePort, and ExternalIP restriction policies | Practitioner | baseline |
| [SAFE-K8S-0505-003](markdown/controls/SAFE-K8S-0505-003.md) | D05 | 5.5 | Internal service endpoint protection | Practitioner | baseline |
| [SAFE-K8S-0505-004](markdown/controls/SAFE-K8S-0505-004.md) | D05 | 5.5 | API server audit log analysis for network-based attack detection | Practitioner | baseline |
| [SAFE-K8S-0505-005](markdown/controls/SAFE-K8S-0505-005.md) | D05 | 5.5 | Identity-based internal service access control | Practitioner | baseline |
| [SAFE-K8S-0505-006](markdown/controls/SAFE-K8S-0505-006.md) | D05 | 5.5 | API server private endpoint and authorized network enforcement | Practitioner | baseline |
| [SAFE-K8S-0505-007](markdown/controls/SAFE-K8S-0505-007.md) | D05 | 5.5 | Administrative API server access path via bastion or VPN | Practitioner | baseline |
| [SAFE-K8S-0601-001](markdown/controls/SAFE-K8S-0601-001.md) | D06 | 6.1 | Base image selection and hardening | Practitioner | ai-specific |
| [SAFE-K8S-0601-002](markdown/controls/SAFE-K8S-0601-002.md) | D06 | 6.1 | Container image vulnerability scanning | Practitioner | ai-specific |
| [SAFE-K8S-0601-003](markdown/controls/SAFE-K8S-0601-003.md) | D06 | 6.1 | Registry access controls | Practitioner | baseline |
| [SAFE-K8S-0601-004](markdown/controls/SAFE-K8S-0601-004.md) | D06 | 6.1 | Image hardening practices | Practitioner | ai-specific |
| [SAFE-K8S-0601-005](markdown/controls/SAFE-K8S-0601-005.md) | D06 | 6.1 | Container image and artifact retention policy | Practitioner | baseline |
| [SAFE-K8S-0601-006](markdown/controls/SAFE-K8S-0601-006.md) | D06 | 6.1 | Approved minimal base images and multi-stage build hardening | Practitioner | ai-specific |
| [SAFE-K8S-0601-007](markdown/controls/SAFE-K8S-0601-007.md) | D06 | 6.1 | AI GPU and ML framework base image validation | Practitioner | ai-specific |
| [SAFE-K8S-0601-008](markdown/controls/SAFE-K8S-0601-008.md) | D06 | 6.1 | CI/CD build-time container image vulnerability scanning | Practitioner | ai-specific |
| [SAFE-K8S-0601-009](markdown/controls/SAFE-K8S-0601-009.md) | D06 | 6.1 | Registry and runtime container vulnerability monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0601-010](markdown/controls/SAFE-K8S-0601-010.md) | D06 | 6.1 | Artifact retention period and lifecycle enforcement | Practitioner | baseline |
| [SAFE-K8S-0601-011](markdown/controls/SAFE-K8S-0601-011.md) | D06 | 6.1 | Integrity metadata co-retention with software artifacts | Practitioner | baseline |
| [SAFE-K8S-0601-012](markdown/controls/SAFE-K8S-0601-012.md) | D06 | 6.1 | Container registry authentication, authorization, and network restriction | Practitioner | baseline |
| [SAFE-K8S-0601-013](markdown/controls/SAFE-K8S-0601-013.md) | D06 | 6.1 | Kubernetes image pull secret management and rotation | Practitioner | baseline |
| [SAFE-K8S-0601-014](markdown/controls/SAFE-K8S-0601-014.md) | D06 | 6.1 | Container image runtime hardening with non-root and read-only filesystem | Practitioner | ai-specific |
| [SAFE-K8S-0601-015](markdown/controls/SAFE-K8S-0601-015.md) | D06 | 6.1 | Inference image minimal composition with GPU runtime-only dependencies | Practitioner | ai-specific |
| [SAFE-K8S-0601-016](markdown/controls/SAFE-K8S-0601-016.md) | D06 | 6.1 | Approved minimal base image catalog enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0601-017](markdown/controls/SAFE-K8S-0601-017.md) | D06 | 6.1 | Multi-stage build and stripped runtime image minimization | Practitioner | ai-specific |
| [SAFE-K8S-0601-018](markdown/controls/SAFE-K8S-0601-018.md) | D06 | 6.1 | Registry push-time container image vulnerability rescanning | Practitioner | ai-specific |
| [SAFE-K8S-0601-019](markdown/controls/SAFE-K8S-0601-019.md) | D06 | 6.1 | Runtime container vulnerability exposure monitoring and exception governance | Practitioner | ai-specific |
| [SAFE-K8S-0601-020](markdown/controls/SAFE-K8S-0601-020.md) | D06 | 6.1 | Container registry authentication and role-based authorization | Practitioner | baseline |
| [SAFE-K8S-0601-021](markdown/controls/SAFE-K8S-0601-021.md) | D06 | 6.1 | Container registry trusted-source network restriction | Practitioner | baseline |
| [SAFE-K8S-0601-022](markdown/controls/SAFE-K8S-0601-022.md) | D06 | 6.1 | Kubernetes image pull secret distribution and external secret integration | Practitioner | baseline |
| [SAFE-K8S-0601-023](markdown/controls/SAFE-K8S-0601-023.md) | D06 | 6.1 | Image pull credential automatic rotation and expiry reduction | Practitioner | baseline |
| [SAFE-K8S-0602-001](markdown/controls/SAFE-K8S-0602-001.md) | D06 | 6.2 | Sigstore/cosign keyless signing and Rekor transparency logging | Practitioner | baseline |
| [SAFE-K8S-0602-002](markdown/controls/SAFE-K8S-0602-002.md) | D06 | 6.2 | Notary v2 (notation) trust policy and signature verification | Practitioner | baseline |
| [SAFE-K8S-0602-003](markdown/controls/SAFE-K8S-0602-003.md) | D06 | 6.2 | Admission enforcement of image signatures | Practitioner | baseline |
| [SAFE-K8S-0602-004](markdown/controls/SAFE-K8S-0602-004.md) | D06 | 6.2 | Notary v2 trust policy and signing identity governance | Practitioner | baseline |
| [SAFE-K8S-0602-005](markdown/controls/SAFE-K8S-0602-005.md) | D06 | 6.2 | Notary v2 OCI signature artifact registry integration | Practitioner | baseline |
| [SAFE-K8S-0602-006](markdown/controls/SAFE-K8S-0602-006.md) | D06 | 6.2 | Fail-closed admission enforcement of image signature verification | Practitioner | baseline |
| [SAFE-K8S-0602-007](markdown/controls/SAFE-K8S-0602-007.md) | D06 | 6.2 | Admission signature bypass and emergency break-glass governance | Practitioner | baseline |
| [SAFE-K8S-0603-001](markdown/controls/SAFE-K8S-0603-001.md) | D06 | 6.3 | Artifact attestation with in-toto and SLSA provenance | Advanced | baseline |
| [SAFE-K8S-0603-002](markdown/controls/SAFE-K8S-0603-002.md) | D06 | 6.3 | Build attestation taxonomy per NIST SP 800-204D | Advanced | baseline |
| [SAFE-K8S-0603-003](markdown/controls/SAFE-K8S-0603-003.md) | D06 | 6.3 | Attestation policy evaluation and lifecycle compliance | Advanced | baseline |
| [SAFE-K8S-0603-004](markdown/controls/SAFE-K8S-0603-004.md) | D06 | 6.3 | Cryptographic agility and post-quantum readiness | Advanced | ai-specific |
| [SAFE-K8S-0603-005](markdown/controls/SAFE-K8S-0603-005.md) | D06 | 6.3 | FIPS 140 cryptographic module validation | Practitioner | baseline |
| [SAFE-K8S-0603-006](markdown/controls/SAFE-K8S-0603-006.md) | D06 | 6.3 | TUF-based secure software update systems | Advanced | baseline |
| [SAFE-K8S-0603-007](markdown/controls/SAFE-K8S-0603-007.md) | D06 | 6.3 | Build environment and process attestations per NIST SP 800-204D | Advanced | baseline |
| [SAFE-K8S-0603-008](markdown/controls/SAFE-K8S-0603-008.md) | D06 | 6.3 | Build materials and artifact attestations per NIST SP 800-204D | Advanced | baseline |
| [SAFE-K8S-0603-009](markdown/controls/SAFE-K8S-0603-009.md) | D06 | 6.3 | In-toto and SLSA provenance attestation generation | Advanced | baseline |
| [SAFE-K8S-0603-010](markdown/controls/SAFE-K8S-0603-010.md) | D06 | 6.3 | SBOM attestation binding to image digests | Advanced | baseline |
| [SAFE-K8S-0603-011](markdown/controls/SAFE-K8S-0603-011.md) | D06 | 6.3 | Attestation policy definition, signing, and change governance | Advanced | baseline |
| [SAFE-K8S-0603-012](markdown/controls/SAFE-K8S-0603-012.md) | D06 | 6.3 | Lifecycle attestation verification and admission enforcement | Advanced | baseline |
| [SAFE-K8S-0603-013](markdown/controls/SAFE-K8S-0603-013.md) | D06 | 6.3 | Lifecycle attestation chain verification across build, promote, and deploy | Advanced | baseline |
| [SAFE-K8S-0603-014](markdown/controls/SAFE-K8S-0603-014.md) | D06 | 6.3 | Fail-closed admission enforcement for attestation requirements | Advanced | baseline |
| [SAFE-K8S-0604-001](markdown/controls/SAFE-K8S-0604-001.md) | D06 | 6.4 | SBOM generation for container and AI artifacts | Practitioner | ai-specific |
| [SAFE-K8S-0604-002](markdown/controls/SAFE-K8S-0604-002.md) | D06 | 6.4 | ML-BOM (ML Bill of Materials) generation | Practitioner | ai-specific |
| [SAFE-K8S-0604-003](markdown/controls/SAFE-K8S-0604-003.md) | D06 | 6.4 | SBOM storage and distribution as OCI artifacts | Practitioner | baseline |
| [SAFE-K8S-0604-004](markdown/controls/SAFE-K8S-0604-004.md) | D06 | 6.4 | VEX (Vulnerability Exploitability eXchange) publication | Practitioner | baseline |
| [SAFE-K8S-0604-005](markdown/controls/SAFE-K8S-0604-005.md) | D06 | 6.4 | Dependency tracking and SLSA build provenance | Practitioner | baseline |
| [SAFE-K8S-0604-006](markdown/controls/SAFE-K8S-0604-006.md) | D06 | 6.4 | Vulnerability prioritization for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0604-007](markdown/controls/SAFE-K8S-0604-007.md) | D06 | 6.4 | Third-party component security requirements documentation | Practitioner | baseline |
| [SAFE-K8S-0604-008](markdown/controls/SAFE-K8S-0604-008.md) | D06 | 6.4 | AI workload vulnerability exposure classification | Practitioner | ai-specific |
| [SAFE-K8S-0604-009](markdown/controls/SAFE-K8S-0604-009.md) | D06 | 6.4 | AI workload vulnerability prioritization and remediation SLAs | Practitioner | ai-specific |
| [SAFE-K8S-0604-010](markdown/controls/SAFE-K8S-0604-010.md) | D06 | 6.4 | Automated AI workload rebuild and redeployment patch pipelines | Practitioner | ai-specific |
| [SAFE-K8S-0604-011](markdown/controls/SAFE-K8S-0604-011.md) | D06 | 6.4 | SLSA provenance generation and target-level governance | Practitioner | baseline |
| [SAFE-K8S-0604-012](markdown/controls/SAFE-K8S-0604-012.md) | D06 | 6.4 | Hermetic build dependency control and source-to-artifact integrity | Practitioner | baseline |
| [SAFE-K8S-0604-013](markdown/controls/SAFE-K8S-0604-013.md) | D06 | 6.4 | Hermetic build execution and pinned dependency input control | Practitioner | baseline |
| [SAFE-K8S-0604-014](markdown/controls/SAFE-K8S-0604-014.md) | D06 | 6.4 | Source-to-artifact integrity linkage for built images | Practitioner | baseline |
| [SAFE-K8S-0605-001](markdown/controls/SAFE-K8S-0605-001.md) | D06 | 6.5 | OPA/Gatekeeper policies for Kubernetes and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0605-002](markdown/controls/SAFE-K8S-0605-002.md) | D06 | 6.5 | Kyverno admission policies | Practitioner | baseline |
| [SAFE-K8S-0605-003](markdown/controls/SAFE-K8S-0605-003.md) | D06 | 6.5 | Kubewarden WebAssembly-based admission policies | Practitioner | baseline |
| [SAFE-K8S-0605-004](markdown/controls/SAFE-K8S-0605-004.md) | D06 | 6.5 | Admission webhook security and availability | Practitioner | baseline |
| [SAFE-K8S-0605-005](markdown/controls/SAFE-K8S-0605-005.md) | D06 | 6.5 | CRD validation and webhook hardening for AI custom resources | Practitioner | ai-specific |
| [SAFE-K8S-0605-006](markdown/controls/SAFE-K8S-0605-006.md) | D06 | 6.5 | Pod Security Admission enforcement for AI workload namespaces | Practitioner | baseline |
| [SAFE-K8S-0605-007](markdown/controls/SAFE-K8S-0605-007.md) | D06 | 6.5 | Admission webhook fail-closed enforcement and timeout bounds | Practitioner | baseline |
| [SAFE-K8S-0605-008](markdown/controls/SAFE-K8S-0605-008.md) | D06 | 6.5 | Admission webhook TLS rotation and high-availability resilience | Practitioner | baseline |
| [SAFE-K8S-0605-009](markdown/controls/SAFE-K8S-0605-009.md) | D06 | 6.5 | AI custom resource validation and policy constraint enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0605-010](markdown/controls/SAFE-K8S-0605-010.md) | D06 | 6.5 | AI custom resource webhook abuse resistance and resource hardening | Practitioner | ai-specific |
| [SAFE-K8S-0606-001](markdown/controls/SAFE-K8S-0606-001.md) | D06 | 6.6 | CNCF lifecycle security and zero-trust CI/CD pipelines | Practitioner | baseline |
| [SAFE-K8S-0606-002](markdown/controls/SAFE-K8S-0606-002.md) | D06 | 6.6 | CI/CD build environment hardening | Practitioner | baseline |
| [SAFE-K8S-0606-003](markdown/controls/SAFE-K8S-0606-003.md) | D06 | 6.6 | CI pipeline security gates | Practitioner | baseline |
| [SAFE-K8S-0606-004](markdown/controls/SAFE-K8S-0606-004.md) | D06 | 6.6 | GitOps repository security | Practitioner | baseline |
| [SAFE-K8S-0606-005](markdown/controls/SAFE-K8S-0606-005.md) | D06 | 6.6 | Helm chart security and provenance | Practitioner | baseline |
| [SAFE-K8S-0606-006](markdown/controls/SAFE-K8S-0606-006.md) | D06 | 6.6 | Kubernetes manifest signing and verification | Advanced | baseline |
| [SAFE-K8S-0606-007](markdown/controls/SAFE-K8S-0606-007.md) | D06 | 6.6 | CI/CD build activity monitoring | Practitioner | baseline |
| [SAFE-K8S-0606-008](markdown/controls/SAFE-K8S-0606-008.md) | D06 | 6.6 | GitOps reconciliation integrity and drift detection | Practitioner | baseline |
| [SAFE-K8S-0606-009](markdown/controls/SAFE-K8S-0606-009.md) | D06 | 6.6 | SSDF v1.1 alignment for secure development practices | Practitioner | baseline |
| [SAFE-K8S-0606-010](markdown/controls/SAFE-K8S-0606-010.md) | D06 | 6.6 | Infrastructure as Code security and policy-as-code integrity | Practitioner | baseline |
| [SAFE-K8S-0606-011](markdown/controls/SAFE-K8S-0606-011.md) | D06 | 6.6 | CI build-time security gate enforcement | Practitioner | baseline |
| [SAFE-K8S-0606-012](markdown/controls/SAFE-K8S-0606-012.md) | D06 | 6.6 | Artifact freshness and SCM security posture enforcement | Practitioner | baseline |
| [SAFE-K8S-0606-013](markdown/controls/SAFE-K8S-0606-013.md) | D06 | 6.6 | GitOps repository access, commit signing, and branch protection | Practitioner | baseline |
| [SAFE-K8S-0606-014](markdown/controls/SAFE-K8S-0606-014.md) | D06 | 6.6 | GitOps release metadata preservation and deployment traceability | Practitioner | baseline |
| [SAFE-K8S-0606-015](markdown/controls/SAFE-K8S-0606-015.md) | D06 | 6.6 | GitOps reconciliation monitoring, drift detection, and automated resync | Practitioner | baseline |
| [SAFE-K8S-0606-016](markdown/controls/SAFE-K8S-0606-016.md) | D06 | 6.6 | Git-only production deployment path and direct-change prohibition | Practitioner | baseline |
| [SAFE-K8S-0606-017](markdown/controls/SAFE-K8S-0606-017.md) | D06 | 6.6 | CNCF lifecycle phase security coverage | Practitioner | baseline |
| [SAFE-K8S-0606-018](markdown/controls/SAFE-K8S-0606-018.md) | D06 | 6.6 | Zero-trust CI/CD handoff verification and independent evidence generation | Practitioner | baseline |
| [SAFE-K8S-0606-019](markdown/controls/SAFE-K8S-0606-019.md) | D06 | 6.6 | Helm chart provenance and signature verification | Practitioner | baseline |
| [SAFE-K8S-0606-020](markdown/controls/SAFE-K8S-0606-020.md) | D06 | 6.6 | Helm values override restriction and dependency integrity governance | Practitioner | baseline |
| [SAFE-K8S-0606-021](markdown/controls/SAFE-K8S-0606-021.md) | D06 | 6.6 | Kubernetes manifest cryptographic signing before deployment | Advanced | baseline |
| [SAFE-K8S-0606-022](markdown/controls/SAFE-K8S-0606-022.md) | D06 | 6.6 | Admission-time verification of Kubernetes manifest signatures | Advanced | baseline |
| [SAFE-K8S-0606-023](markdown/controls/SAFE-K8S-0606-023.md) | D06 | 6.6 | IaC security scanning gate enforcement for deployment platforms | Practitioner | baseline |
| [SAFE-K8S-0606-024](markdown/controls/SAFE-K8S-0606-024.md) | D06 | 6.6 | Policy-as-code and runtime configuration integrity governance | Practitioner | baseline |
| [SAFE-K8S-0606-025](markdown/controls/SAFE-K8S-0606-025.md) | D06 | 6.6 | Artifact freshness limit enforcement for CI/CD promotion | Practitioner | baseline |
| [SAFE-K8S-0606-026](markdown/controls/SAFE-K8S-0606-026.md) | D06 | 6.6 | Automated SCM security posture assessment before promotion reliance | Practitioner | baseline |
| [SAFE-K8S-0606-027](markdown/controls/SAFE-K8S-0606-027.md) | D06 | 6.6 | GitOps repository access restriction and least-privilege deploy credentials | Practitioner | baseline |
| [SAFE-K8S-0606-028](markdown/controls/SAFE-K8S-0606-028.md) | D06 | 6.6 | GitOps commit signing and protected deployment branch governance | Practitioner | baseline |
| [SAFE-K8S-0606-029](markdown/controls/SAFE-K8S-0606-029.md) | D06 | 6.6 | GitOps deployed package and version metadata retention | Practitioner | baseline |
| [SAFE-K8S-0606-030](markdown/controls/SAFE-K8S-0606-030.md) | D06 | 6.6 | GitOps configuration revision and deployment history traceability | Practitioner | baseline |
| [SAFE-K8S-0606-031](markdown/controls/SAFE-K8S-0606-031.md) | D06 | 6.6 | GitOps reconciliation health and integrity monitoring | Practitioner | baseline |
| [SAFE-K8S-0606-032](markdown/controls/SAFE-K8S-0606-032.md) | D06 | 6.6 | GitOps drift detection and automated resync or notification | Practitioner | baseline |
| [SAFE-K8S-0606-033](markdown/controls/SAFE-K8S-0606-033.md) | D06 | 6.6 | Git-only production deployment path enforcement | Practitioner | baseline |
| [SAFE-K8S-0606-034](markdown/controls/SAFE-K8S-0606-034.md) | D06 | 6.6 | Emergency direct-access audit logging and justification governance | Practitioner | baseline |
| [SAFE-K8S-0701-001](markdown/controls/SAFE-K8S-0701-001.md) | D07 | 7.1 | PersistentVolume and PersistentVolumeClaim access mode enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0701-002](markdown/controls/SAFE-K8S-0701-002.md) | D07 | 7.1 | CSI driver security and privilege restriction | Practitioner | baseline |
| [SAFE-K8S-0701-003](markdown/controls/SAFE-K8S-0701-003.md) | D07 | 7.1 | Encryption at rest for persistent volumes | Foundational | baseline |
| [SAFE-K8S-0701-004](markdown/controls/SAFE-K8S-0701-004.md) | D07 | 7.1 | PV reclaim policy enforcement for AI data volumes | Practitioner | ai-specific |
| [SAFE-K8S-0701-005](markdown/controls/SAFE-K8S-0701-005.md) | D07 | 7.1 | Data versioning and immutability for training data and model artifacts | Advanced | ai-specific |
| [SAFE-K8S-0701-006](markdown/controls/SAFE-K8S-0701-006.md) | D07 | 7.1 | Dual authorization for retained AI data volume destruction | Advanced | ai-specific |
| [SAFE-K8S-0701-007](markdown/controls/SAFE-K8S-0701-007.md) | D07 | 7.1 | High-performance AI storage backend hardening | Advanced | ai-specific |
| [SAFE-K8S-0701-008](markdown/controls/SAFE-K8S-0701-008.md) | D07 | 7.1 | Training data and model artifact version tracking for reproducibility | Advanced | ai-specific |
| [SAFE-K8S-0701-009](markdown/controls/SAFE-K8S-0701-009.md) | D07 | 7.1 | Immutable storage protection for training data and model artifacts | Advanced | ai-specific |
| [SAFE-K8S-0702-001](markdown/controls/SAFE-K8S-0702-001.md) | D07 | 7.2 | Namespace isolation model for multi-tenant AI clusters | Practitioner | baseline |
| [SAFE-K8S-0702-002](markdown/controls/SAFE-K8S-0702-002.md) | D07 | 7.2 | Resource quotas per namespace for GPU and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0702-003](markdown/controls/SAFE-K8S-0702-003.md) | D07 | 7.2 | LimitRange enforcement for containers and pods | Foundational | baseline |
| [SAFE-K8S-0702-004](markdown/controls/SAFE-K8S-0702-004.md) | D07 | 7.2 | Virtual cluster isolation for multi-tenant environments | Advanced | baseline |
| [SAFE-K8S-0702-005](markdown/controls/SAFE-K8S-0702-005.md) | D07 | 7.2 | Label and annotation schema definition for AI workload classification | Practitioner | ai-specific |
| [SAFE-K8S-0702-006](markdown/controls/SAFE-K8S-0702-006.md) | D07 | 7.2 | Data type classification labels for pipeline data flows | Practitioner | ai-specific |
| [SAFE-K8S-0702-007](markdown/controls/SAFE-K8S-0702-007.md) | D07 | 7.2 | Classification attribute preservation across model lifecycle stages | Practitioner | ai-specific |
| [SAFE-K8S-0702-008](markdown/controls/SAFE-K8S-0702-008.md) | D07 | 7.2 | Tenant boundary enforcement through admission control, network policy, and RBAC | Practitioner | baseline |
| [SAFE-K8S-0702-009](markdown/controls/SAFE-K8S-0702-009.md) | D07 | 7.2 | Admission control enforcement of workload classification label requirements | Practitioner | ai-specific |
| [SAFE-K8S-0702-010](markdown/controls/SAFE-K8S-0702-010.md) | D07 | 7.2 | Virtual cluster deployment for high-isolation multi-tenant Kubernetes environments | Advanced | baseline |
| [SAFE-K8S-0702-011](markdown/controls/SAFE-K8S-0702-011.md) | D07 | 7.2 | Isolation guarantee validation and residual risk documentation for virtual clusters | Advanced | baseline |
| [SAFE-K8S-0702-012](markdown/controls/SAFE-K8S-0702-012.md) | D07 | 7.2 | Tenant namespace RBAC and admission boundary enforcement | Practitioner | baseline |
| [SAFE-K8S-0702-013](markdown/controls/SAFE-K8S-0702-013.md) | D07 | 7.2 | Tenant default-deny inter-namespace network isolation | Practitioner | baseline |
| [SAFE-K8S-0702-014](markdown/controls/SAFE-K8S-0702-014.md) | D07 | 7.2 | Pipeline data classification taxonomy and label propagation | Practitioner | ai-specific |
| [SAFE-K8S-0702-015](markdown/controls/SAFE-K8S-0702-015.md) | D07 | 7.2 | Classification-driven admission, storage, and network policy enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0702-016](markdown/controls/SAFE-K8S-0702-016.md) | D07 | 7.2 | Classification metadata preservation across model lifecycle stages | Practitioner | ai-specific |
| [SAFE-K8S-0702-017](markdown/controls/SAFE-K8S-0702-017.md) | D07 | 7.2 | Promotion-time reclassification and production gate enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0702-018](markdown/controls/SAFE-K8S-0702-018.md) | D07 | 7.2 | Namespace tenant boundary model and isolation limitation documentation | Practitioner | baseline |
| [SAFE-K8S-0702-019](markdown/controls/SAFE-K8S-0702-019.md) | D07 | 7.2 | Supplementary namespace isolation control enforcement for multi-tenant AI clusters | Practitioner | baseline |
| [SAFE-K8S-0702-020](markdown/controls/SAFE-K8S-0702-020.md) | D07 | 7.2 | Namespace ResourceQuota enforcement for GPU and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0702-021](markdown/controls/SAFE-K8S-0702-021.md) | D07 | 7.2 | Namespace quota utilization monitoring and exhaustion alerting for GPU and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0702-022](markdown/controls/SAFE-K8S-0702-022.md) | D07 | 7.2 | Virtual cluster isolation guarantee and residual risk documentation | Advanced | baseline |
| [SAFE-K8S-0702-023](markdown/controls/SAFE-K8S-0702-023.md) | D07 | 7.2 | Virtual cluster tenant isolation validation and host-cluster access review | Advanced | baseline |
| [SAFE-K8S-0702-024](markdown/controls/SAFE-K8S-0702-024.md) | D07 | 7.2 | Tenant namespace-scoped RBAC boundary enforcement | Practitioner | baseline |
| [SAFE-K8S-0702-025](markdown/controls/SAFE-K8S-0702-025.md) | D07 | 7.2 | Tenant admission boundary enforcement for cross-tenant resource isolation | Practitioner | baseline |
| [SAFE-K8S-0702-026](markdown/controls/SAFE-K8S-0702-026.md) | D07 | 7.2 | Pipeline data classification taxonomy definition | Practitioner | ai-specific |
| [SAFE-K8S-0702-027](markdown/controls/SAFE-K8S-0702-027.md) | D07 | 7.2 | Pipeline classification label application, propagation, and coverage verification | Practitioner | ai-specific |
| [SAFE-K8S-0702-028](markdown/controls/SAFE-K8S-0702-028.md) | D07 | 7.2 | Classification-driven admission policy enforcement for pipeline resources | Practitioner | ai-specific |
| [SAFE-K8S-0702-029](markdown/controls/SAFE-K8S-0702-029.md) | D07 | 7.2 | Classification-driven storage and network restriction enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0702-030](markdown/controls/SAFE-K8S-0702-030.md) | D07 | 7.2 | Promotion-time automatic classification uplift and reclassification execution | Practitioner | ai-specific |
| [SAFE-K8S-0702-031](markdown/controls/SAFE-K8S-0702-031.md) | D07 | 7.2 | Production promotion gate enforcement on validated classification metadata | Practitioner | ai-specific |
| [SAFE-K8S-0703-001](markdown/controls/SAFE-K8S-0703-001.md) | D07 | 7.3 | Priority classes and preemption policies for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0703-002](markdown/controls/SAFE-K8S-0703-002.md) | D07 | 7.3 | Pod Disruption Budgets for workload availability | Foundational | baseline |
| [SAFE-K8S-0703-003](markdown/controls/SAFE-K8S-0703-003.md) | D07 | 7.3 | GPU cost attribution and chargeback mechanisms | Practitioner | ai-specific |
| [SAFE-K8S-0703-004](markdown/controls/SAFE-K8S-0703-004.md) | D07 | 7.3 | GPU resource abuse detection and prevention | Practitioner | ai-specific |
| [SAFE-K8S-0703-005](markdown/controls/SAFE-K8S-0703-005.md) | D07 | 7.3 | AI workload resource exhaustion guardrails | Practitioner | ai-specific |
| [SAFE-K8S-0703-006](markdown/controls/SAFE-K8S-0703-006.md) | D07 | 7.3 | Node affinity, taints, and topology-aware scheduling for AI workload isolation | Practitioner | ai-specific |
| [SAFE-K8S-0703-007](markdown/controls/SAFE-K8S-0703-007.md) | D07 | 7.3 | Fair-share GPU queue management for multi-tenant clusters | Practitioner | ai-specific |
| [SAFE-K8S-0703-008](markdown/controls/SAFE-K8S-0703-008.md) | D07 | 7.3 | Idle GPU detection and resource reclamation | Practitioner | ai-specific |
| [SAFE-K8S-0703-009](markdown/controls/SAFE-K8S-0703-009.md) | D07 | 7.3 | GPU spending limits and budget enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0703-010](markdown/controls/SAFE-K8S-0703-010.md) | D07 | 7.3 | Host-level resource isolation for AI workload nodes | Practitioner | ai-specific |
| [SAFE-K8S-0703-011](markdown/controls/SAFE-K8S-0703-011.md) | D07 | 7.3 | EDoS prevention and chaos engineering for AI resources | Advanced | ai-specific |
| [SAFE-K8S-0703-012](markdown/controls/SAFE-K8S-0703-012.md) | D07 | 7.3 | Node affinity rules, taints, and tolerations for AI workload isolation | Practitioner | ai-specific |
| [SAFE-K8S-0703-013](markdown/controls/SAFE-K8S-0703-013.md) | D07 | 7.3 | Topology-aware scheduling for GPU locality with blast-radius containment | Practitioner | ai-specific |
| [SAFE-K8S-0703-014](markdown/controls/SAFE-K8S-0703-014.md) | D07 | 7.3 | EDoS spending guardrails and autoscaling limits for AI resources | Advanced | ai-specific |
| [SAFE-K8S-0703-015](markdown/controls/SAFE-K8S-0703-015.md) | D07 | 7.3 | Chaos engineering validation for AI resource governance controls | Advanced | ai-specific |
| [SAFE-K8S-0703-016](markdown/controls/SAFE-K8S-0703-016.md) | D07 | 7.3 | AI workload PriorityClass hierarchy and preemption protection | Practitioner | ai-specific |
| [SAFE-K8S-0703-017](markdown/controls/SAFE-K8S-0703-017.md) | D07 | 7.3 | PriorityClass assignment restriction and admission enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0703-018](markdown/controls/SAFE-K8S-0703-018.md) | D07 | 7.3 | GPU cost attribution metering and billing correlation | Practitioner | ai-specific |
| [SAFE-K8S-0703-019](markdown/controls/SAFE-K8S-0703-019.md) | D07 | 7.3 | GPU chargeback and showback reporting accountability | Practitioner | ai-specific |
| [SAFE-K8S-0703-020](markdown/controls/SAFE-K8S-0703-020.md) | D07 | 7.3 | GPU workload abuse detection and response | Practitioner | ai-specific |
| [SAFE-K8S-0703-021](markdown/controls/SAFE-K8S-0703-021.md) | D07 | 7.3 | GPU admission enforcement against unauthorized access and quota bypass | Practitioner | ai-specific |
| [SAFE-K8S-0703-022](markdown/controls/SAFE-K8S-0703-022.md) | D07 | 7.3 | GPU abuse pattern monitoring and detection for Kubernetes AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0703-023](markdown/controls/SAFE-K8S-0703-023.md) | D07 | 7.3 | Investigation and termination of confirmed unauthorized GPU workloads | Practitioner | ai-specific |
| [SAFE-K8S-0704-001](markdown/controls/SAFE-K8S-0704-001.md) | D07 | 7.4 | Cloud IAM to Kubernetes RBAC mapping | Practitioner | baseline |
| [SAFE-K8S-0704-002](markdown/controls/SAFE-K8S-0704-002.md) | D07 | 7.4 | VPC and security group integration with Kubernetes network policies | Practitioner | baseline |
| [SAFE-K8S-0704-003](markdown/controls/SAFE-K8S-0704-003.md) | D07 | 7.4 | Cloud audit log correlation with Kubernetes audit events | Practitioner | baseline |
| [SAFE-K8S-0704-004](markdown/controls/SAFE-K8S-0704-004.md) | D07 | 7.4 | IMDSv2 enforcement on Kubernetes nodes | Foundational | baseline |
| [SAFE-K8S-0704-005](markdown/controls/SAFE-K8S-0704-005.md) | D07 | 7.4 | Restricted use policies for non-organizationally owned systems and external AI services | Practitioner | ai-specific |
| [SAFE-K8S-0704-006](markdown/controls/SAFE-K8S-0704-006.md) | D07 | 7.4 | Cloud provider contingency plans for managed Kubernetes services | Practitioner | ai-specific |
| [SAFE-K8S-0704-007](markdown/controls/SAFE-K8S-0704-007.md) | D07 | 7.4 | Unified cloud and Kubernetes audit log ingestion | Practitioner | baseline |
| [SAFE-K8S-0704-008](markdown/controls/SAFE-K8S-0704-008.md) | D07 | 7.4 | Cloud-to-Kubernetes event correlation for incident investigation | Practitioner | baseline |
| [SAFE-K8S-0704-009](markdown/controls/SAFE-K8S-0704-009.md) | D07 | 7.4 | Cloud IAM to Kubernetes RBAC entitlement mapping governance | Practitioner | baseline |
| [SAFE-K8S-0704-010](markdown/controls/SAFE-K8S-0704-010.md) | D07 | 7.4 | Privileged cloud-to-cluster access boundary enforcement and break-glass control | Practitioner | baseline |
| [SAFE-K8S-0704-011](markdown/controls/SAFE-K8S-0704-011.md) | D07 | 7.4 | Network-level blocking of cloud metadata endpoint access for pods | Foundational | baseline |
| [SAFE-K8S-0704-012](markdown/controls/SAFE-K8S-0704-012.md) | D07 | 7.4 | Pod identity mechanisms replacing node-level instance profiles | Foundational | baseline |
| [SAFE-K8S-0704-013](markdown/controls/SAFE-K8S-0704-013.md) | D07 | 7.4 | Unified cloud and Kubernetes audit source onboarding | Practitioner | baseline |
| [SAFE-K8S-0704-014](markdown/controls/SAFE-K8S-0704-014.md) | D07 | 7.4 | Managed Kubernetes audit log retention enforcement | Practitioner | baseline |
| [SAFE-K8S-0704-015](markdown/controls/SAFE-K8S-0704-015.md) | D07 | 7.4 | Cloud IAM to Kubernetes RBAC entitlement mapping definition | Practitioner | baseline |
| [SAFE-K8S-0704-016](markdown/controls/SAFE-K8S-0704-016.md) | D07 | 7.4 | Cloud IAM to Kubernetes RBAC mapping review and drift remediation | Practitioner | baseline |
| [SAFE-K8S-0704-017](markdown/controls/SAFE-K8S-0704-017.md) | D07 | 7.4 | Least-privilege cloud-to-cluster privileged access boundary enforcement | Practitioner | baseline |
| [SAFE-K8S-0704-018](markdown/controls/SAFE-K8S-0704-018.md) | D07 | 7.4 | Break-glass cloud identity governance for Kubernetes administration | Practitioner | baseline |
| [SAFE-K8S-0704-019](markdown/controls/SAFE-K8S-0704-019.md) | D07 | 7.4 | Per-workload cloud identity binding for managed Kubernetes workloads | Foundational | baseline |
| [SAFE-K8S-0704-020](markdown/controls/SAFE-K8S-0704-020.md) | D07 | 7.4 | Node-level cloud identity restriction for managed Kubernetes workloads | Foundational | baseline |
| [SAFE-K8S-0801-001](markdown/controls/SAFE-K8S-0801-001.md) | D08 | 8.1 | GPU device plugin security configuration and hardening | Practitioner | ai-specific |
| [SAFE-K8S-0801-002](markdown/controls/SAFE-K8S-0801-002.md) | D08 | 8.1 | MIG partitioning for hardware-enforced GPU isolation | Advanced | ai-specific |
| [SAFE-K8S-0801-003](markdown/controls/SAFE-K8S-0801-003.md) | D08 | 8.1 | MPS and time-slicing isolation and memory safety controls | Advanced | ai-specific |
| [SAFE-K8S-0801-004](markdown/controls/SAFE-K8S-0801-004.md) | D08 | 8.1 | vGPU virtualization security controls | Practitioner | ai-specific |
| [SAFE-K8S-0801-005](markdown/controls/SAFE-K8S-0801-005.md) | D08 | 8.1 | GPU topology metadata protection and admission control | Practitioner | ai-specific |
| [SAFE-K8S-0801-006](markdown/controls/SAFE-K8S-0801-006.md) | D08 | 8.1 | GPU memory clearing between workload transitions | Advanced | ai-specific |
| [SAFE-K8S-0801-007](markdown/controls/SAFE-K8S-0801-007.md) | D08 | 8.1 | MPS and time-slicing residual-risk acceptance and workload eligibility controls | Advanced | ai-specific |
| [SAFE-K8S-0801-008](markdown/controls/SAFE-K8S-0801-008.md) | D08 | 8.1 | MPS and time-slicing memory isolation verification and side-channel assessment | Advanced | ai-specific |
| [SAFE-K8S-0801-009](markdown/controls/SAFE-K8S-0801-009.md) | D08 | 8.1 | GPU topology metadata protection and node label visibility restriction | Practitioner | ai-specific |
| [SAFE-K8S-0801-010](markdown/controls/SAFE-K8S-0801-010.md) | D08 | 8.1 | Admission validation of authorized GPU resource requests | Practitioner | ai-specific |
| [SAFE-K8S-0801-011](markdown/controls/SAFE-K8S-0801-011.md) | D08 | 8.1 | MPS and time-slicing residual-risk acceptance and compensating control approval | Advanced | ai-specific |
| [SAFE-K8S-0801-012](markdown/controls/SAFE-K8S-0801-012.md) | D08 | 8.1 | MPS and time-slicing workload eligibility and same-trust co-location enforcement | Advanced | ai-specific |
| [SAFE-K8S-0801-013](markdown/controls/SAFE-K8S-0801-013.md) | D08 | 8.1 | MPS and time-slicing memory remnant prevention verification | Advanced | ai-specific |
| [SAFE-K8S-0801-014](markdown/controls/SAFE-K8S-0801-014.md) | D08 | 8.1 | MPS and time-slicing side-channel risk assessment | Advanced | ai-specific |
| [SAFE-K8S-0802-001](markdown/controls/SAFE-K8S-0802-001.md) | D08 | 8.2 | GPU driver lifecycle and vulnerability management | Practitioner | ai-specific |
| [SAFE-K8S-0802-002](markdown/controls/SAFE-K8S-0802-002.md) | D08 | 8.2 | CUDA library and container toolkit security | Advanced | ai-specific |
| [SAFE-K8S-0802-003](markdown/controls/SAFE-K8S-0802-003.md) | D08 | 8.2 | Device plugin socket and kubelet communication security | Practitioner | ai-specific |
| [SAFE-K8S-0802-004](markdown/controls/SAFE-K8S-0802-004.md) | D08 | 8.2 | GPU firmware integrity monitoring | Advanced | ai-specific |
| [SAFE-K8S-0802-005](markdown/controls/SAFE-K8S-0802-005.md) | D08 | 8.2 | GPU kernel module and driver binary integrity enforcement | Advanced | ai-specific |
| [SAFE-K8S-0802-006](markdown/controls/SAFE-K8S-0802-006.md) | D08 | 8.2 | Device plugin socket directory access restriction and unauthorized socket access monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0802-007](markdown/controls/SAFE-K8S-0802-007.md) | D08 | 8.2 | Device plugin registration authentication monitoring and rogue plugin detection | Practitioner | ai-specific |
| [SAFE-K8S-0802-008](markdown/controls/SAFE-K8S-0802-008.md) | D08 | 8.2 | GPU kernel module signing and Secure Boot enforcement | Advanced | ai-specific |
| [SAFE-K8S-0802-009](markdown/controls/SAFE-K8S-0802-009.md) | D08 | 8.2 | GPU driver binary path file integrity monitoring | Advanced | ai-specific |
| [SAFE-K8S-0803-001](markdown/controls/SAFE-K8S-0803-001.md) | D08 | 8.3 | NVLink and NVSwitch traffic isolation for multi-GPU training | Advanced | ai-specific |
| [SAFE-K8S-0803-002](markdown/controls/SAFE-K8S-0803-002.md) | D08 | 8.3 | InfiniBand and RoCE fabric security controls | Advanced | ai-specific |
| [SAFE-K8S-0803-003](markdown/controls/SAFE-K8S-0803-003.md) | D08 | 8.3 | RDMA memory region and queue pair isolation | Advanced | ai-specific |
| [SAFE-K8S-0803-004](markdown/controls/SAFE-K8S-0803-004.md) | D08 | 8.3 | DPU and SmartNIC firmware integrity and trust boundaries | Advanced | ai-specific |
| [SAFE-K8S-0803-005](markdown/controls/SAFE-K8S-0803-005.md) | D08 | 8.3 | DPU and SmartNIC firmware cryptographic verification and Secure Boot integrity | Advanced | ai-specific |
| [SAFE-K8S-0803-006](markdown/controls/SAFE-K8S-0803-006.md) | D08 | 8.3 | DPU and SmartNIC host trust boundary definition and policy engine administrative restriction | Advanced | ai-specific |
| [SAFE-K8S-0804-001](markdown/controls/SAFE-K8S-0804-001.md) | D08 | 8.4 | TEE-based model and data protection for AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0804-002](markdown/controls/SAFE-K8S-0804-002.md) | D08 | 8.4 | Remote attestation for TEE integrity verification | Advanced | ai-specific |
| [SAFE-K8S-0804-003](markdown/controls/SAFE-K8S-0804-003.md) | D08 | 8.4 | Key management and sealed storage for confidential AI enclaves | Advanced | ai-specific |
| [SAFE-K8S-0804-004](markdown/controls/SAFE-K8S-0804-004.md) | D08 | 8.4 | Confidential AI workload operational constraints and risk assessment | Advanced | ai-specific |
| [SAFE-K8S-0804-005](markdown/controls/SAFE-K8S-0804-005.md) | D08 | 8.4 | Attestation-conditioned enclave key release | Advanced | ai-specific |
| [SAFE-K8S-0804-006](markdown/controls/SAFE-K8S-0804-006.md) | D08 | 8.4 | Sealed storage binding of encrypted AI artifacts to enclave measurements | Advanced | ai-specific |
| [SAFE-K8S-0805-001](markdown/controls/SAFE-K8S-0805-001.md) | D08 | 8.5 | GPU telemetry collection and anomaly detection | Practitioner | ai-specific |
| [SAFE-K8S-0805-002](markdown/controls/SAFE-K8S-0805-002.md) | D08 | 8.5 | GPU allocation audit trail and workload identity tracking | Practitioner | ai-specific |
| [SAFE-K8S-0805-003](markdown/controls/SAFE-K8S-0805-003.md) | D08 | 8.5 | GPU-based attack detection for cryptomining and memory scraping | Advanced | ai-specific |
| [SAFE-K8S-0805-004](markdown/controls/SAFE-K8S-0805-004.md) | D08 | 8.5 | GPU side-channel attack awareness and mitigation | Advanced | ai-specific |
| [SAFE-K8S-0901-001](markdown/controls/SAFE-K8S-0901-001.md) | D09 | 9.1 | Multi-node training worker authentication and encrypted communication | Practitioner | ai-specific |
| [SAFE-K8S-0901-002](markdown/controls/SAFE-K8S-0901-002.md) | D09 | 9.1 | Parameter server and all-reduce security | Advanced | ai-specific |
| [SAFE-K8S-0901-003](markdown/controls/SAFE-K8S-0901-003.md) | D09 | 9.1 | Checkpoint security | Practitioner | ai-specific |
| [SAFE-K8S-0901-004](markdown/controls/SAFE-K8S-0901-004.md) | D09 | 9.1 | Training fault tolerance and security | Practitioner | ai-specific |
| [SAFE-K8S-0901-005](markdown/controls/SAFE-K8S-0901-005.md) | D09 | 9.1 | Federated learning security on Kubernetes | Advanced | ai-specific |
| [SAFE-K8S-0901-006](markdown/controls/SAFE-K8S-0901-006.md) | D09 | 9.1 | Gang scheduling security (Volcano, Kueue) | Practitioner | ai-specific |
| [SAFE-K8S-0901-007](markdown/controls/SAFE-K8S-0901-007.md) | D09 | 9.1 | AI operator privilege management | Practitioner | ai-specific |
| [SAFE-K8S-0901-008](markdown/controls/SAFE-K8S-0901-008.md) | D09 | 9.1 | Training job network isolation | Practitioner | ai-specific |
| [SAFE-K8S-0901-009](markdown/controls/SAFE-K8S-0901-009.md) | D09 | 9.1 | Multi-node training worker mutual authentication | Practitioner | ai-specific |
| [SAFE-K8S-0901-010](markdown/controls/SAFE-K8S-0901-010.md) | D09 | 9.1 | Encrypted inter-worker gradient transport | Practitioner | ai-specific |
| [SAFE-K8S-0902-001](markdown/controls/SAFE-K8S-0902-001.md) | D09 | 9.2 | Inference server hardening | Practitioner | ai-specific |
| [SAFE-K8S-0902-002](markdown/controls/SAFE-K8S-0902-002.md) | D09 | 9.2 | Model loading integrity verification | Practitioner | ai-specific |
| [SAFE-K8S-0902-003](markdown/controls/SAFE-K8S-0902-003.md) | D09 | 9.2 | Inference request validation and input sanitization | Practitioner | ai-specific |
| [SAFE-K8S-0902-004](markdown/controls/SAFE-K8S-0902-004.md) | D09 | 9.2 | Multi-model serving isolation and encryption | Practitioner | ai-specific |
| [SAFE-K8S-0902-005](markdown/controls/SAFE-K8S-0902-005.md) | D09 | 9.2 | Multi-cluster inference routing and failover security | Practitioner | ai-specific |
| [SAFE-K8S-0902-006](markdown/controls/SAFE-K8S-0902-006.md) | D09 | 9.2 | LLM serving configuration security | Practitioner | ai-specific |
| [SAFE-K8S-0902-007](markdown/controls/SAFE-K8S-0902-007.md) | D09 | 9.2 | Infrastructure-layer prompt injection defense and token output filtering | Practitioner | ai-specific |
| [SAFE-K8S-0902-008](markdown/controls/SAFE-K8S-0902-008.md) | D09 | 9.2 | Inference endpoint authentication and authorization | Practitioner | ai-specific |
| [SAFE-K8S-0902-009](markdown/controls/SAFE-K8S-0902-009.md) | D09 | 9.2 | Inference response filtering and output controls | Practitioner | ai-specific |
| [SAFE-K8S-0902-010](markdown/controls/SAFE-K8S-0902-010.md) | D09 | 9.2 | Infrastructure-layer prompt injection classification and instruction boundary enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0902-011](markdown/controls/SAFE-K8S-0902-011.md) | D09 | 9.2 | Streaming token-level output leakage and policy-violation filtering | Practitioner | ai-specific |
| [SAFE-K8S-0903-001](markdown/controls/SAFE-K8S-0903-001.md) | D09 | 9.3 | Adversarial example defenses at the serving layer | Practitioner | ai-specific |
| [SAFE-K8S-0903-002](markdown/controls/SAFE-K8S-0903-002.md) | D09 | 9.3 | Autoscaling safety and queue security | Practitioner | ai-specific |
| [SAFE-K8S-0903-003](markdown/controls/SAFE-K8S-0903-003.md) | D09 | 9.3 | Inference-time resource controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-004](markdown/controls/SAFE-K8S-0903-004.md) | D09 | 9.3 | LLM context window and token resource controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-005](markdown/controls/SAFE-K8S-0903-005.md) | D09 | 9.3 | GPU inference autoscaling safety bounds and budget guardrails | Practitioner | ai-specific |
| [SAFE-K8S-0903-006](markdown/controls/SAFE-K8S-0903-006.md) | D09 | 9.3 | Inference request queue priority, timeout, and depth controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-007](markdown/controls/SAFE-K8S-0903-007.md) | D09 | 9.3 | GPU inference autoscaling replica bounds and stabilization enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0903-008](markdown/controls/SAFE-K8S-0903-008.md) | D09 | 9.3 | Budget-aware inference autoscaling suppression and degraded-service fallback | Practitioner | ai-specific |
| [SAFE-K8S-0904-001](markdown/controls/SAFE-K8S-0904-001.md) | D09 | 9.4 | Pipeline orchestrator hardening | Practitioner | ai-specific |
| [SAFE-K8S-0904-002](markdown/controls/SAFE-K8S-0904-002.md) | D09 | 9.4 | Pipeline artifact encryption and access controls | Practitioner | ai-specific |
| [SAFE-K8S-0904-003](markdown/controls/SAFE-K8S-0904-003.md) | D09 | 9.4 | Notebook and experimentation environment security | Practitioner | ai-specific |
| [SAFE-K8S-0904-004](markdown/controls/SAFE-K8S-0904-004.md) | D09 | 9.4 | Experiment tracking security and pipeline integrity | Practitioner | ai-specific |
| [SAFE-K8S-0904-005](markdown/controls/SAFE-K8S-0904-005.md) | D09 | 9.4 | Scheduled job security and feature freshness monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0904-006](markdown/controls/SAFE-K8S-0904-006.md) | D09 | 9.4 | Pipeline stage isolation and cross-classification authorization | Practitioner | ai-specific |
| [SAFE-K8S-0904-007](markdown/controls/SAFE-K8S-0904-007.md) | D09 | 9.4 | Scheduled feature computation job hardening | Practitioner | ai-specific |
| [SAFE-K8S-0904-008](markdown/controls/SAFE-K8S-0904-008.md) | D09 | 9.4 | Feature freshness and integrity monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0904-009](markdown/controls/SAFE-K8S-0904-009.md) | D09 | 9.4 | Experiment tracking metadata access control and audit logging | Practitioner | ai-specific |
| [SAFE-K8S-0904-010](markdown/controls/SAFE-K8S-0904-010.md) | D09 | 9.4 | Pipeline definition signing, immutability, and rollback integrity | Practitioner | ai-specific |
| [SAFE-K8S-0904-011](markdown/controls/SAFE-K8S-0904-011.md) | D09 | 9.4 | Pipeline stage isolation between sensitivity levels | Practitioner | ai-specific |
| [SAFE-K8S-0904-012](markdown/controls/SAFE-K8S-0904-012.md) | D09 | 9.4 | Cross-classification pipeline data transfer authorization gates | Practitioner | ai-specific |
| [SAFE-K8S-0904-013](markdown/controls/SAFE-K8S-0904-013.md) | D09 | 9.4 | Pipeline artifact storage encryption and object-store access policy enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0904-014](markdown/controls/SAFE-K8S-0904-014.md) | D09 | 9.4 | Pipeline stage-scoped artifact access and retention governance | Practitioner | ai-specific |
| [SAFE-K8S-0904-015](markdown/controls/SAFE-K8S-0904-015.md) | D09 | 9.4 | Experiment tracking metadata access control and tenant visibility enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0904-016](markdown/controls/SAFE-K8S-0904-016.md) | D09 | 9.4 | Experiment tracking access and modification audit logging | Practitioner | ai-specific |
| [SAFE-K8S-0904-017](markdown/controls/SAFE-K8S-0904-017.md) | D09 | 9.4 | Pipeline definition signing and execution-time signature verification | Practitioner | ai-specific |
| [SAFE-K8S-0904-018](markdown/controls/SAFE-K8S-0904-018.md) | D09 | 9.4 | Pipeline definition immutable version storage and controlled rollback governance | Practitioner | ai-specific |
| [SAFE-K8S-0905-001](markdown/controls/SAFE-K8S-0905-001.md) | D09 | 9.5 | AI system lifecycle classification | Practitioner | ai-specific |
| [SAFE-K8S-0905-002](markdown/controls/SAFE-K8S-0905-002.md) | D09 | 9.5 | ML artifact signing and attestation generation | Advanced | ai-specific |
| [SAFE-K8S-0905-003](markdown/controls/SAFE-K8S-0905-003.md) | D09 | 9.5 | Model registry hardening | Practitioner | ai-specific |
| [SAFE-K8S-0905-004](markdown/controls/SAFE-K8S-0905-004.md) | D09 | 9.5 | ML dependency vulnerability management and ML-BOM | Advanced | ai-specific |
| [SAFE-K8S-0905-005](markdown/controls/SAFE-K8S-0905-005.md) | D09 | 9.5 | Automated model promotion gates | Advanced | ai-specific |
| [SAFE-K8S-0905-006](markdown/controls/SAFE-K8S-0905-006.md) | D09 | 9.5 | Model artifact lifecycle management | Advanced | ai-specific |
| [SAFE-K8S-0905-007](markdown/controls/SAFE-K8S-0905-007.md) | D09 | 9.5 | Model format security and deserialization controls | Practitioner | ai-specific |
| [SAFE-K8S-0905-008](markdown/controls/SAFE-K8S-0905-008.md) | D09 | 9.5 | Public model quarantine and vetting workflow | Advanced | ai-specific |
| [SAFE-K8S-0905-009](markdown/controls/SAFE-K8S-0905-009.md) | D09 | 9.5 | Model provenance verification at deployment | Advanced | ai-specific |
| [SAFE-K8S-0905-010](markdown/controls/SAFE-K8S-0905-010.md) | D09 | 9.5 | Model promotion approval and reviewer identity validation | Advanced | ai-specific |
| [SAFE-K8S-0905-011](markdown/controls/SAFE-K8S-0905-011.md) | D09 | 9.5 | Canary and A/B deployment isolation and rollback safety | Advanced | ai-specific |
| [SAFE-K8S-0905-012](markdown/controls/SAFE-K8S-0905-012.md) | D09 | 9.5 | Development-to-production environment separation for AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0905-013](markdown/controls/SAFE-K8S-0905-013.md) | D09 | 9.5 | Approved external model source allowlist enforcement | Advanced | ai-specific |
| [SAFE-K8S-0905-014](markdown/controls/SAFE-K8S-0905-014.md) | D09 | 9.5 | AI workload circuit-breaker and emergency halt mechanisms | Advanced | ai-specific |
| [SAFE-K8S-0905-015](markdown/controls/SAFE-K8S-0905-015.md) | D09 | 9.5 | AI system control profile enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0905-016](markdown/controls/SAFE-K8S-0905-016.md) | D09 | 9.5 | Model registry RBAC, service account scoping, and access review | Practitioner | ai-specific |
| [SAFE-K8S-0905-017](markdown/controls/SAFE-K8S-0905-017.md) | D09 | 9.5 | Model registry operation audit logging and forwarding | Practitioner | ai-specific |
| [SAFE-K8S-0905-018](markdown/controls/SAFE-K8S-0905-018.md) | D09 | 9.5 | ML framework and CUDA dependency vulnerability management | Advanced | ai-specific |
| [SAFE-K8S-0905-019](markdown/controls/SAFE-K8S-0905-019.md) | D09 | 9.5 | ML-BOM generation and model lineage metadata capture | Advanced | ai-specific |
| [SAFE-K8S-0905-020](markdown/controls/SAFE-K8S-0905-020.md) | D09 | 9.5 | Public model quarantine scanning and sandbox vetting | Advanced | ai-specific |
| [SAFE-K8S-0905-021](markdown/controls/SAFE-K8S-0905-021.md) | D09 | 9.5 | External model provenance verification and internal re-registration | Advanced | ai-specific |
| [SAFE-K8S-0905-022](markdown/controls/SAFE-K8S-0905-022.md) | D09 | 9.5 | ML artifact signing and training attestation generation | Advanced | ai-specific |
| [SAFE-K8S-0905-023](markdown/controls/SAFE-K8S-0905-023.md) | D09 | 9.5 | OCI model artifact digest pinning and tag immutability | Advanced | ai-specific |
| [SAFE-K8S-0905-024](markdown/controls/SAFE-K8S-0905-024.md) | D09 | 9.5 | Authenticated reviewer identity validation and approval audit binding | Advanced | ai-specific |
| [SAFE-K8S-0905-025](markdown/controls/SAFE-K8S-0905-025.md) | D09 | 9.5 | Separation of duties enforcement for model promotion approvals | Advanced | ai-specific |
| [SAFE-K8S-0905-026](markdown/controls/SAFE-K8S-0905-026.md) | D09 | 9.5 | Approved external model source allowlist governance and review | Advanced | ai-specific |
| [SAFE-K8S-0905-027](markdown/controls/SAFE-K8S-0905-027.md) | D09 | 9.5 | External model source enforcement through network policy and admission control | Advanced | ai-specific |
| [SAFE-K8S-0905-028](markdown/controls/SAFE-K8S-0905-028.md) | D09 | 9.5 | ML framework and Python dependency vulnerability management | Advanced | ai-specific |
| [SAFE-K8S-0905-029](markdown/controls/SAFE-K8S-0905-029.md) | D09 | 9.5 | CUDA and GPU accelerator dependency vulnerability management | Advanced | ai-specific |
| [SAFE-K8S-0905-030](markdown/controls/SAFE-K8S-0905-030.md) | D09 | 9.5 | External model provenance verification and trust-signal review | Advanced | ai-specific |
| [SAFE-K8S-0905-031](markdown/controls/SAFE-K8S-0905-031.md) | D09 | 9.5 | Internal re-signing, external-origin annotation, and registry admission for external models | Advanced | ai-specific |
| [SAFE-K8S-0905-032](markdown/controls/SAFE-K8S-0905-032.md) | D09 | 9.5 | Safe model format allowlist and unsafe deserialization blocking | Practitioner | ai-specific |
| [SAFE-K8S-0905-033](markdown/controls/SAFE-K8S-0905-033.md) | D09 | 9.5 | Pre-load model file structure and metadata validation | Practitioner | ai-specific |
| [SAFE-K8S-0905-034](markdown/controls/SAFE-K8S-0905-034.md) | D09 | 9.5 | Canary and A/B candidate version isolation and traffic-splitting integrity | Advanced | ai-specific |
| [SAFE-K8S-0905-035](markdown/controls/SAFE-K8S-0905-035.md) | D09 | 9.5 | Automatic canary rollback on error-rate and latency degradation | Advanced | ai-specific |
| [SAFE-K8S-0905-036](markdown/controls/SAFE-K8S-0905-036.md) | D09 | 9.5 | Automated AI workload circuit-breaker threshold enforcement | Advanced | ai-specific |
| [SAFE-K8S-0905-037](markdown/controls/SAFE-K8S-0905-037.md) | D09 | 9.5 | Manual emergency halt governance and forensic evidence preservation | Advanced | ai-specific |
| [SAFE-K8S-0905-038](markdown/controls/SAFE-K8S-0905-038.md) | D09 | 9.5 | Model registry RBAC and workload pull authorization scoping | Practitioner | ai-specific |
| [SAFE-K8S-0905-039](markdown/controls/SAFE-K8S-0905-039.md) | D09 | 9.5 | Model registry access review and stale-permission remediation | Practitioner | ai-specific |
| [SAFE-K8S-0905-040](markdown/controls/SAFE-K8S-0905-040.md) | D09 | 9.5 | Model registry audit event generation and centralized forwarding | Practitioner | ai-specific |
| [SAFE-K8S-0905-041](markdown/controls/SAFE-K8S-0905-041.md) | D09 | 9.5 | Model registry sensitive-operation alerting and anomalous activity review | Practitioner | ai-specific |
| [SAFE-K8S-0905-042](markdown/controls/SAFE-K8S-0905-042.md) | D09 | 9.5 | CTA-2114 ML-BOM generation and lineage metadata capture | Advanced | ai-specific |
| [SAFE-K8S-0905-043](markdown/controls/SAFE-K8S-0905-043.md) | D09 | 9.5 | Durable ML-BOM attachment to model artifacts and versions | Advanced | ai-specific |
| [SAFE-K8S-0905-044](markdown/controls/SAFE-K8S-0905-044.md) | D09 | 9.5 | Public model quarantine isolation and malicious artifact scanning | Advanced | ai-specific |
| [SAFE-K8S-0905-045](markdown/controls/SAFE-K8S-0905-045.md) | D09 | 9.5 | Sandboxed external model behavioral vetting and disposition review | Advanced | ai-specific |
| [SAFE-K8S-0905-046](markdown/controls/SAFE-K8S-0905-046.md) | D09 | 9.5 | ML artifact cryptographic signing with Sigstore or equivalent | Advanced | ai-specific |
| [SAFE-K8S-0905-047](markdown/controls/SAFE-K8S-0905-047.md) | D09 | 9.5 | Training pipeline attestation generation for ML artifacts | Advanced | ai-specific |
| [SAFE-K8S-0905-048](markdown/controls/SAFE-K8S-0905-048.md) | D09 | 9.5 | OCI model artifact digest pinning in deployment and promotion workflows | Advanced | ai-specific |
| [SAFE-K8S-0905-049](markdown/controls/SAFE-K8S-0905-049.md) | D09 | 9.5 | OCI model registry tag immutability and overwrite prevention | Advanced | ai-specific |
| [SAFE-K8S-0905-050](markdown/controls/SAFE-K8S-0905-050.md) | D09 | 9.5 | Authenticated reviewer identity validation for model promotion approvals | Advanced | ai-specific |
| [SAFE-K8S-0905-051](markdown/controls/SAFE-K8S-0905-051.md) | D09 | 9.5 | Model promotion approval audit binding to reviewer identity and model version | Advanced | ai-specific |
| [SAFE-K8S-0905-052](markdown/controls/SAFE-K8S-0905-052.md) | D09 | 9.5 | Approved external model source allowlist definition and maintenance | Advanced | ai-specific |
| [SAFE-K8S-0905-053](markdown/controls/SAFE-K8S-0905-053.md) | D09 | 9.5 | Approved external model source periodic review and allowlist update governance | Advanced | ai-specific |
| [SAFE-K8S-0905-054](markdown/controls/SAFE-K8S-0905-054.md) | D09 | 9.5 | External model source NetworkPolicy enforcement for protected namespaces | Advanced | ai-specific |
| [SAFE-K8S-0905-055](markdown/controls/SAFE-K8S-0905-055.md) | D09 | 9.5 | Admission-time rejection of unapproved external model source references | Advanced | ai-specific |
| [SAFE-K8S-0905-056](markdown/controls/SAFE-K8S-0905-056.md) | D09 | 9.5 | External model publisher identity and provenance metadata verification | Advanced | ai-specific |
| [SAFE-K8S-0905-057](markdown/controls/SAFE-K8S-0905-057.md) | D09 | 9.5 | External model trust-signal assessment and approval review | Advanced | ai-specific |
| [SAFE-K8S-0905-058](markdown/controls/SAFE-K8S-0905-058.md) | D09 | 9.5 | Internal re-signing of approved external models before deployment eligibility | Advanced | ai-specific |
| [SAFE-K8S-0905-059](markdown/controls/SAFE-K8S-0905-059.md) | D09 | 9.5 | External-origin annotation and internal registry enrollment for approved external models | Advanced | ai-specific |
| [SAFE-K8S-0906-001](markdown/controls/SAFE-K8S-0906-001.md) | D09 | 9.6 | Training data provenance and pipeline integrity | Practitioner | ai-specific |
| [SAFE-K8S-0906-002](markdown/controls/SAFE-K8S-0906-002.md) | D09 | 9.6 | Large-scale data integrity verification | Practitioner | ai-specific |
| [SAFE-K8S-0906-003](markdown/controls/SAFE-K8S-0906-003.md) | D09 | 9.6 | Data poisoning and label attack detection | Practitioner | ai-specific |
| [SAFE-K8S-0906-004](markdown/controls/SAFE-K8S-0906-004.md) | D09 | 9.6 | Statistical drift, outlier, and input validation for training data poisoning detection | Practitioner | ai-specific |
| [SAFE-K8S-0906-005](markdown/controls/SAFE-K8S-0906-005.md) | D09 | 9.6 | Annotation pipeline integrity and targeted label attack detection | Practitioner | ai-specific |
| [SAFE-K8S-0906-006](markdown/controls/SAFE-K8S-0906-006.md) | D09 | 9.6 | Training data provenance tracking from ingestion through model training | Practitioner | ai-specific |
| [SAFE-K8S-0906-007](markdown/controls/SAFE-K8S-0906-007.md) | D09 | 9.6 | Integrity verification at each training data transformation stage | Practitioner | ai-specific |
| [SAFE-K8S-0907-001](markdown/controls/SAFE-K8S-0907-001.md) | D09 | 9.7 | Feature store security and leakage prevention | Practitioner | ai-specific |
| [SAFE-K8S-0907-002](markdown/controls/SAFE-K8S-0907-002.md) | D09 | 9.7 | Training data privacy controls | Practitioner | ai-specific |
| [SAFE-K8S-0907-003](markdown/controls/SAFE-K8S-0907-003.md) | D09 | 9.7 | Training dataset and model deployment access controls | Practitioner | ai-specific |
| [SAFE-K8S-0907-004](markdown/controls/SAFE-K8S-0907-004.md) | D09 | 9.7 | Feature store access boundary enforcement and serving authentication | Practitioner | ai-specific |
| [SAFE-K8S-0907-005](markdown/controls/SAFE-K8S-0907-005.md) | D09 | 9.7 | Feature engineering privacy controls and leakage validation | Practitioner | ai-specific |
| [SAFE-K8S-0907-006](markdown/controls/SAFE-K8S-0907-006.md) | D09 | 9.7 | Training dataset access restriction across storage backends | Practitioner | ai-specific |
| [SAFE-K8S-0907-007](markdown/controls/SAFE-K8S-0907-007.md) | D09 | 9.7 | Model deployment authorization and namespace-scoped release control | Practitioner | ai-specific |
| [SAFE-K8S-0908-001](markdown/controls/SAFE-K8S-0908-001.md) | D09 | 9.8 | Oracle attack prevention | Advanced | ai-specific |
| [SAFE-K8S-0908-002](markdown/controls/SAFE-K8S-0908-002.md) | D09 | 9.8 | Inference API information exposure controls | Advanced | ai-specific |
| [SAFE-K8S-0908-003](markdown/controls/SAFE-K8S-0908-003.md) | D09 | 9.8 | Model watermarking and fingerprinting | Advanced | ai-specific |
| [SAFE-K8S-0908-004](markdown/controls/SAFE-K8S-0908-004.md) | D09 | 9.8 | Differential privacy and output perturbation | Advanced | ai-specific |
| [SAFE-K8S-0908-005](markdown/controls/SAFE-K8S-0908-005.md) | D09 | 9.8 | Model abuse logging and alerting | Advanced | ai-specific |
| [SAFE-K8S-0908-006](markdown/controls/SAFE-K8S-0908-006.md) | D09 | 9.8 | Secure aggregation for privacy-preserving model outputs | Advanced | ai-specific |
| [SAFE-K8S-0908-007](markdown/controls/SAFE-K8S-0908-007.md) | D09 | 9.8 | Differential privacy parameter governance and budget tracking for inference | Advanced | ai-specific |
| [SAFE-K8S-0908-008](markdown/controls/SAFE-K8S-0908-008.md) | D09 | 9.8 | Inference output perturbation and privacy-preserving response shaping | Advanced | ai-specific |
| [SAFE-K8S-0908-009](markdown/controls/SAFE-K8S-0908-009.md) | D09 | 9.8 | Differential privacy parameter governance for inference endpoints | Advanced | ai-specific |
| [SAFE-K8S-0908-010](markdown/controls/SAFE-K8S-0908-010.md) | D09 | 9.8 | Inference privacy budget tracking and threshold enforcement | Advanced | ai-specific |
| [SAFE-K8S-0909-001](markdown/controls/SAFE-K8S-0909-001.md) | D09 | 9.9 | Vector database access controls and encryption | Practitioner | ai-specific |
| [SAFE-K8S-0909-002](markdown/controls/SAFE-K8S-0909-002.md) | D09 | 9.9 | Embedding pipeline integrity | Practitioner | ai-specific |
| [SAFE-K8S-0909-003](markdown/controls/SAFE-K8S-0909-003.md) | D09 | 9.9 | Document ingestion and chunking security | Practitioner | ai-specific |
| [SAFE-K8S-0909-004](markdown/controls/SAFE-K8S-0909-004.md) | D09 | 9.9 | Retrieval integrity and context poisoning defense | Practitioner | ai-specific |
| [SAFE-K8S-0909-005](markdown/controls/SAFE-K8S-0909-005.md) | D09 | 9.9 | RAG prompt injection defense | Practitioner | ai-specific |
| [SAFE-K8S-0909-006](markdown/controls/SAFE-K8S-0909-006.md) | D09 | 9.9 | Vector index lifecycle management | Practitioner | ai-specific |
| [SAFE-K8S-0909-007](markdown/controls/SAFE-K8S-0909-007.md) | D09 | 9.9 | Document source access control and provenance validation for RAG ingestion | Practitioner | ai-specific |
| [SAFE-K8S-0909-008](markdown/controls/SAFE-K8S-0909-008.md) | D09 | 9.9 | Classification-aware chunking and vector collection segregation | Practitioner | ai-specific |
| [SAFE-K8S-0909-009](markdown/controls/SAFE-K8S-0909-009.md) | D09 | 9.9 | Vector database authentication and collection-level access control | Practitioner | ai-specific |
| [SAFE-K8S-0909-010](markdown/controls/SAFE-K8S-0909-010.md) | D09 | 9.9 | Vector database encryption in transit and at rest | Practitioner | ai-specific |
| [SAFE-K8S-0909-011](markdown/controls/SAFE-K8S-0909-011.md) | D09 | 9.9 | Retrieved context integrity validation and relevance threshold enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0909-012](markdown/controls/SAFE-K8S-0909-012.md) | D09 | 9.9 | Context poisoning monitoring and incident response for RAG retrieval | Practitioner | ai-specific |
| [SAFE-K8S-0909-013](markdown/controls/SAFE-K8S-0909-013.md) | D09 | 9.9 | Approved source repository access control and allowlist enforcement for RAG ingestion | Practitioner | ai-specific |
| [SAFE-K8S-0909-014](markdown/controls/SAFE-K8S-0909-014.md) | D09 | 9.9 | Document provenance and integrity validation before RAG chunking and indexing | Practitioner | ai-specific |
| [SAFE-K8S-0910-001](markdown/controls/SAFE-K8S-0910-001.md) | D09 | 9.10 | Multi-cluster AI workload orchestration security | Advanced | ai-specific |
| [SAFE-K8S-0910-002](markdown/controls/SAFE-K8S-0910-002.md) | D09 | 9.10 | Cross-cluster model registry federation and replication security | Advanced | ai-specific |
| [SAFE-K8S-0910-003](markdown/controls/SAFE-K8S-0910-003.md) | D09 | 9.10 | Multi-cluster network security for distributed AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0910-004](markdown/controls/SAFE-K8S-0910-004.md) | D09 | 9.10 | Federated learning cross-cluster coordination security | Advanced | ai-specific |
| [SAFE-K8S-0910-005](markdown/controls/SAFE-K8S-0910-005.md) | D09 | 9.10 | Multi-cluster AI governance and compliance consistency | Advanced | ai-specific |
| [SAFE-K8S-0910-006](markdown/controls/SAFE-K8S-0910-006.md) | D09 | 9.10 | Cross-cluster orchestration identity and audit security | Advanced | ai-specific |
| [SAFE-K8S-0910-007](markdown/controls/SAFE-K8S-0910-007.md) | D09 | 9.10 | Security-aware multi-cluster placement and federation isolation | Advanced | ai-specific |
| [SAFE-K8S-0910-008](markdown/controls/SAFE-K8S-0910-008.md) | D09 | 9.10 | Cross-cluster transport encryption and workload authentication | Advanced | ai-specific |
| [SAFE-K8S-0910-009](markdown/controls/SAFE-K8S-0910-009.md) | D09 | 9.10 | Cross-cluster communication authorization and anomaly monitoring | Advanced | ai-specific |
| [SAFE-K8S-0910-010](markdown/controls/SAFE-K8S-0910-010.md) | D09 | 9.10 | Cross-cluster registry replication channel authentication and signature re-verification | Advanced | ai-specific |
| [SAFE-K8S-0910-011](markdown/controls/SAFE-K8S-0910-011.md) | D09 | 9.10 | Cross-cluster model provenance preservation and federation endpoint governance | Advanced | ai-specific |
| [SAFE-K8S-0910-012](markdown/controls/SAFE-K8S-0910-012.md) | D09 | 9.10 | Multi-cluster security policy federation and drift remediation | Advanced | ai-specific |
| [SAFE-K8S-0910-013](markdown/controls/SAFE-K8S-0910-013.md) | D09 | 9.10 | Unified multi-cluster compliance reporting and governance coordination | Advanced | ai-specific |
| [SAFE-K8S-0910-014](markdown/controls/SAFE-K8S-0910-014.md) | D09 | 9.10 | Cross-cluster registry replication channel authentication and endpoint enrollment | Advanced | ai-specific |
| [SAFE-K8S-0910-015](markdown/controls/SAFE-K8S-0910-015.md) | D09 | 9.10 | Destination-side signature and digest re-verification for replicated model artifacts | Advanced | ai-specific |
| [SAFE-K8S-0910-016](markdown/controls/SAFE-K8S-0910-016.md) | D09 | 9.10 | Cross-cluster orchestration identity federation and authorization | Advanced | ai-specific |
| [SAFE-K8S-0910-017](markdown/controls/SAFE-K8S-0910-017.md) | D09 | 9.10 | Centralized audit logging for cross-cluster orchestration actions | Advanced | ai-specific |
| [SAFE-K8S-0910-018](markdown/controls/SAFE-K8S-0910-018.md) | D09 | 9.10 | Security-aware target-cluster posture verification before multi-cluster placement | Advanced | ai-specific |
| [SAFE-K8S-0910-019](markdown/controls/SAFE-K8S-0910-019.md) | D09 | 9.10 | Compromised-cluster federation isolation and re-admission governance | Advanced | ai-specific |
| [SAFE-K8S-0910-020](markdown/controls/SAFE-K8S-0910-020.md) | D09 | 9.10 | Cross-cluster transport encryption for distributed AI traffic | Advanced | ai-specific |
| [SAFE-K8S-0910-021](markdown/controls/SAFE-K8S-0910-021.md) | D09 | 9.10 | Cross-cluster endpoint and workload authentication for AI communication | Advanced | ai-specific |
| [SAFE-K8S-0910-022](markdown/controls/SAFE-K8S-0910-022.md) | D09 | 9.10 | Cross-cluster communication authorization policy enforcement | Advanced | ai-specific |
| [SAFE-K8S-0910-023](markdown/controls/SAFE-K8S-0910-023.md) | D09 | 9.10 | Cross-cluster traffic anomaly monitoring and investigation | Advanced | ai-specific |
| [SAFE-K8S-0910-024](markdown/controls/SAFE-K8S-0910-024.md) | D09 | 9.10 | Cross-cluster model provenance chain-of-custody preservation | Advanced | ai-specific |
| [SAFE-K8S-0910-025](markdown/controls/SAFE-K8S-0910-025.md) | D09 | 9.10 | Cross-cluster registry federation endpoint authorization and reconciliation governance | Advanced | ai-specific |
| [SAFE-K8S-0910-026](markdown/controls/SAFE-K8S-0910-026.md) | D09 | 9.10 | Multi-cluster security policy baseline federation | Advanced | ai-specific |
| [SAFE-K8S-0910-027](markdown/controls/SAFE-K8S-0910-027.md) | D09 | 9.10 | Multi-cluster policy drift detection and remediation | Advanced | ai-specific |
| [SAFE-K8S-0910-028](markdown/controls/SAFE-K8S-0910-028.md) | D09 | 9.10 | Unified multi-cluster compliance reporting | Advanced | ai-specific |
| [SAFE-K8S-0910-029](markdown/controls/SAFE-K8S-0910-029.md) | D09 | 9.10 | Centralized multi-cluster secret, certificate, and incident governance coordination | Advanced | ai-specific |
| [SAFE-K8S-0910-030](markdown/controls/SAFE-K8S-0910-030.md) | D09 | 9.10 | Cross-cluster registry replication channel mutual authentication | Advanced | ai-specific |
| [SAFE-K8S-0910-031](markdown/controls/SAFE-K8S-0910-031.md) | D09 | 9.10 | Cross-cluster registry endpoint enrollment approval | Advanced | ai-specific |
| [SAFE-K8S-0910-032](markdown/controls/SAFE-K8S-0910-032.md) | D09 | 9.10 | Cross-cluster traffic anomaly monitoring for distributed AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0910-033](markdown/controls/SAFE-K8S-0910-033.md) | D09 | 9.10 | Investigation of anomalous cross-cluster AI communication | Advanced | ai-specific |
| [SAFE-K8S-1001-001](markdown/controls/SAFE-K8S-1001-001.md) | D10 | 10.1 | Kubernetes audit policy coverage for AI-relevant API events | Practitioner | ai-specific |
| [SAFE-K8S-1001-002](markdown/controls/SAFE-K8S-1001-002.md) | D10 | 10.1 | Cluster-level logging architecture | Practitioner | baseline |
| [SAFE-K8S-1001-003](markdown/controls/SAFE-K8S-1001-003.md) | D10 | 10.1 | Centralized logging for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-004](markdown/controls/SAFE-K8S-1001-004.md) | D10 | 10.1 | Audit volume management for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-005](markdown/controls/SAFE-K8S-1001-005.md) | D10 | 10.1 | Audit log protection and dual authorization for modification | Practitioner | baseline |
| [SAFE-K8S-1001-006](markdown/controls/SAFE-K8S-1001-006.md) | D10 | 10.1 | SIEM ingestion for Kubernetes AI security events | Practitioner | ai-specific |
| [SAFE-K8S-1001-007](markdown/controls/SAFE-K8S-1001-007.md) | D10 | 10.1 | Supplemental application-level telemetry for AI workload events | Practitioner | ai-specific |
| [SAFE-K8S-1001-008](markdown/controls/SAFE-K8S-1001-008.md) | D10 | 10.1 | Permitted responses to audit findings | Practitioner | baseline |
| [SAFE-K8S-1001-009](markdown/controls/SAFE-K8S-1001-009.md) | D10 | 10.1 | Regulatory log and artifact retention policy enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-010](markdown/controls/SAFE-K8S-1001-010.md) | D10 | 10.1 | Kubernetes audit level and stage filtering for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-011](markdown/controls/SAFE-K8S-1001-011.md) | D10 | 10.1 | Durable and tamper-resistant audit backend delivery | Practitioner | ai-specific |
| [SAFE-K8S-1001-012](markdown/controls/SAFE-K8S-1001-012.md) | D10 | 10.1 | SIEM correlation rules for AI-specific attack patterns | Practitioner | ai-specific |
| [SAFE-K8S-1001-013](markdown/controls/SAFE-K8S-1001-013.md) | D10 | 10.1 | SIEM event forwarding and ingestion health for Kubernetes AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-014](markdown/controls/SAFE-K8S-1001-014.md) | D10 | 10.1 | Centralized collection and segregation of AI workload logs | Practitioner | ai-specific |
| [SAFE-K8S-1001-015](markdown/controls/SAFE-K8S-1001-015.md) | D10 | 10.1 | PII redaction and sensitive payload minimization for inference logs | Practitioner | ai-specific |
| [SAFE-K8S-1001-016](markdown/controls/SAFE-K8S-1001-016.md) | D10 | 10.1 | Audit policy coverage for AI-specific resource and workflow events | Practitioner | ai-specific |
| [SAFE-K8S-1001-017](markdown/controls/SAFE-K8S-1001-017.md) | D10 | 10.1 | Audit capture of admission, authorization, and privileged API decisions for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-018](markdown/controls/SAFE-K8S-1001-018.md) | D10 | 10.1 | Regulatory audit log retention period and durable retrieval enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-019](markdown/controls/SAFE-K8S-1001-019.md) | D10 | 10.1 | Regulatory AI artifact and provenance record retention enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-020](markdown/controls/SAFE-K8S-1001-020.md) | D10 | 10.1 | Cluster-wide AI workload log collection and centralized aggregation | Practitioner | baseline |
| [SAFE-K8S-1001-021](markdown/controls/SAFE-K8S-1001-021.md) | D10 | 10.1 | Centralized log integrity protection and retention enforcement for AI workloads | Practitioner | baseline |
| [SAFE-K8S-1001-022](markdown/controls/SAFE-K8S-1001-022.md) | D10 | 10.1 | Regulatory audit log retention period enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-023](markdown/controls/SAFE-K8S-1001-023.md) | D10 | 10.1 | Regulatory audit log durable retrieval enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-024](markdown/controls/SAFE-K8S-1001-024.md) | D10 | 10.1 | Audit log append-only storage and tamper protection | Practitioner | baseline |
| [SAFE-K8S-1001-025](markdown/controls/SAFE-K8S-1001-025.md) | D10 | 10.1 | Dual authorization for audit log deletion or modification | Practitioner | baseline |
| [SAFE-K8S-1001-026](markdown/controls/SAFE-K8S-1001-026.md) | D10 | 10.1 | Durable audit backend delivery for Kubernetes AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-027](markdown/controls/SAFE-K8S-1001-027.md) | D10 | 10.1 | Tamper-resistant retention for Kubernetes AI audit backends | Practitioner | ai-specific |
| [SAFE-K8S-1001-028](markdown/controls/SAFE-K8S-1001-028.md) | D10 | 10.1 | AI-specific SIEM source onboarding and forwarding | Practitioner | ai-specific |
| [SAFE-K8S-1001-029](markdown/controls/SAFE-K8S-1001-029.md) | D10 | 10.1 | SIEM ingestion health, delivery completeness, and source coverage monitoring | Practitioner | ai-specific |
| [SAFE-K8S-1001-030](markdown/controls/SAFE-K8S-1001-030.md) | D10 | 10.1 | Centralized AI workload log collection and routing | Practitioner | ai-specific |
| [SAFE-K8S-1001-031](markdown/controls/SAFE-K8S-1001-031.md) | D10 | 10.1 | Tenant and workload context preservation for AI log segregation and searchability | Practitioner | ai-specific |
| [SAFE-K8S-1001-032](markdown/controls/SAFE-K8S-1001-032.md) | D10 | 10.1 | Cluster-wide Kubernetes and AI log source coverage | Practitioner | baseline |
| [SAFE-K8S-1001-033](markdown/controls/SAFE-K8S-1001-033.md) | D10 | 10.1 | Centralized aggregation onboarding and export for cluster-wide AI logs | Practitioner | baseline |
| [SAFE-K8S-1001-034](markdown/controls/SAFE-K8S-1001-034.md) | D10 | 10.1 | Centralized AI log backend immutability and integrity verification | Practitioner | baseline |
| [SAFE-K8S-1001-035](markdown/controls/SAFE-K8S-1001-035.md) | D10 | 10.1 | Centralized AI log retention lifecycle enforcement and durable retrieval | Practitioner | baseline |
| [SAFE-K8S-1001-036](markdown/controls/SAFE-K8S-1001-036.md) | D10 | 10.1 | Regulatory audit log retention period configuration and compliance verification | Practitioner | ai-specific |
| [SAFE-K8S-1001-037](markdown/controls/SAFE-K8S-1001-037.md) | D10 | 10.1 | Regulatory audit log immutability and deletion prevention before retention expiry | Practitioner | ai-specific |
| [SAFE-K8S-1001-038](markdown/controls/SAFE-K8S-1001-038.md) | D10 | 10.1 | Centralized AI log retention lifecycle enforcement | Practitioner | baseline |
| [SAFE-K8S-1001-039](markdown/controls/SAFE-K8S-1001-039.md) | D10 | 10.1 | Durable retrieval validation for centralized AI logs | Practitioner | baseline |
| [SAFE-K8S-1002-001](markdown/controls/SAFE-K8S-1002-001.md) | D10 | 10.2 | Metric endpoint authentication | Practitioner | baseline |
| [SAFE-K8S-1002-002](markdown/controls/SAFE-K8S-1002-002.md) | D10 | 10.2 | Distributed tracing for ML pipelines | Practitioner | ai-specific |
| [SAFE-K8S-1002-003](markdown/controls/SAFE-K8S-1002-003.md) | D10 | 10.2 | AI workload telemetry integration into cluster monitoring | Practitioner | ai-specific |
| [SAFE-K8S-1002-004](markdown/controls/SAFE-K8S-1002-004.md) | D10 | 10.2 | AI-specific alerting and failure mode detection | Practitioner | ai-specific |
| [SAFE-K8S-1002-005](markdown/controls/SAFE-K8S-1002-005.md) | D10 | 10.2 | Metric endpoint authorization and RBAC | Practitioner | baseline |
| [SAFE-K8S-1002-006](markdown/controls/SAFE-K8S-1002-006.md) | D10 | 10.2 | Sensitive metric redaction and access restriction | Practitioner | ai-specific |
| [SAFE-K8S-1003-001](markdown/controls/SAFE-K8S-1003-001.md) | D10 | 10.3 | STRIDE threat modeling for Kubernetes AI systems | Practitioner | ai-specific |
| [SAFE-K8S-1003-002](markdown/controls/SAFE-K8S-1003-002.md) | D10 | 10.3 | OCTAVE risk-based threat assessment for Kubernetes AI environments | Advanced | ai-specific |
| [SAFE-K8S-1003-003](markdown/controls/SAFE-K8S-1003-003.md) | D10 | 10.3 | MITRE ATT&CK for Containers threat mapping | Advanced | ai-specific |
| [SAFE-K8S-1003-004](markdown/controls/SAFE-K8S-1003-004.md) | D10 | 10.3 | MITRE ATT&CK for Containers coverage mapping and gap analysis | Advanced | ai-specific |
| [SAFE-K8S-1003-005](markdown/controls/SAFE-K8S-1003-005.md) | D10 | 10.3 | Technique-aligned detection engineering for Kubernetes AI attack scenarios | Advanced | ai-specific |
| [SAFE-K8S-1004-001](markdown/controls/SAFE-K8S-1004-001.md) | D10 | 10.4 | ML threat taxonomy per CTA-2114 mapped to Kubernetes | Advanced | ai-specific |
| [SAFE-K8S-1004-002](markdown/controls/SAFE-K8S-1004-002.md) | D10 | 10.4 | Software supply chain threat model per NIST SP 800-204D | Advanced | ai-specific |
| [SAFE-K8S-1004-003](markdown/controls/SAFE-K8S-1004-003.md) | D10 | 10.4 | Threat intelligence integration for Kubernetes AI environments | Advanced | ai-specific |
| [SAFE-K8S-1004-004](markdown/controls/SAFE-K8S-1004-004.md) | D10 | 10.4 | Kubernetes AI threat intelligence feed ingestion and detection enrichment | Advanced | ai-specific |
| [SAFE-K8S-1004-005](markdown/controls/SAFE-K8S-1004-005.md) | D10 | 10.4 | Adversarial ML threat taxonomy and structured classification | Advanced | ai-specific |
| [SAFE-K8S-1004-006](markdown/controls/SAFE-K8S-1004-006.md) | D10 | 10.4 | Cross-source threat correlation with business context for AI incidents | Advanced | ai-specific |
| [SAFE-K8S-1005-001](markdown/controls/SAFE-K8S-1005-001.md) | D10 | 10.5 | Kubernetes incident response lifecycle | Practitioner | ai-specific |
| [SAFE-K8S-1005-002](markdown/controls/SAFE-K8S-1005-002.md) | D10 | 10.5 | Kubernetes and AI workload containment strategies | Practitioner | ai-specific |
| [SAFE-K8S-1005-003](markdown/controls/SAFE-K8S-1005-003.md) | D10 | 10.5 | Forensic evidence collection for Kubernetes AI incidents | Practitioner | ai-specific |
| [SAFE-K8S-1005-004](markdown/controls/SAFE-K8S-1005-004.md) | D10 | 10.5 | Ransomware and destructive attack response for Kubernetes | Practitioner | baseline |
| [SAFE-K8S-1005-005](markdown/controls/SAFE-K8S-1005-005.md) | D10 | 10.5 | Post-incident model integrity verification and recovery decisions | Practitioner | ai-specific |
| [SAFE-K8S-1005-006](markdown/controls/SAFE-K8S-1005-006.md) | D10 | 10.5 | Lateral movement prevention and component integrity verification during recovery | Practitioner | ai-specific |
| [SAFE-K8S-1005-007](markdown/controls/SAFE-K8S-1005-007.md) | D10 | 10.5 | Vulnerability disclosure and coordination for Kubernetes infrastructure | Practitioner | baseline |
| [SAFE-K8S-1005-008](markdown/controls/SAFE-K8S-1005-008.md) | D10 | 10.5 | AI-specific incident response playbooks for Kubernetes | Practitioner | ai-specific |
| [SAFE-K8S-1005-009](markdown/controls/SAFE-K8S-1005-009.md) | D10 | 10.5 | Kubernetes containment procedures for nodes, namespaces, workloads, and credentials | Practitioner | ai-specific |
| [SAFE-K8S-1005-010](markdown/controls/SAFE-K8S-1005-010.md) | D10 | 10.5 | AI-specific containment actions for GPU nodes, inference services, and pipeline execution | Practitioner | ai-specific |
| [SAFE-K8S-1005-011](markdown/controls/SAFE-K8S-1005-011.md) | D10 | 10.5 | Kubernetes forensic evidence acquisition and chain-of-custody procedures | Practitioner | ai-specific |
| [SAFE-K8S-1005-012](markdown/controls/SAFE-K8S-1005-012.md) | D10 | 10.5 | AI-specific forensic preservation of GPU, model access, and training provenance evidence | Practitioner | ai-specific |
| [SAFE-K8S-1005-013](markdown/controls/SAFE-K8S-1005-013.md) | D10 | 10.5 | Kubernetes backup verification and etcd restoration readiness | Practitioner | baseline |
| [SAFE-K8S-1005-014](markdown/controls/SAFE-K8S-1005-014.md) | D10 | 10.5 | Ransomware recovery prioritization and post-incident preparedness improvement | Practitioner | baseline |
| [SAFE-K8S-1005-015](markdown/controls/SAFE-K8S-1005-015.md) | D10 | 10.5 | Post-incident AI model integrity verification | Practitioner | ai-specific |
| [SAFE-K8S-1005-016](markdown/controls/SAFE-K8S-1005-016.md) | D10 | 10.5 | Documented post-incident model retraining or rollback decisions | Practitioner | ai-specific |
| [SAFE-K8S-1005-017](markdown/controls/SAFE-K8S-1005-017.md) | D10 | 10.5 | Recovery-time lateral movement containment for compromised AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1005-018](markdown/controls/SAFE-K8S-1005-018.md) | D10 | 10.5 | Component integrity verification before restoration after compromise | Practitioner | ai-specific |
| [SAFE-K8S-1005-019](markdown/controls/SAFE-K8S-1005-019.md) | D10 | 10.5 | Vulnerability disclosure policy, intake channels, and triage SLAs for Kubernetes AI infrastructure | Practitioner | baseline |
| [SAFE-K8S-1005-020](markdown/controls/SAFE-K8S-1005-020.md) | D10 | 10.5 | Vulnerability response ownership and multi-party coordination governance for Kubernetes AI infrastructure | Practitioner | baseline |
| [SAFE-K8S-1005-021](markdown/controls/SAFE-K8S-1005-021.md) | D10 | 10.5 | Kubernetes containment runbooks for node draining, namespace isolation, and workload suspension | Practitioner | ai-specific |
| [SAFE-K8S-1005-022](markdown/controls/SAFE-K8S-1005-022.md) | D10 | 10.5 | Kubernetes incident credential revocation procedures for ServiceAccounts and external access | Practitioner | ai-specific |
| [SAFE-K8S-1005-023](markdown/controls/SAFE-K8S-1005-023.md) | D10 | 10.5 | GPU-aware node draining and accelerator workload containment | Practitioner | ai-specific |
| [SAFE-K8S-1005-024](markdown/controls/SAFE-K8S-1005-024.md) | D10 | 10.5 | Inference service quarantine and pipeline execution suspension with state preservation | Practitioner | ai-specific |
| [SAFE-K8S-1005-025](markdown/controls/SAFE-K8S-1005-025.md) | D10 | 10.5 | Kubernetes forensic evidence acquisition for container, node, audit, and network artifacts | Practitioner | ai-specific |
| [SAFE-K8S-1005-026](markdown/controls/SAFE-K8S-1005-026.md) | D10 | 10.5 | Forensic chain-of-custody and evidence handling for Kubernetes AI incidents | Practitioner | ai-specific |
| [SAFE-K8S-1005-027](markdown/controls/SAFE-K8S-1005-027.md) | D10 | 10.5 | GPU and accelerator forensic evidence preservation for Kubernetes AI incidents | Practitioner | ai-specific |
| [SAFE-K8S-1005-028](markdown/controls/SAFE-K8S-1005-028.md) | D10 | 10.5 | Model access and training provenance forensic preservation for Kubernetes AI incidents | Practitioner | ai-specific |
| [SAFE-K8S-1005-029](markdown/controls/SAFE-K8S-1005-029.md) | D10 | 10.5 | Kubernetes backup verification for etcd and AI workload data | Practitioner | baseline |
| [SAFE-K8S-1005-030](markdown/controls/SAFE-K8S-1005-030.md) | D10 | 10.5 | Documented etcd restoration procedures and tested execution readiness | Practitioner | baseline |
| [SAFE-K8S-1006-001](markdown/controls/SAFE-K8S-1006-001.md) | D10 | 10.6 | Regulatory compliance mapping for Kubernetes AI platforms | Practitioner | ai-specific |
| [SAFE-K8S-1006-002](markdown/controls/SAFE-K8S-1006-002.md) | D10 | 10.6 | SSDF v1.1 and SP 800-218A alignment for Kubernetes AI development | Advanced | ai-specific |
| [SAFE-K8S-1006-003](markdown/controls/SAFE-K8S-1006-003.md) | D10 | 10.6 | Policy-as-code for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1006-004](markdown/controls/SAFE-K8S-1006-004.md) | D10 | 10.6 | Automated audit readiness for Kubernetes AI platforms | Advanced | ai-specific |
| [SAFE-K8S-1006-005](markdown/controls/SAFE-K8S-1006-005.md) | D10 | 10.6 | Policy-as-code enforcement for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1006-006](markdown/controls/SAFE-K8S-1006-006.md) | D10 | 10.6 | Continuous compliance evidence generation for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1006-007](markdown/controls/SAFE-K8S-1006-007.md) | D10 | 10.6 | NIST SSDF v1.1 alignment and gap assessment for Kubernetes AI development | Advanced | ai-specific |
| [SAFE-K8S-1006-008](markdown/controls/SAFE-K8S-1006-008.md) | D10 | 10.6 | NIST SP 800-218A AI/ML profile alignment for Kubernetes AI development | Advanced | ai-specific |
| [SAFE-K8S-1006-009](markdown/controls/SAFE-K8S-1006-009.md) | D10 | 10.6 | Continuous policy decision evidence generation and export for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1006-010](markdown/controls/SAFE-K8S-1006-010.md) | D10 | 10.6 | Policy exception approval and expiration governance for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1007-001](markdown/controls/SAFE-K8S-1007-001.md) | D10 | 10.7 | Kubernetes and AI infrastructure upgrade planning | Practitioner | ai-specific |
| [SAFE-K8S-1007-002](markdown/controls/SAFE-K8S-1007-002.md) | D10 | 10.7 | Kubernetes API deprecation and removal tracking | Practitioner | ai-specific |
| [SAFE-K8S-1007-003](markdown/controls/SAFE-K8S-1007-003.md) | D10 | 10.7 | AI infrastructure asset inventory and classification | Practitioner | ai-specific |
| [SAFE-K8S-1007-004](markdown/controls/SAFE-K8S-1007-004.md) | D10 | 10.7 | Continuous security posture management for AI clusters | Practitioner | ai-specific |
| [SAFE-K8S-1007-005](markdown/controls/SAFE-K8S-1007-005.md) | D10 | 10.7 | Change management for production AI model deployments | Practitioner | ai-specific |
| [SAFE-K8S-1007-006](markdown/controls/SAFE-K8S-1007-006.md) | D10 | 10.7 | Secure AI workload decommissioning | Practitioner | ai-specific |
| [SAFE-K8S-1007-007](markdown/controls/SAFE-K8S-1007-007.md) | D10 | 10.7 | Cluster service protection from AI training resource exhaustion | Practitioner | ai-specific |
| [SAFE-K8S-1007-008](markdown/controls/SAFE-K8S-1007-008.md) | D10 | 10.7 | GPU cluster scaling governance and node onboarding security | Advanced | ai-specific |
| [SAFE-K8S-1007-009](markdown/controls/SAFE-K8S-1007-009.md) | D10 | 10.7 | Kubernetes API deprecation monitoring and usage discovery | Practitioner | ai-specific |
| [SAFE-K8S-1007-010](markdown/controls/SAFE-K8S-1007-010.md) | D10 | 10.7 | Pre-upgrade Kubernetes API compatibility testing for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1007-011](markdown/controls/SAFE-K8S-1007-011.md) | D10 | 10.7 | Kubernetes cluster upgrade planning, sequencing, and rollback governance | Practitioner | ai-specific |
| [SAFE-K8S-1007-012](markdown/controls/SAFE-K8S-1007-012.md) | D10 | 10.7 | AI infrastructure compatibility matrix and coordinated component upgrade governance | Practitioner | ai-specific |
| [SAFE-K8S-1007-013](markdown/controls/SAFE-K8S-1007-013.md) | D10 | 10.7 | Automated AI infrastructure asset discovery and continuously updated inventory | Practitioner | ai-specific |
| [SAFE-K8S-1007-014](markdown/controls/SAFE-K8S-1007-014.md) | D10 | 10.7 | AI asset classification and criticality governance for Kubernetes environments | Practitioner | ai-specific |
| [SAFE-K8S-1007-015](markdown/controls/SAFE-K8S-1007-015.md) | D10 | 10.7 | GPU node onboarding security baseline validation gates | Advanced | ai-specific |
| [SAFE-K8S-1007-016](markdown/controls/SAFE-K8S-1007-016.md) | D10 | 10.7 | GPU node hardware attestation, driver integrity, and taint verification | Advanced | ai-specific |
| [SAFE-K8S-1007-017](markdown/controls/SAFE-K8S-1007-017.md) | D10 | 10.7 | Kubernetes release-channel and changelog monitoring for API deprecations | Practitioner | ai-specific |
| [SAFE-K8S-1007-018](markdown/controls/SAFE-K8S-1007-018.md) | D10 | 10.7 | Deprecated Kubernetes API usage inventory and migration tracking for AI workloads | Practitioner | ai-specific |
