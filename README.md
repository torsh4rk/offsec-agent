# offsec-agent

A modular **AI-assisted security testing** framework for authorized use with OpenCode, Codex, and MCP servers, including Burp Suite MCP.

> Use only on assets for which formal authorization and a defined scope exist. This project does not replace human review, rules of engagement, or technical validation.

## Financial AI Red Team — OpenCode jailbreak evaluations and banking/brokerage lab

**New:** [TORSh4rk Financial AI Red Team](financial-ai-redteam/) offers a model-agnostic OpenCode CLI harness for **synthetic, text-only jailbreak / prompt-injection evaluations** and a separate **localhost-only financial API security laboratory**.

- Compare up to five configured OpenCode `provider/model` identifiers with six reproducible, synthetic policy-boundary probes.
- Validate synthetic bank accounts, investment portfolios, trade orders, KYC object ownership, administrative function access, and sensitive caching using eight fixed GET requests.
- Produce concise JSON reports; offline unit tests run without API keys, real brokerage accounts, or production targets.
- [English guide](financial-ai-redteam/README.md) · [Guia em português](financial-ai-redteam/README.pt-BR.md)

**Safety boundary:** this module is a research MVP. It cannot scan external banking domains, move funds, execute shell commands through tested LLMs, or assess real accounts. All findings need human verification and an approved engagement scope.

## Included Skills

### Discovery and assessment orchestration

- `recon-osint`: OSINT, asset discovery, provenance, ownership validation, and passive-first reconnaissance.
- `ai-assisted-pentesting`: controlled orchestration of models, Skills, MCP tools, approvals, evidence, and reporting.
- `bug-bounty`: program-policy parsing, safe testing, impact validation, and disclosure-ready reports.
- `ctf-labs`: structured solving for intentionally vulnerable CTF and lab environments.

### Applications, code, and architecture

- `web-api`: Web, REST, GraphQL, SOAP, WebSocket, authentication, authorization, and business logic.
- `mobile`: Android and iOS using a MASVS/MASTG-aligned approach.
- `secure-code-review`: security-focused data-flow, trust-boundary, authorization, injection, cryptography, and business-logic review.
- `threat-modeling`: assets, actors, data flows, trust boundaries, abuse cases, mitigations, and security requirements.

### Operating systems and enterprise identity

- `active-directory`: AD, Kerberos, LDAP, AD CS, trusts, ACLs, and attack paths.
- `linux-security`: Linux identities, services, privileges, filesystems, networking, and hardening.
- `windows-security`: Windows host, service, policy, privilege, credential-protection, and remote-management review.

### Cloud-native and software supply chain

- `cloud-security`: AWS, Azure, and GCP identity, configuration, network, data, workload, logging, and control-plane security.
- `kubernetes-security`: RBAC, admission, workloads, secrets, networking, nodes, and control-plane security.
- `docker-security`: daemon, image, registry, runtime, Compose, and container-to-host security.
- `cicd-security`: pipelines, runners, identities, secrets, artifacts, provenance, approvals, and deployment controls.
- `devsecops`: risk-tiered security controls throughout planning, coding, build, release, deployment, and operations.

### LLMs, agents, and MCP

- `llm-security`: LLM, RAG, tool, memory, data-leakage, and trust-boundary security.
- `prompt-injection`: direct and indirect prompt-injection evaluation with synthetic data and regression tests.
- `agent-security`: AI-agent identity, planning, delegation, tool authorization, memory, approvals, and containment.
- `jailbreak-evals`: controlled jailbreak attack-and-defense evaluation.
- `mcp-security`: Burp, GitHub, filesystem, database, browser, shell, and custom MCP server security.

### Evidence, PoCs, and reporting

- `poc-automation`: reproducible, dry-run-first PoCs and safe automation in Python or Go.
- `reporting`: OWASP, CWE, CAPEC, CVSS, evidence, remediation, confidence, and retesting.

See [`.agents/skills/README.md`](.agents/skills/README.md) for the full catalog and suggested Skill combinations.

Validate the catalog locally:

```bash
python scripts/validate_skills.py
```

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
3. Load only the Skills relevant to the target and task.
4. Record sanitized evidence.
5. Generate structured findings and review severity.

## License

MIT.
