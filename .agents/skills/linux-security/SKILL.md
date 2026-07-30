---
name: linux-security
description: Assess authorized Linux systems through configuration review, service exposure analysis, identity and privilege-boundary validation, and evidence-driven hardening guidance.
license: MIT
compatibility: opencode,codex
metadata:
  domain: operating-system-security
  platform: linux
  safety: authorized-only
---

# Linux Security

## Purpose

Evaluate Linux hosts, containers, services, and administrative boundaries without assuming that a misconfiguration is exploitable.

## Core workflow

1. Confirm host, distribution, version, role, access method, credentials, and approved actions.
2. Collect read-only system, service, package, mount, network, user, group, sudo, capability, and scheduled-task metadata.
3. Map trust boundaries among users, services, files, sockets, containers, namespaces, and management planes.
4. Form one privilege or exposure hypothesis at a time.
5. Validate with the least invasive proof and capture exact prerequisites.
6. Produce remediation and a safe retest procedure.

## Coverage

- Users, groups, sudoers, PAM, SSH, polkit, Linux capabilities, SUID/SGID, ACLs, and file ownership.
- systemd units, timers, cron, environment files, writable paths, service accounts, and secrets handling.
- Network listeners, firewalls, namespaces, mounts, NFS, shared storage, kernel settings, audit logging, and package hygiene.
- Container-host boundaries and interactions with Docker or Kubernetes Skills.

## Evidence standard

Record commands, sanitized output, effective identity, host, timestamp, expected control, observed state, prerequisite, and demonstrated impact. A writable file or outdated package alone is not proof of privilege escalation.

## Approval boundaries

- Read-only enumeration and configuration review are the default.
- Privilege escalation, credential or key extraction, shell spawning, service modification, namespace escape attempts, kernel exploitation, persistence, pivoting, or lateral movement require explicit approved actions.
- Do not alter accounts, sudoers, SSH keys, services, timers, firewall rules, logs, packages, or production data.

## Deliverables

- Host security baseline.
- Privilege-boundary map.
- Confirmed findings with prerequisites and blast radius.
- Prioritized hardening and retest checklist.
