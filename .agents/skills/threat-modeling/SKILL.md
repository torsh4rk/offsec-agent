---
name: threat-modeling
description: Build evidence-based threat models for applications, infrastructure, cloud, mobile, CI/CD, AI agents, LLMs, and MCP systems using assets, trust boundaries, abuse cases, and mitigations.
license: MIT
compatibility: opencode,codex
metadata:
  domain: security-architecture
  safety: defensive
---

# Threat Modeling

## Purpose

Identify plausible security failures before or during testing by mapping assets, actors, data flows, trust boundaries, controls, assumptions, and abuse cases.

## Core workflow

1. Define business objectives, system boundary, lifecycle stage, stakeholders, and risk criteria.
2. Inventory assets, identities, components, data stores, external dependencies, entry points, and administrative planes.
3. Draw data flows and mark every trust, tenant, privilege, network, process, model, tool, and human-approval boundary.
4. Enumerate threats using STRIDE, attack trees, misuse cases, or another agreed method.
5. Prioritize by likelihood, impact, exposure, detectability, and existing controls.
6. Assign mitigations, owners, validation tests, residual risk, and review triggers.

## Coverage

- Web/API, mobile, desktop, Linux/Windows, cloud, Kubernetes, Docker, CI/CD, and supply chain.
- Authentication, authorization, secrets, cryptography, data lifecycle, privacy, logging, availability, and recovery.
- LLM, RAG, agents, memory, prompt injection, tools, MCP, and human-in-the-loop controls.
- Design changes, new integrations, data classes, privilege changes, and deployment topology.

## Evidence standard

Every threat must reference an asset, actor, entry point, trust boundary, plausible precondition, consequence, existing control, uncertainty, and validation method. Avoid generic threat lists disconnected from the actual architecture.

## Approval boundaries

Threat modeling is analytical and defensive. Do not convert abuse cases into active testing without confirming engagement scope and loading the relevant testing Skill.

## Deliverables

- Architecture and data-flow diagram or structured equivalent.
- Asset and trust-boundary inventory.
- Prioritized threat register with owners and mitigations.
- Security requirements and test-plan handoff.
