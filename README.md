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
- Controls: 21

### Description

API server hardening flags: anonymous auth disabling, profiling endpoint removal, admission controller chain, audit logging activation TLS configuration for API server front-end and back-end connections including certificate rotation Encryption at rest configuration for Secrets and other sensitive API resources using EncryptionConfiguration API server access controls: RBAC bootstrapping, ABAC removal, Node and webhook authorization modes Streaming connection idle timeout: --streaming-connection-idle-timeout configuration to terminate idle exec, attach, and port-forward sessions API server audit policy coverage and event detail: tiered verbosity policy configuration capturing Metadata for all resources, Request for sensitive resources, and RequestResponse for authentication and authorization decisions API server audit log backend durability and retention: durable backend configuration (log file with rotation or webhook to SIEM), persistent storage for audit logs, and retention period enforcement per organizational policy

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0101-001](markdown/controls/SAFE-K8S-0101-001.md) | API server hardening flags | Foundational | baseline |
| [SAFE-K8S-0101-002](markdown/controls/SAFE-K8S-0101-002.md) | API server TLS configuration and certificate rotation | Foundational | baseline |
| [SAFE-K8S-0101-003](markdown/controls/SAFE-K8S-0101-003.md) | Encryption at rest for Secrets and sensitive API resources | Foundational | baseline |
| [SAFE-K8S-0101-004](markdown/controls/SAFE-K8S-0101-004.md) | API server access controls and authorization modes | Foundational | baseline |
| [SAFE-K8S-0101-005](markdown/controls/SAFE-K8S-0101-005.md) | Streaming connection idle timeout enforcement | Foundational | baseline |
| [SAFE-K8S-0101-006](markdown/controls/SAFE-K8S-0101-006.md) | API server audit logging policy and backend configuration | Foundational | baseline |
| [SAFE-K8S-0101-007](markdown/controls/SAFE-K8S-0101-007.md) | API server request rate limiting and API Priority and Fairness | Practitioner | ai-specific |
| [SAFE-K8S-0101-008](markdown/controls/SAFE-K8S-0101-008.md) | API server audit policy coverage and event detail | Foundational | baseline |
| [SAFE-K8S-0101-009](markdown/controls/SAFE-K8S-0101-009.md) | API server audit log backend durability and retention | Foundational | baseline |
| [SAFE-K8S-0101-010](markdown/controls/SAFE-K8S-0101-010.md) | API server anonymous authentication disablement and authorization mode hardening | Foundational | baseline |
| [SAFE-K8S-0101-011](markdown/controls/SAFE-K8S-0101-011.md) | API server profiling disablement and approved admission controller configuration | Foundational | baseline |
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
- Controls: 25

### Description

etcd encryption at rest for all cluster state data with KMS provider integration etcd access controls: client certificate authentication, peer TLS, and network-level isolation from non-control-plane components etcd backup encryption: encrypt snapshots at rest with a separate key and in transit over TLS (SAFE-K8S-0102-003) etcd backup integrity verification: cryptographic checksum or signature generated at creation, verified before storage and before restore (SAFE-K8S-0102-006) etcd backup storage access restriction: least-privilege IAM or ACL policy limiting access to backup service account and named break-glass administrators with audit logging (SAFE-K8S-0102-007) etcd cluster health monitoring, compaction, and defragmentation as security-relevant operational practices

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0102-001](markdown/controls/SAFE-K8S-0102-001.md) | etcd storage-layer disk encryption with externally managed keys | Foundational | baseline |
| [SAFE-K8S-0102-002](markdown/controls/SAFE-K8S-0102-002.md) | etcd access controls and network isolation | Foundational | baseline |
| [SAFE-K8S-0102-003](markdown/controls/SAFE-K8S-0102-003.md) | etcd backup and restore security | Foundational | baseline |
| [SAFE-K8S-0102-004](markdown/controls/SAFE-K8S-0102-004.md) | etcd cluster health monitoring, compaction, and defragmentation | Foundational | baseline |
| [SAFE-K8S-0102-005](markdown/controls/SAFE-K8S-0102-005.md) | etcd certificate rotation and lifecycle management | Practitioner | baseline |
| [SAFE-K8S-0102-006](markdown/controls/SAFE-K8S-0102-006.md) | etcd encryption key rotation scheduling and verification | Foundational | baseline |
| [SAFE-K8S-0102-007](markdown/controls/SAFE-K8S-0102-007.md) | etcd backup storage encryption | Foundational | baseline |
| [SAFE-K8S-0102-008](markdown/controls/SAFE-K8S-0102-008.md) | etcd backup integrity verification and restore assurance | Foundational | baseline |
| [SAFE-K8S-0102-009](markdown/controls/SAFE-K8S-0102-009.md) | etcd backup storage access restriction and auditing | Foundational | baseline |
| [SAFE-K8S-0102-010](markdown/controls/SAFE-K8S-0102-010.md) | etcd certificate rotation execution and testing | Practitioner | baseline |
| [SAFE-K8S-0102-011](markdown/controls/SAFE-K8S-0102-011.md) | etcd certificate validity limits and expiration alerting | Practitioner | baseline |
| [SAFE-K8S-0102-012](markdown/controls/SAFE-K8S-0102-012.md) | etcd health monitoring and alerting | Foundational | baseline |
| [SAFE-K8S-0102-013](markdown/controls/SAFE-K8S-0102-013.md) | etcd compaction and periodic defragmentation | Foundational | baseline |
| [SAFE-K8S-0102-014](markdown/controls/SAFE-K8S-0102-014.md) | etcd certificate rotation coverage and execution | Practitioner | baseline |
| [SAFE-K8S-0102-015](markdown/controls/SAFE-K8S-0102-015.md) | etcd certificate rotation testing and recovery validation | Practitioner | baseline |
| [SAFE-K8S-0102-016](markdown/controls/SAFE-K8S-0102-016.md) | etcd backup repository access restriction and break-glass authorization | Foundational | baseline |
| [SAFE-K8S-0102-017](markdown/controls/SAFE-K8S-0102-017.md) | etcd backup repository access audit logging and review | Foundational | baseline |
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
- Controls: 19

### Description

Controller-manager hardening: bound service account tokens, disabled legacy token provisioning, feature gate configuration Scheduler security: restricted access to scheduling decisions, custom scheduler trust, scheduler extender authentication Cloud controller-manager isolation: minimal cloud IAM permissions, separate deployment from core controllers, credential rotation Leader election security and high-availability configuration for control plane components Profiling endpoint disablement for controller-manager and scheduler: --profiling=false on all control-plane components beyond the API server

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0103-001](markdown/controls/SAFE-K8S-0103-001.md) | Controller-manager service account token hardening | Foundational | baseline |
| [SAFE-K8S-0103-002](markdown/controls/SAFE-K8S-0103-002.md) | Scheduler access restriction and extender authentication | Practitioner | baseline |
| [SAFE-K8S-0103-003](markdown/controls/SAFE-K8S-0103-003.md) | Cloud controller-manager isolation and credential management | Practitioner | baseline |
| [SAFE-K8S-0103-004](markdown/controls/SAFE-K8S-0103-004.md) | Leader election security and control-plane high availability | Practitioner | baseline |
| [SAFE-K8S-0103-005](markdown/controls/SAFE-K8S-0103-005.md) | Pod garbage collection threshold configuration | Foundational | ai-specific |
| [SAFE-K8S-0103-006](markdown/controls/SAFE-K8S-0103-006.md) | Profiling endpoint disablement for controller-manager and scheduler | Foundational | baseline |
| [SAFE-K8S-0103-007](markdown/controls/SAFE-K8S-0103-007.md) | Controller-manager and scheduler bind-address and port hardening | Foundational | baseline |
| [SAFE-K8S-0103-008](markdown/controls/SAFE-K8S-0103-008.md) | Cloud controller-manager deployment isolation | Practitioner | baseline |
| [SAFE-K8S-0103-009](markdown/controls/SAFE-K8S-0103-009.md) | Cloud controller-manager IAM scoping and credential rotation | Practitioner | baseline |
| [SAFE-K8S-0103-010](markdown/controls/SAFE-K8S-0103-010.md) | Leader election configuration and lease object RBAC | Practitioner | baseline |
| [SAFE-K8S-0103-011](markdown/controls/SAFE-K8S-0103-011.md) | Control-plane high availability topology and failover | Practitioner | baseline |
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
- Controls: 23

### Description

CIS Kubernetes Benchmark application: automated assessment with kube-bench, remediation workflows, exception documentation Kubernetes version lifecycle management: upgrade strategy planning, version skew policy compliance, deprecation tracking CVE monitoring and prioritization: monitoring Kubernetes security announcements (kubernetes-security-announce, CVE databases, provider advisories), CVE prioritization framework based on CVSS score, exploitability, and cluster exposure Emergency patch deployment: emergency upgrade procedures for Kubernetes components, organization-defined SLA windows, rollback plans, post-patch validation Feature gate governance: security-relevant feature gates, alpha/beta feature risk assessment, gate lifecycle management

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0104-001](markdown/controls/SAFE-K8S-0104-001.md) | CIS Kubernetes Benchmark automated assessment and remediation | Foundational | baseline |
| [SAFE-K8S-0104-002](markdown/controls/SAFE-K8S-0104-002.md) | Kubernetes version lifecycle and upgrade strategy management | Foundational | baseline |
| [SAFE-K8S-0104-003](markdown/controls/SAFE-K8S-0104-003.md) | Kubernetes CVE monitoring, prioritization, and emergency patching | Foundational | baseline |
| [SAFE-K8S-0104-004](markdown/controls/SAFE-K8S-0104-004.md) | Feature gate governance and lifecycle management | Practitioner | baseline |
| [SAFE-K8S-0104-005](markdown/controls/SAFE-K8S-0104-005.md) | Control plane configuration file permissions | Foundational | baseline |
| [SAFE-K8S-0104-006](markdown/controls/SAFE-K8S-0104-006.md) | Kubernetes CVE monitoring and prioritization | Foundational | baseline |
| [SAFE-K8S-0104-007](markdown/controls/SAFE-K8S-0104-007.md) | Emergency Kubernetes patch deployment procedures | Foundational | baseline |
| [SAFE-K8S-0104-008](markdown/controls/SAFE-K8S-0104-008.md) | Production feature gate approval and risk assessment governance | Practitioner | baseline |
| [SAFE-K8S-0104-009](markdown/controls/SAFE-K8S-0104-009.md) | Feature gate lifecycle transition tracking across Kubernetes upgrades | Practitioner | baseline |
| [SAFE-K8S-0104-010](markdown/controls/SAFE-K8S-0104-010.md) | Recurring CIS Kubernetes Benchmark assessment | Foundational | baseline |
| [SAFE-K8S-0104-011](markdown/controls/SAFE-K8S-0104-011.md) | CIS Benchmark remediation tracking and exception governance | Foundational | baseline |
| [SAFE-K8S-0104-012](markdown/controls/SAFE-K8S-0104-012.md) | Kubernetes supported version window and component skew compliance | Foundational | baseline |
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
- Controls: 16

### Description

Kubelet hardening flags: authentication/authorization enforcement, read-only port disabling, anonymous access prevention Kubelet certificate rotation, TLS bootstrapping, and serving certificate management Node allocatable resource configuration and eviction thresholds for system stability Kubelet configuration file permissions, systemd unit security, and node-level audit controls Kubelet hostname override governance: --hostname-override risk assessment, documentation requirements for legitimate use cases (cloud provider node naming), and verification that overrides do not bypass Node authorization identity binding

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0201-001](markdown/controls/SAFE-K8S-0201-001.md) | Kubelet authentication, authorization, and anonymous access hardening | Foundational | baseline |
| [SAFE-K8S-0201-002](markdown/controls/SAFE-K8S-0201-002.md) | Kubelet certificate rotation and TLS bootstrap | Foundational | baseline |
| [SAFE-K8S-0201-003](markdown/controls/SAFE-K8S-0201-003.md) | Node allocatable resources and eviction thresholds | Foundational | baseline |
| [SAFE-K8S-0201-004](markdown/controls/SAFE-K8S-0201-004.md) | Kubelet configuration file permissions and node-level audit controls | Foundational | baseline |
| [SAFE-K8S-0201-005](markdown/controls/SAFE-K8S-0201-005.md) | Kubelet hostname override governance | Foundational | baseline |
| [SAFE-K8S-0201-006](markdown/controls/SAFE-K8S-0201-006.md) | Node system and kube reserved resource allocations | Foundational | baseline |
| [SAFE-K8S-0201-007](markdown/controls/SAFE-K8S-0201-007.md) | Node eviction threshold tuning for workload pressure | Foundational | baseline |
| [SAFE-K8S-0201-008](markdown/controls/SAFE-K8S-0201-008.md) | Kubelet configuration and credential file ownership and permissions | Foundational | baseline |
| [SAFE-K8S-0201-009](markdown/controls/SAFE-K8S-0201-009.md) | Kubelet systemd unit hardening | Foundational | baseline |
| [SAFE-K8S-0201-010](markdown/controls/SAFE-K8S-0201-010.md) | Node-level kubelet audit verification | Foundational | baseline |
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
- Controls: 11

### Description

Container runtime hardening for containerd and CRI-O: configuration baselines, socket permissions, default runtime settings RuntimeClass configuration for workload-appropriate runtimes: standard runc, sandboxed runtimes (gVisor, Kata Containers), and GPU-compatible runtimes Container runtime vulnerability management: patching cadence, version pinning, compatibility validation Runtime socket protection and prevention of container escape through runtime vulnerabilities

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0202-001](markdown/controls/SAFE-K8S-0202-001.md) | Container runtime configuration baselines and socket protection | Foundational | baseline |
| [SAFE-K8S-0202-002](markdown/controls/SAFE-K8S-0202-002.md) | RuntimeClass configuration for workload-appropriate isolation | Foundational | ai-specific |
| [SAFE-K8S-0202-003](markdown/controls/SAFE-K8S-0202-003.md) | Container runtime patching and version management | Foundational | baseline |
| [SAFE-K8S-0202-004](markdown/controls/SAFE-K8S-0202-004.md) | Runtime socket mount prevention | Foundational | baseline |
| [SAFE-K8S-0202-005](markdown/controls/SAFE-K8S-0202-005.md) | Container escape prevention through kernel security profiles | Foundational | baseline |
| [SAFE-K8S-0202-006](markdown/controls/SAFE-K8S-0202-006.md) | Node seccomp defaults and mandatory access control activation | Foundational | baseline |
| [SAFE-K8S-0202-007](markdown/controls/SAFE-K8S-0202-007.md) | Container runtime user namespace isolation | Foundational | baseline |
| [SAFE-K8S-0202-008](markdown/controls/SAFE-K8S-0202-008.md) | Container runtime socket root-only protection | Foundational | baseline |
| [SAFE-K8S-0202-009](markdown/controls/SAFE-K8S-0202-009.md) | Container runtime secure baseline settings and debug endpoint disablement | Foundational | baseline |
| [SAFE-K8S-0202-010](markdown/controls/SAFE-K8S-0202-010.md) | Node default seccomp profile enforcement | Foundational | baseline |
| [SAFE-K8S-0202-011](markdown/controls/SAFE-K8S-0202-011.md) | Node mandatory access control activation for container workloads | Foundational | baseline |

<a id="knowledge-area-2-3"></a>
## 2.3 - Host OS and Kernel Hardening

- Domain: D02 - Node, Runtime, and OS Security
- Maturity: Foundational
- Controls: 15

### Description

Minimal host OS selection and hardening (unnecessary service removal, package minimization, purpose-built OS distributions) Immutable root filesystem enforcement (dm-verity, read-only root mounts) to prevent persistent host modifications Kernel parameter hardening via sysctl: network stack, memory protection, and namespace isolation settings Cloud provider metadata service protection (IMDSv2 enforcement, network-level metadata endpoint restriction) Secure boot and verified boot chain enforcement Kernel module restriction and lockdown mode (module loading controls, blacklisting, kernel lockdown mode)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0203-001](markdown/controls/SAFE-K8S-0203-001.md) | Minimal and immutable host OS configuration | Foundational | baseline |
| [SAFE-K8S-0203-002](markdown/controls/SAFE-K8S-0203-002.md) | Kernel parameter hardening via sysctl | Foundational | baseline |
| [SAFE-K8S-0203-003](markdown/controls/SAFE-K8S-0203-003.md) | Cloud metadata service protection and IMDSv2 enforcement | Foundational | baseline |
| [SAFE-K8S-0203-004](markdown/controls/SAFE-K8S-0203-004.md) | Secure boot and verified boot chain enforcement | Foundational | baseline |
| [SAFE-K8S-0203-005](markdown/controls/SAFE-K8S-0203-005.md) | Kernel module restriction and lockdown mode | Foundational | baseline |
| [SAFE-K8S-0203-006](markdown/controls/SAFE-K8S-0203-006.md) | Cloud instance metadata service hardening and IMDSv2 configuration | Foundational | baseline |
| [SAFE-K8S-0203-007](markdown/controls/SAFE-K8S-0203-007.md) | Pod metadata endpoint blocking and workload identity replacement | Foundational | baseline |
| [SAFE-K8S-0203-008](markdown/controls/SAFE-K8S-0203-008.md) | Pod metadata endpoint network path blocking | Foundational | baseline |
| [SAFE-K8S-0203-009](markdown/controls/SAFE-K8S-0203-009.md) | Workload identity replacement for cloud API access | Foundational | baseline |
| [SAFE-K8S-0203-010](markdown/controls/SAFE-K8S-0203-010.md) | Minimal purpose-built node OS baseline | Foundational | baseline |
| [SAFE-K8S-0203-011](markdown/controls/SAFE-K8S-0203-011.md) | Immutable node root filesystem enforcement | Foundational | baseline |
| [SAFE-K8S-0203-012](markdown/controls/SAFE-K8S-0203-012.md) | Kernel module restriction and approved module whitelisting | Foundational | baseline |
| [SAFE-K8S-0203-013](markdown/controls/SAFE-K8S-0203-013.md) | Kernel lockdown mode enforcement for runtime integrity | Foundational | baseline |
| [SAFE-K8S-0203-014](markdown/controls/SAFE-K8S-0203-014.md) | Authenticated cloud metadata service mode enforcement | Foundational | baseline |
| [SAFE-K8S-0203-015](markdown/controls/SAFE-K8S-0203-015.md) | Cloud metadata endpoint restriction settings | Foundational | baseline |

