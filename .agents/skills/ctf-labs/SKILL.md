---
name: ctf-labs
description: Solve CTFs and intentionally vulnerable labs through structured enumeration, hypothesis testing, reproducible notes, and environment-contained exploitation.
license: MIT
compatibility: opencode,codex
metadata:
  domain: security-training
  environment: ctf-lab-only
  safety: contained-only
---

# CTF and Labs

## Purpose

Support learning and competition tasks on systems explicitly designed for testing, while keeping lab techniques and credentials contained to that environment.

## Core workflow

1. Confirm the challenge platform, target, rules, allowed tools, flag format, time window, and prohibited collaboration or automation.
2. Inventory files, services, source, binaries, protocols, identities, and challenge hints.
3. Maintain an evidence notebook of observations, hypotheses, experiments, outcomes, and dead ends.
4. Prefer understanding the intended weakness before increasing automation.
5. Build minimal reproducible solvers or PoCs when permitted.
6. Produce a post-solve explanation that separates challenge-specific assumptions from transferable lessons.

## Coverage

- Web, API, crypto, reverse engineering, binary exploitation, forensics, cloud, mobile, Active Directory, containers, Kubernetes, and LLM labs.
- Local fixtures, isolated virtual machines, challenge networks, source review, debugging, and solver development.
- Team notes, flag handling, cleanup, and reproducibility.

## Evidence standard

Record target/challenge identifier, rules, tool versions, inputs, outputs, assumptions, exploit chain, flag location category, and solver behavior. Do not commit active flags or event secrets unless the rules permit it.

## Approval boundaries

- Use only CTF or lab assets explicitly provided for the exercise.
- Do not reuse discovered credentials, payloads, endpoints, or infrastructure outside the lab.
- Respect event rules on scanning, brute force, automation, collaboration, and writeups.
- Avoid attacks on shared platform infrastructure or other participants.

## Deliverables

- Structured solve notes.
- Minimal solver or PoC when appropriate.
- Root-cause explanation and defensive lesson.
- Cleanup and environment-reset steps.
