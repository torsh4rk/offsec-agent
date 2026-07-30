# Skill Catalog

All Skills are stored under `.agents/skills/<skill-name>/SKILL.md` and use YAML frontmatter compatible with OpenCode/Codex-style Agent Skills.

## Complete catalog

| Requested capability | Skill directory | Status |
|---|---|---|
| Recon / OSINT and asset discovery | `recon-osint` | Included |
| Web / API | `web-api` | Included |
| Active Directory | `active-directory` | Included |
| Linux | `linux-security` | Included |
| Windows | `windows-security` | Included |
| Cloud — AWS, Azure, GCP | `cloud-security` | Included |
| Kubernetes | `kubernetes-security` | Included |
| Docker | `docker-security` | Included |
| Mobile — Android/iOS | `mobile` | Included |
| LLM Security | `llm-security` | Included |
| Prompt Injection | `prompt-injection` | Included |
| Agent Security | `agent-security` | Included |
| Jailbreak attack/defense evaluations | `jailbreak-evals` | Included |
| Reporting — OWASP, CWE, CAPEC, CVSS | `reporting` | Included |
| Python/Go PoCs and automation | `poc-automation` | Included |
| MCP — Burp, GitHub, filesystem, custom | `mcp-security` | Included |
| Bug Bounty | `bug-bounty` | Included |
| CTF / Labs | `ctf-labs` | Included |
| Threat Modeling | `threat-modeling` | Included |
| Secure Code Review | `secure-code-review` | Included |
| CI/CD Security | `cicd-security` | Included |
| DevSecOps | `devsecops` | Included |
| AI-assisted Pentesting | `ai-assisted-pentesting` | Included |

## Loading guidance

Load only the Skills relevant to the current task. A typical Web/API assessment may use:

- `recon-osint`
- `web-api`
- `mcp-security` when Burp MCP is enabled
- `poc-automation`
- `reporting`
- `ai-assisted-pentesting`

A cloud-native assessment may add `cloud-security`, `kubernetes-security`, `docker-security`, `cicd-security`, and `devsecops`.

An AI application assessment may use `llm-security`, `prompt-injection`, `agent-security`, `mcp-security`, `jailbreak-evals`, `threat-modeling`, and `reporting`.

## Safety model

The repository-level `AGENTS.md` controls all Skills. Engagement scope, authorization profile, exclusions, rate limits, evidence handling, and approval gates always take priority over Skill guidance.

Run the catalog validator after changes:

```bash
python scripts/validate_skills.py
```