<a id="knowledge-area-2-4"></a>
## 2.4 - Runtime Threat Detection

- Domain: D02 - Node, Runtime, and OS Security
- Maturity: Practitioner
- Controls: 4

### Description

Runtime security tools deployment and configuration: Falco, Tetragon, KubeArmor for syscall and network monitoring Detection rule development for Kubernetes-specific threats: container escape, privilege escalation, lateral movement, cryptomining Drift detection for container filesystems: identifying unexpected binary execution, library loading, or configuration changes Forensic capture capabilities: container snapshot, memory dump, network flow logging for incident investigation

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
- Controls: 11

### Description

kube-proxy mode selection and hardening: iptables, IPVS, and eBPF-based (kube-proxy replacement) security tradeoffs NodePort and HostPort restriction policies to limit node-level network exposure Node-level firewall configuration and integration with Kubernetes network policies eBPF-based networking security: Cilium, Calico eBPF mode, and kernel-level network policy enforcement

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0205-001](markdown/controls/SAFE-K8S-0205-001.md) | kube-proxy mode selection and security hardening | Practitioner | baseline |
| [SAFE-K8S-0205-002](markdown/controls/SAFE-K8S-0205-002.md) | NodePort and HostPort restriction policies | Practitioner | baseline |
| [SAFE-K8S-0205-003](markdown/controls/SAFE-K8S-0205-003.md) | Node-level firewall and Kubernetes network policy integration | Practitioner | baseline |
| [SAFE-K8S-0205-004](markdown/controls/SAFE-K8S-0205-004.md) | eBPF-based kernel-level network policy enforcement | Practitioner | baseline |
| [SAFE-K8S-0205-005](markdown/controls/SAFE-K8S-0205-005.md) | eBPF program integrity verification and loading monitoring | Practitioner | baseline |
| [SAFE-K8S-0205-006](markdown/controls/SAFE-K8S-0205-006.md) | Node-level firewall rule restriction and audit | Practitioner | baseline |
| [SAFE-K8S-0205-007](markdown/controls/SAFE-K8S-0205-007.md) | Node firewall compatibility validation with CNI and network policy | Practitioner | baseline |
| [SAFE-K8S-0205-008](markdown/controls/SAFE-K8S-0205-008.md) | kube-proxy or service proxy mode selection governance | Practitioner | baseline |
| [SAFE-K8S-0205-009](markdown/controls/SAFE-K8S-0205-009.md) | Service proxy path hardening for kube-proxy or replacements | Practitioner | baseline |
| [SAFE-K8S-0205-010](markdown/controls/SAFE-K8S-0205-010.md) | Node-level firewall rule restriction for cluster communication | Practitioner | baseline |
| [SAFE-K8S-0205-011](markdown/controls/SAFE-K8S-0205-011.md) | Node firewall audit and change governance | Practitioner | baseline |

<a id="knowledge-area-3-1"></a>
## 3.1 - Pod Security Standards and Admission

- Domain: D03 - Workload and Pod Security
- Maturity: Foundational
- Controls: 6

### Description

Pod Security Standards levels (Privileged, Baseline, Restricted): requirements, use cases, and enforcement implications Pod Security Admission (PSA) configuration: namespace labels, enforcement modes (enforce, audit, warn), and version pinning Migration strategies from legacy PodSecurityPolicy to PSA: gap analysis, policy mapping, phased rollout Exemption management for system workloads and legitimate privileged pods (e.g., GPU device plugins, CNI agents)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0301-001](markdown/controls/SAFE-K8S-0301-001.md) | Pod Security Standards level assignment | Foundational | baseline |
| [SAFE-K8S-0301-002](markdown/controls/SAFE-K8S-0301-002.md) | Pod Security Admission configuration and version pinning | Foundational | baseline |
| [SAFE-K8S-0301-003](markdown/controls/SAFE-K8S-0301-003.md) | PodSecurityPolicy to PSA migration | Foundational | baseline |
| [SAFE-K8S-0301-004](markdown/controls/SAFE-K8S-0301-004.md) | PSA exemption management for privileged system and GPU workloads | Foundational | ai-specific |
| [SAFE-K8S-0301-005](markdown/controls/SAFE-K8S-0301-005.md) | PSA exemption register and justification tracking | Foundational | ai-specific |
| [SAFE-K8S-0301-006](markdown/controls/SAFE-K8S-0301-006.md) | Scoped PSA exception enforcement and compensating controls | Foundational | ai-specific |

<a id="knowledge-area-3-2"></a>
## 3.2 - Security Contexts and Capabilities

- Domain: D03 - Workload and Pod Security
- Maturity: Foundational
- Controls: 7

### Description

Pod and container security context configuration: runAsNonRoot, runAsUser, readOnlyRootFilesystem, allowPrivilegeEscalation Linux capability management: dropping ALL capabilities, adding only required capabilities, understanding capability implications (including elevated capabilities required for GPU access vs. least-privilege alternatives) Privilege escalation prevention: no-new-privileges flag, UID/GID management, filesystem ownership controls Host namespace restrictions: hostPID, hostIPC, hostNetwork controls and their security implications AI workload security context patterns: seccomp/AppArmor profiles tailored to GPU workload syscall patterns (GPU ioctl, shared memory, RDMA), read-only root filesystems and non-root execution for inference servers and training jobs

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0302-001](markdown/controls/SAFE-K8S-0302-001.md) | Pod and container security context enforcement | Foundational | baseline |
| [SAFE-K8S-0302-002](markdown/controls/SAFE-K8S-0302-002.md) | Linux capability drop-all and least-privilege add-back | Foundational | ai-specific |
| [SAFE-K8S-0302-003](markdown/controls/SAFE-K8S-0302-003.md) | Privilege escalation prevention controls | Foundational | baseline |
| [SAFE-K8S-0302-004](markdown/controls/SAFE-K8S-0302-004.md) | Host namespace isolation enforcement | Foundational | baseline |
| [SAFE-K8S-0302-005](markdown/controls/SAFE-K8S-0302-005.md) | AI workload security context hardening profiles | Foundational | ai-specific |
| [SAFE-K8S-0302-006](markdown/controls/SAFE-K8S-0302-006.md) | No-new-privileges execution enforcement | Foundational | baseline |
| [SAFE-K8S-0302-007](markdown/controls/SAFE-K8S-0302-007.md) | Safe fsGroup and supplementalGroups volume ownership | Foundational | baseline |

<a id="knowledge-area-3-3"></a>
## 3.3 - Mandatory Access Controls

- Domain: D03 - Workload and Pod Security
- Maturity: Practitioner
- Controls: 8

### Description

Seccomp profile enforcement: RuntimeDefault profile, custom profiles for specific workloads, profile auditing and generation AppArmor profile management: loading profiles on nodes, annotating pods, profile development for Kubernetes workloads SELinux context assignment for containers: MCS labels, type enforcement, and multi-tenancy isolation through SELinux Profile creation workflows: generating profiles from runtime behavior, testing in audit mode, iterative refinement

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0303-001](markdown/controls/SAFE-K8S-0303-001.md) | Seccomp profile enforcement | Practitioner | baseline |
| [SAFE-K8S-0303-002](markdown/controls/SAFE-K8S-0303-002.md) | AppArmor profile management and enforcement | Practitioner | baseline |
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
- Controls: 13

### Description

Cloud Native 8 secure defaults: applying the CNCF-recommended baseline security principles to Kubernetes workloads Resource limits and requests: CPU, memory, and ephemeral storage constraints for workload stability and noisy-neighbor prevention Quality of Service (QoS) classes: Guaranteed, Burstable, BestEffort - security implications of eviction behavior Ephemeral container security controls, host volume restriction, and service account token opt-out for pods that do not need API access Ephemeral storage and scratch space controls for training jobs: emptyDir size limits, tmpfs for sensitive intermediate data, and temporary checkpoint storage security

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0304-001](markdown/controls/SAFE-K8S-0304-001.md) | Cloud Native 8 secure defaults enforcement | Foundational | baseline |
| [SAFE-K8S-0304-002](markdown/controls/SAFE-K8S-0304-002.md) | CPU, memory, and ephemeral storage resource limits | Foundational | baseline |
| [SAFE-K8S-0304-003](markdown/controls/SAFE-K8S-0304-003.md) | QoS class assignment for workload stability | Foundational | baseline |
| [SAFE-K8S-0304-004](markdown/controls/SAFE-K8S-0304-004.md) | Ephemeral container security context enforcement | Foundational | baseline |
| [SAFE-K8S-0304-005](markdown/controls/SAFE-K8S-0304-005.md) | Training job ephemeral storage and scratch space security | Foundational | ai-specific |
| [SAFE-K8S-0304-006](markdown/controls/SAFE-K8S-0304-006.md) | Host volume mount restriction | Foundational | baseline |
| [SAFE-K8S-0304-007](markdown/controls/SAFE-K8S-0304-007.md) | Service account token automount opt-out | Foundational | baseline |
| [SAFE-K8S-0304-008](markdown/controls/SAFE-K8S-0304-008.md) | Training scratch volume limits and tmpfs handling | Foundational | ai-specific |
| [SAFE-K8S-0304-009](markdown/controls/SAFE-K8S-0304-009.md) | Temporary checkpoint storage encryption, integrity, and access control | Foundational | ai-specific |
| [SAFE-K8S-0304-010](markdown/controls/SAFE-K8S-0304-010.md) | Pod resource requests and limits specification | Foundational | baseline |
| [SAFE-K8S-0304-011](markdown/controls/SAFE-K8S-0304-011.md) | Namespace LimitRange and ResourceQuota enforcement | Foundational | baseline |
| [SAFE-K8S-0304-012](markdown/controls/SAFE-K8S-0304-012.md) | Training scratch volume size limits and ephemeral-storage quotas | Foundational | baseline |
| [SAFE-K8S-0304-013](markdown/controls/SAFE-K8S-0304-013.md) | Tmpfs-backed handling for sensitive training intermediates | Foundational | baseline |

<a id="knowledge-area-4-1"></a>
## 4.1 - Role-Based Access Control (RBAC)

- Domain: D04 - Identity, Access, and Secrets Management
- Maturity: Foundational
- Controls: 7

### Description

RBAC primitives: Roles, ClusterRoles, RoleBindings, ClusterRoleBindings - design for least-privilege access Permission audit and analysis: identifying overly permissive roles, detecting privilege escalation paths, RBAC tooling (rakkess, kubectl-who-can) Aggregated ClusterRole management: understanding controller-managed role aggregation and preventing unintended permission grants RBAC for custom resources: securing access to AI operators' CRDs (InferenceService, TrainingJob, RayCluster, PodGroup) Separation of duties between ML engineers (model deployment), platform engineers (cluster config), and security teams (policy enforcement); RBAC for GPU resource management (who can request GPU quotas, override scheduling priorities, access GPU metrics)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0401-001](markdown/controls/SAFE-K8S-0401-001.md) | RBAC least-privilege design | Foundational | baseline |
| [SAFE-K8S-0401-002](markdown/controls/SAFE-K8S-0401-002.md) | RBAC permission audit and analysis | Foundational | baseline |
| [SAFE-K8S-0401-003](markdown/controls/SAFE-K8S-0401-003.md) | Aggregated ClusterRole governance | Foundational | baseline |
| [SAFE-K8S-0401-004](markdown/controls/SAFE-K8S-0401-004.md) | RBAC for AI operator custom resources | Foundational | ai-specific |
| [SAFE-K8S-0401-005](markdown/controls/SAFE-K8S-0401-005.md) | Separation of duties for ML, platform, and security roles | Foundational | ai-specific |
| [SAFE-K8S-0401-006](markdown/controls/SAFE-K8S-0401-006.md) | Organizational role separation for ML, platform, and security functions | Foundational | ai-specific |
| [SAFE-K8S-0401-007](markdown/controls/SAFE-K8S-0401-007.md) | GPU resource governance permission boundaries | Foundational | ai-specific |

<a id="knowledge-area-4-2"></a>
## 4.2 - Service Accounts and Workload Identity

- Domain: D04 - Identity, Access, and Secrets Management
- Maturity: Practitioner
- Controls: 23

### Description

Default service account restrictions: disabling auto-mount of service account tokens, creating dedicated service accounts per workload Inactive service account identification and disabling, stale credential revocation Preventing service account identifiers from public exposure Identity attribute maintenance and protection for workload identities Projected service account tokens: audience-scoped, time-bound tokens replacing legacy static tokens Workload identity federation with cloud providers: GKE Workload Identity, EKS IRSA/Pod Identity, AKS Workload Identity for secure cloud service access (model registries, data lakes, feature stores) OIDC integration for Kubernetes authentication: external identity provider configuration, token validation, group mappings AI workload identity patterns: pod identity assignment for training jobs, inference servers, and pipeline components with distinct access needs Identity lifecycle management for ephemeral training jobs: short-lived credentials, automatic rotation, cleanup on job completion Cross-cluster and cross-cloud cryptographic identity federation for federated training and multi-cluster inference: SPIFFE/SPIRE trust domain federation (hub-spoke, mesh, and hierarchical topologies), trust bundle exchange and rotation, cloud-native cross-account trust (AWS cross-account roles with IRSA, GCP cross-project service account impersonation, Azure cross-subscription workload identity), hybrid cloud identity bridging via OIDC federation from on-premises SPIRE to cloud IAM, credential lifecycle for cross-cluster workloads, federation audit trail, trust boundary inventory, and break-glass trust revocation procedures Prohibition on shared static credentials or replicated secrets for cross-environment access in federated training and multi-cluster inference: identification of prohibited credential patterns (replicated kubeconfigs, long-lived cross-cluster tokens, shared API keys), admission control enforcement, periodic credential scanning, CI/CD pipeline gates, and remediation path for migrating from static credentials to federated mechanisms

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0402-001](markdown/controls/SAFE-K8S-0402-001.md) | Default service account restriction | Foundational | baseline |
| [SAFE-K8S-0402-002](markdown/controls/SAFE-K8S-0402-002.md) | Inactive service account and stale credential remediation | Practitioner | baseline |
| [SAFE-K8S-0402-003](markdown/controls/SAFE-K8S-0402-003.md) | Service account identifier exposure prevention | Practitioner | baseline |
| [SAFE-K8S-0402-004](markdown/controls/SAFE-K8S-0402-004.md) | Workload identity attribute integrity | Practitioner | baseline |
| [SAFE-K8S-0402-005](markdown/controls/SAFE-K8S-0402-005.md) | Projected service account token configuration | Foundational | baseline |
| [SAFE-K8S-0402-006](markdown/controls/SAFE-K8S-0402-006.md) | Cloud workload identity federation for AI services | Practitioner | ai-specific |
| [SAFE-K8S-0402-007](markdown/controls/SAFE-K8S-0402-007.md) | OIDC authentication integration | Practitioner | baseline |
| [SAFE-K8S-0402-008](markdown/controls/SAFE-K8S-0402-008.md) | Distinct identity assignment for AI workload types | Practitioner | ai-specific |
| [SAFE-K8S-0402-009](markdown/controls/SAFE-K8S-0402-009.md) | Ephemeral training job credential lifecycle management | Practitioner | ai-specific |
| [SAFE-K8S-0402-010](markdown/controls/SAFE-K8S-0402-010.md) | Cross-cluster and cross-cloud cryptographic identity federation | Advanced | ai-specific |
| [SAFE-K8S-0402-011](markdown/controls/SAFE-K8S-0402-011.md) | Cross-environment static credential prohibition | Advanced | ai-specific |
| [SAFE-K8S-0402-012](markdown/controls/SAFE-K8S-0402-012.md) | Ephemeral training job credential expiration | Practitioner | ai-specific |
| [SAFE-K8S-0402-013](markdown/controls/SAFE-K8S-0402-013.md) | Ephemeral training job credential rotation | Practitioner | ai-specific |
| [SAFE-K8S-0402-014](markdown/controls/SAFE-K8S-0402-014.md) | Ephemeral training job credential revocation on completion | Practitioner | ai-specific |
| [SAFE-K8S-0402-015](markdown/controls/SAFE-K8S-0402-015.md) | Legacy service account token secret removal | Foundational | baseline |
| [SAFE-K8S-0402-016](markdown/controls/SAFE-K8S-0402-016.md) | Projected service account token audience and TokenRequest enforcement | Foundational | baseline |
| [SAFE-K8S-0402-017](markdown/controls/SAFE-K8S-0402-017.md) | Projected token lifetime bounds and long-lived token exception governance | Foundational | baseline |
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
- Controls: 30

### Description

