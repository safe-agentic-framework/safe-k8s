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
- Controls: 593
- Crosswalk rows: 4916

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

## Knowledge Areas

- [1.1 - Kubernetes API Server Security](#knowledge-area-1-1)
- [1.2 - etcd and Cluster State Protection](#knowledge-area-1-2)
- [1.3 - Controller-Manager, Scheduler, and Cloud Controller Security](#knowledge-area-1-3)
- [1.4 - CIS Benchmarks and Patch Management](#knowledge-area-1-4)
- [2.1 - Kubelet and Node Configuration Hardening](#knowledge-area-2-1)
- [2.2 - Container Runtime Security](#knowledge-area-2-2)
- [2.3 - Host OS and Kernel Hardening](#knowledge-area-2-3)
- [2.4 - Runtime Threat Detection](#knowledge-area-2-4)
- [2.5 - kube-proxy and Node Networking Security](#knowledge-area-2-5)
- [3.1 - Pod Security Standards and Admission](#knowledge-area-3-1)
- [3.2 - Security Contexts and Capabilities](#knowledge-area-3-2)
- [3.3 - Mandatory Access Controls](#knowledge-area-3-3)
- [3.4 - Secure Defaults and Resource Constraints](#knowledge-area-3-4)
- [4.1 - Role-Based Access Control (RBAC)](#knowledge-area-4-1)
- [4.2 - Service Accounts and Workload Identity](#knowledge-area-4-2)
- [4.3 - Secrets Management](#knowledge-area-4-3)
- [4.4 - Certificate Management](#knowledge-area-4-4)
- [4.5 - Identity Abuse Detection and Mitigation](#knowledge-area-4-5)
- [5.1 - Network Policies](#knowledge-area-5-1)
- [5.2 - CNI Plugins and Pod Networking Security](#knowledge-area-5-2)
- [5.3 - Ingress, Egress, and DNS Hardening](#knowledge-area-5-3)
- [5.4 - Zero Trust Architecture and Service Mesh](#knowledge-area-5-4)
- [5.5 - API Server and Service Exposure Protection](#knowledge-area-5-5)
- [6.1 - Container Image and Registry Security](#knowledge-area-6-1)
- [6.2 - Image Signing and Admission Enforcement](#knowledge-area-6-2)
- [6.3 - Attestation, Provenance, and Cryptographic Assurance](#knowledge-area-6-3)
- [6.4 - SBOMs and Vulnerability Intelligence](#knowledge-area-6-4)
- [6.5 - Admission Control](#knowledge-area-6-5)
- [6.6 - CI/CD and GitOps Pipeline Security](#knowledge-area-6-6)
- [7.1 - Persistent Storage Security](#knowledge-area-7-1)
- [7.2 - Namespace Isolation and Multi-Tenancy](#knowledge-area-7-2)
- [7.3 - Resource Governance and Priority](#knowledge-area-7-3)
- [7.4 - Cloud Provider Security Integration](#knowledge-area-7-4)
- [8.1 - GPU Device Plugins and Resource Allocation](#knowledge-area-8-1)
- [8.2 - GPU Driver, Library, and Toolkit Security](#knowledge-area-8-2)
- [8.3 - High-Performance Interconnect Security](#knowledge-area-8-3)
- [8.4 - Confidential Computing for AI Workloads](#knowledge-area-8-4)
- [8.5 - GPU Workload Auditing and Monitoring](#knowledge-area-8-5)
- [9.1 - Distributed Training Workload Security](#knowledge-area-9-1)
- [9.2 - Inference Server and Model Serving Security](#knowledge-area-9-2)
- [9.3 - Inference Resilience, Adversarial Defense, and Resource Controls](#knowledge-area-9-3)
- [9.4 - AI Pipeline Orchestration and Experimentation Security](#knowledge-area-9-4)
- [9.5 - AI Supply Chain and Model Lifecycle](#knowledge-area-9-5)
- [9.6 - Training Data Integrity and Poisoning Defense](#knowledge-area-9-6)
- [9.7 - Feature Store Security and Data Access Controls](#knowledge-area-9-7)
- [9.8 - Model Abuse and Extraction Prevention](#knowledge-area-9-8)
- [9.9 - RAG Infrastructure Security](#knowledge-area-9-9)
- [9.10 - Multi-Cluster and Federated AI Security](#knowledge-area-9-10)
- [10.1 - Logging and Audit](#knowledge-area-10-1)
- [10.2 - Monitoring, Metrics, and Tracing](#knowledge-area-10-2)
- [10.3 - Threat Modeling Methodologies](#knowledge-area-10-3)
- [10.4 - AI and Supply Chain Threat Taxonomy](#knowledge-area-10-4)
- [10.5 - Incident Response for Kubernetes](#knowledge-area-10-5)
- [10.6 - Compliance and Governance](#knowledge-area-10-6)
- [10.7 - Cluster Lifecycle and Asset Inventory](#knowledge-area-10-7)

<a id="knowledge-area-1-1"></a>
## 1.1 - Kubernetes API Server Security

- Domain: D01 - Control Plane and Cluster Hardening
- Maturity: Foundational
- Controls: 14

### Description

This knowledge area focuses on: Encryption at rest for Secrets and sensitive API resources, Streaming connection idle timeout enforcement, API server request rate limiting and API Priority and Fairness, API server audit policy coverage and event detail, and API server TLS enforcement. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0101-003](markdown/controls/SAFE-K8S-0101-003.md) | Encryption at rest for Secrets and sensitive API resources | Foundational | baseline |
| [SAFE-K8S-0101-005](markdown/controls/SAFE-K8S-0101-005.md) | Streaming connection idle timeout enforcement | Foundational | baseline |
| [SAFE-K8S-0101-007](markdown/controls/SAFE-K8S-0101-007.md) | API server request rate limiting and API Priority and Fairness | Practitioner | ai-specific |
| [SAFE-K8S-0101-008](markdown/controls/SAFE-K8S-0101-008.md) | API server audit policy coverage and event detail | Foundational | baseline |
| [SAFE-K8S-0101-012](markdown/controls/SAFE-K8S-0101-012.md) | API server TLS enforcement | Foundational | baseline |
| [SAFE-K8S-0101-013](markdown/controls/SAFE-K8S-0101-013.md) | API server certificate rotation and validation | Foundational | baseline |
| [SAFE-K8S-0101-014](markdown/controls/SAFE-K8S-0101-014.md) | API server authorization mode baseline enforcement | Foundational | baseline |
| [SAFE-K8S-0101-015](markdown/controls/SAFE-K8S-0101-015.md) | API server webhook authorizer endpoint trust controls | Foundational | baseline |
| [SAFE-K8S-0101-016](markdown/controls/SAFE-K8S-0101-016.md) | API server audit log backend delivery and durable storage | Foundational | baseline |
| [SAFE-K8S-0101-017](markdown/controls/SAFE-K8S-0101-017.md) | API server audit log retention enforcement | Foundational | baseline |
| [SAFE-K8S-0101-018](markdown/controls/SAFE-K8S-0101-018.md) | API server anonymous authentication disablement | Foundational | baseline |
| [SAFE-K8S-0101-019](markdown/controls/SAFE-K8S-0101-019.md) | API server AlwaysAllow prohibition | Foundational | baseline |
| [SAFE-K8S-0101-020](markdown/controls/SAFE-K8S-0101-020.md) | API server profiling and debug exposure disablement | Foundational | baseline |
| [SAFE-K8S-0101-021](markdown/controls/SAFE-K8S-0101-021.md) | API server approved admission controller chain configuration | Foundational | baseline |

<a id="knowledge-area-1-2"></a>
## 1.2 - etcd and Cluster State Protection

- Domain: D01 - Control Plane and Cluster Hardening
- Maturity: Foundational
- Controls: 16

### Description

This knowledge area focuses on: etcd storage-layer disk encryption with externally managed keys, etcd encryption key rotation scheduling and verification, etcd backup storage encryption, etcd backup integrity verification and restore assurance, and etcd health monitoring and alerting. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0102-001](markdown/controls/SAFE-K8S-0102-001.md) | etcd storage-layer disk encryption with externally managed keys | Foundational | baseline |
| [SAFE-K8S-0102-006](markdown/controls/SAFE-K8S-0102-006.md) | etcd encryption key rotation scheduling and verification | Foundational | baseline |
| [SAFE-K8S-0102-007](markdown/controls/SAFE-K8S-0102-007.md) | etcd backup storage encryption | Foundational | baseline |
| [SAFE-K8S-0102-008](markdown/controls/SAFE-K8S-0102-008.md) | etcd backup integrity verification and restore assurance | Foundational | baseline |
| [SAFE-K8S-0102-012](markdown/controls/SAFE-K8S-0102-012.md) | etcd health monitoring and alerting | Foundational | baseline |
| [SAFE-K8S-0102-013](markdown/controls/SAFE-K8S-0102-013.md) | etcd compaction and periodic defragmentation | Foundational | baseline |
| [SAFE-K8S-0102-014](markdown/controls/SAFE-K8S-0102-014.md) | etcd certificate rotation coverage and execution | Practitioner | baseline |
| [SAFE-K8S-0102-015](markdown/controls/SAFE-K8S-0102-015.md) | etcd certificate rotation testing and recovery validation | Practitioner | baseline |
| [SAFE-K8S-0102-018](markdown/controls/SAFE-K8S-0102-018.md) | etcd client and peer certificate authentication | Foundational | baseline |
| [SAFE-K8S-0102-019](markdown/controls/SAFE-K8S-0102-019.md) | etcd endpoint network isolation from worker and workload traffic | Foundational | baseline |
| [SAFE-K8S-0102-020](markdown/controls/SAFE-K8S-0102-020.md) | etcd certificate maximum validity period enforcement | Practitioner | baseline |
| [SAFE-K8S-0102-021](markdown/controls/SAFE-K8S-0102-021.md) | etcd certificate expiration monitoring and lead-time alerting | Practitioner | baseline |
| [SAFE-K8S-0102-022](markdown/controls/SAFE-K8S-0102-022.md) | etcd backup repository least-privilege access restriction | Foundational | baseline |
| [SAFE-K8S-0102-023](markdown/controls/SAFE-K8S-0102-023.md) | etcd backup break-glass authorization governance | Foundational | baseline |
| [SAFE-K8S-0102-024](markdown/controls/SAFE-K8S-0102-024.md) | etcd backup repository access audit logging | Foundational | baseline |
| [SAFE-K8S-0102-025](markdown/controls/SAFE-K8S-0102-025.md) | etcd backup repository access review and alerting | Foundational | baseline |

<a id="knowledge-area-1-3"></a>
## 1.3 - Controller-Manager, Scheduler, and Cloud Controller Security

- Domain: D01 - Control Plane and Cluster Hardening
- Maturity: Practitioner
- Controls: 13

### Description

This knowledge area focuses on: Controller-manager service account token hardening, Pod garbage collection threshold configuration, Profiling endpoint disablement for controller-manager and scheduler, Cloud controller-manager deployment isolation, and Leader election configuration and lease object RBAC. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0103-001](markdown/controls/SAFE-K8S-0103-001.md) | Controller-manager service account token hardening | Foundational | baseline |
| [SAFE-K8S-0103-005](markdown/controls/SAFE-K8S-0103-005.md) | Pod garbage collection threshold configuration | Foundational | ai-specific |
| [SAFE-K8S-0103-006](markdown/controls/SAFE-K8S-0103-006.md) | Profiling endpoint disablement for controller-manager and scheduler | Foundational | baseline |
| [SAFE-K8S-0103-008](markdown/controls/SAFE-K8S-0103-008.md) | Cloud controller-manager deployment isolation | Practitioner | baseline |
| [SAFE-K8S-0103-010](markdown/controls/SAFE-K8S-0103-010.md) | Leader election configuration and lease object RBAC | Practitioner | baseline |
| [SAFE-K8S-0103-012](markdown/controls/SAFE-K8S-0103-012.md) | Cloud controller-manager cloud IAM least-privilege scoping | Practitioner | baseline |
| [SAFE-K8S-0103-013](markdown/controls/SAFE-K8S-0103-013.md) | Cloud controller-manager workload identity and credential rotation | Practitioner | baseline |
| [SAFE-K8S-0103-014](markdown/controls/SAFE-K8S-0103-014.md) | Scheduler API and decision endpoint access restriction | Practitioner | baseline |
| [SAFE-K8S-0103-015](markdown/controls/SAFE-K8S-0103-015.md) | Scheduler extender authentication and custom scheduler approval | Practitioner | baseline |
| [SAFE-K8S-0103-016](markdown/controls/SAFE-K8S-0103-016.md) | Controller-manager and scheduler loopback bind-address enforcement | Foundational | baseline |
| [SAFE-K8S-0103-017](markdown/controls/SAFE-K8S-0103-017.md) | Controller-manager and scheduler insecure-port disablement and non-public health-metrics exposure | Foundational | baseline |
| [SAFE-K8S-0103-018](markdown/controls/SAFE-K8S-0103-018.md) | Control-plane replica distribution and etcd quorum topology | Practitioner | baseline |
| [SAFE-K8S-0103-019](markdown/controls/SAFE-K8S-0103-019.md) | API server load-balancer health-check failover | Practitioner | baseline |

<a id="knowledge-area-1-4"></a>
## 1.4 - CIS Benchmarks and Patch Management

- Domain: D01 - Control Plane and Cluster Hardening
- Maturity: Foundational
- Controls: 14

### Description

This knowledge area focuses on: Control plane configuration file permissions, Emergency Kubernetes patch deployment procedures, Feature gate lifecycle transition tracking across Kubernetes upgrades, Kubernetes upgrade strategy, validation, and rollback planning, and Recurring CIS Kubernetes Benchmark scan execution. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0104-005](markdown/controls/SAFE-K8S-0104-005.md) | Control plane configuration file permissions | Foundational | baseline |
| [SAFE-K8S-0104-007](markdown/controls/SAFE-K8S-0104-007.md) | Emergency Kubernetes patch deployment procedures | Foundational | baseline |
| [SAFE-K8S-0104-009](markdown/controls/SAFE-K8S-0104-009.md) | Feature gate lifecycle transition tracking across Kubernetes upgrades | Practitioner | baseline |
| [SAFE-K8S-0104-013](markdown/controls/SAFE-K8S-0104-013.md) | Kubernetes upgrade strategy, validation, and rollback planning | Foundational | baseline |
| [SAFE-K8S-0104-014](markdown/controls/SAFE-K8S-0104-014.md) | Recurring CIS Kubernetes Benchmark scan execution | Foundational | baseline |
| [SAFE-K8S-0104-015](markdown/controls/SAFE-K8S-0104-015.md) | CIS Benchmark result retention and posture trend reporting | Foundational | baseline |
| [SAFE-K8S-0104-016](markdown/controls/SAFE-K8S-0104-016.md) | CIS Benchmark remediation workflow tracking | Foundational | baseline |
| [SAFE-K8S-0104-017](markdown/controls/SAFE-K8S-0104-017.md) | CIS Benchmark exception approval and re-review governance | Foundational | baseline |
| [SAFE-K8S-0104-018](markdown/controls/SAFE-K8S-0104-018.md) | Kubernetes security advisory and provider bulletin monitoring | Foundational | baseline |
| [SAFE-K8S-0104-019](markdown/controls/SAFE-K8S-0104-019.md) | Kubernetes CVE risk prioritization framework | Foundational | baseline |
| [SAFE-K8S-0104-020](markdown/controls/SAFE-K8S-0104-020.md) | Kubernetes supported version window compliance | Foundational | baseline |
| [SAFE-K8S-0104-021](markdown/controls/SAFE-K8S-0104-021.md) | Kubernetes component version skew compliance | Foundational | baseline |
| [SAFE-K8S-0104-022](markdown/controls/SAFE-K8S-0104-022.md) | Non-default feature gate inventory for production clusters | Practitioner | baseline |
| [SAFE-K8S-0104-023](markdown/controls/SAFE-K8S-0104-023.md) | Stage-based approval and risk assessment for production feature gates | Practitioner | baseline |

<a id="knowledge-area-2-1"></a>
## 2.1 - Kubelet and Node Configuration Hardening

- Domain: D02 - Node, Runtime, and OS Security
- Maturity: Foundational
- Controls: 11

### Description

This knowledge area focuses on: Kubelet hostname override governance, Node system and kube reserved resource allocations, Node eviction threshold tuning for workload pressure, Kubelet configuration and credential file ownership and permissions, and Kubelet systemd unit hardening. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0201-005](markdown/controls/SAFE-K8S-0201-005.md) | Kubelet hostname override governance | Foundational | baseline |
| [SAFE-K8S-0201-006](markdown/controls/SAFE-K8S-0201-006.md) | Node system and kube reserved resource allocations | Foundational | baseline |
| [SAFE-K8S-0201-007](markdown/controls/SAFE-K8S-0201-007.md) | Node eviction threshold tuning for workload pressure | Foundational | baseline |
| [SAFE-K8S-0201-008](markdown/controls/SAFE-K8S-0201-008.md) | Kubelet configuration and credential file ownership and permissions | Foundational | baseline |
| [SAFE-K8S-0201-009](markdown/controls/SAFE-K8S-0201-009.md) | Kubelet systemd unit hardening | Foundational | baseline |
| [SAFE-K8S-0201-011](markdown/controls/SAFE-K8S-0201-011.md) | Kubelet webhook authentication and authorization enforcement | Foundational | baseline |
| [SAFE-K8S-0201-012](markdown/controls/SAFE-K8S-0201-012.md) | Kubelet anonymous access and read-only port lockdown | Foundational | baseline |
| [SAFE-K8S-0201-013](markdown/controls/SAFE-K8S-0201-013.md) | Kubelet client certificate rotation via TLS bootstrap | Foundational | baseline |
| [SAFE-K8S-0201-014](markdown/controls/SAFE-K8S-0201-014.md) | Kubelet serving certificate trust and expiry enforcement | Foundational | baseline |
| [SAFE-K8S-0201-015](markdown/controls/SAFE-K8S-0201-015.md) | Node-level kubelet audit rule coverage | Foundational | baseline |
| [SAFE-K8S-0201-016](markdown/controls/SAFE-K8S-0201-016.md) | Node audit log forwarding and centralized reviewability | Foundational | baseline |

<a id="knowledge-area-2-2"></a>
## 2.2 - Container Runtime Security

- Domain: D02 - Node, Runtime, and OS Security
- Maturity: Foundational
- Controls: 8

### Description

This knowledge area focuses on: RuntimeClass configuration for workload-appropriate isolation, Container runtime patching and version management, Runtime socket mount prevention, Container runtime user namespace isolation, and Container runtime socket root-only protection. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0202-002](markdown/controls/SAFE-K8S-0202-002.md) | RuntimeClass configuration for workload-appropriate isolation | Foundational | ai-specific |
| [SAFE-K8S-0202-003](markdown/controls/SAFE-K8S-0202-003.md) | Container runtime patching and version management | Foundational | baseline |
| [SAFE-K8S-0202-004](markdown/controls/SAFE-K8S-0202-004.md) | Runtime socket mount prevention | Foundational | baseline |
| [SAFE-K8S-0202-007](markdown/controls/SAFE-K8S-0202-007.md) | Container runtime user namespace isolation | Foundational | baseline |
| [SAFE-K8S-0202-008](markdown/controls/SAFE-K8S-0202-008.md) | Container runtime socket root-only protection | Foundational | baseline |
| [SAFE-K8S-0202-009](markdown/controls/SAFE-K8S-0202-009.md) | Container runtime secure baseline settings and debug endpoint disablement | Foundational | baseline |
| [SAFE-K8S-0202-010](markdown/controls/SAFE-K8S-0202-010.md) | Node default seccomp profile enforcement | Foundational | baseline |
| [SAFE-K8S-0202-011](markdown/controls/SAFE-K8S-0202-011.md) | Node mandatory access control activation for container workloads | Foundational | baseline |

<a id="knowledge-area-2-3"></a>
## 2.3 - Host OS and Kernel Hardening

- Domain: D02 - Node, Runtime, and OS Security
- Maturity: Foundational
- Controls: 11

### Description

This knowledge area focuses on: Kernel parameter hardening via sysctl, Secure boot and verified boot chain enforcement, Pod metadata endpoint network path blocking, Workload identity replacement for cloud API access, and Minimal purpose-built node OS baseline. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0203-002](markdown/controls/SAFE-K8S-0203-002.md) | Kernel parameter hardening via sysctl | Foundational | baseline |
| [SAFE-K8S-0203-004](markdown/controls/SAFE-K8S-0203-004.md) | Secure boot and verified boot chain enforcement | Foundational | baseline |
| [SAFE-K8S-0203-008](markdown/controls/SAFE-K8S-0203-008.md) | Pod metadata endpoint network path blocking | Foundational | baseline |
| [SAFE-K8S-0203-009](markdown/controls/SAFE-K8S-0203-009.md) | Workload identity replacement for cloud API access | Foundational | baseline |
| [SAFE-K8S-0203-010](markdown/controls/SAFE-K8S-0203-010.md) | Minimal purpose-built node OS baseline | Foundational | baseline |
| [SAFE-K8S-0203-011](markdown/controls/SAFE-K8S-0203-011.md) | Immutable node root filesystem enforcement | Foundational | baseline |
| [SAFE-K8S-0203-012](markdown/controls/SAFE-K8S-0203-012.md) | Kernel module restriction and approved module whitelisting | Foundational | baseline |
| [SAFE-K8S-0203-013](markdown/controls/SAFE-K8S-0203-013.md) | Kernel lockdown mode enforcement for runtime integrity | Foundational | baseline |
| [SAFE-K8S-0203-014](markdown/controls/SAFE-K8S-0203-014.md) | Authenticated cloud metadata service mode enforcement | Foundational | baseline |
| [SAFE-K8S-0203-015](markdown/controls/SAFE-K8S-0203-015.md) | Cloud metadata endpoint restriction settings | Foundational | baseline |
| [SAFE-K8S-0203-016](markdown/controls/SAFE-K8S-0203-016.md) | Node time synchronization with authoritative time sources | Foundational | baseline |

<a id="knowledge-area-2-4"></a>
## 2.4 - Runtime Threat Detection

- Domain: D02 - Node, Runtime, and OS Security
- Maturity: Practitioner
- Controls: 4

### Description

This knowledge area focuses on: Runtime security tool deployment for syscall and network monitoring, Kubernetes-specific runtime detection rules, Container filesystem drift detection, and Forensic capture capabilities for container incident investigation.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0204-001](markdown/controls/SAFE-K8S-0204-001.md) | Runtime security tool deployment for syscall and network monitoring | Practitioner | baseline |
| [SAFE-K8S-0204-002](markdown/controls/SAFE-K8S-0204-002.md) | Kubernetes-specific runtime detection rules | Practitioner | baseline |
| [SAFE-K8S-0204-003](markdown/controls/SAFE-K8S-0204-003.md) | Container filesystem drift detection | Practitioner | baseline |
| [SAFE-K8S-0204-004](markdown/controls/SAFE-K8S-0204-004.md) | Forensic capture capabilities for container incident investigation | Practitioner | baseline |

<a id="knowledge-area-2-5"></a>
## 2.5 - kube-proxy and Node Networking Security

- Domain: D02 - Node, Runtime, and OS Security
- Maturity: Practitioner
- Controls: 8

### Description

This knowledge area focuses on: NodePort and HostPort restriction policies, eBPF-based kernel-level network policy enforcement, eBPF program integrity verification and loading monitoring, Node firewall compatibility validation with CNI and network policy, and kube-proxy or service proxy mode selection governance. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0205-002](markdown/controls/SAFE-K8S-0205-002.md) | NodePort and HostPort restriction policies | Practitioner | baseline |
| [SAFE-K8S-0205-004](markdown/controls/SAFE-K8S-0205-004.md) | eBPF-based kernel-level network policy enforcement | Practitioner | baseline |
| [SAFE-K8S-0205-005](markdown/controls/SAFE-K8S-0205-005.md) | eBPF program integrity verification and loading monitoring | Practitioner | baseline |
| [SAFE-K8S-0205-007](markdown/controls/SAFE-K8S-0205-007.md) | Node firewall compatibility validation with CNI and network policy | Practitioner | baseline |
| [SAFE-K8S-0205-008](markdown/controls/SAFE-K8S-0205-008.md) | kube-proxy or service proxy mode selection governance | Practitioner | baseline |
| [SAFE-K8S-0205-009](markdown/controls/SAFE-K8S-0205-009.md) | Service proxy path hardening for kube-proxy or replacements | Practitioner | baseline |
| [SAFE-K8S-0205-010](markdown/controls/SAFE-K8S-0205-010.md) | Node-level firewall rule restriction for cluster communication | Practitioner | baseline |
| [SAFE-K8S-0205-011](markdown/controls/SAFE-K8S-0205-011.md) | Node firewall audit and change governance | Practitioner | baseline |

<a id="knowledge-area-3-1"></a>
## 3.1 - Pod Security Standards and Admission

- Domain: D03 - Workload and Pod Security
- Maturity: Foundational
- Controls: 5

### Description

This knowledge area focuses on: Pod Security Standards level assignment, Pod Security Admission configuration and version pinning, PodSecurityPolicy to PSA migration, PSA exemption register and justification tracking, and Scoped PSA exception enforcement and compensating controls.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0301-001](markdown/controls/SAFE-K8S-0301-001.md) | Pod Security Standards level assignment | Foundational | baseline |
| [SAFE-K8S-0301-002](markdown/controls/SAFE-K8S-0301-002.md) | Pod Security Admission configuration and version pinning | Foundational | baseline |
| [SAFE-K8S-0301-003](markdown/controls/SAFE-K8S-0301-003.md) | PodSecurityPolicy to PSA migration | Foundational | baseline |
| [SAFE-K8S-0301-005](markdown/controls/SAFE-K8S-0301-005.md) | PSA exemption register and justification tracking | Foundational | ai-specific |
| [SAFE-K8S-0301-006](markdown/controls/SAFE-K8S-0301-006.md) | Scoped PSA exception enforcement and compensating controls | Foundational | ai-specific |

<a id="knowledge-area-3-2"></a>
## 3.2 - Security Contexts and Capabilities

- Domain: D03 - Workload and Pod Security
- Maturity: Foundational
- Controls: 6

### Description

This knowledge area focuses on: Pod and container security context enforcement, Linux capability drop-all and least-privilege add-back, Host namespace isolation enforcement, AI workload security context hardening profiles, and No-new-privileges execution enforcement. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0302-001](markdown/controls/SAFE-K8S-0302-001.md) | Pod and container security context enforcement | Foundational | baseline |
| [SAFE-K8S-0302-002](markdown/controls/SAFE-K8S-0302-002.md) | Linux capability drop-all and least-privilege add-back | Foundational | ai-specific |
| [SAFE-K8S-0302-004](markdown/controls/SAFE-K8S-0302-004.md) | Host namespace isolation enforcement | Foundational | baseline |
| [SAFE-K8S-0302-005](markdown/controls/SAFE-K8S-0302-005.md) | AI workload security context hardening profiles | Foundational | ai-specific |
| [SAFE-K8S-0302-006](markdown/controls/SAFE-K8S-0302-006.md) | No-new-privileges execution enforcement | Foundational | baseline |
| [SAFE-K8S-0302-007](markdown/controls/SAFE-K8S-0302-007.md) | Safe fsGroup and supplementalGroups volume ownership | Foundational | baseline |

<a id="knowledge-area-3-3"></a>
## 3.3 - Mandatory Access Controls

- Domain: D03 - Workload and Pod Security
- Maturity: Practitioner
- Controls: 7

### Description

This knowledge area focuses on: Seccomp profile enforcement, SELinux context assignment and multi-tenancy isolation, MAC profile generation from runtime behavior, MAC profile pre-enforcement audit-mode validation, and MAC profile iterative refinement cycle. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0303-001](markdown/controls/SAFE-K8S-0303-001.md) | Seccomp profile enforcement | Practitioner | baseline |
| [SAFE-K8S-0303-003](markdown/controls/SAFE-K8S-0303-003.md) | SELinux context assignment and multi-tenancy isolation | Practitioner | baseline |
| [SAFE-K8S-0303-004](markdown/controls/SAFE-K8S-0303-004.md) | MAC profile generation from runtime behavior | Practitioner | baseline |
| [SAFE-K8S-0303-005](markdown/controls/SAFE-K8S-0303-005.md) | MAC profile pre-enforcement audit-mode validation | Practitioner | baseline |
| [SAFE-K8S-0303-006](markdown/controls/SAFE-K8S-0303-006.md) | MAC profile iterative refinement cycle | Practitioner | baseline |
| [SAFE-K8S-0303-007](markdown/controls/SAFE-K8S-0303-007.md) | AppArmor profile distribution and node readiness | Practitioner | baseline |
| [SAFE-K8S-0303-008](markdown/controls/SAFE-K8S-0303-008.md) | AppArmor workload profile assignment and unconfined-mode restriction | Practitioner | baseline |

<a id="knowledge-area-3-4"></a>
## 3.4 - Secure Defaults and Resource Constraints

- Domain: D03 - Workload and Pod Security
- Maturity: Foundational
- Controls: 9

### Description

This knowledge area focuses on: QoS class assignment for workload stability, Ephemeral container security context enforcement, Host volume mount restriction, Service account token automount opt-out, and Temporary checkpoint storage encryption, integrity, and access control. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0304-003](markdown/controls/SAFE-K8S-0304-003.md) | QoS class assignment for workload stability | Foundational | baseline |
| [SAFE-K8S-0304-004](markdown/controls/SAFE-K8S-0304-004.md) | Ephemeral container security context enforcement | Foundational | baseline |
| [SAFE-K8S-0304-006](markdown/controls/SAFE-K8S-0304-006.md) | Host volume mount restriction | Foundational | baseline |
| [SAFE-K8S-0304-007](markdown/controls/SAFE-K8S-0304-007.md) | Service account token automount opt-out | Foundational | baseline |
| [SAFE-K8S-0304-009](markdown/controls/SAFE-K8S-0304-009.md) | Temporary checkpoint storage encryption, integrity, and access control | Foundational | ai-specific |
| [SAFE-K8S-0304-010](markdown/controls/SAFE-K8S-0304-010.md) | Pod resource requests and limits specification | Foundational | baseline |
| [SAFE-K8S-0304-011](markdown/controls/SAFE-K8S-0304-011.md) | Namespace LimitRange and ResourceQuota enforcement | Foundational | baseline |
| [SAFE-K8S-0304-012](markdown/controls/SAFE-K8S-0304-012.md) | Training scratch volume size limits and ephemeral-storage quotas | Foundational | baseline |
| [SAFE-K8S-0304-013](markdown/controls/SAFE-K8S-0304-013.md) | Tmpfs-backed handling for sensitive training intermediates | Foundational | baseline |

<a id="knowledge-area-4-1"></a>
## 4.1 - Role-Based Access Control (RBAC)

- Domain: D04 - Identity, Access, and Secrets Management
- Maturity: Foundational
- Controls: 6

### Description

This knowledge area focuses on: RBAC least-privilege design, RBAC permission audit and analysis, Aggregated ClusterRole governance, RBAC for AI operator custom resources, and Organizational role separation for ML, platform, and security functions. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0401-001](markdown/controls/SAFE-K8S-0401-001.md) | RBAC least-privilege design | Foundational | baseline |
| [SAFE-K8S-0401-002](markdown/controls/SAFE-K8S-0401-002.md) | RBAC permission audit and analysis | Foundational | baseline |
| [SAFE-K8S-0401-003](markdown/controls/SAFE-K8S-0401-003.md) | Aggregated ClusterRole governance | Foundational | baseline |
| [SAFE-K8S-0401-004](markdown/controls/SAFE-K8S-0401-004.md) | RBAC for AI operator custom resources | Foundational | ai-specific |
| [SAFE-K8S-0401-006](markdown/controls/SAFE-K8S-0401-006.md) | Organizational role separation for ML, platform, and security functions | Foundational | ai-specific |
| [SAFE-K8S-0401-007](markdown/controls/SAFE-K8S-0401-007.md) | GPU resource governance permission boundaries | Foundational | ai-specific |

<a id="knowledge-area-4-2"></a>
## 4.2 - Service Accounts and Workload Identity

- Domain: D04 - Identity, Access, and Secrets Management
- Maturity: Practitioner
- Controls: 18

### Description

This knowledge area focuses on: Inactive service account and stale credential remediation, Service account identifier exposure prevention, Workload identity attribute integrity, Cloud workload identity federation for AI services, and OIDC authentication integration. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0402-002](markdown/controls/SAFE-K8S-0402-002.md) | Inactive service account and stale credential remediation | Practitioner | baseline |
| [SAFE-K8S-0402-003](markdown/controls/SAFE-K8S-0402-003.md) | Service account identifier exposure prevention | Practitioner | baseline |
| [SAFE-K8S-0402-004](markdown/controls/SAFE-K8S-0402-004.md) | Workload identity attribute integrity | Practitioner | baseline |
| [SAFE-K8S-0402-006](markdown/controls/SAFE-K8S-0402-006.md) | Cloud workload identity federation for AI services | Practitioner | ai-specific |
| [SAFE-K8S-0402-007](markdown/controls/SAFE-K8S-0402-007.md) | OIDC authentication integration | Practitioner | baseline |
| [SAFE-K8S-0402-008](markdown/controls/SAFE-K8S-0402-008.md) | Distinct identity assignment for AI workload types | Practitioner | ai-specific |
| [SAFE-K8S-0402-010](markdown/controls/SAFE-K8S-0402-010.md) | Cross-cluster and cross-cloud cryptographic identity federation | Advanced | ai-specific |
| [SAFE-K8S-0402-011](markdown/controls/SAFE-K8S-0402-011.md) | Cross-environment static credential prohibition | Advanced | ai-specific |
| [SAFE-K8S-0402-012](markdown/controls/SAFE-K8S-0402-012.md) | Ephemeral training job credential expiration | Practitioner | ai-specific |
| [SAFE-K8S-0402-013](markdown/controls/SAFE-K8S-0402-013.md) | Ephemeral training job credential rotation | Practitioner | ai-specific |
| [SAFE-K8S-0402-014](markdown/controls/SAFE-K8S-0402-014.md) | Ephemeral training job credential revocation on completion | Practitioner | ai-specific |
| [SAFE-K8S-0402-015](markdown/controls/SAFE-K8S-0402-015.md) | Legacy service account token secret removal | Foundational | baseline |
| [SAFE-K8S-0402-018](markdown/controls/SAFE-K8S-0402-018.md) | Default service account disablement and token automount hardening | Foundational | baseline |
| [SAFE-K8S-0402-019](markdown/controls/SAFE-K8S-0402-019.md) | Dedicated workload service accounts and least-privilege assignment | Foundational | baseline |
| [SAFE-K8S-0402-020](markdown/controls/SAFE-K8S-0402-020.md) | Projected service account token issuance path enforcement | Foundational | baseline |
| [SAFE-K8S-0402-021](markdown/controls/SAFE-K8S-0402-021.md) | Workload token explicit audience binding | Foundational | baseline |
| [SAFE-K8S-0402-022](markdown/controls/SAFE-K8S-0402-022.md) | Projected service account token lifetime bounds enforcement | Foundational | baseline |
| [SAFE-K8S-0402-023](markdown/controls/SAFE-K8S-0402-023.md) | Long-lived workload token exception governance and retirement tracking | Foundational | baseline |

<a id="knowledge-area-4-3"></a>
## 4.3 - Secrets Management

- Domain: D04 - Identity, Access, and Secrets Management
- Maturity: Foundational
- Controls: 20

### Description

This knowledge area focuses on: External secrets management integration, Approved secret injection pattern standards, Secret rotation and expiration enforcement, AI pipeline secret leakage prevention, and Per-workload credential scoping for AI jobs. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0403-002](markdown/controls/SAFE-K8S-0403-002.md) | External secrets management integration | Foundational | baseline |
| [SAFE-K8S-0403-003](markdown/controls/SAFE-K8S-0403-003.md) | Approved secret injection pattern standards | Foundational | baseline |
| [SAFE-K8S-0403-004](markdown/controls/SAFE-K8S-0403-004.md) | Secret rotation and expiration enforcement | Foundational | baseline |
| [SAFE-K8S-0403-005](markdown/controls/SAFE-K8S-0403-005.md) | AI pipeline secret leakage prevention | Foundational | ai-specific |
| [SAFE-K8S-0403-006](markdown/controls/SAFE-K8S-0403-006.md) | Per-workload credential scoping for AI jobs | Practitioner | ai-specific |
| [SAFE-K8S-0403-011](markdown/controls/SAFE-K8S-0403-011.md) | Secrets KMS key rotation and re-encryption verification | Foundational | baseline |
| [SAFE-K8S-0403-017](markdown/controls/SAFE-K8S-0403-017.md) | AI platform key-domain hierarchy and envelope encryption architecture | Foundational | baseline |
| [SAFE-K8S-0403-018](markdown/controls/SAFE-K8S-0403-018.md) | AI platform cryptographic key access domain separation | Foundational | baseline |
| [SAFE-K8S-0403-019](markdown/controls/SAFE-K8S-0403-019.md) | Kubernetes Secrets external KMS provider integration | Foundational | baseline |
| [SAFE-K8S-0403-020](markdown/controls/SAFE-K8S-0403-020.md) | Kubernetes Secrets KMS key least-privilege access policy | Foundational | baseline |
| [SAFE-K8S-0403-021](markdown/controls/SAFE-K8S-0403-021.md) | Automated AI workload credential inventory | Practitioner | ai-specific |
| [SAFE-K8S-0403-022](markdown/controls/SAFE-K8S-0403-022.md) | Orphaned AI workload credential detection and remediation | Practitioner | ai-specific |
| [SAFE-K8S-0403-023](markdown/controls/SAFE-K8S-0403-023.md) | Credential scope drift monitoring for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0403-024](markdown/controls/SAFE-K8S-0403-024.md) | Credential lifecycle metrics publication and governance | Practitioner | ai-specific |
| [SAFE-K8S-0403-025](markdown/controls/SAFE-K8S-0403-025.md) | Automated secret leak detection coverage across development and runtime surfaces | Practitioner | baseline |
| [SAFE-K8S-0403-026](markdown/controls/SAFE-K8S-0403-026.md) | Secret leak prevention gate and enforcement controls | Practitioner | baseline |
| [SAFE-K8S-0403-027](markdown/controls/SAFE-K8S-0403-027.md) | Secret leak incident triage and containment workflow | Practitioner | baseline |
| [SAFE-K8S-0403-028](markdown/controls/SAFE-K8S-0403-028.md) | Exposed credential revocation and replacement execution | Practitioner | baseline |
| [SAFE-K8S-0403-029](markdown/controls/SAFE-K8S-0403-029.md) | Environment variable secret injection prohibition enforcement | Foundational | baseline |
| [SAFE-K8S-0403-030](markdown/controls/SAFE-K8S-0403-030.md) | Environment variable secret injection exception governance | Foundational | baseline |

<a id="knowledge-area-4-4"></a>
## 4.4 - Certificate Management

- Domain: D04 - Identity, Access, and Secrets Management
- Maturity: Practitioner
- Controls: 7

### Description

This knowledge area focuses on: cert-manager deployment and Issuer configuration, TLS provisioning for webhooks, API aggregation, and internal services, mTLS for service-to-service authentication, Automated certificate rotation before expiry, and Certificate expiry monitoring and alerting. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0404-001](markdown/controls/SAFE-K8S-0404-001.md) | cert-manager deployment and Issuer configuration | Practitioner | baseline |
| [SAFE-K8S-0404-002](markdown/controls/SAFE-K8S-0404-002.md) | TLS provisioning for webhooks, API aggregation, and internal services | Practitioner | baseline |
| [SAFE-K8S-0404-003](markdown/controls/SAFE-K8S-0404-003.md) | mTLS for service-to-service authentication | Practitioner | baseline |
| [SAFE-K8S-0404-007](markdown/controls/SAFE-K8S-0404-007.md) | Automated certificate rotation before expiry | Practitioner | baseline |
| [SAFE-K8S-0404-008](markdown/controls/SAFE-K8S-0404-008.md) | Certificate expiry monitoring and alerting | Practitioner | baseline |
| [SAFE-K8S-0404-009](markdown/controls/SAFE-K8S-0404-009.md) | Compromised certificate revocation and re-issuance execution | Practitioner | baseline |
| [SAFE-K8S-0404-010](markdown/controls/SAFE-K8S-0404-010.md) | Post-compromise certificate recovery validation | Practitioner | baseline |

<a id="knowledge-area-4-5"></a>
## 4.5 - Identity Abuse Detection and Mitigation

- Domain: D04 - Identity, Access, and Secrets Management
- Maturity: Practitioner
- Controls: 16

### Description

This knowledge area focuses on: Privilege escalation detection and monitoring, Kubeconfig security and hygiene, Security awareness for Kubernetes and GPU administrators, Attribute-based access control for AI artifacts, and Authentication endpoint availability and DoS protection. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0405-002](markdown/controls/SAFE-K8S-0405-002.md) | Privilege escalation detection and monitoring | Practitioner | baseline |
| [SAFE-K8S-0405-003](markdown/controls/SAFE-K8S-0405-003.md) | Kubeconfig security and hygiene | Practitioner | baseline |
| [SAFE-K8S-0405-004](markdown/controls/SAFE-K8S-0405-004.md) | Security awareness for Kubernetes and GPU administrators | Practitioner | baseline |
| [SAFE-K8S-0405-006](markdown/controls/SAFE-K8S-0405-006.md) | Attribute-based access control for AI artifacts | Advanced | ai-specific |
| [SAFE-K8S-0405-007](markdown/controls/SAFE-K8S-0405-007.md) | Authentication endpoint availability and DoS protection | Practitioner | baseline |
| [SAFE-K8S-0405-009](markdown/controls/SAFE-K8S-0405-009.md) | API impersonation RBAC restriction | Practitioner | baseline |
| [SAFE-K8S-0405-010](markdown/controls/SAFE-K8S-0405-010.md) | API impersonation audit logging and alerting | Practitioner | baseline |
| [SAFE-K8S-0405-012](markdown/controls/SAFE-K8S-0405-012.md) | Privileged MFA enforcement for cluster administration | Practitioner | baseline |
| [SAFE-K8S-0405-017](markdown/controls/SAFE-K8S-0405-017.md) | Credential policy baseline requirements | Practitioner | baseline |
| [SAFE-K8S-0405-018](markdown/controls/SAFE-K8S-0405-018.md) | Secure credential storage and lifecycle governance | Practitioner | baseline |
| [SAFE-K8S-0405-019](markdown/controls/SAFE-K8S-0405-019.md) | Break-glass recovery procedure definition | Practitioner | baseline |
| [SAFE-K8S-0405-020](markdown/controls/SAFE-K8S-0405-020.md) | Break-glass recovery exercise validation | Practitioner | baseline |
| [SAFE-K8S-0405-021](markdown/controls/SAFE-K8S-0405-021.md) | Break-glass activation multi-party approval enforcement | Practitioner | baseline |
| [SAFE-K8S-0405-022](markdown/controls/SAFE-K8S-0405-022.md) | Tenant-scoped break-glass credential boundary enforcement | Practitioner | baseline |
| [SAFE-K8S-0405-023](markdown/controls/SAFE-K8S-0405-023.md) | Break-glass access audit logging coverage | Practitioner | baseline |
| [SAFE-K8S-0405-024](markdown/controls/SAFE-K8S-0405-024.md) | Break-glass credential automatic expiration and revocation enforcement | Practitioner | baseline |

<a id="knowledge-area-5-1"></a>
## 5.1 - Network Policies

- Domain: D05 - Network Security and Communication
- Maturity: Foundational
- Controls: 8

### Description

This knowledge area focuses on: Default deny ingress and egress network policies, Namespace network isolation patterns, Workload egress controls, CNI-specific network policy extensions, and Multi-cluster network segmentation for federated AI workloads. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0501-001](markdown/controls/SAFE-K8S-0501-001.md) | Default deny ingress and egress network policies | Foundational | baseline |
| [SAFE-K8S-0501-002](markdown/controls/SAFE-K8S-0501-002.md) | Namespace network isolation patterns | Foundational | baseline |
| [SAFE-K8S-0501-003](markdown/controls/SAFE-K8S-0501-003.md) | Workload egress controls | Foundational | baseline |
| [SAFE-K8S-0501-004](markdown/controls/SAFE-K8S-0501-004.md) | CNI-specific network policy extensions | Practitioner | baseline |
| [SAFE-K8S-0501-006](markdown/controls/SAFE-K8S-0501-006.md) | Multi-cluster network segmentation for federated AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0501-007](markdown/controls/SAFE-K8S-0501-007.md) | East-west AI workload traffic monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0501-008](markdown/controls/SAFE-K8S-0501-008.md) | AI workload type network microsegmentation | Foundational | ai-specific |
| [SAFE-K8S-0501-009](markdown/controls/SAFE-K8S-0501-009.md) | Model download path isolation from training data paths | Foundational | ai-specific |

<a id="knowledge-area-5-2"></a>
## 5.2 - CNI Plugins and Pod Networking Security

- Domain: D05 - Network Security and Communication
- Maturity: Practitioner
- Controls: 8

### Description

This knowledge area focuses on: CNI plugin security selection criteria, Pod-to-pod traffic encryption, CNI plugin hardening and lifecycle management, AI workload data path encryption in transit, and Kubernetes pod IP anti-spoofing enforcement and validation. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0502-001](markdown/controls/SAFE-K8S-0502-001.md) | CNI plugin security selection criteria | Practitioner | baseline |
| [SAFE-K8S-0502-002](markdown/controls/SAFE-K8S-0502-002.md) | Pod-to-pod traffic encryption | Practitioner | baseline |
| [SAFE-K8S-0502-004](markdown/controls/SAFE-K8S-0502-004.md) | CNI plugin hardening and lifecycle management | Practitioner | baseline |
| [SAFE-K8S-0502-005](markdown/controls/SAFE-K8S-0502-005.md) | AI workload data path encryption in transit | Practitioner | ai-specific |
| [SAFE-K8S-0502-007](markdown/controls/SAFE-K8S-0502-007.md) | Kubernetes pod IP anti-spoofing enforcement and validation | Practitioner | baseline |
| [SAFE-K8S-0502-008](markdown/controls/SAFE-K8S-0502-008.md) | Network policy design for AI-specific traffic patterns | Practitioner | ai-specific |
| [SAFE-K8S-0502-009](markdown/controls/SAFE-K8S-0502-009.md) | Kubernetes CNI IPAM capacity sizing | Practitioner | baseline |
| [SAFE-K8S-0502-010](markdown/controls/SAFE-K8S-0502-010.md) | Kubernetes CNI IP pool exhaustion monitoring and alerting | Practitioner | baseline |

<a id="knowledge-area-5-3"></a>
## 5.3 - Ingress, Egress, and DNS Hardening

- Domain: D05 - Network Security and Communication
- Maturity: Practitioner
- Controls: 11

### Description

This knowledge area focuses on: Internal load balancer annotation enforcement, DNS exfiltration detection, Cloud load balancer security group configuration, Ingress TLS termination and boundary configuration hardening, and CoreDNS and upstream resolver hardening. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0503-004](markdown/controls/SAFE-K8S-0503-004.md) | Internal load balancer annotation enforcement | Practitioner | baseline |
| [SAFE-K8S-0503-005](markdown/controls/SAFE-K8S-0503-005.md) | DNS exfiltration detection | Practitioner | baseline |
| [SAFE-K8S-0503-006](markdown/controls/SAFE-K8S-0503-006.md) | Cloud load balancer security group configuration | Practitioner | baseline |
| [SAFE-K8S-0503-007](markdown/controls/SAFE-K8S-0503-007.md) | Ingress TLS termination and boundary configuration hardening | Practitioner | baseline |
| [SAFE-K8S-0503-009](markdown/controls/SAFE-K8S-0503-009.md) | CoreDNS and upstream resolver hardening | Practitioner | baseline |
| [SAFE-K8S-0503-011](markdown/controls/SAFE-K8S-0503-011.md) | External traffic policy mode selection and tradeoff governance | Practitioner | baseline |
| [SAFE-K8S-0503-012](markdown/controls/SAFE-K8S-0503-012.md) | Client source IP preservation for external services | Practitioner | baseline |
| [SAFE-K8S-0503-013](markdown/controls/SAFE-K8S-0503-013.md) | Ingress web application firewall integration and request filtering | Practitioner | baseline |
| [SAFE-K8S-0503-014](markdown/controls/SAFE-K8S-0503-014.md) | Ingress rate limiting and abuse throttling | Practitioner | baseline |
| [SAFE-K8S-0503-015](markdown/controls/SAFE-K8S-0503-015.md) | Approved DNS resolution path enforcement | Practitioner | baseline |
| [SAFE-K8S-0503-016](markdown/controls/SAFE-K8S-0503-016.md) | Namespace-scoped DNS service discovery restriction | Practitioner | baseline |

<a id="knowledge-area-5-4"></a>
## 5.4 - Zero Trust Architecture and Service Mesh

- Domain: D05 - Network Security and Communication
- Maturity: Practitioner
- Controls: 7

### Description

This knowledge area focuses on: Zero trust networking principles for Kubernetes, Service mesh mTLS and authorization policies, Service mesh tuning for AI workloads, SPIFFE/SPIRE workload identity issuance and lifecycle management, and SPIFFE trust domain scoping and cross-cluster federation governance. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0504-001](markdown/controls/SAFE-K8S-0504-001.md) | Zero trust networking principles for Kubernetes | Practitioner | baseline |
| [SAFE-K8S-0504-002](markdown/controls/SAFE-K8S-0504-002.md) | Service mesh mTLS and authorization policies | Practitioner | baseline |
| [SAFE-K8S-0504-005](markdown/controls/SAFE-K8S-0504-005.md) | Service mesh tuning for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0504-006](markdown/controls/SAFE-K8S-0504-006.md) | SPIFFE/SPIRE workload identity issuance and lifecycle management | Advanced | baseline |
| [SAFE-K8S-0504-007](markdown/controls/SAFE-K8S-0504-007.md) | SPIFFE trust domain scoping and cross-cluster federation governance | Advanced | baseline |
| [SAFE-K8S-0504-008](markdown/controls/SAFE-K8S-0504-008.md) | L7 service authorization policy enforcement | Practitioner | baseline |
| [SAFE-K8S-0504-009](markdown/controls/SAFE-K8S-0504-009.md) | API-aware request contract validation | Practitioner | baseline |

<a id="knowledge-area-5-5"></a>
## 5.5 - API Server and Service Exposure Protection

- Domain: D05 - Network Security and Communication
- Maturity: Practitioner
- Controls: 6

### Description

This knowledge area focuses on: LoadBalancer, NodePort, and ExternalIP restriction policies, Internal service endpoint protection, API server audit log analysis for network-based attack detection, Identity-based internal service access control, and API server private endpoint and authorized network enforcement. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0505-002](markdown/controls/SAFE-K8S-0505-002.md) | LoadBalancer, NodePort, and ExternalIP restriction policies | Practitioner | baseline |
| [SAFE-K8S-0505-003](markdown/controls/SAFE-K8S-0505-003.md) | Internal service endpoint protection | Practitioner | baseline |
| [SAFE-K8S-0505-004](markdown/controls/SAFE-K8S-0505-004.md) | API server audit log analysis for network-based attack detection | Practitioner | baseline |
| [SAFE-K8S-0505-005](markdown/controls/SAFE-K8S-0505-005.md) | Identity-based internal service access control | Practitioner | baseline |
| [SAFE-K8S-0505-006](markdown/controls/SAFE-K8S-0505-006.md) | API server private endpoint and authorized network enforcement | Practitioner | baseline |
| [SAFE-K8S-0505-007](markdown/controls/SAFE-K8S-0505-007.md) | Administrative API server access path via bastion or VPN | Practitioner | baseline |

<a id="knowledge-area-6-1"></a>
## 6.1 - Container Image and Registry Security

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Practitioner
- Controls: 14

### Description

This knowledge area focuses on: AI GPU and ML framework base image validation, CI/CD build-time container image vulnerability scanning, Artifact retention period and lifecycle enforcement, Integrity metadata co-retention with software artifacts, and Container image runtime hardening with non-root and read-only filesystem. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0601-007](markdown/controls/SAFE-K8S-0601-007.md) | AI GPU and ML framework base image validation | Practitioner | ai-specific |
| [SAFE-K8S-0601-008](markdown/controls/SAFE-K8S-0601-008.md) | CI/CD build-time container image vulnerability scanning | Practitioner | ai-specific |
| [SAFE-K8S-0601-010](markdown/controls/SAFE-K8S-0601-010.md) | Artifact retention period and lifecycle enforcement | Practitioner | baseline |
| [SAFE-K8S-0601-011](markdown/controls/SAFE-K8S-0601-011.md) | Integrity metadata co-retention with software artifacts | Practitioner | baseline |
| [SAFE-K8S-0601-014](markdown/controls/SAFE-K8S-0601-014.md) | Container image runtime hardening with non-root and read-only filesystem | Practitioner | ai-specific |
| [SAFE-K8S-0601-015](markdown/controls/SAFE-K8S-0601-015.md) | Inference image minimal composition with GPU runtime-only dependencies | Practitioner | ai-specific |
| [SAFE-K8S-0601-016](markdown/controls/SAFE-K8S-0601-016.md) | Approved minimal base image catalog enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0601-017](markdown/controls/SAFE-K8S-0601-017.md) | Multi-stage build and stripped runtime image minimization | Practitioner | ai-specific |
| [SAFE-K8S-0601-018](markdown/controls/SAFE-K8S-0601-018.md) | Registry push-time container image vulnerability rescanning | Practitioner | ai-specific |
| [SAFE-K8S-0601-019](markdown/controls/SAFE-K8S-0601-019.md) | Runtime container vulnerability exposure monitoring and exception governance | Practitioner | ai-specific |
| [SAFE-K8S-0601-020](markdown/controls/SAFE-K8S-0601-020.md) | Container registry authentication and role-based authorization | Practitioner | baseline |
| [SAFE-K8S-0601-021](markdown/controls/SAFE-K8S-0601-021.md) | Container registry trusted-source network restriction | Practitioner | baseline |
| [SAFE-K8S-0601-022](markdown/controls/SAFE-K8S-0601-022.md) | Kubernetes image pull secret distribution and external secret integration | Practitioner | baseline |
| [SAFE-K8S-0601-023](markdown/controls/SAFE-K8S-0601-023.md) | Image pull credential automatic rotation and expiry reduction | Practitioner | baseline |

<a id="knowledge-area-6-2"></a>
## 6.2 - Image Signing and Admission Enforcement

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Advanced
- Controls: 5

### Description

This knowledge area focuses on: Sigstore/cosign keyless signing and Rekor transparency logging, Notary v2 trust policy and signing identity governance, Notary v2 OCI signature artifact registry integration, Fail-closed admission enforcement of image signature verification, and Admission signature bypass and emergency break-glass governance.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0602-001](markdown/controls/SAFE-K8S-0602-001.md) | Sigstore/cosign keyless signing and Rekor transparency logging | Practitioner | baseline |
| [SAFE-K8S-0602-004](markdown/controls/SAFE-K8S-0602-004.md) | Notary v2 trust policy and signing identity governance | Practitioner | baseline |
| [SAFE-K8S-0602-005](markdown/controls/SAFE-K8S-0602-005.md) | Notary v2 OCI signature artifact registry integration | Practitioner | baseline |
| [SAFE-K8S-0602-006](markdown/controls/SAFE-K8S-0602-006.md) | Fail-closed admission enforcement of image signature verification | Practitioner | baseline |
| [SAFE-K8S-0602-007](markdown/controls/SAFE-K8S-0602-007.md) | Admission signature bypass and emergency break-glass governance | Practitioner | baseline |

<a id="knowledge-area-6-3"></a>
## 6.3 - Attestation, Provenance, and Cryptographic Assurance

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Advanced
- Controls: 10

### Description

This knowledge area focuses on: Cryptographic agility and post-quantum readiness, FIPS 140 cryptographic module validation, TUF-based secure software update systems, Build environment and process attestations per NIST SP 800-204D, and Build materials and artifact attestations per NIST SP 800-204D. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0603-004](markdown/controls/SAFE-K8S-0603-004.md) | Cryptographic agility and post-quantum readiness | Advanced | ai-specific |
| [SAFE-K8S-0603-005](markdown/controls/SAFE-K8S-0603-005.md) | FIPS 140 cryptographic module validation | Practitioner | baseline |
| [SAFE-K8S-0603-006](markdown/controls/SAFE-K8S-0603-006.md) | TUF-based secure software update systems | Advanced | baseline |
| [SAFE-K8S-0603-007](markdown/controls/SAFE-K8S-0603-007.md) | Build environment and process attestations per NIST SP 800-204D | Advanced | baseline |
| [SAFE-K8S-0603-008](markdown/controls/SAFE-K8S-0603-008.md) | Build materials and artifact attestations per NIST SP 800-204D | Advanced | baseline |
| [SAFE-K8S-0603-009](markdown/controls/SAFE-K8S-0603-009.md) | In-toto and SLSA provenance attestation generation | Advanced | baseline |
| [SAFE-K8S-0603-010](markdown/controls/SAFE-K8S-0603-010.md) | SBOM attestation binding to image digests | Advanced | baseline |
| [SAFE-K8S-0603-011](markdown/controls/SAFE-K8S-0603-011.md) | Attestation policy definition, signing, and change governance | Advanced | baseline |
| [SAFE-K8S-0603-013](markdown/controls/SAFE-K8S-0603-013.md) | Lifecycle attestation chain verification across build, promote, and deploy | Advanced | baseline |
| [SAFE-K8S-0603-014](markdown/controls/SAFE-K8S-0603-014.md) | Fail-closed admission enforcement for attestation requirements | Advanced | baseline |

<a id="knowledge-area-6-4"></a>
## 6.4 - SBOMs and Vulnerability Intelligence

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Practitioner
- Controls: 11

### Description

This knowledge area focuses on: SBOM generation for container and AI artifacts, ML-BOM (ML Bill of Materials) generation, SBOM storage and distribution as OCI artifacts, VEX (Vulnerability Exploitability eXchange) publication, and Third-party component security requirements documentation. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0604-001](markdown/controls/SAFE-K8S-0604-001.md) | SBOM generation for container and AI artifacts | Practitioner | ai-specific |
| [SAFE-K8S-0604-002](markdown/controls/SAFE-K8S-0604-002.md) | ML-BOM (ML Bill of Materials) generation | Practitioner | ai-specific |
| [SAFE-K8S-0604-003](markdown/controls/SAFE-K8S-0604-003.md) | SBOM storage and distribution as OCI artifacts | Practitioner | baseline |
| [SAFE-K8S-0604-004](markdown/controls/SAFE-K8S-0604-004.md) | VEX (Vulnerability Exploitability eXchange) publication | Practitioner | baseline |
| [SAFE-K8S-0604-007](markdown/controls/SAFE-K8S-0604-007.md) | Third-party component security requirements documentation | Practitioner | baseline |
| [SAFE-K8S-0604-008](markdown/controls/SAFE-K8S-0604-008.md) | AI workload vulnerability exposure classification | Practitioner | ai-specific |
| [SAFE-K8S-0604-009](markdown/controls/SAFE-K8S-0604-009.md) | AI workload vulnerability prioritization and remediation SLAs | Practitioner | ai-specific |
| [SAFE-K8S-0604-010](markdown/controls/SAFE-K8S-0604-010.md) | Automated AI workload rebuild and redeployment patch pipelines | Practitioner | ai-specific |
| [SAFE-K8S-0604-011](markdown/controls/SAFE-K8S-0604-011.md) | SLSA provenance generation and target-level governance | Practitioner | baseline |
| [SAFE-K8S-0604-013](markdown/controls/SAFE-K8S-0604-013.md) | Hermetic build execution and pinned dependency input control | Practitioner | baseline |
| [SAFE-K8S-0604-014](markdown/controls/SAFE-K8S-0604-014.md) | Source-to-artifact integrity linkage for built images | Practitioner | baseline |

<a id="knowledge-area-6-5"></a>
## 6.5 - Admission Control

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Practitioner
- Controls: 8

### Description

This knowledge area focuses on: OPA/Gatekeeper policies for Kubernetes and AI workloads, Kyverno admission policies, Kubewarden WebAssembly-based admission policies, Pod Security Admission enforcement for AI workload namespaces, and Admission webhook fail-closed enforcement and timeout bounds. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0605-001](markdown/controls/SAFE-K8S-0605-001.md) | OPA/Gatekeeper policies for Kubernetes and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0605-002](markdown/controls/SAFE-K8S-0605-002.md) | Kyverno admission policies | Practitioner | baseline |
| [SAFE-K8S-0605-003](markdown/controls/SAFE-K8S-0605-003.md) | Kubewarden WebAssembly-based admission policies | Practitioner | baseline |
| [SAFE-K8S-0605-006](markdown/controls/SAFE-K8S-0605-006.md) | Pod Security Admission enforcement for AI workload namespaces | Practitioner | baseline |
| [SAFE-K8S-0605-007](markdown/controls/SAFE-K8S-0605-007.md) | Admission webhook fail-closed enforcement and timeout bounds | Practitioner | baseline |
| [SAFE-K8S-0605-008](markdown/controls/SAFE-K8S-0605-008.md) | Admission webhook TLS rotation and high-availability resilience | Practitioner | baseline |
| [SAFE-K8S-0605-009](markdown/controls/SAFE-K8S-0605-009.md) | AI custom resource validation and policy constraint enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0605-010](markdown/controls/SAFE-K8S-0605-010.md) | AI custom resource webhook abuse resistance and resource hardening | Practitioner | ai-specific |

<a id="knowledge-area-6-6"></a>
## 6.6 - CI/CD and GitOps Pipeline Security

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Practitioner
- Controls: 22

### Description

This knowledge area focuses on: CI/CD build environment hardening, CI/CD build activity monitoring, SSDF v1.1 alignment for secure development practices, CI build-time security gate enforcement, and CNCF lifecycle phase security coverage. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0606-002](markdown/controls/SAFE-K8S-0606-002.md) | CI/CD build environment hardening | Practitioner | baseline |
| [SAFE-K8S-0606-007](markdown/controls/SAFE-K8S-0606-007.md) | CI/CD build activity monitoring | Practitioner | baseline |
| [SAFE-K8S-0606-009](markdown/controls/SAFE-K8S-0606-009.md) | SSDF v1.1 alignment for secure development practices | Practitioner | baseline |
| [SAFE-K8S-0606-011](markdown/controls/SAFE-K8S-0606-011.md) | CI build-time security gate enforcement | Practitioner | baseline |
| [SAFE-K8S-0606-017](markdown/controls/SAFE-K8S-0606-017.md) | CNCF lifecycle phase security coverage | Practitioner | baseline |
| [SAFE-K8S-0606-018](markdown/controls/SAFE-K8S-0606-018.md) | Zero-trust CI/CD handoff verification and independent evidence generation | Practitioner | baseline |
| [SAFE-K8S-0606-019](markdown/controls/SAFE-K8S-0606-019.md) | Helm chart provenance and signature verification | Practitioner | baseline |
| [SAFE-K8S-0606-020](markdown/controls/SAFE-K8S-0606-020.md) | Helm values override restriction and dependency integrity governance | Practitioner | baseline |
| [SAFE-K8S-0606-021](markdown/controls/SAFE-K8S-0606-021.md) | Kubernetes manifest cryptographic signing before deployment | Advanced | baseline |
| [SAFE-K8S-0606-022](markdown/controls/SAFE-K8S-0606-022.md) | Admission-time verification of Kubernetes manifest signatures | Advanced | baseline |
| [SAFE-K8S-0606-023](markdown/controls/SAFE-K8S-0606-023.md) | IaC security scanning gate enforcement for deployment platforms | Practitioner | baseline |
| [SAFE-K8S-0606-024](markdown/controls/SAFE-K8S-0606-024.md) | Policy-as-code and runtime configuration integrity governance | Practitioner | baseline |
| [SAFE-K8S-0606-025](markdown/controls/SAFE-K8S-0606-025.md) | Artifact freshness limit enforcement for CI/CD promotion | Practitioner | baseline |
| [SAFE-K8S-0606-026](markdown/controls/SAFE-K8S-0606-026.md) | Automated SCM security posture assessment before promotion reliance | Practitioner | baseline |
| [SAFE-K8S-0606-027](markdown/controls/SAFE-K8S-0606-027.md) | GitOps repository access restriction and least-privilege deploy credentials | Practitioner | baseline |
| [SAFE-K8S-0606-028](markdown/controls/SAFE-K8S-0606-028.md) | GitOps commit signing and protected deployment branch governance | Practitioner | baseline |
| [SAFE-K8S-0606-029](markdown/controls/SAFE-K8S-0606-029.md) | GitOps deployed package and version metadata retention | Practitioner | baseline |
| [SAFE-K8S-0606-030](markdown/controls/SAFE-K8S-0606-030.md) | GitOps configuration revision and deployment history traceability | Practitioner | baseline |
| [SAFE-K8S-0606-031](markdown/controls/SAFE-K8S-0606-031.md) | GitOps reconciliation health and integrity monitoring | Practitioner | baseline |
| [SAFE-K8S-0606-032](markdown/controls/SAFE-K8S-0606-032.md) | GitOps drift detection and automated resync or notification | Practitioner | baseline |
| [SAFE-K8S-0606-033](markdown/controls/SAFE-K8S-0606-033.md) | Git-only production deployment path enforcement | Practitioner | baseline |
| [SAFE-K8S-0606-034](markdown/controls/SAFE-K8S-0606-034.md) | Emergency direct-access audit logging and justification governance | Practitioner | baseline |

<a id="knowledge-area-7-1"></a>
## 7.1 - Persistent Storage Security

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Maturity: Practitioner
- Controls: 8

### Description

This knowledge area focuses on: PersistentVolume and PersistentVolumeClaim access mode enforcement, CSI driver security and privilege restriction, Encryption at rest for persistent volumes, PV reclaim policy enforcement for AI data volumes, and Dual authorization for retained AI data volume destruction. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0701-001](markdown/controls/SAFE-K8S-0701-001.md) | PersistentVolume and PersistentVolumeClaim access mode enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0701-002](markdown/controls/SAFE-K8S-0701-002.md) | CSI driver security and privilege restriction | Practitioner | baseline |
| [SAFE-K8S-0701-003](markdown/controls/SAFE-K8S-0701-003.md) | Encryption at rest for persistent volumes | Foundational | baseline |
| [SAFE-K8S-0701-004](markdown/controls/SAFE-K8S-0701-004.md) | PV reclaim policy enforcement for AI data volumes | Practitioner | ai-specific |
| [SAFE-K8S-0701-006](markdown/controls/SAFE-K8S-0701-006.md) | Dual authorization for retained AI data volume destruction | Advanced | ai-specific |
| [SAFE-K8S-0701-007](markdown/controls/SAFE-K8S-0701-007.md) | High-performance AI storage backend hardening | Advanced | ai-specific |
| [SAFE-K8S-0701-008](markdown/controls/SAFE-K8S-0701-008.md) | Training data and model artifact version tracking for reproducibility | Advanced | ai-specific |
| [SAFE-K8S-0701-009](markdown/controls/SAFE-K8S-0701-009.md) | Immutable storage protection for training data and model artifacts | Advanced | ai-specific |

<a id="knowledge-area-7-2"></a>
## 7.2 - Namespace Isolation and Multi-Tenancy

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Maturity: Practitioner
- Controls: 20

### Description

This knowledge area focuses on: LimitRange enforcement for containers and pods, Label and annotation schema definition for AI workload classification, Admission control enforcement of workload classification label requirements, Virtual cluster deployment for high-isolation multi-tenant Kubernetes environments, and Tenant default-deny inter-namespace network isolation. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0702-003](markdown/controls/SAFE-K8S-0702-003.md) | LimitRange enforcement for containers and pods | Foundational | baseline |
| [SAFE-K8S-0702-005](markdown/controls/SAFE-K8S-0702-005.md) | Label and annotation schema definition for AI workload classification | Practitioner | ai-specific |
| [SAFE-K8S-0702-009](markdown/controls/SAFE-K8S-0702-009.md) | Admission control enforcement of workload classification label requirements | Practitioner | ai-specific |
| [SAFE-K8S-0702-010](markdown/controls/SAFE-K8S-0702-010.md) | Virtual cluster deployment for high-isolation multi-tenant Kubernetes environments | Advanced | baseline |
| [SAFE-K8S-0702-013](markdown/controls/SAFE-K8S-0702-013.md) | Tenant default-deny inter-namespace network isolation | Practitioner | baseline |
| [SAFE-K8S-0702-016](markdown/controls/SAFE-K8S-0702-016.md) | Classification metadata preservation across model lifecycle stages | Practitioner | ai-specific |
| [SAFE-K8S-0702-018](markdown/controls/SAFE-K8S-0702-018.md) | Namespace tenant boundary model and isolation limitation documentation | Practitioner | baseline |
| [SAFE-K8S-0702-019](markdown/controls/SAFE-K8S-0702-019.md) | Supplementary namespace isolation control enforcement for multi-tenant AI clusters | Practitioner | baseline |
| [SAFE-K8S-0702-020](markdown/controls/SAFE-K8S-0702-020.md) | Namespace ResourceQuota enforcement for GPU and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0702-021](markdown/controls/SAFE-K8S-0702-021.md) | Namespace quota utilization monitoring and exhaustion alerting for GPU and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0702-022](markdown/controls/SAFE-K8S-0702-022.md) | Virtual cluster isolation guarantee and residual risk documentation | Advanced | baseline |
| [SAFE-K8S-0702-023](markdown/controls/SAFE-K8S-0702-023.md) | Virtual cluster tenant isolation validation and host-cluster access review | Advanced | baseline |
| [SAFE-K8S-0702-024](markdown/controls/SAFE-K8S-0702-024.md) | Tenant namespace-scoped RBAC boundary enforcement | Practitioner | baseline |
| [SAFE-K8S-0702-025](markdown/controls/SAFE-K8S-0702-025.md) | Tenant admission boundary enforcement for cross-tenant resource isolation | Practitioner | baseline |
| [SAFE-K8S-0702-026](markdown/controls/SAFE-K8S-0702-026.md) | Pipeline data classification taxonomy definition | Practitioner | ai-specific |
| [SAFE-K8S-0702-027](markdown/controls/SAFE-K8S-0702-027.md) | Pipeline classification label application, propagation, and coverage verification | Practitioner | ai-specific |
| [SAFE-K8S-0702-028](markdown/controls/SAFE-K8S-0702-028.md) | Classification-driven admission policy enforcement for pipeline resources | Practitioner | ai-specific |
| [SAFE-K8S-0702-029](markdown/controls/SAFE-K8S-0702-029.md) | Classification-driven storage and network restriction enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0702-030](markdown/controls/SAFE-K8S-0702-030.md) | Promotion-time automatic classification uplift and reclassification execution | Practitioner | ai-specific |
| [SAFE-K8S-0702-031](markdown/controls/SAFE-K8S-0702-031.md) | Production promotion gate enforcement on validated classification metadata | Practitioner | ai-specific |

<a id="knowledge-area-7-3"></a>
## 7.3 - Resource Governance and Priority

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Maturity: Practitioner
- Controls: 17

### Description

This knowledge area focuses on: Pod Disruption Budgets for workload availability, AI workload resource exhaustion guardrails, Fair-share GPU queue management for multi-tenant clusters, Idle GPU detection and resource reclamation, and GPU spending limits and budget enforcement. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0703-002](markdown/controls/SAFE-K8S-0703-002.md) | Pod Disruption Budgets for workload availability | Foundational | baseline |
| [SAFE-K8S-0703-005](markdown/controls/SAFE-K8S-0703-005.md) | AI workload resource exhaustion guardrails | Practitioner | ai-specific |
| [SAFE-K8S-0703-007](markdown/controls/SAFE-K8S-0703-007.md) | Fair-share GPU queue management for multi-tenant clusters | Practitioner | ai-specific |
| [SAFE-K8S-0703-008](markdown/controls/SAFE-K8S-0703-008.md) | Idle GPU detection and resource reclamation | Practitioner | ai-specific |
| [SAFE-K8S-0703-009](markdown/controls/SAFE-K8S-0703-009.md) | GPU spending limits and budget enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0703-010](markdown/controls/SAFE-K8S-0703-010.md) | Host-level resource isolation for AI workload nodes | Practitioner | ai-specific |
| [SAFE-K8S-0703-012](markdown/controls/SAFE-K8S-0703-012.md) | Node affinity rules, taints, and tolerations for AI workload isolation | Practitioner | ai-specific |
| [SAFE-K8S-0703-013](markdown/controls/SAFE-K8S-0703-013.md) | Topology-aware scheduling for GPU locality with blast-radius containment | Practitioner | ai-specific |
| [SAFE-K8S-0703-014](markdown/controls/SAFE-K8S-0703-014.md) | EDoS spending guardrails and autoscaling limits for AI resources | Advanced | ai-specific |
| [SAFE-K8S-0703-015](markdown/controls/SAFE-K8S-0703-015.md) | Chaos engineering validation for AI resource governance controls | Advanced | ai-specific |
| [SAFE-K8S-0703-016](markdown/controls/SAFE-K8S-0703-016.md) | AI workload PriorityClass hierarchy and preemption protection | Practitioner | ai-specific |
| [SAFE-K8S-0703-017](markdown/controls/SAFE-K8S-0703-017.md) | PriorityClass assignment restriction and admission enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0703-018](markdown/controls/SAFE-K8S-0703-018.md) | GPU cost attribution metering and billing correlation | Practitioner | ai-specific |
| [SAFE-K8S-0703-019](markdown/controls/SAFE-K8S-0703-019.md) | GPU chargeback and showback reporting accountability | Practitioner | ai-specific |
| [SAFE-K8S-0703-021](markdown/controls/SAFE-K8S-0703-021.md) | GPU admission enforcement against unauthorized access and quota bypass | Practitioner | ai-specific |
| [SAFE-K8S-0703-022](markdown/controls/SAFE-K8S-0703-022.md) | GPU abuse pattern monitoring and detection for Kubernetes AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0703-023](markdown/controls/SAFE-K8S-0703-023.md) | Investigation and termination of confirmed unauthorized GPU workloads | Practitioner | ai-specific |

<a id="knowledge-area-7-4"></a>
## 7.4 - Cloud Provider Security Integration

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Maturity: Practitioner
- Controls: 14

### Description

This knowledge area focuses on: VPC and security group integration with Kubernetes network policies, IMDSv2 enforcement on Kubernetes nodes, Restricted use policies for non-organizationally owned systems and external AI services, Cloud provider contingency plans for managed Kubernetes services, and Cloud-to-Kubernetes event correlation for incident investigation. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0704-002](markdown/controls/SAFE-K8S-0704-002.md) | VPC and security group integration with Kubernetes network policies | Practitioner | baseline |
| [SAFE-K8S-0704-004](markdown/controls/SAFE-K8S-0704-004.md) | IMDSv2 enforcement on Kubernetes nodes | Foundational | baseline |
| [SAFE-K8S-0704-005](markdown/controls/SAFE-K8S-0704-005.md) | Restricted use policies for non-organizationally owned systems and external AI services | Practitioner | ai-specific |
| [SAFE-K8S-0704-006](markdown/controls/SAFE-K8S-0704-006.md) | Cloud provider contingency plans for managed Kubernetes services | Practitioner | ai-specific |
| [SAFE-K8S-0704-008](markdown/controls/SAFE-K8S-0704-008.md) | Cloud-to-Kubernetes event correlation for incident investigation | Practitioner | baseline |
| [SAFE-K8S-0704-011](markdown/controls/SAFE-K8S-0704-011.md) | Network-level blocking of cloud metadata endpoint access for pods | Foundational | baseline |
| [SAFE-K8S-0704-013](markdown/controls/SAFE-K8S-0704-013.md) | Unified cloud and Kubernetes audit source onboarding | Practitioner | baseline |
| [SAFE-K8S-0704-014](markdown/controls/SAFE-K8S-0704-014.md) | Managed Kubernetes audit log retention enforcement | Practitioner | baseline |
| [SAFE-K8S-0704-015](markdown/controls/SAFE-K8S-0704-015.md) | Cloud IAM to Kubernetes RBAC entitlement mapping definition | Practitioner | baseline |
| [SAFE-K8S-0704-016](markdown/controls/SAFE-K8S-0704-016.md) | Cloud IAM to Kubernetes RBAC mapping review and drift remediation | Practitioner | baseline |
| [SAFE-K8S-0704-017](markdown/controls/SAFE-K8S-0704-017.md) | Least-privilege cloud-to-cluster privileged access boundary enforcement | Practitioner | baseline |
| [SAFE-K8S-0704-018](markdown/controls/SAFE-K8S-0704-018.md) | Break-glass cloud identity governance for Kubernetes administration | Practitioner | baseline |
| [SAFE-K8S-0704-019](markdown/controls/SAFE-K8S-0704-019.md) | Per-workload cloud identity binding for managed Kubernetes workloads | Foundational | baseline |
| [SAFE-K8S-0704-020](markdown/controls/SAFE-K8S-0704-020.md) | Node-level cloud identity restriction for managed Kubernetes workloads | Foundational | baseline |

<a id="knowledge-area-8-1"></a>
## 8.1 - GPU Device Plugins and Resource Allocation

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Maturity: Advanced
- Controls: 10

### Description

This knowledge area focuses on: GPU device plugin security configuration and hardening, MIG partitioning for hardware-enforced GPU isolation, vGPU virtualization security controls, GPU memory clearing between workload transitions, and GPU topology metadata protection and node label visibility restriction. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0801-001](markdown/controls/SAFE-K8S-0801-001.md) | GPU device plugin security configuration and hardening | Practitioner | ai-specific |
| [SAFE-K8S-0801-002](markdown/controls/SAFE-K8S-0801-002.md) | MIG partitioning for hardware-enforced GPU isolation | Advanced | ai-specific |
| [SAFE-K8S-0801-004](markdown/controls/SAFE-K8S-0801-004.md) | vGPU virtualization security controls | Practitioner | ai-specific |
| [SAFE-K8S-0801-006](markdown/controls/SAFE-K8S-0801-006.md) | GPU memory clearing between workload transitions | Advanced | ai-specific |
| [SAFE-K8S-0801-009](markdown/controls/SAFE-K8S-0801-009.md) | GPU topology metadata protection and node label visibility restriction | Practitioner | ai-specific |
| [SAFE-K8S-0801-010](markdown/controls/SAFE-K8S-0801-010.md) | Admission validation of authorized GPU resource requests | Practitioner | ai-specific |
| [SAFE-K8S-0801-011](markdown/controls/SAFE-K8S-0801-011.md) | MPS and time-slicing residual-risk acceptance and compensating control approval | Advanced | ai-specific |
| [SAFE-K8S-0801-012](markdown/controls/SAFE-K8S-0801-012.md) | MPS and time-slicing workload eligibility and same-trust co-location enforcement | Advanced | ai-specific |
| [SAFE-K8S-0801-013](markdown/controls/SAFE-K8S-0801-013.md) | MPS and time-slicing memory remnant prevention verification | Advanced | ai-specific |
| [SAFE-K8S-0801-014](markdown/controls/SAFE-K8S-0801-014.md) | MPS and time-slicing side-channel risk assessment | Advanced | ai-specific |

<a id="knowledge-area-8-2"></a>
## 8.2 - GPU Driver, Library, and Toolkit Security

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Maturity: Advanced
- Controls: 7

### Description

This knowledge area focuses on: GPU driver lifecycle and vulnerability management, CUDA library and container toolkit security, GPU firmware integrity monitoring, Device plugin socket directory access restriction and unauthorized socket access monitoring, and Device plugin registration authentication monitoring and rogue plugin detection. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0802-001](markdown/controls/SAFE-K8S-0802-001.md) | GPU driver lifecycle and vulnerability management | Practitioner | ai-specific |
| [SAFE-K8S-0802-002](markdown/controls/SAFE-K8S-0802-002.md) | CUDA library and container toolkit security | Advanced | ai-specific |
| [SAFE-K8S-0802-004](markdown/controls/SAFE-K8S-0802-004.md) | GPU firmware integrity monitoring | Advanced | ai-specific |
| [SAFE-K8S-0802-006](markdown/controls/SAFE-K8S-0802-006.md) | Device plugin socket directory access restriction and unauthorized socket access monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0802-007](markdown/controls/SAFE-K8S-0802-007.md) | Device plugin registration authentication monitoring and rogue plugin detection | Practitioner | ai-specific |
| [SAFE-K8S-0802-008](markdown/controls/SAFE-K8S-0802-008.md) | GPU kernel module signing and Secure Boot enforcement | Advanced | ai-specific |
| [SAFE-K8S-0802-009](markdown/controls/SAFE-K8S-0802-009.md) | GPU driver binary path file integrity monitoring | Advanced | ai-specific |

<a id="knowledge-area-8-3"></a>
## 8.3 - High-Performance Interconnect Security

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Maturity: Advanced
- Controls: 5

### Description

This knowledge area focuses on: NVLink and NVSwitch traffic isolation for multi-GPU training, InfiniBand and RoCE fabric security controls, RDMA memory region and queue pair isolation, DPU and SmartNIC firmware cryptographic verification and Secure Boot integrity, and DPU and SmartNIC host trust boundary definition and policy engine administrative restriction.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0803-001](markdown/controls/SAFE-K8S-0803-001.md) | NVLink and NVSwitch traffic isolation for multi-GPU training | Advanced | ai-specific |
| [SAFE-K8S-0803-002](markdown/controls/SAFE-K8S-0803-002.md) | InfiniBand and RoCE fabric security controls | Advanced | ai-specific |
| [SAFE-K8S-0803-003](markdown/controls/SAFE-K8S-0803-003.md) | RDMA memory region and queue pair isolation | Advanced | ai-specific |
| [SAFE-K8S-0803-005](markdown/controls/SAFE-K8S-0803-005.md) | DPU and SmartNIC firmware cryptographic verification and Secure Boot integrity | Advanced | ai-specific |
| [SAFE-K8S-0803-006](markdown/controls/SAFE-K8S-0803-006.md) | DPU and SmartNIC host trust boundary definition and policy engine administrative restriction | Advanced | ai-specific |

<a id="knowledge-area-8-4"></a>
## 8.4 - Confidential Computing for AI Workloads

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Maturity: Advanced
- Controls: 5

### Description

This knowledge area focuses on: TEE-based model and data protection for AI workloads, Remote attestation for TEE integrity verification, Confidential AI workload operational constraints and risk assessment, Attestation-conditioned enclave key release, and Sealed storage binding of encrypted AI artifacts to enclave measurements.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0804-001](markdown/controls/SAFE-K8S-0804-001.md) | TEE-based model and data protection for AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0804-002](markdown/controls/SAFE-K8S-0804-002.md) | Remote attestation for TEE integrity verification | Advanced | ai-specific |
| [SAFE-K8S-0804-004](markdown/controls/SAFE-K8S-0804-004.md) | Confidential AI workload operational constraints and risk assessment | Advanced | ai-specific |
| [SAFE-K8S-0804-005](markdown/controls/SAFE-K8S-0804-005.md) | Attestation-conditioned enclave key release | Advanced | ai-specific |
| [SAFE-K8S-0804-006](markdown/controls/SAFE-K8S-0804-006.md) | Sealed storage binding of encrypted AI artifacts to enclave measurements | Advanced | ai-specific |

<a id="knowledge-area-8-5"></a>
## 8.5 - GPU Workload Auditing and Monitoring

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Maturity: Advanced
- Controls: 4

### Description

This knowledge area focuses on: GPU telemetry collection and anomaly detection, GPU allocation audit trail and workload identity tracking, GPU-based attack detection for cryptomining and memory scraping, and GPU side-channel attack awareness and mitigation.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0805-001](markdown/controls/SAFE-K8S-0805-001.md) | GPU telemetry collection and anomaly detection | Practitioner | ai-specific |
| [SAFE-K8S-0805-002](markdown/controls/SAFE-K8S-0805-002.md) | GPU allocation audit trail and workload identity tracking | Practitioner | ai-specific |
| [SAFE-K8S-0805-003](markdown/controls/SAFE-K8S-0805-003.md) | GPU-based attack detection for cryptomining and memory scraping | Advanced | ai-specific |
| [SAFE-K8S-0805-004](markdown/controls/SAFE-K8S-0805-004.md) | GPU side-channel attack awareness and mitigation | Advanced | ai-specific |

<a id="knowledge-area-9-1"></a>
## 9.1 - Distributed Training Workload Security

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 9

### Description

This knowledge area focuses on: Parameter server and all-reduce security, Checkpoint security, Training fault tolerance and security, Federated learning security on Kubernetes, and Gang scheduling security (Volcano, Kueue). Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0901-002](markdown/controls/SAFE-K8S-0901-002.md) | Parameter server and all-reduce security | Advanced | ai-specific |
| [SAFE-K8S-0901-003](markdown/controls/SAFE-K8S-0901-003.md) | Checkpoint security | Practitioner | ai-specific |
| [SAFE-K8S-0901-004](markdown/controls/SAFE-K8S-0901-004.md) | Training fault tolerance and security | Practitioner | ai-specific |
| [SAFE-K8S-0901-005](markdown/controls/SAFE-K8S-0901-005.md) | Federated learning security on Kubernetes | Advanced | ai-specific |
| [SAFE-K8S-0901-006](markdown/controls/SAFE-K8S-0901-006.md) | Gang scheduling security (Volcano, Kueue) | Practitioner | ai-specific |
| [SAFE-K8S-0901-007](markdown/controls/SAFE-K8S-0901-007.md) | AI operator privilege management | Practitioner | ai-specific |
| [SAFE-K8S-0901-008](markdown/controls/SAFE-K8S-0901-008.md) | Training job network isolation | Practitioner | ai-specific |
| [SAFE-K8S-0901-009](markdown/controls/SAFE-K8S-0901-009.md) | Multi-node training worker mutual authentication | Practitioner | ai-specific |
| [SAFE-K8S-0901-010](markdown/controls/SAFE-K8S-0901-010.md) | Encrypted inter-worker gradient transport | Practitioner | ai-specific |

