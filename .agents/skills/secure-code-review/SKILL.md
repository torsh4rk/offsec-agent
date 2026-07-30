---
name: secure-code-review
description: Review authorized source code for security-relevant data flows, trust boundaries, authorization, injection, cryptography, secret handling, unsafe APIs, and exploitable business logic.
license: MIT
compatibility: opencode,codex
metadata:
  domain: application-security
  activity: secure-code-review
  safety: authorized-only
---

# Secure Code Review

## Purpose

Find root causes in source code and configuration, trace attacker-controlled data to security-sensitive sinks, and produce precise fixes and tests.

## Core workflow

1. Read repository instructions, architecture, build files, entry points, dependencies, generated-code boundaries, and threat model.
2. Identify authentication, authorization, parsing, serialization, storage, cryptography, command execution, filesystem, network, template, and output-rendering sinks.
3. Trace sources, transformations, validation, canonicalization, policy checks, and sinks across modules and services.
4. Review security controls for consistency, centralization, fail-closed behavior, and server-side enforcement.
5. Confirm findings with unit/integration tests or a local fixture when possible.
6. Propose the smallest correct patch, regression test, and broader control improvement.

## Coverage

- Broken access control, tenant isolation, authentication, session, and business logic.
- SQL/NoSQL/LDAP/OS/template/XML injection, SSRF, path traversal, unsafe deserialization, file handling, and output encoding.
- Cryptographic design, key/secret handling, token verification, randomness, and sensitive logging.
- Concurrency, race conditions, error handling, dependency use, insecure defaults, and configuration drift.
- AI/LLM code paths, tool calls, prompt construction, retrieval authorization, and model-output handling.

## Evidence standard

Reference exact file paths, symbols, lines or commits, data-flow path, prerequisite, expected control, reachable impact, and confidence. A dangerous API or stale dependency is not a confirmed vulnerability without reachable, relevant usage and impact.

## Approval boundaries

- Static analysis and local tests are the default.
- Do not insert backdoors, weaken safeguards, introduce stealth, or create weaponized exploitation code.
- Do not send traffic to production or use real secrets during validation.
- Preserve project behavior unless the remediation explicitly changes a security requirement.

## Deliverables

- Prioritized code findings with root cause and data flow.
- Minimal patch recommendations or review-ready diffs.
- Regression tests and affected-call-site search.
- Architectural recommendations for systemic issues.