Kubernetes Secrets encryption at rest: EncryptionConfiguration with KMS providers (AWS KMS, GCP KMS, Azure Key Vault, HashiCorp Vault) External secrets management: External Secrets Operator, Vault CSI Provider, cloud-native secret stores with automatic sync and rotation Secret injection patterns: environment variables vs. volume mounts vs. init containers vs. sidecar agents - security tradeoffs Secret lifecycle management: rotation policies, expiration enforcement, revocation procedures, and leak detection Prevention of secret leakage through training logs, model artifacts, checkpoint files, and pipeline metadata; secrets management for model registry credentials, training data access tokens, and API keys used by inference endpoints Per-workload credential scoping for AI jobs: resource-level IAM policies, Vault templated paths, and admission enforcement ensuring each training job, inference server, and pipeline step receives credentials scoped to exactly the storage prefixes, model repositories, and API endpoints it requires AI platform key hierarchy and envelope encryption architecture: structured key hierarchy using envelope encryption with distinct key domains for training data, model artifacts, model signing, and inference payloads ensuring compromise of one domain does not propagate to others HSM-backed root key protection for AI platform KMS: root keys and KEKs protected by HSMs with FIPS 140-2 Level 3 or higher certification, key material non-exportable outside HSM boundary, HSM attestation records maintained for audit Per-domain automated key rotation for AI platform: domain-specific rotation schedules reflecting risk profile (inference payload keys more frequent than signing keys), automated rotation with workload health verification, rotation monitoring and alerting Key access policy separation between AI pipeline environments: KMS policies enforcing strict separation between training, serving, and governance identities, preventing cross-domain key access, with audit-only governance access and monitoring for policy violations Credential inventory and sprawl governance at scale: automated tracking of all active AI workload credentials, orphaned credential detection for completed jobs, credential scope drift monitoring, and lifecycle metrics dashboards for governing credential sprawl across AI platforms

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0403-001](markdown/controls/SAFE-K8S-0403-001.md) | Kubernetes Secrets external KMS integration and key lifecycle | Foundational | baseline |
| [SAFE-K8S-0403-002](markdown/controls/SAFE-K8S-0403-002.md) | External secrets management integration | Foundational | baseline |
| [SAFE-K8S-0403-003](markdown/controls/SAFE-K8S-0403-003.md) | Approved secret injection pattern standards | Foundational | baseline |
| [SAFE-K8S-0403-004](markdown/controls/SAFE-K8S-0403-004.md) | Secret rotation and expiration enforcement | Foundational | baseline |
| [SAFE-K8S-0403-005](markdown/controls/SAFE-K8S-0403-005.md) | AI pipeline secret leakage prevention | Foundational | ai-specific |
| [SAFE-K8S-0403-006](markdown/controls/SAFE-K8S-0403-006.md) | Per-workload credential scoping for AI jobs | Practitioner | ai-specific |
| [SAFE-K8S-0403-007](markdown/controls/SAFE-K8S-0403-007.md) | AI platform key hierarchy and KMS architecture | Advanced | ai-specific |
| [SAFE-K8S-0403-008](markdown/controls/SAFE-K8S-0403-008.md) | Credential inventory and sprawl governance at scale | Practitioner | ai-specific |
| [SAFE-K8S-0403-009](markdown/controls/SAFE-K8S-0403-009.md) | Automated secret leak detection and response | Practitioner | baseline |
| [SAFE-K8S-0403-010](markdown/controls/SAFE-K8S-0403-010.md) | Kubernetes Secrets external KMS integration and least-privilege key policy | Foundational | baseline |
| [SAFE-K8S-0403-011](markdown/controls/SAFE-K8S-0403-011.md) | Secrets KMS key rotation and re-encryption verification | Foundational | baseline |
| [SAFE-K8S-0403-012](markdown/controls/SAFE-K8S-0403-012.md) | Automated credential inventory and orphaned credential reconciliation | Practitioner | ai-specific |
| [SAFE-K8S-0403-013](markdown/controls/SAFE-K8S-0403-013.md) | Credential scope drift monitoring and lifecycle metrics governance | Practitioner | ai-specific |
| [SAFE-K8S-0403-014](markdown/controls/SAFE-K8S-0403-014.md) | Automated secret leak detection coverage and enforcement | Practitioner | baseline |
| [SAFE-K8S-0403-015](markdown/controls/SAFE-K8S-0403-015.md) | Secret leak incident response and credential revocation | Practitioner | baseline |
| [SAFE-K8S-0403-016](markdown/controls/SAFE-K8S-0403-016.md) | Environment variable secret injection prohibition and exception governance | Foundational | baseline |
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
- Controls: 10

### Description

cert-manager deployment and configuration: Issuers, ClusterIssuers, Certificate resources, ACME integration TLS certificate provisioning for webhooks, API aggregation, and internal service communication mTLS bootstrapping for service-to-service authentication within the cluster Certificate rotation automation, expiry monitoring, and incident response for compromised certificates

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0404-001](markdown/controls/SAFE-K8S-0404-001.md) | cert-manager deployment and Issuer configuration | Practitioner | baseline |
| [SAFE-K8S-0404-002](markdown/controls/SAFE-K8S-0404-002.md) | TLS provisioning for webhooks, API aggregation, and internal services | Practitioner | baseline |
| [SAFE-K8S-0404-003](markdown/controls/SAFE-K8S-0404-003.md) | mTLS for service-to-service authentication | Practitioner | baseline |
| [SAFE-K8S-0404-004](markdown/controls/SAFE-K8S-0404-004.md) | Certificate rotation, expiry monitoring, and compromise response | Practitioner | baseline |
| [SAFE-K8S-0404-005](markdown/controls/SAFE-K8S-0404-005.md) | Certificate rotation execution and expiry monitoring | Practitioner | baseline |
| [SAFE-K8S-0404-006](markdown/controls/SAFE-K8S-0404-006.md) | Certificate compromise revocation and re-issuance response | Practitioner | baseline |
| [SAFE-K8S-0404-007](markdown/controls/SAFE-K8S-0404-007.md) | Automated certificate rotation before expiry | Practitioner | baseline |
| [SAFE-K8S-0404-008](markdown/controls/SAFE-K8S-0404-008.md) | Certificate expiry monitoring and alerting | Practitioner | baseline |
| [SAFE-K8S-0404-009](markdown/controls/SAFE-K8S-0404-009.md) | Compromised certificate revocation and re-issuance execution | Practitioner | baseline |
| [SAFE-K8S-0404-010](markdown/controls/SAFE-K8S-0404-010.md) | Post-compromise certificate recovery validation | Practitioner | baseline |

<a id="knowledge-area-4-5"></a>
## 4.5 - Identity Abuse Detection and Mitigation

- Domain: D04 - Identity, Access, and Secrets Management
- Maturity: Practitioner
- Controls: 24

### Description

Impersonation control: restricting and auditing the use of Kubernetes API impersonation headers Privilege escalation detection: monitoring for RBAC changes, service account token theft, and unauthorized cluster-admin usage kubeconfig hygiene: secure storage, credential expiry, context management, and kubeconfig audit for shared environments Operator security awareness: recognizing social engineering and credential phishing targeting Kubernetes administrators (kubeconfig theft, cloud console credential harvesting, CI/CD token exfiltration); security awareness requirements for personnel with cluster-admin or GPU resource access Credential management best practices and DoS/availability controls for authentication endpoints (see Appendix A: Identity Governance Patterns) Attribute-based access control for AI artifacts based on data classification, model sensitivity, and deployment environment (see Appendix A: Identity Governance Patterns)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0405-001](markdown/controls/SAFE-K8S-0405-001.md) | API impersonation restriction and auditing | Practitioner | baseline |
| [SAFE-K8S-0405-002](markdown/controls/SAFE-K8S-0405-002.md) | Privilege escalation detection and monitoring | Practitioner | baseline |
| [SAFE-K8S-0405-003](markdown/controls/SAFE-K8S-0405-003.md) | Kubeconfig security and hygiene | Practitioner | baseline |
| [SAFE-K8S-0405-004](markdown/controls/SAFE-K8S-0405-004.md) | Security awareness for Kubernetes and GPU administrators | Practitioner | baseline |
| [SAFE-K8S-0405-005](markdown/controls/SAFE-K8S-0405-005.md) | Credential management and multi-factor authentication | Practitioner | baseline |
| [SAFE-K8S-0405-006](markdown/controls/SAFE-K8S-0405-006.md) | Attribute-based access control for AI artifacts | Advanced | ai-specific |
| [SAFE-K8S-0405-007](markdown/controls/SAFE-K8S-0405-007.md) | Authentication endpoint availability and DoS protection | Practitioner | baseline |
| [SAFE-K8S-0405-008](markdown/controls/SAFE-K8S-0405-008.md) | Break-glass emergency access procedures | Practitioner | baseline |
| [SAFE-K8S-0405-009](markdown/controls/SAFE-K8S-0405-009.md) | API impersonation RBAC restriction | Practitioner | baseline |
| [SAFE-K8S-0405-010](markdown/controls/SAFE-K8S-0405-010.md) | API impersonation audit logging and alerting | Practitioner | baseline |
| [SAFE-K8S-0405-011](markdown/controls/SAFE-K8S-0405-011.md) | Credential policy and secure storage governance | Practitioner | baseline |
| [SAFE-K8S-0405-012](markdown/controls/SAFE-K8S-0405-012.md) | Privileged MFA enforcement for cluster administration | Practitioner | baseline |
| [SAFE-K8S-0405-013](markdown/controls/SAFE-K8S-0405-013.md) | Break-glass recovery procedure definition and testing | Practitioner | baseline |
| [SAFE-K8S-0405-014](markdown/controls/SAFE-K8S-0405-014.md) | Break-glass access auditing, dual-authorization, and automatic expiration | Practitioner | baseline |
| [SAFE-K8S-0405-015](markdown/controls/SAFE-K8S-0405-015.md) | Break-glass dual-authorization and tenant-scoped activation guardrails | Practitioner | baseline |
| [SAFE-K8S-0405-016](markdown/controls/SAFE-K8S-0405-016.md) | Break-glass access audit logging and automatic expiration | Practitioner | baseline |
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
- Controls: 9

### Description

Default deny ingress and egress policies as namespace security baselines Namespace isolation patterns: restricting cross-namespace communication while allowing required system services (DNS, monitoring) Egress controls: restricting outbound access by workload, allowing only required external endpoints, DNS-based egress policies CNI-specific network policy extensions: Cilium CiliumNetworkPolicy, Calico GlobalNetworkPolicy, advanced L7 policies AI workload network segmentation: microsegmentation between training, inference, pipeline, and notebook workloads; isolation of model download paths from training data paths to prevent cross-contamination; east-west traffic monitoring between AI workloads for anomalous communication patterns Multi-cluster network segmentation for federated AI workloads: cross-cluster network models (multi-cluster service mesh, Kubernetes Multi-Cluster Services API, VPN/interconnect with gateway pods, API gateway federation), cross-cluster communication matrix definition and enforcement, Cilium Cluster Mesh and Istio multi-cluster policy for AI traffic, gateway-based segmentation with identity-aware routing, cross-cluster egress restriction for federated learning participants, unified cross-cluster flow logging and anomaly detection, cross-cluster network policy audit and connectivity testing

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0501-001](markdown/controls/SAFE-K8S-0501-001.md) | Default deny ingress and egress network policies | Foundational | baseline |
| [SAFE-K8S-0501-002](markdown/controls/SAFE-K8S-0501-002.md) | Namespace network isolation patterns | Foundational | baseline |
| [SAFE-K8S-0501-003](markdown/controls/SAFE-K8S-0501-003.md) | Workload egress controls | Foundational | baseline |
| [SAFE-K8S-0501-004](markdown/controls/SAFE-K8S-0501-004.md) | CNI-specific network policy extensions | Practitioner | baseline |
| [SAFE-K8S-0501-005](markdown/controls/SAFE-K8S-0501-005.md) | AI workload network segmentation | Foundational | ai-specific |
| [SAFE-K8S-0501-006](markdown/controls/SAFE-K8S-0501-006.md) | Multi-cluster network segmentation for federated AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0501-007](markdown/controls/SAFE-K8S-0501-007.md) | East-west AI workload traffic monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0501-008](markdown/controls/SAFE-K8S-0501-008.md) | AI workload type network microsegmentation | Foundational | ai-specific |
| [SAFE-K8S-0501-009](markdown/controls/SAFE-K8S-0501-009.md) | Model download path isolation from training data paths | Foundational | ai-specific |

<a id="knowledge-area-5-2"></a>
## 5.2 - CNI Plugins and Pod Networking Security

- Domain: D05 - Network Security and Communication
- Maturity: Practitioner
- Controls: 10

### Description

CNI plugin selection criteria: security features, network policy support, encryption capabilities, performance characteristics Pod-to-pod encryption: WireGuard (Cilium, Calico), IPsec, and transparent encryption for in-transit data protection IPAM security: IP address management, IP exhaustion prevention, and IP spoofing protection CNI plugin hardening: configuration baselines, vulnerability management, and upgrade procedures Data path encryption between compute nodes and storage backends for training and inference workloads; network policy design for AI-specific traffic patterns (NCCL inter-node training communication, model download paths, inference traffic)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0502-001](markdown/controls/SAFE-K8S-0502-001.md) | CNI plugin security selection criteria | Practitioner | baseline |
| [SAFE-K8S-0502-002](markdown/controls/SAFE-K8S-0502-002.md) | Pod-to-pod traffic encryption | Practitioner | baseline |
| [SAFE-K8S-0502-003](markdown/controls/SAFE-K8S-0502-003.md) | IPAM security and IP spoofing protection | Practitioner | baseline |
| [SAFE-K8S-0502-004](markdown/controls/SAFE-K8S-0502-004.md) | CNI plugin hardening and lifecycle management | Practitioner | baseline |
| [SAFE-K8S-0502-005](markdown/controls/SAFE-K8S-0502-005.md) | AI workload data path encryption in transit | Practitioner | ai-specific |
| [SAFE-K8S-0502-006](markdown/controls/SAFE-K8S-0502-006.md) | Kubernetes CNI IPAM capacity sizing and exhaustion monitoring | Practitioner | baseline |
| [SAFE-K8S-0502-007](markdown/controls/SAFE-K8S-0502-007.md) | Kubernetes pod IP anti-spoofing enforcement and validation | Practitioner | baseline |
| [SAFE-K8S-0502-008](markdown/controls/SAFE-K8S-0502-008.md) | Network policy design for AI-specific traffic patterns | Practitioner | ai-specific |
| [SAFE-K8S-0502-009](markdown/controls/SAFE-K8S-0502-009.md) | Kubernetes CNI IPAM capacity sizing | Practitioner | baseline |
| [SAFE-K8S-0502-010](markdown/controls/SAFE-K8S-0502-010.md) | Kubernetes CNI IP pool exhaustion monitoring and alerting | Practitioner | baseline |

<a id="knowledge-area-5-3"></a>
## 5.3 - Ingress, Egress, and DNS Hardening

- Domain: D05 - Network Security and Communication
- Maturity: Practitioner
- Controls: 16

### Description

Ingress controller hardening: TLS termination configuration, WAF integration, request filtering, and rate limiting DNS security: CoreDNS configuration, DNS policy enforcement, DNS-based service discovery security, and DNS exfiltration prevention External traffic policy: Local vs. Cluster traffic routing, source IP preservation, and client IP-based access controls LoadBalancer and NodePort security: restricting service exposure, internal load balancer annotations, and cloud load balancer security groups

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0503-001](markdown/controls/SAFE-K8S-0503-001.md) | Ingress controller hardening | Practitioner | baseline |
| [SAFE-K8S-0503-002](markdown/controls/SAFE-K8S-0503-002.md) | DNS infrastructure hardening | Practitioner | baseline |
| [SAFE-K8S-0503-003](markdown/controls/SAFE-K8S-0503-003.md) | External traffic policy and source IP preservation | Practitioner | baseline |
| [SAFE-K8S-0503-004](markdown/controls/SAFE-K8S-0503-004.md) | Internal load balancer annotation enforcement | Practitioner | baseline |
| [SAFE-K8S-0503-005](markdown/controls/SAFE-K8S-0503-005.md) | DNS exfiltration detection | Practitioner | baseline |
| [SAFE-K8S-0503-006](markdown/controls/SAFE-K8S-0503-006.md) | Cloud load balancer security group configuration | Practitioner | baseline |
| [SAFE-K8S-0503-007](markdown/controls/SAFE-K8S-0503-007.md) | Ingress TLS termination and boundary configuration hardening | Practitioner | baseline |
| [SAFE-K8S-0503-008](markdown/controls/SAFE-K8S-0503-008.md) | Ingress WAF integration and rate limiting | Practitioner | baseline |
| [SAFE-K8S-0503-009](markdown/controls/SAFE-K8S-0503-009.md) | CoreDNS and upstream resolver hardening | Practitioner | baseline |
| [SAFE-K8S-0503-010](markdown/controls/SAFE-K8S-0503-010.md) | DNS resolution path enforcement and namespace-scoped service discovery | Practitioner | baseline |
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
- Controls: 9

### Description

Zero trust architecture principles for Kubernetes: identity-centric access, continuous verification, microsegmentation, least-privilege networking Service mesh deployment and security: Istio, Linkerd, or Cilium service mesh for automatic mTLS, authorization policies, and traffic observability SPIFFE/SPIRE for workload identity: cryptographic identity issuance, trust domain management, and cross-cluster identity federation Microsegmentation beyond network policies: L7 authorization, service-level access control, and API-aware security policies Service mesh considerations for AI workloads: mTLS overhead on high-throughput GPU training traffic, sidecar resource consumption impact on GPU workloads, and ingress/API gateway hardening for model serving endpoints

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0504-001](markdown/controls/SAFE-K8S-0504-001.md) | Zero trust networking principles for Kubernetes | Practitioner | baseline |
| [SAFE-K8S-0504-002](markdown/controls/SAFE-K8S-0504-002.md) | Service mesh mTLS and authorization policies | Practitioner | baseline |
| [SAFE-K8S-0504-003](markdown/controls/SAFE-K8S-0504-003.md) | SPIFFE/SPIRE workload identity management | Advanced | baseline |
| [SAFE-K8S-0504-004](markdown/controls/SAFE-K8S-0504-004.md) | L7 microsegmentation and API-aware policies | Practitioner | baseline |
| [SAFE-K8S-0504-005](markdown/controls/SAFE-K8S-0504-005.md) | Service mesh tuning for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0504-006](markdown/controls/SAFE-K8S-0504-006.md) | SPIFFE/SPIRE workload identity issuance and lifecycle management | Advanced | baseline |
| [SAFE-K8S-0504-007](markdown/controls/SAFE-K8S-0504-007.md) | SPIFFE trust domain scoping and cross-cluster federation governance | Advanced | baseline |
| [SAFE-K8S-0504-008](markdown/controls/SAFE-K8S-0504-008.md) | L7 service authorization policy enforcement | Practitioner | baseline |
| [SAFE-K8S-0504-009](markdown/controls/SAFE-K8S-0504-009.md) | API-aware request contract validation | Practitioner | baseline |

<a id="knowledge-area-5-5"></a>
## 5.5 - API Server and Service Exposure Protection

- Domain: D05 - Network Security and Communication
- Maturity: Practitioner
- Controls: 7