<a id="knowledge-area-9-2"></a>
## 9.2 - Inference Server and Model Serving Security

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 10

### Description

This knowledge area focuses on: Inference server hardening, Model loading integrity verification, Inference request validation and input sanitization, Multi-model serving isolation and encryption, and Multi-cluster inference routing and failover security. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0902-001](markdown/controls/SAFE-K8S-0902-001.md) | Inference server hardening | Practitioner | ai-specific |
| [SAFE-K8S-0902-002](markdown/controls/SAFE-K8S-0902-002.md) | Model loading integrity verification | Practitioner | ai-specific |
| [SAFE-K8S-0902-003](markdown/controls/SAFE-K8S-0902-003.md) | Inference request validation and input sanitization | Practitioner | ai-specific |
| [SAFE-K8S-0902-004](markdown/controls/SAFE-K8S-0902-004.md) | Multi-model serving isolation and encryption | Practitioner | ai-specific |
| [SAFE-K8S-0902-005](markdown/controls/SAFE-K8S-0902-005.md) | Multi-cluster inference routing and failover security | Practitioner | ai-specific |
| [SAFE-K8S-0902-006](markdown/controls/SAFE-K8S-0902-006.md) | LLM serving configuration security | Practitioner | ai-specific |
| [SAFE-K8S-0902-008](markdown/controls/SAFE-K8S-0902-008.md) | Inference endpoint authentication and authorization | Practitioner | ai-specific |
| [SAFE-K8S-0902-009](markdown/controls/SAFE-K8S-0902-009.md) | Inference response filtering and output controls | Practitioner | ai-specific |
| [SAFE-K8S-0902-010](markdown/controls/SAFE-K8S-0902-010.md) | Infrastructure-layer prompt injection classification and instruction boundary enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0902-011](markdown/controls/SAFE-K8S-0902-011.md) | Streaming token-level output leakage and policy-violation filtering | Practitioner | ai-specific |

