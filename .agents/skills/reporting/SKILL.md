---
name: reporting
description: Produce reproducible security findings and reports with evidence-backed OWASP, CWE, CAPEC, CVSS, remediation, and retest guidance.
license: MIT
compatibility: opencode,codex
---

# Security Reporting

## Workflow

1. Load engagement scope and structured findings.
2. Reject unsupported conclusions, missing evidence, and scope ambiguity.
3. Normalize title, root cause, affected asset, prerequisites, actual versus expected behavior, and demonstrated impact.
4. Assign CWE/OWASP/CAPEC only when supported by evidence.
5. Calculate CVSS and explain every metric assumption.
6. Separate technical impact from business impact.
7. Provide specific remediation and a deterministic retest.
8. Redact credentials, tokens, personal data, and undisclosed targets before distribution.

## Required finding fields

- ID, title, status, severity, and confidence.
- Asset, component, endpoint, role, and prerequisites.
- Sanitized evidence and minimal reproduction steps.
- Technical and business impact.
- CWE, OWASP, optional CAPEC, and justified CVSS vector.
- Remediation, retest procedure, limitations, and references.

## Quality rules

Scanner output alone is not a finding. Do not inflate severity. Use root-cause CWE mappings. State uncertainty. Never publish private evidence or secrets.