### Description

API server network access: restricting access to control plane endpoints, private cluster configuration, bastion host patterns LoadBalancer and NodePort restriction policies: preventing unintended service exposure to the internet Internal service endpoint protection: ClusterIP services, headless services, and service account-based access patterns API server audit log analysis for network-based attack detection and unauthorized access attempts

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0505-001](markdown/controls/SAFE-K8S-0505-001.md) | API server network access restriction | Practitioner | baseline |
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
- Controls: 23

### Description

Base image selection and hardening: minimal images (distroless, scratch), multi-stage builds, unnecessary package removal; AI-specific base image considerations (CUDA base images, ML framework images, inference server images) and GPU compatibility constraints Container image vulnerability scanning: integration with CI/CD, registry-level scanning, runtime scanning; vulnerability scanning for AI-specific dependencies (PyTorch, TensorFlow, JAX, ONNX Runtime, Triton) and their native library chains Registry access controls: authentication, authorization, network restrictions, and image pull secrets management Image hardening practices: non-root users, read-only filesystems, no shell binaries, and minimal attack surface; minimal image construction for inference (distroless, multi-stage builds) to reduce attack surface while maintaining GPU compatibility

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0601-001](markdown/controls/SAFE-K8S-0601-001.md) | Base image selection and hardening | Practitioner | ai-specific |
| [SAFE-K8S-0601-002](markdown/controls/SAFE-K8S-0601-002.md) | Container image vulnerability scanning | Practitioner | ai-specific |
| [SAFE-K8S-0601-003](markdown/controls/SAFE-K8S-0601-003.md) | Registry access controls | Practitioner | baseline |
| [SAFE-K8S-0601-004](markdown/controls/SAFE-K8S-0601-004.md) | Image hardening practices | Practitioner | ai-specific |
| [SAFE-K8S-0601-005](markdown/controls/SAFE-K8S-0601-005.md) | Container image and artifact retention policy | Practitioner | baseline |
| [SAFE-K8S-0601-006](markdown/controls/SAFE-K8S-0601-006.md) | Approved minimal base images and multi-stage build hardening | Practitioner | ai-specific |
| [SAFE-K8S-0601-007](markdown/controls/SAFE-K8S-0601-007.md) | AI GPU and ML framework base image validation | Practitioner | ai-specific |
| [SAFE-K8S-0601-008](markdown/controls/SAFE-K8S-0601-008.md) | CI/CD build-time container image vulnerability scanning | Practitioner | ai-specific |
| [SAFE-K8S-0601-009](markdown/controls/SAFE-K8S-0601-009.md) | Registry and runtime container vulnerability monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0601-010](markdown/controls/SAFE-K8S-0601-010.md) | Artifact retention period and lifecycle enforcement | Practitioner | baseline |
| [SAFE-K8S-0601-011](markdown/controls/SAFE-K8S-0601-011.md) | Integrity metadata co-retention with software artifacts | Practitioner | baseline |
| [SAFE-K8S-0601-012](markdown/controls/SAFE-K8S-0601-012.md) | Container registry authentication, authorization, and network restriction | Practitioner | baseline |
| [SAFE-K8S-0601-013](markdown/controls/SAFE-K8S-0601-013.md) | Kubernetes image pull secret management and rotation | Practitioner | baseline |
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
- Controls: 7

### Description

Sigstore/cosign keyless signing with Fulcio, signature storage in Rekor transparency log, verification workflows Notary v2 (notation) trust policy configuration, signature verification, and registry integration Admission enforcement of image signatures: configuring admission controllers (Kyverno, OPA/Gatekeeper, Sigstore policy-controller) to reject unsigned images

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0602-001](markdown/controls/SAFE-K8S-0602-001.md) | Sigstore/cosign keyless signing and Rekor transparency logging | Practitioner | baseline |
| [SAFE-K8S-0602-002](markdown/controls/SAFE-K8S-0602-002.md) | Notary v2 (notation) trust policy and signature verification | Practitioner | baseline |
| [SAFE-K8S-0602-003](markdown/controls/SAFE-K8S-0602-003.md) | Admission enforcement of image signatures | Practitioner | baseline |
| [SAFE-K8S-0602-004](markdown/controls/SAFE-K8S-0602-004.md) | Notary v2 trust policy and signing identity governance | Practitioner | baseline |
| [SAFE-K8S-0602-005](markdown/controls/SAFE-K8S-0602-005.md) | Notary v2 OCI signature artifact registry integration | Practitioner | baseline |
| [SAFE-K8S-0602-006](markdown/controls/SAFE-K8S-0602-006.md) | Fail-closed admission enforcement of image signature verification | Practitioner | baseline |
| [SAFE-K8S-0602-007](markdown/controls/SAFE-K8S-0602-007.md) | Admission signature bypass and emergency break-glass governance | Practitioner | baseline |

<a id="knowledge-area-6-3"></a>
## 6.3 - Attestation, Provenance, and Cryptographic Assurance

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Advanced
- Controls: 14

### Description

Artifact attestation: in-toto attestations, SBOMit, SLSA provenance, and build-time metadata attached to container images Build attestation taxonomy per NIST SP 800-204D: environment attestation (build platform inventory), process attestation (build tools and transformations), materials attestation (source inputs and dependencies), and artifacts attestation (build outputs and intermediate products) Attestation policy evaluation: signed policies that encode artifact requirements, lifecycle compliance tracing through attestation verification at each pipeline stage, and policy-based admission decisions grounded in verified attestation chains Cryptographic agility and post-quantum readiness: algorithm selection for long-lived model artifacts, migration planning for post-quantum signature schemes, and hashing/signing coverage across the full ML lifecycle (inputs, models, outputs, intermediate artifacts) Cryptographic module authentication and validation requirements (FIPS 140 compliance for signing and verification operations) TUF (The Update Framework) for secure software update systems: threshold and quorum trust for signing keys, HSM-based key storage for online signing roles, key rotation procedures, and protection against known attacks on software update metadata

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0603-001](markdown/controls/SAFE-K8S-0603-001.md) | Artifact attestation with in-toto and SLSA provenance | Advanced | baseline |
| [SAFE-K8S-0603-002](markdown/controls/SAFE-K8S-0603-002.md) | Build attestation taxonomy per NIST SP 800-204D | Advanced | baseline |
| [SAFE-K8S-0603-003](markdown/controls/SAFE-K8S-0603-003.md) | Attestation policy evaluation and lifecycle compliance | Advanced | baseline |
| [SAFE-K8S-0603-004](markdown/controls/SAFE-K8S-0603-004.md) | Cryptographic agility and post-quantum readiness | Advanced | ai-specific |
| [SAFE-K8S-0603-005](markdown/controls/SAFE-K8S-0603-005.md) | FIPS 140 cryptographic module validation | Practitioner | baseline |
| [SAFE-K8S-0603-006](markdown/controls/SAFE-K8S-0603-006.md) | TUF-based secure software update systems | Advanced | baseline |
| [SAFE-K8S-0603-007](markdown/controls/SAFE-K8S-0603-007.md) | Build environment and process attestations per NIST SP 800-204D | Advanced | baseline |
| [SAFE-K8S-0603-008](markdown/controls/SAFE-K8S-0603-008.md) | Build materials and artifact attestations per NIST SP 800-204D | Advanced | baseline |
| [SAFE-K8S-0603-009](markdown/controls/SAFE-K8S-0603-009.md) | In-toto and SLSA provenance attestation generation | Advanced | baseline |
| [SAFE-K8S-0603-010](markdown/controls/SAFE-K8S-0603-010.md) | SBOM attestation binding to image digests | Advanced | baseline |
| [SAFE-K8S-0603-011](markdown/controls/SAFE-K8S-0603-011.md) | Attestation policy definition, signing, and change governance | Advanced | baseline |
| [SAFE-K8S-0603-012](markdown/controls/SAFE-K8S-0603-012.md) | Lifecycle attestation verification and admission enforcement | Advanced | baseline |
| [SAFE-K8S-0603-013](markdown/controls/SAFE-K8S-0603-013.md) | Lifecycle attestation chain verification across build, promote, and deploy | Advanced | baseline |
| [SAFE-K8S-0603-014](markdown/controls/SAFE-K8S-0603-014.md) | Fail-closed admission enforcement for attestation requirements | Advanced | baseline |

<a id="knowledge-area-6-4"></a>
## 6.4 - SBOMs and Vulnerability Intelligence

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Practitioner
- Controls: 14

### Description

SBOM generation: producing SBOMs in SPDX, CycloneDX, and SWID formats during CI/CD builds; SBOM generation for AI container images and model artifacts ML-BOM (ML Bill of Materials): extending SBOMs to capture model lineage, training data provenance, hyperparameter configurations, framework versions, training infrastructure identity, and dataset composition - enabling end-to-end ML supply chain transparency per CTA-2114 SBOM storage and distribution: attaching SBOMs to container images as OCI artifacts, registry-based SBOM discovery VEX (Vulnerability Exploitability eXchange): communicating vulnerability applicability, reducing false-positive noise in scanning results Dependency tracking and build provenance: SLSA levels, hermetic builds, and source-to-artifact integrity verification Vulnerability prioritization for AI workloads: distinguishing training-time vs. inference-time exposure, GPU driver CVEs vs. application-layer CVEs; automated rebuild and redeployment pipelines for patching AI workload images without retraining models

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0604-001](markdown/controls/SAFE-K8S-0604-001.md) | SBOM generation for container and AI artifacts | Practitioner | ai-specific |
| [SAFE-K8S-0604-002](markdown/controls/SAFE-K8S-0604-002.md) | ML-BOM (ML Bill of Materials) generation | Practitioner | ai-specific |
| [SAFE-K8S-0604-003](markdown/controls/SAFE-K8S-0604-003.md) | SBOM storage and distribution as OCI artifacts | Practitioner | baseline |
| [SAFE-K8S-0604-004](markdown/controls/SAFE-K8S-0604-004.md) | VEX (Vulnerability Exploitability eXchange) publication | Practitioner | baseline |
| [SAFE-K8S-0604-005](markdown/controls/SAFE-K8S-0604-005.md) | Dependency tracking and SLSA build provenance | Practitioner | baseline |
| [SAFE-K8S-0604-006](markdown/controls/SAFE-K8S-0604-006.md) | Vulnerability prioritization for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0604-007](markdown/controls/SAFE-K8S-0604-007.md) | Third-party component security requirements documentation | Practitioner | baseline |
| [SAFE-K8S-0604-008](markdown/controls/SAFE-K8S-0604-008.md) | AI workload vulnerability exposure classification | Practitioner | ai-specific |
| [SAFE-K8S-0604-009](markdown/controls/SAFE-K8S-0604-009.md) | AI workload vulnerability prioritization and remediation SLAs | Practitioner | ai-specific |
| [SAFE-K8S-0604-010](markdown/controls/SAFE-K8S-0604-010.md) | Automated AI workload rebuild and redeployment patch pipelines | Practitioner | ai-specific |
| [SAFE-K8S-0604-011](markdown/controls/SAFE-K8S-0604-011.md) | SLSA provenance generation and target-level governance | Practitioner | baseline |
| [SAFE-K8S-0604-012](markdown/controls/SAFE-K8S-0604-012.md) | Hermetic build dependency control and source-to-artifact integrity | Practitioner | baseline |
| [SAFE-K8S-0604-013](markdown/controls/SAFE-K8S-0604-013.md) | Hermetic build execution and pinned dependency input control | Practitioner | baseline |
| [SAFE-K8S-0604-014](markdown/controls/SAFE-K8S-0604-014.md) | Source-to-artifact integrity linkage for built images | Practitioner | baseline |

<a id="knowledge-area-6-5"></a>
## 6.5 - Admission Control

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Practitioner
- Controls: 10

### Description

OPA/Gatekeeper constraint templates and constraints for Kubernetes policy enforcement; AI workload admission policies including GPU request validation, image provenance, and runtime class enforcement Kyverno policies: validation, mutation, generation, and image verification rules Kubewarden policies: WebAssembly-based admission policies, policy development, and runtime Admission webhook security: failure policies (Fail vs. Ignore), timeout configuration, webhook certificate management, and availability considerations CRD validation and webhook hardening for AI custom resources (InferenceService, TrainingJob, RayCluster, PodGroup); PSA label enforcement via admission policies

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0605-001](markdown/controls/SAFE-K8S-0605-001.md) | OPA/Gatekeeper policies for Kubernetes and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0605-002](markdown/controls/SAFE-K8S-0605-002.md) | Kyverno admission policies | Practitioner | baseline |
| [SAFE-K8S-0605-003](markdown/controls/SAFE-K8S-0605-003.md) | Kubewarden WebAssembly-based admission policies | Practitioner | baseline |
| [SAFE-K8S-0605-004](markdown/controls/SAFE-K8S-0605-004.md) | Admission webhook security and availability | Practitioner | baseline |
| [SAFE-K8S-0605-005](markdown/controls/SAFE-K8S-0605-005.md) | CRD validation and webhook hardening for AI custom resources | Practitioner | ai-specific |
| [SAFE-K8S-0605-006](markdown/controls/SAFE-K8S-0605-006.md) | Pod Security Admission enforcement for AI workload namespaces | Practitioner | baseline |
| [SAFE-K8S-0605-007](markdown/controls/SAFE-K8S-0605-007.md) | Admission webhook fail-closed enforcement and timeout bounds | Practitioner | baseline |
| [SAFE-K8S-0605-008](markdown/controls/SAFE-K8S-0605-008.md) | Admission webhook TLS rotation and high-availability resilience | Practitioner | baseline |
| [SAFE-K8S-0605-009](markdown/controls/SAFE-K8S-0605-009.md) | AI custom resource validation and policy constraint enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0605-010](markdown/controls/SAFE-K8S-0605-010.md) | AI custom resource webhook abuse resistance and resource hardening | Practitioner | ai-specific |

<a id="knowledge-area-6-6"></a>
## 6.6 - CI/CD and GitOps Pipeline Security

- Domain: D06 - Supply Chain, Images, and Admission Control
- Maturity: Practitioner
- Controls: 34

### Description

CNCF lifecycle security: applying security controls across Develop → Distribute → Deploy phases; zero trust for CI/CD pipelines per NIST SP 800-204D - trust established and verified at every pipeline step through artifact integrity verification, authenticated handoffs between stages, and concurrent evidence generation with higher trust than the build process itself CI/CD build environment hardening: isolated build platforms (sandboxed CI runner pods, ephemeral build VMs), CI/CD runner pod security in Kubernetes (credential isolation, network restrictions, ephemeral storage), prevention of credential theft from build environments (signing keys, cloud credentials, environment variables), and real-time monitoring of CI/CD server activity for tampering or exfiltration CI pipeline security gates: SAST (static application security testing), DAST (dynamic application security testing), and SCA (software composition analysis) integrated into CI pipelines; secret scanning with push protection to prevent credentials from entering repositories; dependency review at pull request time; code freshness enforcement ("build horizon" - deployed artifacts must not exceed a maximum age from committed code); OpenSSF Scorecard for automated SCM security posture assessment GitOps security with Flux and ArgoCD: repository access controls, signed commits, branch protection, reconciliation integrity; drift detection and remediation - monitoring for runtime configuration deviations from Git-declared state with automated resync or notification; no manual runtime changes (kubectl apply) - Git as the single source of truth; release metadata preservation for all deployed packages, versions, and configuration files Helm chart security: chart provenance, signature verification, values injection controls, and dependency pinning Manifest signing, SSDF v1.1 alignment for secure development practices, and infrastructure as code (IaC) security for deployment platform definitions; policy as code for runtime settings and configuration code integrity verification

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0606-001](markdown/controls/SAFE-K8S-0606-001.md) | CNCF lifecycle security and zero-trust CI/CD pipelines | Practitioner | baseline |
| [SAFE-K8S-0606-002](markdown/controls/SAFE-K8S-0606-002.md) | CI/CD build environment hardening | Practitioner | baseline |
| [SAFE-K8S-0606-003](markdown/controls/SAFE-K8S-0606-003.md) | CI pipeline security gates | Practitioner | baseline |
| [SAFE-K8S-0606-004](markdown/controls/SAFE-K8S-0606-004.md) | GitOps repository security | Practitioner | baseline |
| [SAFE-K8S-0606-005](markdown/controls/SAFE-K8S-0606-005.md) | Helm chart security and provenance | Practitioner | baseline |
| [SAFE-K8S-0606-006](markdown/controls/SAFE-K8S-0606-006.md) | Kubernetes manifest signing and verification | Advanced | baseline |
| [SAFE-K8S-0606-007](markdown/controls/SAFE-K8S-0606-007.md) | CI/CD build activity monitoring | Practitioner | baseline |
| [SAFE-K8S-0606-008](markdown/controls/SAFE-K8S-0606-008.md) | GitOps reconciliation integrity and drift detection | Practitioner | baseline |
| [SAFE-K8S-0606-009](markdown/controls/SAFE-K8S-0606-009.md) | SSDF v1.1 alignment for secure development practices | Practitioner | baseline |
| [SAFE-K8S-0606-010](markdown/controls/SAFE-K8S-0606-010.md) | Infrastructure as Code security and policy-as-code integrity | Practitioner | baseline |
| [SAFE-K8S-0606-011](markdown/controls/SAFE-K8S-0606-011.md) | CI build-time security gate enforcement | Practitioner | baseline |
| [SAFE-K8S-0606-012](markdown/controls/SAFE-K8S-0606-012.md) | Artifact freshness and SCM security posture enforcement | Practitioner | baseline |
| [SAFE-K8S-0606-013](markdown/controls/SAFE-K8S-0606-013.md) | GitOps repository access, commit signing, and branch protection | Practitioner | baseline |
| [SAFE-K8S-0606-014](markdown/controls/SAFE-K8S-0606-014.md) | GitOps release metadata preservation and deployment traceability | Practitioner | baseline |
| [SAFE-K8S-0606-015](markdown/controls/SAFE-K8S-0606-015.md) | GitOps reconciliation monitoring, drift detection, and automated resync | Practitioner | baseline |
| [SAFE-K8S-0606-016](markdown/controls/SAFE-K8S-0606-016.md) | Git-only production deployment path and direct-change prohibition | Practitioner | baseline |
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
- Controls: 9