<a id="knowledge-area-9-3"></a>
## 9.3 - Inference Resilience, Adversarial Defense, and Resource Controls

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 6

### Description

This knowledge area focuses on: Adversarial example defenses at the serving layer, Inference-time resource controls, LLM context window and token resource controls, Inference request queue priority, timeout, and depth controls, and GPU inference autoscaling replica bounds and stabilization enforcement. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0903-001](markdown/controls/SAFE-K8S-0903-001.md) | Adversarial example defenses at the serving layer | Practitioner | ai-specific |
| [SAFE-K8S-0903-003](markdown/controls/SAFE-K8S-0903-003.md) | Inference-time resource controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-004](markdown/controls/SAFE-K8S-0903-004.md) | LLM context window and token resource controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-006](markdown/controls/SAFE-K8S-0903-006.md) | Inference request queue priority, timeout, and depth controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-007](markdown/controls/SAFE-K8S-0903-007.md) | GPU inference autoscaling replica bounds and stabilization enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0903-008](markdown/controls/SAFE-K8S-0903-008.md) | Budget-aware inference autoscaling suppression and degraded-service fallback | Practitioner | ai-specific |

<a id="knowledge-area-9-4"></a>
## 9.4 - AI Pipeline Orchestration and Experimentation Security

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 12

