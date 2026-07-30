---
name: active-directory
description: Authorized Active Directory assessment covering identity topology, Kerberos, LDAP, AD CS, trusts, ACLs, and controlled attack-path validation.
license: MIT
compatibility: opencode,codex
---

# Active Directory

## Workflow

1. Confirm authorized domains, forests, CIDRs, credentials, hosts, and collection methods.
2. Begin with read-only directory and host metadata.
3. Map users, groups, computers, trusts, delegation, service accounts, ACLs, GPO, and certificate services.
4. Model potential paths without assuming exploitability.
5. Validate one edge at a time using the least invasive action.
6. Record prerequisites, blast radius, evidence, remediation, and retest steps.

## Checks

- Excessive ACLs, nested privileged groups, and stale memberships.
- Kerberos delegation and service principal exposure.
- AD CS templates, enrollment rights, and certificate trust.
- LDAP signing/channel binding, SMB signing, NTLM restrictions, and legacy protocols.
- Trust direction, SID filtering, and cross-domain privilege paths.
- GPO edit/link rights and local-administrator exposure.

## Approval boundaries

Secrets dumping, credential/hash extraction, ticket forging, password changes, privilege escalation, lateral movement, pivoting, service creation, scheduled tasks, persistence, and destructive changes require explicit written approval for the exact target and action.
