---
name: prompt-injection
description: Evaluate authorized LLM applications for direct and indirect prompt injection using synthetic data, harmless actions, traceable test cases, and defense-focused regression testing.
license: MIT
compatibility: opencode,codex
metadata:
  domain: llm-security
  specialty: prompt-injection
  safety: authorized-only
---

# Prompt Injection

## Purpose

Test whether untrusted user, retrieved, document, web, email, tool, or memory content can override policy, cross authorization boundaries, leak protected synthetic data, or trigger unauthorized actions.

## Core workflow

1. Document the instruction hierarchy, trusted data sources, untrusted inputs, tools, identities, memory, output sinks, and application policy.
2. Define allowed behavior, prohibited behavior, synthetic canaries, and harmless mock actions.
3. Build direct, indirect, multi-turn, multilingual, transformed, and encoded test families.
4. Run controlled cases with repeatable model/configuration metadata.
5. Capture complete application traces, retrieval context, tool proposals, approvals, outputs, and control decisions.
6. Convert confirmed failures into regression tests and layered mitigations.

## Coverage

- Direct and indirect prompt injection.
- Instruction/data confusion in RAG, documents, web pages, emails, tool output, and memory.
- Goal hijacking, prompt leakage, context poisoning, cross-user leakage, and unsafe output handling.
- Tool-call influence, argument manipulation, authorization inheritance, and approval bypass.
- Input isolation, provenance, contextual encoding, least privilege, policy enforcement, and output validation.

## Evidence standard

Record application and model version, system configuration when authorized, conversation history, retrieved content, canary identifiers, tool trace, expected behavior, observed behavior, repeatability, and real-world impact. A model following an unusual instruction is not a security finding unless an application trust boundary or policy is violated.

## Approval boundaries

- Use synthetic secrets, test users, mock tools, and reversible actions.
- Do not exfiltrate real credentials, hidden data, private prompts, or unrelated user content.
- Do not use the Skill to bypass safeguards on systems outside the engagement.
- Consequential tool actions require an explicit human approval gate.

## Deliverables

- Threat and trust-boundary map.
- Versioned evaluation dataset and scoring rubric.
- Reproducible failures with traces.
- Defense recommendations and regression suite.