### Description

This knowledge area focuses on: Pipeline orchestrator hardening, Notebook and experimentation environment security, Scheduled feature computation job hardening, Feature freshness and integrity monitoring, and Pipeline stage isolation between sensitivity levels. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0904-001](markdown/controls/SAFE-K8S-0904-001.md) | Pipeline orchestrator hardening | Practitioner | ai-specific |
| [SAFE-K8S-0904-003](markdown/controls/SAFE-K8S-0904-003.md) | Notebook and experimentation environment security | Practitioner | ai-specific |
| [SAFE-K8S-0904-007](markdown/controls/SAFE-K8S-0904-007.md) | Scheduled feature computation job hardening | Practitioner | ai-specific |
| [SAFE-K8S-0904-008](markdown/controls/SAFE-K8S-0904-008.md) | Feature freshness and integrity monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0904-011](markdown/controls/SAFE-K8S-0904-011.md) | Pipeline stage isolation between sensitivity levels | Practitioner | ai-specific |
| [SAFE-K8S-0904-012](markdown/controls/SAFE-K8S-0904-012.md) | Cross-classification pipeline data transfer authorization gates | Practitioner | ai-specific |
| [SAFE-K8S-0904-013](markdown/controls/SAFE-K8S-0904-013.md) | Pipeline artifact storage encryption and object-store access policy enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0904-014](markdown/controls/SAFE-K8S-0904-014.md) | Pipeline stage-scoped artifact access and retention governance | Practitioner | ai-specific |
| [SAFE-K8S-0904-015](markdown/controls/SAFE-K8S-0904-015.md) | Experiment tracking metadata access control and tenant visibility enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0904-016](markdown/controls/SAFE-K8S-0904-016.md) | Experiment tracking access and modification audit logging | Practitioner | ai-specific |
| [SAFE-K8S-0904-017](markdown/controls/SAFE-K8S-0904-017.md) | Pipeline definition signing and execution-time signature verification | Practitioner | ai-specific |
| [SAFE-K8S-0904-018](markdown/controls/SAFE-K8S-0904-018.md) | Pipeline definition immutable version storage and controlled rollback governance | Practitioner | ai-specific |

