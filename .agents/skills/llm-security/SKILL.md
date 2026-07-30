---
name: llm-security
description: Authorized evaluation of LLM, RAG, agent, tool-calling, memory, and MCP trust boundaries using synthetic data and harmless actions.
license: MIT
compatibility: opencode,codex
---

# LLM Security

## Workflow

1. Document models, prompts, identities, tools, MCP servers, data sources, retrieval, memory, and output consumers.
2. Classify trusted instructions, untrusted content, secrets, and authorization boundaries.
3. Use synthetic canaries and harmless tools.
4. Evaluate direct and indirect prompt injection, retrieval authorization, excessive agency, unsafe output handling, data leakage, memory isolation, and tool argument validation.
5. Capture full test case, model/configuration, conversation, tool trace, expected behavior, and observed behavior.
6. Convert confirmed failures into regression tests and layered mitigations.

## Checks

- Retrieved or uploaded content cannot redefine policy.
- Tool calls enforce server-side identity, scope, and argument validation.
- Model output is not executed or rendered unsafely.
- Memory and conversation data remain tenant-isolated.
- MCP server identity, permissions, schemas, and tool descriptions are trusted.
- Human approval protects consequential actions.
- Monitoring detects abnormal tool use and repeated injection attempts.

## Approval boundaries

Do not exfiltrate real secrets, act against external users or services, test model-provider infrastructure outside scope, or perform consequential tool actions. Use synthetic data and reversible test fixtures.