### Description

PersistentVolume and PersistentVolumeClaim access modes: ReadWriteOnce, ReadOnlyMany, ReadWriteMany - security implications per mode; PV security for training datasets, model checkpoints, and feature stores CSI driver security: driver privilege requirements, volume snapshot access controls, and storage class restrictions; high-performance AI storage (Lustre, GPFS, NFS, object storage) and their elevated privilege requirements Encryption at rest for persistent volumes: cloud provider encryption, dm-crypt/LUKS, and storage-level encryption PV reclaim policy security: Retain vs. Delete policies, data remnant prevention, and secure volume cleanup; dual authorization requirements for destruction of training data backups and model checkpoint archives Data versioning and immutability controls in Kubernetes-native storage: PV snapshots, object storage versioning, and DVC integration for training data and model artifact integrity

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0701-001](markdown/controls/SAFE-K8S-0701-001.md) | PersistentVolume and PersistentVolumeClaim access mode enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0701-002](markdown/controls/SAFE-K8S-0701-002.md) | CSI driver security and privilege restriction | Practitioner | baseline |
| [SAFE-K8S-0701-003](markdown/controls/SAFE-K8S-0701-003.md) | Encryption at rest for persistent volumes | Foundational | baseline |
| [SAFE-K8S-0701-004](markdown/controls/SAFE-K8S-0701-004.md) | PV reclaim policy enforcement for AI data volumes | Practitioner | ai-specific |
| [SAFE-K8S-0701-005](markdown/controls/SAFE-K8S-0701-005.md) | Data versioning and immutability for training data and model artifacts | Advanced | ai-specific |
| [SAFE-K8S-0701-006](markdown/controls/SAFE-K8S-0701-006.md) | Dual authorization for retained AI data volume destruction | Advanced | ai-specific |
| [SAFE-K8S-0701-007](markdown/controls/SAFE-K8S-0701-007.md) | High-performance AI storage backend hardening | Advanced | ai-specific |
| [SAFE-K8S-0701-008](markdown/controls/SAFE-K8S-0701-008.md) | Training data and model artifact version tracking for reproducibility | Advanced | ai-specific |
| [SAFE-K8S-0701-009](markdown/controls/SAFE-K8S-0701-009.md) | Immutable storage protection for training data and model artifacts | Advanced | ai-specific |

<a id="knowledge-area-7-2"></a>
## 7.2 - Namespace Isolation and Multi-Tenancy

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Maturity: Practitioner
- Controls: 31

### Description

Namespace as a security boundary: isolation properties, limitations, and supplementary controls needed for true multi-tenancy; namespace-per-team vs. namespace-per-workload-type isolation models for mixed AI/non-AI clusters Resource quotas per namespace: CPU, memory, storage, GPU, and object count limits to prevent resource monopolization; ResourceQuota and LimitRange configuration specific to GPU and AI namespaces LimitRange enforcement: default and maximum resource limits per container and pod within a namespace Virtual cluster approaches (vCluster, HNC) for stronger tenant isolation while sharing underlying infrastructure Label and annotation standards for AI workload classification (training vs. inference, data sensitivity, model tier) Data type classification labels for pipeline data flows Maintaining classification attributes across model lifecycle stages (dev to staging to production) Automated reclassification mechanisms during model promotion to apply environment-specific security controls Validation gate preventing model promotion to production without validated classification metadata Tenant boundary enforcement through admission control, network policy, and RBAC at the namespace level

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0702-001](markdown/controls/SAFE-K8S-0702-001.md) | Namespace isolation model for multi-tenant AI clusters | Practitioner | baseline |
| [SAFE-K8S-0702-002](markdown/controls/SAFE-K8S-0702-002.md) | Resource quotas per namespace for GPU and AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0702-003](markdown/controls/SAFE-K8S-0702-003.md) | LimitRange enforcement for containers and pods | Foundational | baseline |
| [SAFE-K8S-0702-004](markdown/controls/SAFE-K8S-0702-004.md) | Virtual cluster isolation for multi-tenant environments | Advanced | baseline |
| [SAFE-K8S-0702-005](markdown/controls/SAFE-K8S-0702-005.md) | Label and annotation schema definition for AI workload classification | Practitioner | ai-specific |
| [SAFE-K8S-0702-006](markdown/controls/SAFE-K8S-0702-006.md) | Data type classification labels for pipeline data flows | Practitioner | ai-specific |
| [SAFE-K8S-0702-007](markdown/controls/SAFE-K8S-0702-007.md) | Classification attribute preservation across model lifecycle stages | Practitioner | ai-specific |
| [SAFE-K8S-0702-008](markdown/controls/SAFE-K8S-0702-008.md) | Tenant boundary enforcement through admission control, network policy, and RBAC | Practitioner | baseline |
| [SAFE-K8S-0702-009](markdown/controls/SAFE-K8S-0702-009.md) | Admission control enforcement of workload classification label requirements | Practitioner | ai-specific |
| [SAFE-K8S-0702-010](markdown/controls/SAFE-K8S-0702-010.md) | Virtual cluster deployment for high-isolation multi-tenant Kubernetes environments | Advanced | baseline |
| [SAFE-K8S-0702-011](markdown/controls/SAFE-K8S-0702-011.md) | Isolation guarantee validation and residual risk documentation for virtual clusters | Advanced | baseline |
| [SAFE-K8S-0702-012](markdown/controls/SAFE-K8S-0702-012.md) | Tenant namespace RBAC and admission boundary enforcement | Practitioner | baseline |
| [SAFE-K8S-0702-013](markdown/controls/SAFE-K8S-0702-013.md) | Tenant default-deny inter-namespace network isolation | Practitioner | baseline |
| [SAFE-K8S-0702-014](markdown/controls/SAFE-K8S-0702-014.md) | Pipeline data classification taxonomy and label propagation | Practitioner | ai-specific |
| [SAFE-K8S-0702-015](markdown/controls/SAFE-K8S-0702-015.md) | Classification-driven admission, storage, and network policy enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0702-016](markdown/controls/SAFE-K8S-0702-016.md) | Classification metadata preservation across model lifecycle stages | Practitioner | ai-specific |
| [SAFE-K8S-0702-017](markdown/controls/SAFE-K8S-0702-017.md) | Promotion-time reclassification and production gate enforcement | Practitioner | ai-specific |
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
- Controls: 23

### Description

Priority classes and preemption: system-critical, high-priority, and default priority classes - preemption policies for training jobs vs. inference workloads vs. development notebooks; Kueue and Volcano queue management for fair-share GPU scheduling across tenants Pod Disruption Budgets: maintaining availability during node maintenance and cluster upgrades GPU cost governance: per-namespace, per-team, and per-job GPU cost attribution and chargeback; idle GPU detection and reclamation (abandoned training jobs, over-provisioned inference deployments, unused GPU reservations); spending limits and budget alerts with automatic enforcement (job suspension, scale-down triggers) Detection and prevention of GPU resource squatting, quota circumvention, and unauthorized GPU usage (cryptomining, personal workloads, resource policy violations) Resource exhaustion resilience: chaos engineering for GPU and AI resource controls, queue management with bounded queues and backpressure handling, training-time resource protection (job-level memory ceilings, training data size limits), and Economic Denial of Sustainability (EDoS) awareness for cloud-hosted AI infrastructure Node affinity rules, taints, and tolerations to prevent AI workloads from impacting non-AI services, ensuring GPU nodes are dedicated to AI workloads and preventing noisy-neighbor scheduling conflicts Topology-aware scheduling for GPU locality (NVLink, NVSwitch) for distributed training workloads, balanced against blast-radius containment through failure domain distribution

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0703-001](markdown/controls/SAFE-K8S-0703-001.md) | Priority classes and preemption policies for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0703-002](markdown/controls/SAFE-K8S-0703-002.md) | Pod Disruption Budgets for workload availability | Foundational | baseline |
| [SAFE-K8S-0703-003](markdown/controls/SAFE-K8S-0703-003.md) | GPU cost attribution and chargeback mechanisms | Practitioner | ai-specific |
| [SAFE-K8S-0703-004](markdown/controls/SAFE-K8S-0703-004.md) | GPU resource abuse detection and prevention | Practitioner | ai-specific |
| [SAFE-K8S-0703-005](markdown/controls/SAFE-K8S-0703-005.md) | AI workload resource exhaustion guardrails | Practitioner | ai-specific |
| [SAFE-K8S-0703-006](markdown/controls/SAFE-K8S-0703-006.md) | Node affinity, taints, and topology-aware scheduling for AI workload isolation | Practitioner | ai-specific |
| [SAFE-K8S-0703-007](markdown/controls/SAFE-K8S-0703-007.md) | Fair-share GPU queue management for multi-tenant clusters | Practitioner | ai-specific |
| [SAFE-K8S-0703-008](markdown/controls/SAFE-K8S-0703-008.md) | Idle GPU detection and resource reclamation | Practitioner | ai-specific |
| [SAFE-K8S-0703-009](markdown/controls/SAFE-K8S-0703-009.md) | GPU spending limits and budget enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0703-010](markdown/controls/SAFE-K8S-0703-010.md) | Host-level resource isolation for AI workload nodes | Practitioner | ai-specific |
| [SAFE-K8S-0703-011](markdown/controls/SAFE-K8S-0703-011.md) | EDoS prevention and chaos engineering for AI resources | Advanced | ai-specific |
| [SAFE-K8S-0703-012](markdown/controls/SAFE-K8S-0703-012.md) | Node affinity rules, taints, and tolerations for AI workload isolation | Practitioner | ai-specific |
| [SAFE-K8S-0703-013](markdown/controls/SAFE-K8S-0703-013.md) | Topology-aware scheduling for GPU locality with blast-radius containment | Practitioner | ai-specific |
| [SAFE-K8S-0703-014](markdown/controls/SAFE-K8S-0703-014.md) | EDoS spending guardrails and autoscaling limits for AI resources | Advanced | ai-specific |
| [SAFE-K8S-0703-015](markdown/controls/SAFE-K8S-0703-015.md) | Chaos engineering validation for AI resource governance controls | Advanced | ai-specific |
| [SAFE-K8S-0703-016](markdown/controls/SAFE-K8S-0703-016.md) | AI workload PriorityClass hierarchy and preemption protection | Practitioner | ai-specific |
| [SAFE-K8S-0703-017](markdown/controls/SAFE-K8S-0703-017.md) | PriorityClass assignment restriction and admission enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0703-018](markdown/controls/SAFE-K8S-0703-018.md) | GPU cost attribution metering and billing correlation | Practitioner | ai-specific |
| [SAFE-K8S-0703-019](markdown/controls/SAFE-K8S-0703-019.md) | GPU chargeback and showback reporting accountability | Practitioner | ai-specific |
| [SAFE-K8S-0703-020](markdown/controls/SAFE-K8S-0703-020.md) | GPU workload abuse detection and response | Practitioner | ai-specific |
| [SAFE-K8S-0703-021](markdown/controls/SAFE-K8S-0703-021.md) | GPU admission enforcement against unauthorized access and quota bypass | Practitioner | ai-specific |
| [SAFE-K8S-0703-022](markdown/controls/SAFE-K8S-0703-022.md) | GPU abuse pattern monitoring and detection for Kubernetes AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-0703-023](markdown/controls/SAFE-K8S-0703-023.md) | Investigation and termination of confirmed unauthorized GPU workloads | Practitioner | ai-specific |

<a id="knowledge-area-7-4"></a>
## 7.4 - Cloud Provider Security Integration

- Domain: D07 - Storage, Multi-tenancy, and Resource Governance
- Maturity: Practitioner
- Controls: 20

### Description

Cloud IAM to Kubernetes RBAC mapping: cloud-native role bindings for managed Kubernetes services (EKS, GKE, AKS) VPC and security group integration: node network isolation, control plane endpoint access, and cloud firewall alignment with K8s network policies Cloud audit log integration: correlating cloud provider audit logs with Kubernetes audit events for unified security monitoring Metadata service protections: IMDSv2 enforcement, network-level restrictions, and preventing credential theft from cloud metadata endpoints Restricted use policies for non-organizationally owned systems and external AI services; cloud provider contingency plan requirements for managed Kubernetes services

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0704-001](markdown/controls/SAFE-K8S-0704-001.md) | Cloud IAM to Kubernetes RBAC mapping | Practitioner | baseline |
| [SAFE-K8S-0704-002](markdown/controls/SAFE-K8S-0704-002.md) | VPC and security group integration with Kubernetes network policies | Practitioner | baseline |
| [SAFE-K8S-0704-003](markdown/controls/SAFE-K8S-0704-003.md) | Cloud audit log correlation with Kubernetes audit events | Practitioner | baseline |
| [SAFE-K8S-0704-004](markdown/controls/SAFE-K8S-0704-004.md) | IMDSv2 enforcement on Kubernetes nodes | Foundational | baseline |
| [SAFE-K8S-0704-005](markdown/controls/SAFE-K8S-0704-005.md) | Restricted use policies for non-organizationally owned systems and external AI services | Practitioner | ai-specific |
| [SAFE-K8S-0704-006](markdown/controls/SAFE-K8S-0704-006.md) | Cloud provider contingency plans for managed Kubernetes services | Practitioner | ai-specific |
| [SAFE-K8S-0704-007](markdown/controls/SAFE-K8S-0704-007.md) | Unified cloud and Kubernetes audit log ingestion | Practitioner | baseline |
| [SAFE-K8S-0704-008](markdown/controls/SAFE-K8S-0704-008.md) | Cloud-to-Kubernetes event correlation for incident investigation | Practitioner | baseline |
| [SAFE-K8S-0704-009](markdown/controls/SAFE-K8S-0704-009.md) | Cloud IAM to Kubernetes RBAC entitlement mapping governance | Practitioner | baseline |
| [SAFE-K8S-0704-010](markdown/controls/SAFE-K8S-0704-010.md) | Privileged cloud-to-cluster access boundary enforcement and break-glass control | Practitioner | baseline |
| [SAFE-K8S-0704-011](markdown/controls/SAFE-K8S-0704-011.md) | Network-level blocking of cloud metadata endpoint access for pods | Foundational | baseline |
| [SAFE-K8S-0704-012](markdown/controls/SAFE-K8S-0704-012.md) | Pod identity mechanisms replacing node-level instance profiles | Foundational | baseline |
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
- Controls: 14

### Description

Device plugin framework: how GPU device plugins expose accelerators to the kubelet and scheduling implications; NVIDIA device plugin, GPU Operator, and GPU Feature Discovery security configuration and hardening MIG (Multi-Instance GPU) partitioning: hardware-enforced isolation between tenants, MIG profile configuration, and resource advertisement MPS and time-slicing: shared GPU access patterns, security tradeoffs between utilization efficiency and isolation guarantees; GPU memory isolation verification, side-channel resistance assessment, and cross-tenant data remnant prevention vGPU configuration: hypervisor-based GPU virtualization, resource allocation granularity, and vendor-specific security controls Hardware topology exposure risks and metadata leakage through Kubernetes device plugin advertisements and node labels; GPU request validation through admission control policies

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0801-001](markdown/controls/SAFE-K8S-0801-001.md) | GPU device plugin security configuration and hardening | Practitioner | ai-specific |
| [SAFE-K8S-0801-002](markdown/controls/SAFE-K8S-0801-002.md) | MIG partitioning for hardware-enforced GPU isolation | Advanced | ai-specific |
| [SAFE-K8S-0801-003](markdown/controls/SAFE-K8S-0801-003.md) | MPS and time-slicing isolation and memory safety controls | Advanced | ai-specific |
| [SAFE-K8S-0801-004](markdown/controls/SAFE-K8S-0801-004.md) | vGPU virtualization security controls | Practitioner | ai-specific |
| [SAFE-K8S-0801-005](markdown/controls/SAFE-K8S-0801-005.md) | GPU topology metadata protection and admission control | Practitioner | ai-specific |
| [SAFE-K8S-0801-006](markdown/controls/SAFE-K8S-0801-006.md) | GPU memory clearing between workload transitions | Advanced | ai-specific |
| [SAFE-K8S-0801-007](markdown/controls/SAFE-K8S-0801-007.md) | MPS and time-slicing residual-risk acceptance and workload eligibility controls | Advanced | ai-specific |
| [SAFE-K8S-0801-008](markdown/controls/SAFE-K8S-0801-008.md) | MPS and time-slicing memory isolation verification and side-channel assessment | Advanced | ai-specific |
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
- Controls: 9

### Description

GPU driver version management: vulnerability patching, compatibility validation, driver containers, and NVIDIA GPU Operator lifecycle CUDA library and runtime security: container toolkit configuration, compat libraries, driver persistence mode implications Device plugin socket security: kubelet communication integrity, unauthorized GPU access prevention, and device health monitoring GPU firmware integrity: monitoring for firmware tampering, driver replacement, and unauthorized kernel module loading

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0802-001](markdown/controls/SAFE-K8S-0802-001.md) | GPU driver lifecycle and vulnerability management | Practitioner | ai-specific |
| [SAFE-K8S-0802-002](markdown/controls/SAFE-K8S-0802-002.md) | CUDA library and container toolkit security | Advanced | ai-specific |
| [SAFE-K8S-0802-003](markdown/controls/SAFE-K8S-0802-003.md) | Device plugin socket and kubelet communication security | Practitioner | ai-specific |
| [SAFE-K8S-0802-004](markdown/controls/SAFE-K8S-0802-004.md) | GPU firmware integrity monitoring | Advanced | ai-specific |
| [SAFE-K8S-0802-005](markdown/controls/SAFE-K8S-0802-005.md) | GPU kernel module and driver binary integrity enforcement | Advanced | ai-specific |
| [SAFE-K8S-0802-006](markdown/controls/SAFE-K8S-0802-006.md) | Device plugin socket directory access restriction and unauthorized socket access monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0802-007](markdown/controls/SAFE-K8S-0802-007.md) | Device plugin registration authentication monitoring and rogue plugin detection | Practitioner | ai-specific |
| [SAFE-K8S-0802-008](markdown/controls/SAFE-K8S-0802-008.md) | GPU kernel module signing and Secure Boot enforcement | Advanced | ai-specific |
| [SAFE-K8S-0802-009](markdown/controls/SAFE-K8S-0802-009.md) | GPU driver binary path file integrity monitoring | Advanced | ai-specific |