<a id="knowledge-area-9-5"></a>
## 9.5 - AI Supply Chain and Model Lifecycle

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Advanced
- Controls: 37

### Description

This knowledge area focuses on: AI system lifecycle classification, Automated model promotion gates, Model artifact lifecycle management, Model provenance verification at deployment, and Development-to-production environment separation for AI workloads. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0905-001](markdown/controls/SAFE-K8S-0905-001.md) | AI system lifecycle classification | Practitioner | ai-specific |
| [SAFE-K8S-0905-005](markdown/controls/SAFE-K8S-0905-005.md) | Automated model promotion gates | Advanced | ai-specific |
| [SAFE-K8S-0905-006](markdown/controls/SAFE-K8S-0905-006.md) | Model artifact lifecycle management | Advanced | ai-specific |
| [SAFE-K8S-0905-009](markdown/controls/SAFE-K8S-0905-009.md) | Model provenance verification at deployment | Advanced | ai-specific |
| [SAFE-K8S-0905-012](markdown/controls/SAFE-K8S-0905-012.md) | Development-to-production environment separation for AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0905-015](markdown/controls/SAFE-K8S-0905-015.md) | AI system control profile enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0905-025](markdown/controls/SAFE-K8S-0905-025.md) | Separation of duties enforcement for model promotion approvals | Advanced | ai-specific |
| [SAFE-K8S-0905-028](markdown/controls/SAFE-K8S-0905-028.md) | ML framework and Python dependency vulnerability management | Advanced | ai-specific |
| [SAFE-K8S-0905-029](markdown/controls/SAFE-K8S-0905-029.md) | CUDA and GPU accelerator dependency vulnerability management | Advanced | ai-specific |
| [SAFE-K8S-0905-032](markdown/controls/SAFE-K8S-0905-032.md) | Safe model format allowlist and unsafe deserialization blocking | Practitioner | ai-specific |
| [SAFE-K8S-0905-033](markdown/controls/SAFE-K8S-0905-033.md) | Pre-load model file structure and metadata validation | Practitioner | ai-specific |
| [SAFE-K8S-0905-034](markdown/controls/SAFE-K8S-0905-034.md) | Canary and A/B candidate version isolation and traffic-splitting integrity | Advanced | ai-specific |
| [SAFE-K8S-0905-035](markdown/controls/SAFE-K8S-0905-035.md) | Automatic canary rollback on error-rate and latency degradation | Advanced | ai-specific |
| [SAFE-K8S-0905-036](markdown/controls/SAFE-K8S-0905-036.md) | Automated AI workload circuit-breaker threshold enforcement | Advanced | ai-specific |
| [SAFE-K8S-0905-037](markdown/controls/SAFE-K8S-0905-037.md) | Manual emergency halt governance and forensic evidence preservation | Advanced | ai-specific |
| [SAFE-K8S-0905-038](markdown/controls/SAFE-K8S-0905-038.md) | Model registry RBAC and workload pull authorization scoping | Practitioner | ai-specific |
| [SAFE-K8S-0905-039](markdown/controls/SAFE-K8S-0905-039.md) | Model registry access review and stale-permission remediation | Practitioner | ai-specific |
| [SAFE-K8S-0905-040](markdown/controls/SAFE-K8S-0905-040.md) | Model registry audit event generation and centralized forwarding | Practitioner | ai-specific |
| [SAFE-K8S-0905-041](markdown/controls/SAFE-K8S-0905-041.md) | Model registry sensitive-operation alerting and anomalous activity review | Practitioner | ai-specific |
| [SAFE-K8S-0905-042](markdown/controls/SAFE-K8S-0905-042.md) | CTA-2114 ML-BOM generation and lineage metadata capture | Advanced | ai-specific |
| [SAFE-K8S-0905-043](markdown/controls/SAFE-K8S-0905-043.md) | Durable ML-BOM attachment to model artifacts and versions | Advanced | ai-specific |
| [SAFE-K8S-0905-044](markdown/controls/SAFE-K8S-0905-044.md) | Public model quarantine isolation and malicious artifact scanning | Advanced | ai-specific |
| [SAFE-K8S-0905-045](markdown/controls/SAFE-K8S-0905-045.md) | Sandboxed external model behavioral vetting and disposition review | Advanced | ai-specific |
| [SAFE-K8S-0905-046](markdown/controls/SAFE-K8S-0905-046.md) | ML artifact cryptographic signing with Sigstore or equivalent | Advanced | ai-specific |
| [SAFE-K8S-0905-047](markdown/controls/SAFE-K8S-0905-047.md) | Training pipeline attestation generation for ML artifacts | Advanced | ai-specific |
| [SAFE-K8S-0905-048](markdown/controls/SAFE-K8S-0905-048.md) | OCI model artifact digest pinning in deployment and promotion workflows | Advanced | ai-specific |
| [SAFE-K8S-0905-049](markdown/controls/SAFE-K8S-0905-049.md) | OCI model registry tag immutability and overwrite prevention | Advanced | ai-specific |
| [SAFE-K8S-0905-050](markdown/controls/SAFE-K8S-0905-050.md) | Authenticated reviewer identity validation for model promotion approvals | Advanced | ai-specific |
| [SAFE-K8S-0905-051](markdown/controls/SAFE-K8S-0905-051.md) | Model promotion approval audit binding to reviewer identity and model version | Advanced | ai-specific |
| [SAFE-K8S-0905-052](markdown/controls/SAFE-K8S-0905-052.md) | Approved external model source allowlist definition and maintenance | Advanced | ai-specific |
| [SAFE-K8S-0905-053](markdown/controls/SAFE-K8S-0905-053.md) | Approved external model source periodic review and allowlist update governance | Advanced | ai-specific |
| [SAFE-K8S-0905-054](markdown/controls/SAFE-K8S-0905-054.md) | External model source NetworkPolicy enforcement for protected namespaces | Advanced | ai-specific |
| [SAFE-K8S-0905-055](markdown/controls/SAFE-K8S-0905-055.md) | Admission-time rejection of unapproved external model source references | Advanced | ai-specific |
| [SAFE-K8S-0905-056](markdown/controls/SAFE-K8S-0905-056.md) | External model publisher identity and provenance metadata verification | Advanced | ai-specific |
| [SAFE-K8S-0905-057](markdown/controls/SAFE-K8S-0905-057.md) | External model trust-signal assessment and approval review | Advanced | ai-specific |
| [SAFE-K8S-0905-058](markdown/controls/SAFE-K8S-0905-058.md) | Internal re-signing of approved external models before deployment eligibility | Advanced | ai-specific |
| [SAFE-K8S-0905-059](markdown/controls/SAFE-K8S-0905-059.md) | External-origin annotation and internal registry enrollment for approved external models | Advanced | ai-specific |

