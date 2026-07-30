---
name: poc-automation
description: Create safe, deterministic, reviewable PoCs and authorized pentest automations in Python or Go with scope checks, dry-run, timeouts, and rate limits.
license: MIT
compatibility: opencode,codex
---

# PoC and Automation

## Workflow

1. Define exactly one security claim to prove.
2. Specify target, allowlist, prerequisites, expected signal, request count, and stop condition.
3. Implement dry-run by default.
4. Add explicit target validation, timeout, bounded concurrency, rate limiting, redaction, and structured output.
5. Test against a local fixture before an authorized target.
6. Distinguish `confirmed`, `not reproduced`, and `inconclusive`.
7. Attach sanitized output to the finding.

## Python requirements

Use type hints, `argparse`, clear errors, explicit timeouts, minimal dependencies, and no embedded secrets.

## Go requirements

Use `context`, explicit HTTP transports and timeouts, bounded workers, deterministic output, and no panic for expected failures.

## Approval boundaries

Do not automate shell acquisition, privilege escalation, pivoting, persistence, credential theft, mass exploitation, destructive actions, stealth, or uncontrolled scanning. Never package weaponized payloads.