<a id="knowledge-area-8-3"></a>
## 8.3 - High-Performance Interconnect Security

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Maturity: Advanced
- Controls: 6

### Description

NVLink and NVSwitch security for multi-GPU training: traffic isolation, topology exposure risks, and cross-tenant data leakage prevention InfiniBand and RoCE security: subnet manager access controls, partition key configuration, and network fabric isolation RDMA security: memory region access controls, queue pair isolation, and protection against remote memory attacks DPU/SmartNIC security: firmware integrity, policy enforcement at the network device level, and offload trust boundaries

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0803-001](markdown/controls/SAFE-K8S-0803-001.md) | NVLink and NVSwitch traffic isolation for multi-GPU training | Advanced | ai-specific |
| [SAFE-K8S-0803-002](markdown/controls/SAFE-K8S-0803-002.md) | InfiniBand and RoCE fabric security controls | Advanced | ai-specific |
| [SAFE-K8S-0803-003](markdown/controls/SAFE-K8S-0803-003.md) | RDMA memory region and queue pair isolation | Advanced | ai-specific |
| [SAFE-K8S-0803-004](markdown/controls/SAFE-K8S-0803-004.md) | DPU and SmartNIC firmware integrity and trust boundaries | Advanced | ai-specific |
| [SAFE-K8S-0803-005](markdown/controls/SAFE-K8S-0803-005.md) | DPU and SmartNIC firmware cryptographic verification and Secure Boot integrity | Advanced | ai-specific |
| [SAFE-K8S-0803-006](markdown/controls/SAFE-K8S-0803-006.md) | DPU and SmartNIC host trust boundary definition and policy engine administrative restriction | Advanced | ai-specific |

<a id="knowledge-area-8-4"></a>
## 8.4 - Confidential Computing for AI Workloads

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Maturity: Advanced
- Controls: 6

### Description

TEE-based model protection: NVIDIA H100 Confidential Computing, Intel TDX, and AMD SEV-SNP for inference and training Remote attestation workflows: verifying TEE integrity before loading models or sensitive training data Key management and sealed storage for models and data within confidential computing enclaves Performance, compatibility, and operational constraints of confidential AI workloads on Kubernetes

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0804-001](markdown/controls/SAFE-K8S-0804-001.md) | TEE-based model and data protection for AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0804-002](markdown/controls/SAFE-K8S-0804-002.md) | Remote attestation for TEE integrity verification | Advanced | ai-specific |
| [SAFE-K8S-0804-003](markdown/controls/SAFE-K8S-0804-003.md) | Key management and sealed storage for confidential AI enclaves | Advanced | ai-specific |
| [SAFE-K8S-0804-004](markdown/controls/SAFE-K8S-0804-004.md) | Confidential AI workload operational constraints and risk assessment | Advanced | ai-specific |
| [SAFE-K8S-0804-005](markdown/controls/SAFE-K8S-0804-005.md) | Attestation-conditioned enclave key release | Advanced | ai-specific |
| [SAFE-K8S-0804-006](markdown/controls/SAFE-K8S-0804-006.md) | Sealed storage binding of encrypted AI artifacts to enclave measurements | Advanced | ai-specific |

<a id="knowledge-area-8-5"></a>
## 8.5 - GPU Workload Auditing and Monitoring

- Domain: D08 - GPU, Accelerator, and Confidential Computing
- Maturity: Advanced
- Controls: 4

### Description

GPU telemetry collection: DCGM exporter, NVML metrics for utilization, memory, temperature, and error injection detection Accelerator allocation audit trails: tracking which pods used which GPUs, for how long, and with what workload identity GPU-based attack detection: cryptocurrency mining on training clusters, GPU memory scraping, covert channels via GPU shared memory Side-channel awareness: GPU shared memory timing attacks, memory access pattern leakage, and cross-tenant information disclosure

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
- Controls: 10

### Description

Multi-node training job security: PyTorchJob, MPIJob, TFJob - inter-worker authentication, encrypted gradient communication (NCCL, MPI); inter-worker encryption for all data in transit within distributed training pipelines Parameter server and all-reduce security: protection against gradient poisoning, worker impersonation, and Byzantine fault injection Checkpoint security: encrypted storage, integrity verification, and access controls for model checkpoints and optimizer state Training fault tolerance and security: corrupted data detection and recovery, adversary-exploitable fault tolerance mechanisms (retry logic manipulation, corruption injection during recovery), backup and rollback strategies for training state Federated learning security on Kubernetes: secure aggregation protocols, differential privacy for gradient updates, gradient leakage and model inversion prevention, Byzantine-resilient aggregation, participant authentication, and isolation of federated training participants; cross-cluster FL architecture (Flower, FATE, NVIDIA FLARE deployment patterns on Kubernetes), SPIFFE-based FL participant enrollment and revocation, cross-cluster FL network security (end-to-end mTLS, network path control, gradient payload inspection), data residency and sovereignty enforcement for cross-cluster FL (local data verification, residency labels, gradient-only egress, compliance audit trail), FL-specific monitoring and anomaly detection (gradient norm tracking, privacy budget monitoring, participant contribution rate analysis, aggregation round duration) Gang scheduling security (Volcano, Kueue): prevention of resource manipulation and priority abuse during distributed training Security implications of AI operators (NVIDIA GPU Operator, KServe, Kubeflow, Ray, Volcano, Kueue) and their elevated privileges; operator RBAC scoping, namespace restrictions, least-privilege service accounts, and upgrade/vulnerability management for AI operators and their dependencies

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0901-001](markdown/controls/SAFE-K8S-0901-001.md) | Multi-node training worker authentication and encrypted communication | Practitioner | ai-specific |
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
- Controls: 11

### Description

Inference server hardening (vLLM, Triton, TGI, KServe): minimal privilege, read-only model mounts, restricted network access; inference server vulnerability management (patching cadence for serving frameworks, CUDA runtime, and API dependencies) Model loading security: verifying model integrity at server startup, preventing model replacement, and secure model caching; model endpoint authentication and authorization via API gateway integration, token validation, and per-model access controls Input validation and sanitization for inference requests: adversarial input detection, payload size controls, request format enforcement, and injection attack prevention; response filtering and output controls to prevent model output from leaking training data, PII, or sensitive patterns Multi-model serving security: model mesh isolation, shared-memory protections, and per-model resource accounting; TLS termination and end-to-end encryption for inference traffic including internal service-to-service model calls Multi-cluster inference routing and failover security: geographic routing, active-active, active-passive failover, and canary cross-cluster deployment patterns; model version consistency verification across serving clusters (central model registry, staleness detection, promotion synchronization via GitOps); authenticated cross-cluster request routing with federated identity, request integrity and authorization forwarding, policy consistency enforcement across serving clusters; failover security controls (model version verification before failover, cluster health validation, failover audit logging); multi-cluster inference observability (unified distributed tracing, cross-cluster metrics, incident correlation across serving federation)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0902-001](markdown/controls/SAFE-K8S-0902-001.md) | Inference server hardening | Practitioner | ai-specific |
| [SAFE-K8S-0902-002](markdown/controls/SAFE-K8S-0902-002.md) | Model loading integrity verification | Practitioner | ai-specific |
| [SAFE-K8S-0902-003](markdown/controls/SAFE-K8S-0902-003.md) | Inference request validation and input sanitization | Practitioner | ai-specific |
| [SAFE-K8S-0902-004](markdown/controls/SAFE-K8S-0902-004.md) | Multi-model serving isolation and encryption | Practitioner | ai-specific |
| [SAFE-K8S-0902-005](markdown/controls/SAFE-K8S-0902-005.md) | Multi-cluster inference routing and failover security | Practitioner | ai-specific |
| [SAFE-K8S-0902-006](markdown/controls/SAFE-K8S-0902-006.md) | LLM serving configuration security | Practitioner | ai-specific |
| [SAFE-K8S-0902-007](markdown/controls/SAFE-K8S-0902-007.md) | Infrastructure-layer prompt injection defense and token output filtering | Practitioner | ai-specific |
| [SAFE-K8S-0902-008](markdown/controls/SAFE-K8S-0902-008.md) | Inference endpoint authentication and authorization | Practitioner | ai-specific |
| [SAFE-K8S-0902-009](markdown/controls/SAFE-K8S-0902-009.md) | Inference response filtering and output controls | Practitioner | ai-specific |
| [SAFE-K8S-0902-010](markdown/controls/SAFE-K8S-0902-010.md) | Infrastructure-layer prompt injection classification and instruction boundary enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0902-011](markdown/controls/SAFE-K8S-0902-011.md) | Streaming token-level output leakage and policy-violation filtering | Practitioner | ai-specific |

<a id="knowledge-area-9-3"></a>
## 9.3 - Inference Resilience, Adversarial Defense, and Resource Controls

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 8

### Description

Adversarial example defenses at the serving layer: input transformation and data augmentation as detection mechanisms, adversarial input rejection policies, perturbation detection, and infrastructure requirements for adversarial training; explainable AI (xAI) integration for security - using model explanations to detect adversarial inputs, identify poisoned model behavior, and flag anomalous predictions, while managing xAI as an attack surface (explanation exploitation for model reverse engineering) Autoscaling safety: GPU-aware HPA configuration, maximum replica bounds, cooldown periods, and denial-of-wallet prevention; inference request queue security (priority queuing, timeout enforcement, queue depth limits to prevent backpressure attacks) Inference-time resource controls: computational complexity bounds per request, input size restrictions, multi-level timeouts (request, session, batch), GPU memory ceilings per inference pod, and overload handling (graceful degradation, circuit breakers); Economic Denial of Sustainability (EDoS) prevention for cloud-hosted inference

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0903-001](markdown/controls/SAFE-K8S-0903-001.md) | Adversarial example defenses at the serving layer | Practitioner | ai-specific |
| [SAFE-K8S-0903-002](markdown/controls/SAFE-K8S-0903-002.md) | Autoscaling safety and queue security | Practitioner | ai-specific |
| [SAFE-K8S-0903-003](markdown/controls/SAFE-K8S-0903-003.md) | Inference-time resource controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-004](markdown/controls/SAFE-K8S-0903-004.md) | LLM context window and token resource controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-005](markdown/controls/SAFE-K8S-0903-005.md) | GPU inference autoscaling safety bounds and budget guardrails | Practitioner | ai-specific |
| [SAFE-K8S-0903-006](markdown/controls/SAFE-K8S-0903-006.md) | Inference request queue priority, timeout, and depth controls | Practitioner | ai-specific |
| [SAFE-K8S-0903-007](markdown/controls/SAFE-K8S-0903-007.md) | GPU inference autoscaling replica bounds and stabilization enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0903-008](markdown/controls/SAFE-K8S-0903-008.md) | Budget-aware inference autoscaling suppression and degraded-service fallback | Practitioner | ai-specific |

<a id="knowledge-area-9-4"></a>
## 9.4 - AI Pipeline Orchestration and Experimentation Security

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 18

### Description

Pipeline orchestrator hardening: Kubeflow Pipelines, Argo Workflows, Airflow, and Tekton - RBAC for pipeline definitions, execution isolation, and secret management Pipeline artifact security: intermediate data, model artifacts, and metadata storage protection in MinIO, S3, or GCS; pipeline step isolation to prevent data leakage between stages with different sensitivity levels; procedural and authorization requirements for data transfer between pipeline stages with different classification levels Notebook and experimentation security: per-user isolation, kernel security, resource limits, network restrictions, approved base images, extension vetting; data access controls from notebook environments to prevent unauthorized dataset access, model exfiltration, and credential harvesting Experiment tracking security (MLflow, Weights & Biases): protecting experiment metadata, hyperparameters, and metric data from unauthorized access; pipeline definition integrity with signed manifests, immutable versions, and rollback controls Kubernetes CronJob and batch job security for scheduled feature computation and data refresh; feature freshness and integrity monitoring to detect stale, poisoned, or tampered features before they reach training or inference

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0904-001](markdown/controls/SAFE-K8S-0904-001.md) | Pipeline orchestrator hardening | Practitioner | ai-specific |
| [SAFE-K8S-0904-002](markdown/controls/SAFE-K8S-0904-002.md) | Pipeline artifact encryption and access controls | Practitioner | ai-specific |
| [SAFE-K8S-0904-003](markdown/controls/SAFE-K8S-0904-003.md) | Notebook and experimentation environment security | Practitioner | ai-specific |
| [SAFE-K8S-0904-004](markdown/controls/SAFE-K8S-0904-004.md) | Experiment tracking security and pipeline integrity | Practitioner | ai-specific |
| [SAFE-K8S-0904-005](markdown/controls/SAFE-K8S-0904-005.md) | Scheduled job security and feature freshness monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0904-006](markdown/controls/SAFE-K8S-0904-006.md) | Pipeline stage isolation and cross-classification authorization | Practitioner | ai-specific |
| [SAFE-K8S-0904-007](markdown/controls/SAFE-K8S-0904-007.md) | Scheduled feature computation job hardening | Practitioner | ai-specific |
| [SAFE-K8S-0904-008](markdown/controls/SAFE-K8S-0904-008.md) | Feature freshness and integrity monitoring | Practitioner | ai-specific |
| [SAFE-K8S-0904-009](markdown/controls/SAFE-K8S-0904-009.md) | Experiment tracking metadata access control and audit logging | Practitioner | ai-specific |
| [SAFE-K8S-0904-010](markdown/controls/SAFE-K8S-0904-010.md) | Pipeline definition signing, immutability, and rollback integrity | Practitioner | ai-specific |
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
- Controls: 59

### Description

System classification and security controls: differentiating train-verify-lock systems (model fixed at deployment) from continuous learning systems (model updates post-deployment) - each classification requires distinct control profiles for integrity verification, update authorization, and drift monitoring on Kubernetes Model signing and provenance: Sigstore for models, in-toto attestations for training pipelines, model origin verification at deploy time; OCI artifact storage for models with digest pinning, tag immutability, and access-controlled registries; hashing and signing of all ML lifecycle artifacts (inputs, models, outputs, intermediate artifacts) with integrity verification at each transition point Model registry hardening (Harbor, MLflow, Hugging Face Hub on-prem): access controls, audit logging, retention policies; registry federation and replication security for multi-cluster and multi-region AI deployments ML dependency vulnerability management: software composition analysis for ML frameworks (PyTorch, TensorFlow, JAX), CUDA toolkits, and Python ecosystem dependencies to identify and remediate known CVEs, including deserialization vulnerability tracking in model loading libraries Model promotion gates: security scan pass, bias evaluation, performance threshold, and adversarial robustness test before production deployment; reviewer identity validation in promotion approval workflows; A/B testing and canary infrastructure security (isolation between model versions, traffic splitting integrity, rollback safety) Artifact lifecycle management: model deprecation, archival, and secure deletion of retired model versions; propagation of data correction and deletion notices to derived model artifacts; development-to-production environment separation to prevent training environment credentials from leaking to production inference Model format security and deserialization controls: enforcement of safe serialization formats (SafeTensors, ONNX, GGUF) over unsafe pickle-based formats (Python pickle, PyTorch .pt/.pth, joblib, cloudpickle); deserialization hardening (torch.load with weights_only=True); model file structure validation before loading; format allowlisting for production deployment; admission policies that reject pods loading models via unsafe deserialization paths; CI/CD scanning for malicious pickle opcodes using tools such as fickling; container image hardening to remove unsafe deserialization libraries Public model hub security and third-party model vetting: quarantine and scanning workflow for models from public hubs (Hugging Face Hub, model zoos, community repositories); malicious model payload scanning (embedded code, pickle exploits, steganographic payloads, backdoor triggers); typosquatting detection for model repository names; dependency confusion prevention; sandbox execution with syscall monitoring; provenance verification (commit signatures, model cards, community trust scores); internal re-signing of externally sourced models; curated allowlist of approved external model sources with periodic governance review

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0905-001](markdown/controls/SAFE-K8S-0905-001.md) | AI system lifecycle classification | Practitioner | ai-specific |
| [SAFE-K8S-0905-002](markdown/controls/SAFE-K8S-0905-002.md) | ML artifact signing and attestation generation | Advanced | ai-specific |
| [SAFE-K8S-0905-003](markdown/controls/SAFE-K8S-0905-003.md) | Model registry hardening | Practitioner | ai-specific |
| [SAFE-K8S-0905-004](markdown/controls/SAFE-K8S-0905-004.md) | ML dependency vulnerability management and ML-BOM | Advanced | ai-specific |
| [SAFE-K8S-0905-005](markdown/controls/SAFE-K8S-0905-005.md) | Automated model promotion gates | Advanced | ai-specific |
| [SAFE-K8S-0905-006](markdown/controls/SAFE-K8S-0905-006.md) | Model artifact lifecycle management | Advanced | ai-specific |
| [SAFE-K8S-0905-007](markdown/controls/SAFE-K8S-0905-007.md) | Model format security and deserialization controls | Practitioner | ai-specific |
| [SAFE-K8S-0905-008](markdown/controls/SAFE-K8S-0905-008.md) | Public model quarantine and vetting workflow | Advanced | ai-specific |
| [SAFE-K8S-0905-009](markdown/controls/SAFE-K8S-0905-009.md) | Model provenance verification at deployment | Advanced | ai-specific |
| [SAFE-K8S-0905-010](markdown/controls/SAFE-K8S-0905-010.md) | Model promotion approval and reviewer identity validation | Advanced | ai-specific |
| [SAFE-K8S-0905-011](markdown/controls/SAFE-K8S-0905-011.md) | Canary and A/B deployment isolation and rollback safety | Advanced | ai-specific |
| [SAFE-K8S-0905-012](markdown/controls/SAFE-K8S-0905-012.md) | Development-to-production environment separation for AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0905-013](markdown/controls/SAFE-K8S-0905-013.md) | Approved external model source allowlist enforcement | Advanced | ai-specific |
| [SAFE-K8S-0905-014](markdown/controls/SAFE-K8S-0905-014.md) | AI workload circuit-breaker and emergency halt mechanisms | Advanced | ai-specific |
| [SAFE-K8S-0905-015](markdown/controls/SAFE-K8S-0905-015.md) | AI system control profile enforcement | Practitioner | ai-specific |
| [SAFE-K8S-0905-016](markdown/controls/SAFE-K8S-0905-016.md) | Model registry RBAC, service account scoping, and access review | Practitioner | ai-specific |
| [SAFE-K8S-0905-017](markdown/controls/SAFE-K8S-0905-017.md) | Model registry operation audit logging and forwarding | Practitioner | ai-specific |
| [SAFE-K8S-0905-018](markdown/controls/SAFE-K8S-0905-018.md) | ML framework and CUDA dependency vulnerability management | Advanced | ai-specific |
| [SAFE-K8S-0905-019](markdown/controls/SAFE-K8S-0905-019.md) | ML-BOM generation and model lineage metadata capture | Advanced | ai-specific |
| [SAFE-K8S-0905-020](markdown/controls/SAFE-K8S-0905-020.md) | Public model quarantine scanning and sandbox vetting | Advanced | ai-specific |
| [SAFE-K8S-0905-021](markdown/controls/SAFE-K8S-0905-021.md) | External model provenance verification and internal re-registration | Advanced | ai-specific |
| [SAFE-K8S-0905-022](markdown/controls/SAFE-K8S-0905-022.md) | ML artifact signing and training attestation generation | Advanced | ai-specific |
| [SAFE-K8S-0905-023](markdown/controls/SAFE-K8S-0905-023.md) | OCI model artifact digest pinning and tag immutability | Advanced | ai-specific |
| [SAFE-K8S-0905-024](markdown/controls/SAFE-K8S-0905-024.md) | Authenticated reviewer identity validation and approval audit binding | Advanced | ai-specific |
| [SAFE-K8S-0905-025](markdown/controls/SAFE-K8S-0905-025.md) | Separation of duties enforcement for model promotion approvals | Advanced | ai-specific |
| [SAFE-K8S-0905-026](markdown/controls/SAFE-K8S-0905-026.md) | Approved external model source allowlist governance and review | Advanced | ai-specific |
| [SAFE-K8S-0905-027](markdown/controls/SAFE-K8S-0905-027.md) | External model source enforcement through network policy and admission control | Advanced | ai-specific |
| [SAFE-K8S-0905-028](markdown/controls/SAFE-K8S-0905-028.md) | ML framework and Python dependency vulnerability management | Advanced | ai-specific |
| [SAFE-K8S-0905-029](markdown/controls/SAFE-K8S-0905-029.md) | CUDA and GPU accelerator dependency vulnerability management | Advanced | ai-specific |
| [SAFE-K8S-0905-030](markdown/controls/SAFE-K8S-0905-030.md) | External model provenance verification and trust-signal review | Advanced | ai-specific |
| [SAFE-K8S-0905-031](markdown/controls/SAFE-K8S-0905-031.md) | Internal re-signing, external-origin annotation, and registry admission for external models | Advanced | ai-specific |
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
- Controls: 7

