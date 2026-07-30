---
name: agent-security
description: Assess authorized AI agents for identity, planning, tool authorization, memory, delegation, approvals, output handling, monitoring, and excessive-agency risks.
license: MIT
compatibility: opencode,codex
metadata:
  domain: ai-agent-security
  safety: authorized-only
---

# Agent Security

## Purpose

Evaluate autonomous and semi-autonomous systems where models plan, call tools, delegate tasks, maintain state, and take actions across trust boundaries.

## Core workflow

1. Inventory agents, models, identities, tools, MCP servers, data stores, memories, queues, delegates, approval gates, and output sinks.
2. Map who authorizes each action and where identity, scope, arguments, and policy are enforced.
3. Model untrusted inputs entering plans, memory, retrieval, tools, and inter-agent messages.
4. Test with synthetic principals, mock tools, canary data, and reversible actions.
5. Evaluate failure containment, retries, timeouts, budgets, auditability, and human intervention.
6. Turn failures into policy, architecture, and regression-test changes.

## Coverage

- Excessive agency, confused deputy, privilege propagation, and cross-agent trust.
- Tool selection, argument validation, capability scoping, approval binding, and transaction integrity.
- Memory poisoning, cross-user state leakage, stale context, and unsafe long-term retention.
- Delegation loops, recursive tasks, unbounded execution, error recovery, and side-effect duplication.
- Output-to-action injection, unsafe code execution, filesystem access, browser automation, and message sending.

## Evidence standard

Record agent and model versions, initiating principal, plan/trace, selected tool, proposed and executed arguments, approval decision, side effect, expected policy, observed behavior, repeatability, and containment. Model intent is not evidence; the application-enforced action is the security boundary.

## Approval boundaries

- Default to mock or sandboxed tools and synthetic data.
- No real payments, messages, account changes, code deployment, secret access, destructive actions, or external side effects without explicit approval.
- Do not rely on prompt text as the sole authorization control.

## Deliverables

- Agent capability and trust graph.
- Tool/identity/approval matrix.
- Failure-mode evaluation suite.
- Least-privilege, containment, observability, and human-control recommendations.
