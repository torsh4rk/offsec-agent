---
name: cloud-security
description: Assess authorized AWS, Azure, and GCP environments through identity, configuration, network, data, workload, logging, and control-plane review.
license: MIT
compatibility: opencode,codex
metadata:
  domain: cloud-security
  platforms: aws,azure,gcp
  safety: authorized-only
---

# Cloud Security — AWS, Azure, and GCP

## Purpose

Evaluate cloud control planes and workloads with provider-aware identity analysis, explicit tenant boundaries, and least-invasive validation.

## Core workflow

1. Confirm provider, organization or tenant, accounts/subscriptions/projects, regions, credentials, test roles, and excluded resources.
2. Inventory identities, role bindings, policies, resource hierarchy, networks, public endpoints, data stores, secrets, workloads, and audit controls.
3. Build trust paths from principals to actions and resources; distinguish assigned, effective, and conditionally reachable privilege.
4. Prioritize public exposure, cross-tenant trust, privilege paths, data access, key management, and logging gaps.
5. Validate with read-only API calls or harmless synthetic resources when authorized.
6. Record provider-native remediation and retest queries.

## Coverage

- AWS IAM, Organizations, STS, resource policies, S3, KMS, Lambda, EC2, EKS, CloudTrail, and network controls.
- Microsoft Entra ID, Azure RBAC, subscriptions, managed identities, Key Vault, Storage, Functions, VMs, AKS, Activity Logs, and network controls.
- GCP IAM, organizations/folders/projects, service accounts, Cloud Storage, KMS, Cloud Run/Functions, Compute Engine, GKE, audit logs, and VPC controls.
- CI/CD federation, workload identity, third-party applications, secrets, snapshots, backups, and cross-account sharing.

## Evidence standard

Record tenant/account/project, region, principal, API operation, resource identifier, policy path, expected denial or boundary, observed result, timestamp, and scope reference. A broad-looking policy is not a confirmed privilege path until conditions, resource scope, trust policy, and effective permissions are evaluated.

## Approval boundaries

- Default to inventory and policy simulation or read-only API operations.
- Role assumption beyond designated test roles, access-key creation, secret retrieval, metadata access, cross-account movement, resource deployment, public exposure changes, data copying, persistence, or destructive actions require explicit approval.
- Never test provider infrastructure or unrelated tenants.

## Deliverables

- Resource and identity inventory.
- Effective privilege and trust-path map.
- Public exposure and logging coverage summary.
- Provider-specific findings, remediation, and retest procedures.
