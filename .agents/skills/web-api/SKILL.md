---
name: web-api
description: Authorized Web and API security assessment using Burp evidence, trust-boundary analysis, and low-impact validation.
license: MIT
compatibility: opencode,codex
---

# Web/API Security

## Use when

Assessing an explicitly authorized Web, REST, GraphQL, SOAP, or WebSocket target.

## Workflow

1. Read `AGENTS.md` and `engagement.json`.
2. Inventory hosts, methods, paths, parameters, content types, authentication, roles, object IDs, tenant IDs, and state changes from existing traffic.
3. Build an authorization matrix across authorized test accounts.
4. Prioritize broken access control, authentication/session flaws, business logic, SSRF, server-side injection, uploads, deserialization, and parsing inconsistencies.
5. Validate with the smallest reversible request change.
6. Preserve sanitized evidence and state limitations.

## Checks

- Unauthenticated, expired, logged-out, and alternate-token behavior.
- Horizontal and vertical authorization using test accounts only.
- Mass assignment and hidden fields.
- Method, path, API-version, and content-type inconsistencies.
- Upload/download ownership and validation.
- Server-side URL fetching and callback allowlists.
- Race, replay, and rate-limit controls within approved limits.

## Approval boundaries

No destructive upload, mass fuzzing, brute force, DoS, real-user data access, shell acquisition, or command execution beyond a harmless marker without explicit written approval.
