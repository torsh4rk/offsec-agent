---
name: cicd-security
description: Assess authorized CI/CD systems for identity, pipeline, runner, artifact, secret, approval, provenance, dependency, and deployment-control weaknesses.
license: MIT
compatibility: opencode,codex
metadata:
  domain: software-supply-chain
  activity: cicd-security
  safety: authorized-only
---

# CI/CD Security

## Purpose

Evaluate how source changes become trusted artifacts and deployments, with emphasis on identities, untrusted contributions, secrets, runners, approvals, and provenance.

## Core workflow

1. Inventory repositories, workflows, branches, environments, runners, registries, artifact stores, deployment targets, identities, and external integrations.
2. Map trigger-to-execution and source-to-deployment trust boundaries.
3. Classify untrusted inputs including pull requests, forks, commit metadata, issue text, artifacts, caches, dependencies, and generated outputs.
4. Review permissions, secret availability, token scope, runner isolation, approval gates, and environment protections.
5. Validate with a designated test repository, branch, runner, artifact, and synthetic secrets.
6. Recommend least privilege, provenance, isolation, deterministic builds, and regression checks.

## Coverage

- GitHub Actions, GitLab CI, Jenkins, Azure Pipelines, Buildkite, CircleCI, and analogous systems.
- Workflow triggers, reusable workflows, actions/plugins, scripts, expressions, command construction, and checkout behavior.
- Hosted and self-hosted runners, ephemeral isolation, network access, caches, artifacts, logs, and workspace cleanup.
- OIDC federation, deploy keys, personal tokens, cloud roles, environments, approvals, branch protection, signing, SBOM, and attestations.

## Evidence standard

Record platform, workflow and revision, trigger, principal, token permissions, secret exposure condition, runner context, artifact or deployment path, expected control, observed result, and scope reference. A broad token is a risk; a finding should show a reachable unauthorized action or material exposure.

## Approval boundaries

- Static workflow review and synthetic test pipelines are the default.
- Do not modify production workflows, expose real secrets, poison shared caches, publish malicious packages, deploy code, access unrelated repositories, or compromise shared runners.
- Repository writes, workflow execution, artifact publication, and deployment actions require explicit approval.

## Deliverables

- Pipeline and identity trust map.
- Secret/token/runner risk matrix.
- Supply-chain and deployment-control findings.
- Hardened workflow guidance and regression tests.
