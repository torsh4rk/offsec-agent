---
name: kubernetes-security
description: Assess authorized Kubernetes clusters through RBAC, workload, admission, network, secret, supply-chain, node, and control-plane review.
license: MIT
compatibility: opencode,codex
metadata:
  domain: container-orchestration-security
  platform: kubernetes
  safety: authorized-only
---

# Kubernetes Security

## Purpose

Evaluate Kubernetes security boundaries from identities and admission through workloads, networking, nodes, and the control plane.

## Core workflow

1. Confirm clusters, contexts, namespaces, identities, kubeconfig handling, workloads, nodes, and excluded resources.
2. Collect read-only cluster, namespace, workload, RBAC, admission, network-policy, secret-reference, and audit configuration.
3. Map subjects to effective verbs, resources, subresources, namespaces, and impersonation paths.
4. Review pod security context, service accounts, token mounts, host access, image provenance, and runtime isolation.
5. Validate only with approved test namespaces and synthetic resources.
6. Document remediation as manifests or policy changes with rollback and retest commands.

## Coverage

- RBAC, aggregated roles, impersonation, service accounts, token audiences, and workload identity.
- Pod Security Standards, admission controllers, policy engines, seccomp, AppArmor/SELinux, Linux capabilities, and privileged workloads.
- Secrets, ConfigMaps, etcd exposure, audit logs, API server settings, kubelet access, and node boundaries.
- NetworkPolicy, ingress, egress, service meshes, DNS, image registries, signatures, SBOMs, and supply chain.

## Evidence standard

Record cluster/context, namespace, identity, API verb/resource, manifest fragment, effective permission, expected boundary, observed behavior, timestamp, and scope reference. A permissive role is not a confirmed escalation unless its binding and reachable impact are demonstrated.

## Approval boundaries

- Read-only discovery is the default.
- Pod creation, exec, attach, port-forward, secret reads, impersonation, privileged workloads, host mounts, node access, token extraction, workload mutation, or control-plane changes require explicit approval.
- Never disrupt scheduling, admission, networking, storage, or production workloads.

## Deliverables

- Cluster and namespace security map.
- RBAC and workload-risk matrix.
- Admission, runtime, network, and supply-chain findings.
- Safe remediation manifests and retest plan.