<a id="knowledge-area-9-6"></a>
## 9.6 - Training Data Integrity and Poisoning Defense

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 5

### Description

This knowledge area focuses on: Large-scale data integrity verification, Statistical drift, outlier, and input validation for training data poisoning detection, Annotation pipeline integrity and targeted label attack detection, Training data provenance tracking from ingestion through model training, and Integrity verification at each training data transformation stage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0906-002](markdown/controls/SAFE-K8S-0906-002.md) | Large-scale data integrity verification | Practitioner | ai-specific |
| [SAFE-K8S-0906-004](markdown/controls/SAFE-K8S-0906-004.md) | Statistical drift, outlier, and input validation for training data poisoning detection | Practitioner | ai-specific |
| [SAFE-K8S-0906-005](markdown/controls/SAFE-K8S-0906-005.md) | Annotation pipeline integrity and targeted label attack detection | Practitioner | ai-specific |
| [SAFE-K8S-0906-006](markdown/controls/SAFE-K8S-0906-006.md) | Training data provenance tracking from ingestion through model training | Practitioner | ai-specific |
| [SAFE-K8S-0906-007](markdown/controls/SAFE-K8S-0906-007.md) | Integrity verification at each training data transformation stage | Practitioner | ai-specific |

<a id="knowledge-area-9-7"></a>
## 9.7 - Feature Store Security and Data Access Controls

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 5

