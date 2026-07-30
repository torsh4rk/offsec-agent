---
name: bug-bounty
description: Conduct policy-compliant bug bounty research with program-scope parsing, safe testing, duplicate-aware evidence, impact validation, and high-quality disclosure reports.
license: MIT
compatibility: opencode,codex
metadata:
  domain: vulnerability-research
  program: bug-bounty
  safety: authorized-only
---

# Bug Bounty

## Purpose

Help researchers operate within a program's published policy, identify meaningful vulnerabilities, minimize impact, and submit reproducible reports.

## Core workflow

1. Save and read the current program policy, scope, exclusions, safe-harbor terms, rate limits, testing windows, and submission rules.
2. Normalize assets and resolve wildcard, third-party, acquisition, mobile, API, and cloud ambiguities before testing.
3. Start passive-first, then prioritize high-value application workflows and authorization boundaries.
4. Use designated researcher accounts and the least invasive proof.
5. Stop after demonstrating impact; do not expand access merely to increase severity.
6. Prepare a concise, duplicate-resistant report with sanitized evidence and remediation context.

## Coverage

- Program policy and scope interpretation.
- Asset triage, endpoint mapping, authentication, authorization, business logic, mobile/API, and LLM application testing.
- Report title, summary, steps, impact, evidence, environment, severity rationale, and retest guidance.
- Duplicate avoidance through root-cause and affected-component analysis, without accessing other researchers' private work.

## Evidence standard

Record the policy version/date, exact scoped asset, test account, request/response, timestamp, expected behavior, observed behavior, minimum impact, and cleanup. Avoid collecting real-user data; use researcher-owned objects whenever possible.

## Approval boundaries

- The published policy and safe harbor are the authorization source.
- Do not test excluded assets or techniques, perform social engineering, spam, denial of service, destructive testing, credential attacks, broad data extraction, persistence, or lateral movement.
- Do not access, modify, or retain more data than minimally necessary to prove the issue.
- Pause and contact the program when scope or impact is ambiguous.

## Deliverables

- Policy and scope digest.
- Prioritized test plan.
- Reproducible submission-ready report.
- Cleanup and retest notes.
