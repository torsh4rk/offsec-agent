# offsec-agent

Framework modular de **AI-assisted security testing** para uso autorizado com OpenCode, Codex e servidores MCP, incluindo Burp Suite MCP.

> Use somente em ativos para os quais exista autorização formal e escopo definido. O projeto não substitui revisão humana, regras de engajamento ou validação técnica.

## Skills incluídas

- `web-api`: Web, REST, GraphQL, SOAP, WebSocket, autenticação, autorização e lógica de negócio.
- `active-directory`: AD, Kerberos, LDAP, AD CS, trusts, ACLs e caminhos de ataque.
- `mobile`: Android e iOS com abordagem MASVS/MASTG.
- `llm-security`: prompt injection, RAG, agentes, ferramentas, memória e MCP.
- `jailbreak-evals`: avaliação controlada de jailbreaks, ataque e defesa.
- `reporting`: OWASP, CWE, CAPEC, CVSS, evidências, remediação e reteste.
- `poc-automation`: PoCs reproduzíveis e automações seguras em Python ou Go.

## Uso com OpenCode

```bash
git clone git@github.com:torsh4rk/offsec-agent.git
cd offsec-agent
export OPENAI_API_KEY='sua-chave'
opencode mcp list
opencode
```

O OpenCode encontra o `AGENTS.md`, o `opencode.json` e as Skills em `.agents/skills/` ao ser iniciado na raiz do repositório.

## Uso com Codex

```bash
cd offsec-agent
codex
```

Use o Codex principalmente para revisão de código, criação de PoCs mínimos, parsers, automações e testes. Mantenha aprovações habilitadas e revise cada comando antes da execução.

## Burp MCP

A configuração padrão espera o MCP do Burp em:

```text
http://127.0.0.1:9876/
```

Confirme o listener e a integração:

```bash
ss -lntp | grep 9876
opencode mcp list
```

## Segurança operacional

O perfil padrão exige aprovação para comandos e ferramentas MCP. RCE, shell, escalada de privilégios, pivoting, extração de credenciais, persistência, força bruta, negação de serviço e ações destrutivas exigem autorização explícita e contextual.

## Próximos passos

1. Criar `engagement.json` com escopo, exclusões, contas de teste e limites.
2. Capturar tráfego inicial no Burp.
3. Carregar a Skill correspondente ao alvo.
4. Registrar evidências sanitizadas.
5. Gerar findings estruturados e revisar severidade.

## Licença

MIT.