### Description

This knowledge area focuses on: Training data privacy controls, Feature store access boundary enforcement and serving authentication, Feature engineering privacy controls and leakage validation, Training dataset access restriction across storage backends, and Model deployment authorization and namespace-scoped release control.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0907-002](markdown/controls/SAFE-K8S-0907-002.md) | Training data privacy controls | Practitioner | ai-specific |
| [SAFE-K8S-0907-004](markdown/controls/SAFE-K8S-0907-004.md) | Feature store access boundary enforcement and serving authentication | Practitioner | ai-specific |
| [SAFE-K8S-0907-005](markdown/controls/SAFE-K8S-0907-005.md) | Feature engineering privacy controls and leakage validation | Practitioner | ai-specific |
| [SAFE-K8S-0907-006](markdown/controls/SAFE-K8S-0907-006.md) | Training dataset access restriction across storage backends | Practitioner | ai-specific |
| [SAFE-K8S-0907-007](markdown/controls/SAFE-K8S-0907-007.md) | Model deployment authorization and namespace-scoped release control | Practitioner | ai-specific |

<a id="knowledge-area-9-8"></a>
## 9.8 - Model Abuse and Extraction Prevention

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Advanced
- Controls: 8

### Description

This knowledge area focuses on: Oracle attack prevention, Inference API information exposure controls, Model watermarking and fingerprinting, Model abuse logging and alerting, and Secure aggregation for privacy-preserving model outputs. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0908-001](markdown/controls/SAFE-K8S-0908-001.md) | Oracle attack prevention | Advanced | ai-specific |
| [SAFE-K8S-0908-002](markdown/controls/SAFE-K8S-0908-002.md) | Inference API information exposure controls | Advanced | ai-specific |
| [SAFE-K8S-0908-003](markdown/controls/SAFE-K8S-0908-003.md) | Model watermarking and fingerprinting | Advanced | ai-specific |
| [SAFE-K8S-0908-005](markdown/controls/SAFE-K8S-0908-005.md) | Model abuse logging and alerting | Advanced | ai-specific |
| [SAFE-K8S-0908-006](markdown/controls/SAFE-K8S-0908-006.md) | Secure aggregation for privacy-preserving model outputs | Advanced | ai-specific |
| [SAFE-K8S-0908-008](markdown/controls/SAFE-K8S-0908-008.md) | Inference output perturbation and privacy-preserving response shaping | Advanced | ai-specific |
| [SAFE-K8S-0908-009](markdown/controls/SAFE-K8S-0908-009.md) | Differential privacy parameter governance for inference endpoints | Advanced | ai-specific |
| [SAFE-K8S-0908-010](markdown/controls/SAFE-K8S-0908-010.md) | Inference privacy budget tracking and threshold enforcement | Advanced | ai-specific |

<a id="knowledge-area-9-9"></a>
## 9.9 - RAG Infrastructure Security

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 10

### Description

This knowledge area focuses on: Embedding pipeline integrity, RAG prompt injection defense, Vector index lifecycle management, Classification-aware chunking and vector collection segregation, and Vector database authentication and collection-level access control. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0909-002](markdown/controls/SAFE-K8S-0909-002.md) | Embedding pipeline integrity | Practitioner | ai-specific |
| [SAFE-K8S-0909-005](markdown/controls/SAFE-K8S-0909-005.md) | RAG prompt injection defense | Practitioner | ai-specific |
| [SAFE-K8S-0909-006](markdown/controls/SAFE-K8S-0909-006.md) | Vector index lifecycle management | Practitioner | ai-specific |
| [SAFE-K8S-0909-008](markdown/controls/SAFE-K8S-0909-008.md) | Classification-aware chunking and vector collection segregation | Practitioner | ai-specific |
| [SAFE-K8S-0909-009](markdown/controls/SAFE-K8S-0909-009.md) | Vector database authentication and collection-level access control | Practitioner | ai-specific |
| [SAFE-K8S-0909-010](markdown/controls/SAFE-K8S-0909-010.md) | Vector database encryption in transit and at rest | Practitioner | ai-specific |
| [SAFE-K8S-0909-011](markdown/controls/SAFE-K8S-0909-011.md) | Retrieved context integrity validation and relevance threshold enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0909-012](markdown/controls/SAFE-K8S-0909-012.md) | Context poisoning monitoring and incident response for RAG retrieval | Practitioner | ai-specific |
| [SAFE-K8S-0909-013](markdown/controls/SAFE-K8S-0909-013.md) | Approved source repository access control and allowlist enforcement for RAG ingestion | Practitioner | ai-specific |
| [SAFE-K8S-0909-014](markdown/controls/SAFE-K8S-0909-014.md) | Document provenance and integrity validation before RAG chunking and indexing | Practitioner | ai-specific |

<a id="knowledge-area-9-10"></a>
## 9.10 - Multi-Cluster and Federated AI Security

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Advanced
- Controls: 19

### Description

This knowledge area focuses on: Federated learning cross-cluster coordination security, Destination-side signature and digest re-verification for replicated model artifacts, Cross-cluster orchestration identity federation and authorization, Centralized audit logging for cross-cluster orchestration actions, and Security-aware target-cluster posture verification before multi-cluster placement. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0910-004](markdown/controls/SAFE-K8S-0910-004.md) | Federated learning cross-cluster coordination security | Advanced | ai-specific |
| [SAFE-K8S-0910-015](markdown/controls/SAFE-K8S-0910-015.md) | Destination-side signature and digest re-verification for replicated model artifacts | Advanced | ai-specific |
| [SAFE-K8S-0910-016](markdown/controls/SAFE-K8S-0910-016.md) | Cross-cluster orchestration identity federation and authorization | Advanced | ai-specific |
| [SAFE-K8S-0910-017](markdown/controls/SAFE-K8S-0910-017.md) | Centralized audit logging for cross-cluster orchestration actions | Advanced | ai-specific |
| [SAFE-K8S-0910-018](markdown/controls/SAFE-K8S-0910-018.md) | Security-aware target-cluster posture verification before multi-cluster placement | Advanced | ai-specific |
| [SAFE-K8S-0910-019](markdown/controls/SAFE-K8S-0910-019.md) | Compromised-cluster federation isolation and re-admission governance | Advanced | ai-specific |
| [SAFE-K8S-0910-020](markdown/controls/SAFE-K8S-0910-020.md) | Cross-cluster transport encryption for distributed AI traffic | Advanced | ai-specific |
| [SAFE-K8S-0910-021](markdown/controls/SAFE-K8S-0910-021.md) | Cross-cluster endpoint and workload authentication for AI communication | Advanced | ai-specific |
| [SAFE-K8S-0910-022](markdown/controls/SAFE-K8S-0910-022.md) | Cross-cluster communication authorization policy enforcement | Advanced | ai-specific |
| [SAFE-K8S-0910-024](markdown/controls/SAFE-K8S-0910-024.md) | Cross-cluster model provenance chain-of-custody preservation | Advanced | ai-specific |
| [SAFE-K8S-0910-025](markdown/controls/SAFE-K8S-0910-025.md) | Cross-cluster registry federation endpoint authorization and reconciliation governance | Advanced | ai-specific |
| [SAFE-K8S-0910-026](markdown/controls/SAFE-K8S-0910-026.md) | Multi-cluster security policy baseline federation | Advanced | ai-specific |
| [SAFE-K8S-0910-027](markdown/controls/SAFE-K8S-0910-027.md) | Multi-cluster policy drift detection and remediation | Advanced | ai-specific |
| [SAFE-K8S-0910-028](markdown/controls/SAFE-K8S-0910-028.md) | Unified multi-cluster compliance reporting | Advanced | ai-specific |
| [SAFE-K8S-0910-029](markdown/controls/SAFE-K8S-0910-029.md) | Centralized multi-cluster secret, certificate, and incident governance coordination | Advanced | ai-specific |
| [SAFE-K8S-0910-030](markdown/controls/SAFE-K8S-0910-030.md) | Cross-cluster registry replication channel mutual authentication | Advanced | ai-specific |
| [SAFE-K8S-0910-031](markdown/controls/SAFE-K8S-0910-031.md) | Cross-cluster registry endpoint enrollment approval | Advanced | ai-specific |
| [SAFE-K8S-0910-032](markdown/controls/SAFE-K8S-0910-032.md) | Cross-cluster traffic anomaly monitoring for distributed AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0910-033](markdown/controls/SAFE-K8S-0910-033.md) | Investigation of anomalous cross-cluster AI communication | Advanced | ai-specific |

<a id="knowledge-area-10-1"></a>
## 10.1 - Logging and Audit

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Practitioner
- Controls: 25

### Description

