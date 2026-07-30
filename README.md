# offsec-agent

A modular **AI-assisted security testing** framework for authorized use with OpenCode, Codex, and MCP servers, including Burp Suite MCP.

> Use only on assets for which formal authorization and a defined scope exist. This project does not replace human review, rules of engagement, or technical validation.

## Included Skills

- `web-api`: Web, REST, GraphQL, SOAP, WebSocket, authentication, authorization, and business logic.
- `active-directory`: AD, Kerberos, LDAP, AD CS, trusts, ACLs, and attack paths.
- `mobile`: Android and iOS using a MASVS/MASTG-aligned approach.
- `llm-security`: prompt injection, RAG, agents, tools, memory, and MCP.
- `jailbreak-evals`: controlled jailbreak evaluation, attack, and defense.
- `reporting`: OWASP, CWE, CAPEC, CVSS, evidence, remediation, and retesting.
- `poc-automation`: reproducible PoCs and safe automation in Python or Go.

## Using with OpenCode

```bash
git clone git@github.com:torsh4rk/offsec-agent.git
cd offsec-agent
export OPENAI_API_KEY='your-key'
opencode mcp list
opencode
```

OpenCode discovers `AGENTS.md`, `opencode.json`, and the Skills under `.agents/skills/` when started from the repository root.

## Using with Codex

```bash
cd offsec-agent
codex
```

Use Codex primarily for code review, minimal PoC creation, parsers, automation, and testing. Keep approvals enabled and review every command before execution.

## Burp MCP

The default configuration expects the Burp MCP server at:

```text
http://127.0.0.1:9876/
```

Confirm the listener and integration:

```bash
ss -lntp | grep 9876
opencode mcp list
```

## Operational Security

The default profile requires approval for commands and MCP tools. RCE, shell access, privilege escalation, pivoting, credential extraction, persistence, brute force, denial of service, and destructive actions require explicit and contextual authorization.

## Next Steps

1. Create `engagement.json` with scope, exclusions, test accounts, and limits.
2. Capture initial traffic in Burp.
3. Load the Skill that matches the target.
4. Record sanitized evidence.
5. Generate structured findings and review severity.

## License

MIT.
