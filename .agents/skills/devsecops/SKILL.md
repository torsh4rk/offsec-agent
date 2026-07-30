---
name: devsecops
description: Design and review practical DevSecOps controls across planning, coding, build, test, release, deployment, operations, monitoring, and vulnerability remediation.
license: MIT
compatibility: opencode,codex
metadata:
  domain: devsecops
  safety: defensive
---

# DevSecOps

## Purpose

Integrate proportionate security controls into software delivery without reducing security to scanner deployment or blocking development without actionable ownership.

## Core workflow

1. Map the software-delivery lifecycle, repositories, teams, technologies, environments, risk tiers, and release process.
2. Define security requirements and threat-model triggers by application and data criticality.
3. Select controls for source, dependencies, secrets, infrastructure as code, containers, cloud, CI/CD, testing, deployment, and runtime.
4. Assign owners, service-level objectives, exception handling, evidence, and metrics.
5. Pilot controls in advisory mode, tune signal quality, then enforce based on risk.
6. Feed production incidents, pentest findings, and recurring defects back into standards and regression tests.

## Coverage

- Secure design and coding standards, code review, threat modeling, and developer enablement.
- SAST, SCA, secret scanning, IaC, container, API, DAST, fuzzing, SBOM, signatures, and provenance.
- CI/CD identity, runner isolation, deployment approvals, environment protections, and rollback.
- Vulnerability intake, triage, remediation SLAs, exceptions, retesting, dashboards, and risk acceptance.
- Cloud, Kubernetes, Docker, mobile, LLM, agent, and MCP-specific quality gates.

## Evidence standard

For each control, record purpose, owner, covered risk, trigger, enforcement point, failure behavior, false-positive process, evidence artifact, exception path, metric, and review cadence. Tool output alone is not risk reduction.

## Approval boundaries

DevSecOps work is defensive. Do not enable automated exploitation against production, commit secrets, weaken branch protections, bypass approvals, or introduce blocking controls without an agreed rollout and recovery process.

## Deliverables

- Maturity and gap assessment.
- Risk-tiered control matrix.
- Implementation roadmap with owners and milestones.
- Metrics focused on coverage, time to remediation, recurrence, and control effectiveness.