### Description

Training data provenance tracking: lineage from ingestion through feature engineering to model training; secure data pipeline ingestion with integrity checks at each transformation stage Data integrity at scale: hierarchical hashing for large training datasets, manifest-based integrity verification, segmented integrity checking for datasets across distributed storage, and erasure coding vs. mirroring tradeoffs for ML data resilience Data poisoning detection: statistical drift detection, outlier analysis, label verification, and input validation controls; label modification attack detection - integrity verification for annotation pipelines, annotator authentication, and detection of targeted label flipping distinct from broader data poisoning

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0906-001](markdown/controls/SAFE-K8S-0906-001.md) | Training data provenance and pipeline integrity | Practitioner | ai-specific |
| [SAFE-K8S-0906-002](markdown/controls/SAFE-K8S-0906-002.md) | Large-scale data integrity verification | Practitioner | ai-specific |
| [SAFE-K8S-0906-003](markdown/controls/SAFE-K8S-0906-003.md) | Data poisoning and label attack detection | Practitioner | ai-specific |
| [SAFE-K8S-0906-004](markdown/controls/SAFE-K8S-0906-004.md) | Statistical drift, outlier, and input validation for training data poisoning detection | Practitioner | ai-specific |
| [SAFE-K8S-0906-005](markdown/controls/SAFE-K8S-0906-005.md) | Annotation pipeline integrity and targeted label attack detection | Practitioner | ai-specific |
| [SAFE-K8S-0906-006](markdown/controls/SAFE-K8S-0906-006.md) | Training data provenance tracking from ingestion through model training | Practitioner | ai-specific |
| [SAFE-K8S-0906-007](markdown/controls/SAFE-K8S-0906-007.md) | Integrity verification at each training data transformation stage | Practitioner | ai-specific |

<a id="knowledge-area-9-7"></a>
## 9.7 - Feature Store Security and Data Access Controls

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 7

### Description

Feature store security (Feast, Tecton): access controls for feature definitions, online/offline store separation, serving authentication; data preprocessing job security (raw data access controls, PII handling during feature engineering, output validation); feature leakage prevention (unintended exposure of target variables or future information in features) and target leakage controls Privacy controls for training data: PII handling, data classification, anonymization, and data access audit trails (see Appendix A: AI Data Privacy Governance for consent management, privacy notices, and individual data rights) Data access controls for training datasets stored in persistent volumes, object storage, and feature stores; Kubernetes-native and external authorization for model download and deployment (who can pull which models, deploy to which namespaces)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0907-001](markdown/controls/SAFE-K8S-0907-001.md) | Feature store security and leakage prevention | Practitioner | ai-specific |
| [SAFE-K8S-0907-002](markdown/controls/SAFE-K8S-0907-002.md) | Training data privacy controls | Practitioner | ai-specific |
| [SAFE-K8S-0907-003](markdown/controls/SAFE-K8S-0907-003.md) | Training dataset and model deployment access controls | Practitioner | ai-specific |
| [SAFE-K8S-0907-004](markdown/controls/SAFE-K8S-0907-004.md) | Feature store access boundary enforcement and serving authentication | Practitioner | ai-specific |
| [SAFE-K8S-0907-005](markdown/controls/SAFE-K8S-0907-005.md) | Feature engineering privacy controls and leakage validation | Practitioner | ai-specific |
| [SAFE-K8S-0907-006](markdown/controls/SAFE-K8S-0907-006.md) | Training dataset access restriction across storage backends | Practitioner | ai-specific |
| [SAFE-K8S-0907-007](markdown/controls/SAFE-K8S-0907-007.md) | Model deployment authorization and namespace-scoped release control | Practitioner | ai-specific |

<a id="knowledge-area-9-8"></a>
## 9.8 - Model Abuse and Extraction Prevention

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Advanced
- Controls: 10

### Description

Oracle attack prevention at the serving infrastructure layer: model extraction (stealing model weights through systematic queries), model inversion (reconstructing training data from model outputs), and membership inference (determining whether specific data was in the training set) - rate limiting per principal, query pattern analysis, and anomaly detection as infrastructure-level controls Information exposure controls: inference API design to minimize information disclosure, output confidence score restriction, logit/probability access controls, feature leakage prevention, and model architecture obfuscation at the serving boundary Watermarking and fingerprinting integration at the serving layer to detect stolen model outputs Differential privacy and output perturbation controls deployed at inference time to limit information leakage; secure aggregation for privacy-preserving model outputs Logging and alerting for model abuse patterns: query volume anomalies, input distribution shifts, coordinated extraction campaigns, and evasion attack detection (adversarial inputs designed to cause misclassification); monitoring external sites and channels for leaked or stolen model outputs

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0908-001](markdown/controls/SAFE-K8S-0908-001.md) | Oracle attack prevention | Advanced | ai-specific |
| [SAFE-K8S-0908-002](markdown/controls/SAFE-K8S-0908-002.md) | Inference API information exposure controls | Advanced | ai-specific |
| [SAFE-K8S-0908-003](markdown/controls/SAFE-K8S-0908-003.md) | Model watermarking and fingerprinting | Advanced | ai-specific |
| [SAFE-K8S-0908-004](markdown/controls/SAFE-K8S-0908-004.md) | Differential privacy and output perturbation | Advanced | ai-specific |
| [SAFE-K8S-0908-005](markdown/controls/SAFE-K8S-0908-005.md) | Model abuse logging and alerting | Advanced | ai-specific |
| [SAFE-K8S-0908-006](markdown/controls/SAFE-K8S-0908-006.md) | Secure aggregation for privacy-preserving model outputs | Advanced | ai-specific |
| [SAFE-K8S-0908-007](markdown/controls/SAFE-K8S-0908-007.md) | Differential privacy parameter governance and budget tracking for inference | Advanced | ai-specific |
| [SAFE-K8S-0908-008](markdown/controls/SAFE-K8S-0908-008.md) | Inference output perturbation and privacy-preserving response shaping | Advanced | ai-specific |
| [SAFE-K8S-0908-009](markdown/controls/SAFE-K8S-0908-009.md) | Differential privacy parameter governance for inference endpoints | Advanced | ai-specific |
| [SAFE-K8S-0908-010](markdown/controls/SAFE-K8S-0908-010.md) | Inference privacy budget tracking and threshold enforcement | Advanced | ai-specific |

<a id="knowledge-area-9-9"></a>
## 9.9 - RAG Infrastructure Security

- Domain: D09 - AI Workload Security: Training, Serving, and Pipelines
- Maturity: Practitioner
- Controls: 14

### Description

Vector database access controls and encryption: authentication, RBAC, and collection-level access controls for vector databases (Milvus, Weaviate, Qdrant, pgvector, Chroma); encryption at rest and in transit; network isolation for vector database pods Embedding pipeline integrity: embedding model signature verification and version pinning; input document validation and sanitization; deterministic embedding configurations for auditability Document ingestion and chunking security: source repository access controls; document provenance and integrity verification; security-aware chunking that preserves classification boundaries and prevents cross-classification content mixing Retrieved context integrity verification: chunk metadata validation; source provenance checking; index change monitoring and alerting; retrieval audit logging; context poisoning detection via snapshot diffing; source attribution and redundant retrieval strategies Retrieval relevance threshold enforcement: minimum similarity threshold configuration; top-K result limiting; per-query-type threshold profiles; threshold rejection rate monitoring for poisoning detection RAG prompt injection defense: indirect prompt injection mitigation through retrieved chunk sanitization, instruction-data separation in prompt templates, and monitoring for prompt injection patterns in retrieval results Vector index lifecycle management: versioned index snapshots, integrity verification, controlled rebuild and migration procedures, and secure deletion of retired indexes and associated embedding data

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0909-001](markdown/controls/SAFE-K8S-0909-001.md) | Vector database access controls and encryption | Practitioner | ai-specific |
| [SAFE-K8S-0909-002](markdown/controls/SAFE-K8S-0909-002.md) | Embedding pipeline integrity | Practitioner | ai-specific |
| [SAFE-K8S-0909-003](markdown/controls/SAFE-K8S-0909-003.md) | Document ingestion and chunking security | Practitioner | ai-specific |
| [SAFE-K8S-0909-004](markdown/controls/SAFE-K8S-0909-004.md) | Retrieval integrity and context poisoning defense | Practitioner | ai-specific |
| [SAFE-K8S-0909-005](markdown/controls/SAFE-K8S-0909-005.md) | RAG prompt injection defense | Practitioner | ai-specific |
| [SAFE-K8S-0909-006](markdown/controls/SAFE-K8S-0909-006.md) | Vector index lifecycle management | Practitioner | ai-specific |
| [SAFE-K8S-0909-007](markdown/controls/SAFE-K8S-0909-007.md) | Document source access control and provenance validation for RAG ingestion | Practitioner | ai-specific |
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
- Controls: 33

### Description

Cross-cluster orchestration identity and audit security: authenticated and authorized cross-cluster API calls using federated workload identity; centralized orchestration audit trails for placement and routing decisions Security-aware multi-cluster placement and federation isolation: target-cluster security posture verification before workload placement; circuit-breaker isolation and controlled re-admission for compromised clusters Cross-cluster model registry federation and replication security: signature re-verification on pull, authenticated replication channels, provenance chain-of-custody across cluster boundaries, replication integrity verification, federation membership governance Multi-cluster network security for distributed AI workloads: cross-cluster encryption and authentication, cross-cluster network policy, cross-cluster traffic monitoring, bandwidth and latency governance Federated learning cross-cluster coordination security: cross-cluster participant authentication, cross-boundary secure aggregation, consistent privacy enforcement, single-cluster compromise resilience, cross-cluster FL audit trail Multi-cluster AI governance and compliance consistency: policy federation, configuration drift detection, unified compliance reporting, centralized secret and certificate governance, multi-cluster incident coordination

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-0910-001](markdown/controls/SAFE-K8S-0910-001.md) | Multi-cluster AI workload orchestration security | Advanced | ai-specific |
| [SAFE-K8S-0910-002](markdown/controls/SAFE-K8S-0910-002.md) | Cross-cluster model registry federation and replication security | Advanced | ai-specific |
| [SAFE-K8S-0910-003](markdown/controls/SAFE-K8S-0910-003.md) | Multi-cluster network security for distributed AI workloads | Advanced | ai-specific |
| [SAFE-K8S-0910-004](markdown/controls/SAFE-K8S-0910-004.md) | Federated learning cross-cluster coordination security | Advanced | ai-specific |
| [SAFE-K8S-0910-005](markdown/controls/SAFE-K8S-0910-005.md) | Multi-cluster AI governance and compliance consistency | Advanced | ai-specific |
| [SAFE-K8S-0910-006](markdown/controls/SAFE-K8S-0910-006.md) | Cross-cluster orchestration identity and audit security | Advanced | ai-specific |
| [SAFE-K8S-0910-007](markdown/controls/SAFE-K8S-0910-007.md) | Security-aware multi-cluster placement and federation isolation | Advanced | ai-specific |
| [SAFE-K8S-0910-008](markdown/controls/SAFE-K8S-0910-008.md) | Cross-cluster transport encryption and workload authentication | Advanced | ai-specific |
| [SAFE-K8S-0910-009](markdown/controls/SAFE-K8S-0910-009.md) | Cross-cluster communication authorization and anomaly monitoring | Advanced | ai-specific |
| [SAFE-K8S-0910-010](markdown/controls/SAFE-K8S-0910-010.md) | Cross-cluster registry replication channel authentication and signature re-verification | Advanced | ai-specific |
| [SAFE-K8S-0910-011](markdown/controls/SAFE-K8S-0910-011.md) | Cross-cluster model provenance preservation and federation endpoint governance | Advanced | ai-specific |
| [SAFE-K8S-0910-012](markdown/controls/SAFE-K8S-0910-012.md) | Multi-cluster security policy federation and drift remediation | Advanced | ai-specific |
| [SAFE-K8S-0910-013](markdown/controls/SAFE-K8S-0910-013.md) | Unified multi-cluster compliance reporting and governance coordination | Advanced | ai-specific |
| [SAFE-K8S-0910-014](markdown/controls/SAFE-K8S-0910-014.md) | Cross-cluster registry replication channel authentication and endpoint enrollment | Advanced | ai-specific |
| [SAFE-K8S-0910-015](markdown/controls/SAFE-K8S-0910-015.md) | Destination-side signature and digest re-verification for replicated model artifacts | Advanced | ai-specific |
| [SAFE-K8S-0910-016](markdown/controls/SAFE-K8S-0910-016.md) | Cross-cluster orchestration identity federation and authorization | Advanced | ai-specific |
| [SAFE-K8S-0910-017](markdown/controls/SAFE-K8S-0910-017.md) | Centralized audit logging for cross-cluster orchestration actions | Advanced | ai-specific |
| [SAFE-K8S-0910-018](markdown/controls/SAFE-K8S-0910-018.md) | Security-aware target-cluster posture verification before multi-cluster placement | Advanced | ai-specific |
| [SAFE-K8S-0910-019](markdown/controls/SAFE-K8S-0910-019.md) | Compromised-cluster federation isolation and re-admission governance | Advanced | ai-specific |
| [SAFE-K8S-0910-020](markdown/controls/SAFE-K8S-0910-020.md) | Cross-cluster transport encryption for distributed AI traffic | Advanced | ai-specific |
| [SAFE-K8S-0910-021](markdown/controls/SAFE-K8S-0910-021.md) | Cross-cluster endpoint and workload authentication for AI communication | Advanced | ai-specific |
| [SAFE-K8S-0910-022](markdown/controls/SAFE-K8S-0910-022.md) | Cross-cluster communication authorization policy enforcement | Advanced | ai-specific |
| [SAFE-K8S-0910-023](markdown/controls/SAFE-K8S-0910-023.md) | Cross-cluster traffic anomaly monitoring and investigation | Advanced | ai-specific |
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
- Controls: 39

### Description

