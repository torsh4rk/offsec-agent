---
name: windows-security
description: Assess authorized Windows hosts and enterprise services through configuration review, identity-boundary analysis, service exposure validation, and safe remediation planning.
license: MIT
compatibility: opencode,codex
metadata:
  domain: operating-system-security
  platform: windows
  safety: authorized-only
---

# Windows Security

## Purpose

Evaluate Windows workstations and servers while separating host-local weaknesses from Active Directory attack paths.

## Core workflow

1. Confirm host, edition, build, role, domain membership, access method, accounts, and approved actions.
2. Collect read-only operating-system, service, task, registry, policy, software, network, share, and event-log metadata.
3. Map local users, groups, service identities, token boundaries, remote-management surfaces, and trust relationships.
4. Prioritize remotely reachable and privilege-relevant controls.
5. Validate one hypothesis with a reversible, minimal-impact method.
6. Document remediation, rollback considerations, and retest steps.

## Coverage

- Local users and groups, UAC, service permissions, scheduled tasks, registry ACLs, filesystem ACLs, and credential protection.
- PowerShell policy and logging, Windows Defender, firewall, RDP, WinRM, SMB, RPC, WMI, and remote administration.
- LSA protection, Credential Guard, cached credentials, secrets storage, patch posture, application control, and audit policy.
- Handoff to the Active Directory Skill for domain-level identity paths.

## Evidence standard

Record effective identity, host, timestamp, sanitized command/output, expected control, observed state, prerequisites, and demonstrated impact. An unquoted path, service version, or writable location is not a confirmed escalation without a viable execution boundary.

## Approval boundaries

- Read-only collection and configuration review are the default.
- Token theft, credential or hash extraction, service modification, privilege escalation, remote execution, persistence, defense tampering, pivoting, or lateral movement require explicit approved actions.
- Do not disable security products, clear logs, create users, change passwords, modify services, or deploy binaries without written approval.

## Deliverables

- Host exposure and hardening baseline.
- Local privilege and remote-management map.
- Confirmed findings with prerequisites and business impact.
- Retest checklist aligned to the remediation owner.