This knowledge area focuses on: Audit volume management for AI workloads, Supplemental application-level telemetry for AI workload events, Permitted responses to audit findings, Kubernetes audit level and stage filtering for AI workloads, and SIEM correlation rules for AI-specific attack patterns. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1001-004](markdown/controls/SAFE-K8S-1001-004.md) | Audit volume management for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-007](markdown/controls/SAFE-K8S-1001-007.md) | Supplemental application-level telemetry for AI workload events | Practitioner | ai-specific |
| [SAFE-K8S-1001-008](markdown/controls/SAFE-K8S-1001-008.md) | Permitted responses to audit findings | Practitioner | baseline |
| [SAFE-K8S-1001-010](markdown/controls/SAFE-K8S-1001-010.md) | Kubernetes audit level and stage filtering for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-012](markdown/controls/SAFE-K8S-1001-012.md) | SIEM correlation rules for AI-specific attack patterns | Practitioner | ai-specific |
| [SAFE-K8S-1001-015](markdown/controls/SAFE-K8S-1001-015.md) | PII redaction and sensitive payload minimization for inference logs | Practitioner | ai-specific |
| [SAFE-K8S-1001-016](markdown/controls/SAFE-K8S-1001-016.md) | Audit policy coverage for AI-specific resource and workflow events | Practitioner | ai-specific |
| [SAFE-K8S-1001-017](markdown/controls/SAFE-K8S-1001-017.md) | Audit capture of admission, authorization, and privileged API decisions for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-019](markdown/controls/SAFE-K8S-1001-019.md) | Regulatory AI artifact and provenance record retention enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-023](markdown/controls/SAFE-K8S-1001-023.md) | Regulatory audit log durable retrieval enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-024](markdown/controls/SAFE-K8S-1001-024.md) | Audit log append-only storage and tamper protection | Practitioner | baseline |
| [SAFE-K8S-1001-025](markdown/controls/SAFE-K8S-1001-025.md) | Dual authorization for audit log deletion or modification | Practitioner | baseline |
| [SAFE-K8S-1001-026](markdown/controls/SAFE-K8S-1001-026.md) | Durable audit backend delivery for Kubernetes AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-027](markdown/controls/SAFE-K8S-1001-027.md) | Tamper-resistant retention for Kubernetes AI audit backends | Practitioner | ai-specific |
| [SAFE-K8S-1001-028](markdown/controls/SAFE-K8S-1001-028.md) | AI-specific SIEM source onboarding and forwarding | Practitioner | ai-specific |
| [SAFE-K8S-1001-029](markdown/controls/SAFE-K8S-1001-029.md) | SIEM ingestion health, delivery completeness, and source coverage monitoring | Practitioner | ai-specific |
| [SAFE-K8S-1001-030](markdown/controls/SAFE-K8S-1001-030.md) | Centralized AI workload log collection and routing | Practitioner | ai-specific |
| [SAFE-K8S-1001-031](markdown/controls/SAFE-K8S-1001-031.md) | Tenant and workload context preservation for AI log segregation and searchability | Practitioner | ai-specific |
| [SAFE-K8S-1001-032](markdown/controls/SAFE-K8S-1001-032.md) | Cluster-wide Kubernetes and AI log source coverage | Practitioner | baseline |
| [SAFE-K8S-1001-033](markdown/controls/SAFE-K8S-1001-033.md) | Centralized aggregation onboarding and export for cluster-wide AI logs | Practitioner | baseline |
| [SAFE-K8S-1001-034](markdown/controls/SAFE-K8S-1001-034.md) | Centralized AI log backend immutability and integrity verification | Practitioner | baseline |
| [SAFE-K8S-1001-036](markdown/controls/SAFE-K8S-1001-036.md) | Regulatory audit log retention period configuration and compliance verification | Practitioner | ai-specific |
| [SAFE-K8S-1001-037](markdown/controls/SAFE-K8S-1001-037.md) | Regulatory audit log immutability and deletion prevention before retention expiry | Practitioner | ai-specific |
| [SAFE-K8S-1001-038](markdown/controls/SAFE-K8S-1001-038.md) | Centralized AI log retention lifecycle enforcement | Practitioner | baseline |
| [SAFE-K8S-1001-039](markdown/controls/SAFE-K8S-1001-039.md) | Durable retrieval validation for centralized AI logs | Practitioner | baseline |

<a id="knowledge-area-10-2"></a>
## 10.2 - Monitoring, Metrics, and Tracing

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Practitioner
- Controls: 6

### Description

This knowledge area focuses on: Metric endpoint authentication, Distributed tracing for ML pipelines, AI workload telemetry integration into cluster monitoring, AI-specific alerting and failure mode detection, and Metric endpoint authorization and RBAC. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1002-001](markdown/controls/SAFE-K8S-1002-001.md) | Metric endpoint authentication | Practitioner | baseline |
| [SAFE-K8S-1002-002](markdown/controls/SAFE-K8S-1002-002.md) | Distributed tracing for ML pipelines | Practitioner | ai-specific |
| [SAFE-K8S-1002-003](markdown/controls/SAFE-K8S-1002-003.md) | AI workload telemetry integration into cluster monitoring | Practitioner | ai-specific |
| [SAFE-K8S-1002-004](markdown/controls/SAFE-K8S-1002-004.md) | AI-specific alerting and failure mode detection | Practitioner | ai-specific |
| [SAFE-K8S-1002-005](markdown/controls/SAFE-K8S-1002-005.md) | Metric endpoint authorization and RBAC | Practitioner | baseline |
| [SAFE-K8S-1002-006](markdown/controls/SAFE-K8S-1002-006.md) | Sensitive metric redaction and access restriction | Practitioner | ai-specific |

<a id="knowledge-area-10-3"></a>
## 10.3 - Threat Modeling Methodologies

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Advanced
- Controls: 4

### Description

This knowledge area focuses on: STRIDE threat modeling for Kubernetes AI systems, OCTAVE risk-based threat assessment for Kubernetes AI environments, MITRE ATT&CK for Containers coverage mapping and gap analysis, and Technique-aligned detection engineering for Kubernetes AI attack scenarios.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1003-001](markdown/controls/SAFE-K8S-1003-001.md) | STRIDE threat modeling for Kubernetes AI systems | Practitioner | ai-specific |
| [SAFE-K8S-1003-002](markdown/controls/SAFE-K8S-1003-002.md) | OCTAVE risk-based threat assessment for Kubernetes AI environments | Advanced | ai-specific |
| [SAFE-K8S-1003-004](markdown/controls/SAFE-K8S-1003-004.md) | MITRE ATT&CK for Containers coverage mapping and gap analysis | Advanced | ai-specific |
| [SAFE-K8S-1003-005](markdown/controls/SAFE-K8S-1003-005.md) | Technique-aligned detection engineering for Kubernetes AI attack scenarios | Advanced | ai-specific |

<a id="knowledge-area-10-4"></a>
## 10.4 - AI and Supply Chain Threat Taxonomy

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Advanced
- Controls: 5

### Description

This knowledge area focuses on: ML threat taxonomy per CTA-2114 mapped to Kubernetes, Software supply chain threat model per NIST SP 800-204D, Kubernetes AI threat intelligence feed ingestion and detection enrichment, Adversarial ML threat taxonomy and structured classification, and Cross-source threat correlation with business context for AI incidents.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1004-001](markdown/controls/SAFE-K8S-1004-001.md) | ML threat taxonomy per CTA-2114 mapped to Kubernetes | Advanced | ai-specific |
| [SAFE-K8S-1004-002](markdown/controls/SAFE-K8S-1004-002.md) | Software supply chain threat model per NIST SP 800-204D | Advanced | ai-specific |
| [SAFE-K8S-1004-004](markdown/controls/SAFE-K8S-1004-004.md) | Kubernetes AI threat intelligence feed ingestion and detection enrichment | Advanced | ai-specific |
| [SAFE-K8S-1004-005](markdown/controls/SAFE-K8S-1004-005.md) | Adversarial ML threat taxonomy and structured classification | Advanced | ai-specific |
| [SAFE-K8S-1004-006](markdown/controls/SAFE-K8S-1004-006.md) | Cross-source threat correlation with business context for AI incidents | Advanced | ai-specific |

<a id="knowledge-area-10-5"></a>
## 10.5 - Incident Response for Kubernetes

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Practitioner
- Controls: 19

### Description

This knowledge area focuses on: Kubernetes incident response lifecycle, AI-specific incident response playbooks for Kubernetes, Ransomware recovery prioritization and post-incident preparedness improvement, Post-incident AI model integrity verification, and Documented post-incident model retraining or rollback decisions. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1005-001](markdown/controls/SAFE-K8S-1005-001.md) | Kubernetes incident response lifecycle | Practitioner | ai-specific |
| [SAFE-K8S-1005-008](markdown/controls/SAFE-K8S-1005-008.md) | AI-specific incident response playbooks for Kubernetes | Practitioner | ai-specific |
| [SAFE-K8S-1005-014](markdown/controls/SAFE-K8S-1005-014.md) | Ransomware recovery prioritization and post-incident preparedness improvement | Practitioner | baseline |
| [SAFE-K8S-1005-015](markdown/controls/SAFE-K8S-1005-015.md) | Post-incident AI model integrity verification | Practitioner | ai-specific |
| [SAFE-K8S-1005-016](markdown/controls/SAFE-K8S-1005-016.md) | Documented post-incident model retraining or rollback decisions | Practitioner | ai-specific |
| [SAFE-K8S-1005-017](markdown/controls/SAFE-K8S-1005-017.md) | Recovery-time lateral movement containment for compromised AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1005-018](markdown/controls/SAFE-K8S-1005-018.md) | Component integrity verification before restoration after compromise | Practitioner | ai-specific |
| [SAFE-K8S-1005-019](markdown/controls/SAFE-K8S-1005-019.md) | Vulnerability disclosure policy, intake channels, and triage SLAs for Kubernetes AI infrastructure | Practitioner | baseline |
| [SAFE-K8S-1005-020](markdown/controls/SAFE-K8S-1005-020.md) | Vulnerability response ownership and multi-party coordination governance for Kubernetes AI infrastructure | Practitioner | baseline |
| [SAFE-K8S-1005-021](markdown/controls/SAFE-K8S-1005-021.md) | Kubernetes containment runbooks for node draining, namespace isolation, and workload suspension | Practitioner | ai-specific |
| [SAFE-K8S-1005-022](markdown/controls/SAFE-K8S-1005-022.md) | Kubernetes incident credential revocation procedures for ServiceAccounts and external access | Practitioner | ai-specific |
| [SAFE-K8S-1005-023](markdown/controls/SAFE-K8S-1005-023.md) | GPU-aware node draining and accelerator workload containment | Practitioner | ai-specific |
| [SAFE-K8S-1005-024](markdown/controls/SAFE-K8S-1005-024.md) | Inference service quarantine and pipeline execution suspension with state preservation | Practitioner | ai-specific |
| [SAFE-K8S-1005-025](markdown/controls/SAFE-K8S-1005-025.md) | Kubernetes forensic evidence acquisition for container, node, audit, and network artifacts | Practitioner | ai-specific |
| [SAFE-K8S-1005-026](markdown/controls/SAFE-K8S-1005-026.md) | Forensic chain-of-custody and evidence handling for Kubernetes AI incidents | Practitioner | ai-specific |
| [SAFE-K8S-1005-027](markdown/controls/SAFE-K8S-1005-027.md) | GPU and accelerator forensic evidence preservation for Kubernetes AI incidents | Practitioner | ai-specific |
| [SAFE-K8S-1005-028](markdown/controls/SAFE-K8S-1005-028.md) | Model access and training provenance forensic preservation for Kubernetes AI incidents | Practitioner | ai-specific |
| [SAFE-K8S-1005-029](markdown/controls/SAFE-K8S-1005-029.md) | Kubernetes backup verification for etcd and AI workload data | Practitioner | baseline |
| [SAFE-K8S-1005-030](markdown/controls/SAFE-K8S-1005-030.md) | Documented etcd restoration procedures and tested execution readiness | Practitioner | baseline |

<a id="knowledge-area-10-6"></a>
## 10.6 - Compliance and Governance

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Advanced
- Controls: 7

### Description

This knowledge area focuses on: Regulatory compliance mapping for Kubernetes AI platforms, Automated audit readiness for Kubernetes AI platforms, Policy-as-code enforcement for AI workload compliance, NIST SSDF v1.1 alignment and gap assessment for Kubernetes AI development, and NIST SP 800-218A AI/ML profile alignment for Kubernetes AI development. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1006-001](markdown/controls/SAFE-K8S-1006-001.md) | Regulatory compliance mapping for Kubernetes AI platforms | Practitioner | ai-specific |
| [SAFE-K8S-1006-004](markdown/controls/SAFE-K8S-1006-004.md) | Automated audit readiness for Kubernetes AI platforms | Advanced | ai-specific |
| [SAFE-K8S-1006-005](markdown/controls/SAFE-K8S-1006-005.md) | Policy-as-code enforcement for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1006-007](markdown/controls/SAFE-K8S-1006-007.md) | NIST SSDF v1.1 alignment and gap assessment for Kubernetes AI development | Advanced | ai-specific |
| [SAFE-K8S-1006-008](markdown/controls/SAFE-K8S-1006-008.md) | NIST SP 800-218A AI/ML profile alignment for Kubernetes AI development | Advanced | ai-specific |
| [SAFE-K8S-1006-009](markdown/controls/SAFE-K8S-1006-009.md) | Continuous policy decision evidence generation and export for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1006-010](markdown/controls/SAFE-K8S-1006-010.md) | Policy exception approval and expiration governance for AI workload compliance | Practitioner | ai-specific |

<a id="knowledge-area-10-7"></a>
## 10.7 - Cluster Lifecycle and Asset Inventory

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Practitioner
- Controls: 13

### Description

This knowledge area focuses on: Continuous security posture management for AI clusters, Change management for production AI model deployments, Secure AI workload decommissioning, Cluster service protection from AI training resource exhaustion, and Pre-upgrade Kubernetes API compatibility testing for AI workloads. Additional controls in the table below extend this coverage.

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1007-004](markdown/controls/SAFE-K8S-1007-004.md) | Continuous security posture management for AI clusters | Practitioner | ai-specific |
| [SAFE-K8S-1007-005](markdown/controls/SAFE-K8S-1007-005.md) | Change management for production AI model deployments | Practitioner | ai-specific |
| [SAFE-K8S-1007-006](markdown/controls/SAFE-K8S-1007-006.md) | Secure AI workload decommissioning | Practitioner | ai-specific |
| [SAFE-K8S-1007-007](markdown/controls/SAFE-K8S-1007-007.md) | Cluster service protection from AI training resource exhaustion | Practitioner | ai-specific |
| [SAFE-K8S-1007-010](markdown/controls/SAFE-K8S-1007-010.md) | Pre-upgrade Kubernetes API compatibility testing for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1007-011](markdown/controls/SAFE-K8S-1007-011.md) | Kubernetes cluster upgrade planning, sequencing, and rollback governance | Practitioner | ai-specific |
| [SAFE-K8S-1007-012](markdown/controls/SAFE-K8S-1007-012.md) | AI infrastructure compatibility matrix and coordinated component upgrade governance | Practitioner | ai-specific |
| [SAFE-K8S-1007-013](markdown/controls/SAFE-K8S-1007-013.md) | Automated AI infrastructure asset discovery and continuously updated inventory | Practitioner | ai-specific |
| [SAFE-K8S-1007-014](markdown/controls/SAFE-K8S-1007-014.md) | AI asset classification and criticality governance for Kubernetes environments | Practitioner | ai-specific |
| [SAFE-K8S-1007-015](markdown/controls/SAFE-K8S-1007-015.md) | GPU node onboarding security baseline validation gates | Advanced | ai-specific |
| [SAFE-K8S-1007-016](markdown/controls/SAFE-K8S-1007-016.md) | GPU node hardware attestation, driver integrity, and taint verification | Advanced | ai-specific |
| [SAFE-K8S-1007-017](markdown/controls/SAFE-K8S-1007-017.md) | Kubernetes release-channel and changelog monitoring for API deprecations | Practitioner | ai-specific |
| [SAFE-K8S-1007-018](markdown/controls/SAFE-K8S-1007-018.md) | Deprecated Kubernetes API usage inventory and migration tracking for AI workloads | Practitioner | ai-specific |