Kubernetes audit policy configuration: audit levels (None, Metadata, Request, RequestResponse), stage filtering, and backend selection; audit policy rules for AI-relevant API requests (CRD operations, GPU resource changes, admission decisions); supplemental application-level telemetry for non-API events (model loading, GPU process activity, inference request content) Cluster-level logging architecture: node-level log collection, centralized log aggregation, log integrity, and retention policies Centralized logging for AI workloads: training logs, inference request/response logs (with PII redaction), and pipeline execution logs Audit volume management for high-throughput AI workloads: selective audit policy design (tiered levels, omitStages), backend tuning (batching, throttling, buffer sizing, capacity planning), and drop/backpressure monitoring Permitted responses to audit findings and dual authorization requirements for audit log deletion or modification SIEM integration: forwarding Kubernetes audit logs and security events to SIEM platforms, correlation rule development

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1001-001](markdown/controls/SAFE-K8S-1001-001.md) | Kubernetes audit policy coverage for AI-relevant API events | Practitioner | ai-specific |
| [SAFE-K8S-1001-002](markdown/controls/SAFE-K8S-1001-002.md) | Cluster-level logging architecture | Practitioner | baseline |
| [SAFE-K8S-1001-003](markdown/controls/SAFE-K8S-1001-003.md) | Centralized logging for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-004](markdown/controls/SAFE-K8S-1001-004.md) | Audit volume management for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-005](markdown/controls/SAFE-K8S-1001-005.md) | Audit log protection and dual authorization for modification | Practitioner | baseline |
| [SAFE-K8S-1001-006](markdown/controls/SAFE-K8S-1001-006.md) | SIEM ingestion for Kubernetes AI security events | Practitioner | ai-specific |
| [SAFE-K8S-1001-007](markdown/controls/SAFE-K8S-1001-007.md) | Supplemental application-level telemetry for AI workload events | Practitioner | ai-specific |
| [SAFE-K8S-1001-008](markdown/controls/SAFE-K8S-1001-008.md) | Permitted responses to audit findings | Practitioner | baseline |
| [SAFE-K8S-1001-009](markdown/controls/SAFE-K8S-1001-009.md) | Regulatory log and artifact retention policy enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-010](markdown/controls/SAFE-K8S-1001-010.md) | Kubernetes audit level and stage filtering for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-011](markdown/controls/SAFE-K8S-1001-011.md) | Durable and tamper-resistant audit backend delivery | Practitioner | ai-specific |
| [SAFE-K8S-1001-012](markdown/controls/SAFE-K8S-1001-012.md) | SIEM correlation rules for AI-specific attack patterns | Practitioner | ai-specific |
| [SAFE-K8S-1001-013](markdown/controls/SAFE-K8S-1001-013.md) | SIEM event forwarding and ingestion health for Kubernetes AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-014](markdown/controls/SAFE-K8S-1001-014.md) | Centralized collection and segregation of AI workload logs | Practitioner | ai-specific |
| [SAFE-K8S-1001-015](markdown/controls/SAFE-K8S-1001-015.md) | PII redaction and sensitive payload minimization for inference logs | Practitioner | ai-specific |
| [SAFE-K8S-1001-016](markdown/controls/SAFE-K8S-1001-016.md) | Audit policy coverage for AI-specific resource and workflow events | Practitioner | ai-specific |
| [SAFE-K8S-1001-017](markdown/controls/SAFE-K8S-1001-017.md) | Audit capture of admission, authorization, and privileged API decisions for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1001-018](markdown/controls/SAFE-K8S-1001-018.md) | Regulatory audit log retention period and durable retrieval enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-019](markdown/controls/SAFE-K8S-1001-019.md) | Regulatory AI artifact and provenance record retention enforcement | Practitioner | ai-specific |
| [SAFE-K8S-1001-020](markdown/controls/SAFE-K8S-1001-020.md) | Cluster-wide AI workload log collection and centralized aggregation | Practitioner | baseline |
| [SAFE-K8S-1001-021](markdown/controls/SAFE-K8S-1001-021.md) | Centralized log integrity protection and retention enforcement for AI workloads | Practitioner | baseline |
| [SAFE-K8S-1001-022](markdown/controls/SAFE-K8S-1001-022.md) | Regulatory audit log retention period enforcement | Practitioner | ai-specific |
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
| [SAFE-K8S-1001-035](markdown/controls/SAFE-K8S-1001-035.md) | Centralized AI log retention lifecycle enforcement and durable retrieval | Practitioner | baseline |
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

Metrics security: Prometheus/metrics-server access controls, metric endpoint authentication, and sensitive metric redaction; AI workload telemetry integration (GPU metrics via DCGM exporter, training job progress, inference latency, and model performance indicators) Distributed tracing for ML pipelines: end-to-end trace propagation from data ingestion through training to inference serving; alert design for AI-specific failure modes (training divergence, model staleness, GPU errors, inference accuracy degradation)

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
- Controls: 5

### Description

STRIDE methodology applied to Kubernetes: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege - mapped to K8s components OCTAVE methodology: risk-based threat assessment for Kubernetes environments, asset identification, and threat profiling MITRE ATT&CK Threat Matrix for Containers: understanding tactics and techniques specific to container and Kubernetes attacks

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1003-001](markdown/controls/SAFE-K8S-1003-001.md) | STRIDE threat modeling for Kubernetes AI systems | Practitioner | ai-specific |
| [SAFE-K8S-1003-002](markdown/controls/SAFE-K8S-1003-002.md) | OCTAVE risk-based threat assessment for Kubernetes AI environments | Advanced | ai-specific |
| [SAFE-K8S-1003-003](markdown/controls/SAFE-K8S-1003-003.md) | MITRE ATT&CK for Containers threat mapping | Advanced | ai-specific |
| [SAFE-K8S-1003-004](markdown/controls/SAFE-K8S-1003-004.md) | MITRE ATT&CK for Containers coverage mapping and gap analysis | Advanced | ai-specific |
| [SAFE-K8S-1003-005](markdown/controls/SAFE-K8S-1003-005.md) | Technique-aligned detection engineering for Kubernetes AI attack scenarios | Advanced | ai-specific |

<a id="knowledge-area-10-4"></a>
## 10.4 - AI and Supply Chain Threat Taxonomy

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Advanced
- Controls: 6

### Description

ML threat taxonomy per CTA-2114: formal classification of AI-specific threats - Data Poisoning, Model Poisoning, Targeted Poisoning, Label Modification, Model Disclosure, Data Disclosure, Evasion (adversarial examples), Oracle Attacks (extraction, inversion, membership inference), and Denial of Service via computational complexity - mapped to Kubernetes infrastructure attack surfaces and control points Software supply chain threat model per NIST SP 800-204D: three-stage SSC attack lifecycle (Compromise → Propagation → Exploitation), SSC defects vs. SSC attacks distinction, attack targets (source code, credentials, build systems, internal operations), and attack vectors (dependency confusion, typosquatting, malicious PRs, compromised build tools) applied to Kubernetes CI/CD and AI pipeline infrastructure Threat intelligence integration: consuming Kubernetes CVE feeds, runtime threat intelligence, and attack pattern libraries for detection rule development; NISTIR 8269 adversarial ML taxonomy for structured threat classification; correlating technical audit data with business context and non-technical sources (organizational risk indicators, physical security events, HR actions)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1004-001](markdown/controls/SAFE-K8S-1004-001.md) | ML threat taxonomy per CTA-2114 mapped to Kubernetes | Advanced | ai-specific |
| [SAFE-K8S-1004-002](markdown/controls/SAFE-K8S-1004-002.md) | Software supply chain threat model per NIST SP 800-204D | Advanced | ai-specific |
| [SAFE-K8S-1004-003](markdown/controls/SAFE-K8S-1004-003.md) | Threat intelligence integration for Kubernetes AI environments | Advanced | ai-specific |
| [SAFE-K8S-1004-004](markdown/controls/SAFE-K8S-1004-004.md) | Kubernetes AI threat intelligence feed ingestion and detection enrichment | Advanced | ai-specific |
| [SAFE-K8S-1004-005](markdown/controls/SAFE-K8S-1004-005.md) | Adversarial ML threat taxonomy and structured classification | Advanced | ai-specific |
| [SAFE-K8S-1004-006](markdown/controls/SAFE-K8S-1004-006.md) | Cross-source threat correlation with business context for AI incidents | Advanced | ai-specific |

<a id="knowledge-area-10-5"></a>
## 10.5 - Incident Response for Kubernetes

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Practitioner
- Controls: 30

### Description

IR lifecycle for Kubernetes environments: preparation, detection and analysis, containment, eradication and recovery, post-incident activity; AI-specific IR playbooks for compromised training jobs, model poisoning detection, GPU cryptomining, and inference endpoint abuse Containment strategies: draining compromised nodes, isolating namespaces with network policies, suspending workloads, revoking credentials; AI-specific containment (draining GPU nodes, quarantining inference services, suspending pipeline executions) Automated containment triggers: automated node cordoning on anomaly detection, programmatic namespace isolation via network policy templates, automated inference service scaling to zero, and pipeline controller suspension without manual intervention Forensic evidence collection: container snapshots, audit log preservation, network flow capture, and chain-of-custody procedures; AI-specific forensic evidence (GPU allocation logs, model access audit trails, training data provenance records) Ransomware and destructive attack response: backup verification, etcd restoration, workload recovery prioritization, and lessons-learned processes Post-incident model validation: verifying model integrity after infrastructure compromise, retraining decisions, rollback procedures, and protection against lateral movement from compromised AI workloads to cluster control plane or other tenants; component protection during recovery operations (preventing reinfection, integrity verification before restoration)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1005-001](markdown/controls/SAFE-K8S-1005-001.md) | Kubernetes incident response lifecycle | Practitioner | ai-specific |
| [SAFE-K8S-1005-002](markdown/controls/SAFE-K8S-1005-002.md) | Kubernetes and AI workload containment strategies | Practitioner | ai-specific |
| [SAFE-K8S-1005-003](markdown/controls/SAFE-K8S-1005-003.md) | Forensic evidence collection for Kubernetes AI incidents | Practitioner | ai-specific |
| [SAFE-K8S-1005-004](markdown/controls/SAFE-K8S-1005-004.md) | Ransomware and destructive attack response for Kubernetes | Practitioner | baseline |
| [SAFE-K8S-1005-005](markdown/controls/SAFE-K8S-1005-005.md) | Post-incident model integrity verification and recovery decisions | Practitioner | ai-specific |
| [SAFE-K8S-1005-006](markdown/controls/SAFE-K8S-1005-006.md) | Lateral movement prevention and component integrity verification during recovery | Practitioner | ai-specific |
| [SAFE-K8S-1005-007](markdown/controls/SAFE-K8S-1005-007.md) | Vulnerability disclosure and coordination for Kubernetes infrastructure | Practitioner | baseline |
| [SAFE-K8S-1005-008](markdown/controls/SAFE-K8S-1005-008.md) | AI-specific incident response playbooks for Kubernetes | Practitioner | ai-specific |
| [SAFE-K8S-1005-009](markdown/controls/SAFE-K8S-1005-009.md) | Kubernetes containment procedures for nodes, namespaces, workloads, and credentials | Practitioner | ai-specific |
| [SAFE-K8S-1005-010](markdown/controls/SAFE-K8S-1005-010.md) | AI-specific containment actions for GPU nodes, inference services, and pipeline execution | Practitioner | ai-specific |
| [SAFE-K8S-1005-011](markdown/controls/SAFE-K8S-1005-011.md) | Kubernetes forensic evidence acquisition and chain-of-custody procedures | Practitioner | ai-specific |
| [SAFE-K8S-1005-012](markdown/controls/SAFE-K8S-1005-012.md) | AI-specific forensic preservation of GPU, model access, and training provenance evidence | Practitioner | ai-specific |
| [SAFE-K8S-1005-013](markdown/controls/SAFE-K8S-1005-013.md) | Kubernetes backup verification and etcd restoration readiness | Practitioner | baseline |
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
- Controls: 10

### Description

Regulatory compliance mapping: NIST AI RMF, applicable EU AI Act obligations based on organizational role (provider or deployer) and AI system risk classification, SOC 2 considerations for Kubernetes platforms (see Appendix A: Compliance Framework Mapping for detailed regulatory mapping) SSDF v1.1 and SP 800-218A alignment: mapping Kubernetes security practices to NIST SSDF v1.1 (SP 800-218) requirements and the SP 800-218A AI/ML-specific community profile (see Appendix A: Compliance Framework Mapping for SSDF adaptation for AI/ML systems) Policy-as-code for compliance: OPA/Gatekeeper, Kyverno, and Kubewarden policies generating continuous compliance evidence; AI workload governance policies (enforce image provenance, GPU limits, security contexts) Audit readiness: automated compliance evidence collection, configuration snapshot generation, and framework crosswalk documentation (see Appendix A: Compliance Framework Mapping for extended audit readiness and metrics review)

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1006-001](markdown/controls/SAFE-K8S-1006-001.md) | Regulatory compliance mapping for Kubernetes AI platforms | Practitioner | ai-specific |
| [SAFE-K8S-1006-002](markdown/controls/SAFE-K8S-1006-002.md) | SSDF v1.1 and SP 800-218A alignment for Kubernetes AI development | Advanced | ai-specific |
| [SAFE-K8S-1006-003](markdown/controls/SAFE-K8S-1006-003.md) | Policy-as-code for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1006-004](markdown/controls/SAFE-K8S-1006-004.md) | Automated audit readiness for Kubernetes AI platforms | Advanced | ai-specific |
| [SAFE-K8S-1006-005](markdown/controls/SAFE-K8S-1006-005.md) | Policy-as-code enforcement for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1006-006](markdown/controls/SAFE-K8S-1006-006.md) | Continuous compliance evidence generation for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1006-007](markdown/controls/SAFE-K8S-1006-007.md) | NIST SSDF v1.1 alignment and gap assessment for Kubernetes AI development | Advanced | ai-specific |
| [SAFE-K8S-1006-008](markdown/controls/SAFE-K8S-1006-008.md) | NIST SP 800-218A AI/ML profile alignment for Kubernetes AI development | Advanced | ai-specific |
| [SAFE-K8S-1006-009](markdown/controls/SAFE-K8S-1006-009.md) | Continuous policy decision evidence generation and export for AI workload compliance | Practitioner | ai-specific |
| [SAFE-K8S-1006-010](markdown/controls/SAFE-K8S-1006-010.md) | Policy exception approval and expiration governance for AI workload compliance | Practitioner | ai-specific |

<a id="knowledge-area-10-7"></a>
## 10.7 - Cluster Lifecycle and Asset Inventory

- Domain: D10 - Observability, Incident Response, and Governance
- Maturity: Practitioner
- Controls: 18

### Description

Kubernetes upgrade plan documentation: version skew policy requirements, component-by-component upgrade sequencing procedures, rollback procedures per component, and AI infrastructure component compatibility matrix (GPU drivers, CUDA toolkits, operators, and serving frameworks) Non-disruptive cluster upgrade execution: staging-environment validation before production promotion, training job schedule coordination, GPU node drain and cordon procedures, and post-upgrade security posture verification Deprecation tracking: API version migration, removed feature detection, and proactive compatibility testing AI infrastructure asset inventory: automated discovery and classification of models, datasets, pipelines, inference endpoints, and GPU allocations Security posture management: continuous assessment of cluster configuration drift, benchmark compliance, and vulnerability exposure; capacity planning and security implications of GPU cluster scaling (new node onboarding security, hardware attestation, driver verification) Change management for model deployments: approval workflows, deployment windows, and rollback procedures for production model updates; AI workload decommissioning (secure cleanup of training data, model artifacts, GPU reservations, secrets, and access grants); protection of cluster-level services (DNS, metrics, logging) from resource exhaustion by large-scale training jobs

### Controls

| Control ID | Title | Maturity | Class |
| --- | --- | --- | --- |
| [SAFE-K8S-1007-001](markdown/controls/SAFE-K8S-1007-001.md) | Kubernetes and AI infrastructure upgrade planning | Practitioner | ai-specific |
| [SAFE-K8S-1007-002](markdown/controls/SAFE-K8S-1007-002.md) | Kubernetes API deprecation and removal tracking | Practitioner | ai-specific |
| [SAFE-K8S-1007-003](markdown/controls/SAFE-K8S-1007-003.md) | AI infrastructure asset inventory and classification | Practitioner | ai-specific |
| [SAFE-K8S-1007-004](markdown/controls/SAFE-K8S-1007-004.md) | Continuous security posture management for AI clusters | Practitioner | ai-specific |
| [SAFE-K8S-1007-005](markdown/controls/SAFE-K8S-1007-005.md) | Change management for production AI model deployments | Practitioner | ai-specific |
| [SAFE-K8S-1007-006](markdown/controls/SAFE-K8S-1007-006.md) | Secure AI workload decommissioning | Practitioner | ai-specific |
| [SAFE-K8S-1007-007](markdown/controls/SAFE-K8S-1007-007.md) | Cluster service protection from AI training resource exhaustion | Practitioner | ai-specific |
| [SAFE-K8S-1007-008](markdown/controls/SAFE-K8S-1007-008.md) | GPU cluster scaling governance and node onboarding security | Advanced | ai-specific |
| [SAFE-K8S-1007-009](markdown/controls/SAFE-K8S-1007-009.md) | Kubernetes API deprecation monitoring and usage discovery | Practitioner | ai-specific |
| [SAFE-K8S-1007-010](markdown/controls/SAFE-K8S-1007-010.md) | Pre-upgrade Kubernetes API compatibility testing for AI workloads | Practitioner | ai-specific |
| [SAFE-K8S-1007-011](markdown/controls/SAFE-K8S-1007-011.md) | Kubernetes cluster upgrade planning, sequencing, and rollback governance | Practitioner | ai-specific |
| [SAFE-K8S-1007-012](markdown/controls/SAFE-K8S-1007-012.md) | AI infrastructure compatibility matrix and coordinated component upgrade governance | Practitioner | ai-specific |
| [SAFE-K8S-1007-013](markdown/controls/SAFE-K8S-1007-013.md) | Automated AI infrastructure asset discovery and continuously updated inventory | Practitioner | ai-specific |
| [SAFE-K8S-1007-014](markdown/controls/SAFE-K8S-1007-014.md) | AI asset classification and criticality governance for Kubernetes environments | Practitioner | ai-specific |
| [SAFE-K8S-1007-015](markdown/controls/SAFE-K8S-1007-015.md) | GPU node onboarding security baseline validation gates | Advanced | ai-specific |
| [SAFE-K8S-1007-016](markdown/controls/SAFE-K8S-1007-016.md) | GPU node hardware attestation, driver integrity, and taint verification | Advanced | ai-specific |
| [SAFE-K8S-1007-017](markdown/controls/SAFE-K8S-1007-017.md) | Kubernetes release-channel and changelog monitoring for API deprecations | Practitioner | ai-specific |
| [SAFE-K8S-1007-018](markdown/controls/SAFE-K8S-1007-018.md) | Deprecated Kubernetes API usage inventory and migration tracking for AI workloads | Practitioner | ai-specific |
