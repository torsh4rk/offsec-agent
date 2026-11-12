# TORSh4rk Financial AI Red Team

**Avaliação de resistência a jailbreak/prompt injection em modelos do OpenCode e testes de segurança de APIs financeiras em laboratório sintético.**

**Idiomas:** [English (documentação completa)](README.md) · [Português (Brasil)](README.pt-BR.md)

> **MVP de pesquisa, não pronto para produção.** Desenvolvido como extensão do repositório [torsh4rk/offsec-agent](https://github.com/torsh4rk/offsec-agent), sem alterar suas 23 Skills, sua política `AGENTS.md` nem a configuração existente. Não testa bancos ou corretoras reais e não movimenta fundos.

## Módulos

| Recurso | O que faz | Restrição |
| --- | --- | --- |
| **AI Red Team** | Executa de 1 a 6 cenários sintéticos de jailbreak por modelo, como falsificação de papéis, instruções maliciosas em documentos, tentativa de revelar um canário fictício, histórico de conversa falso e texto codificado | Até 5 modelos configurados no OpenCode; sem ferramentas do agente; respostas exigem revisão humana |
| **Financial Lab** | Verifica IDOR/BOLA de contas, carteiras de investimento, ordens, dados KYC, BFLA de funções administrativas e `Cache-Control` em respostas sensíveis | Oito requisições GET fixas, somente em `127.0.0.1` e somente no serviço simulado incluído |

Nenhum módulo executa exploits em produção, força bruta, extração de credenciais ou transferência financeira.

## Pré-requisitos

- **Python 3.11 ou superior** para ambos os módulos; somente biblioteca padrão.
- **Git** para clonar o repositório.
- **OpenCode CLI** com os provedores/modelos configurados para avaliação de LLMs. Os testes do laboratório bancário não precisam do OpenCode nem de chaves de API.

## 1. Instalação e testes locais

```bash
git clone https://github.com/torsh4rk/offsec-agent.git
cd offsec-agent/financial-ai-redteam
python3 -m unittest discover -s tests -v
```

O primeiro comando baixa o repositório público; o segundo entra na pasta do novo agente; o terceiro executa os testes automatizados offline. Espera-se **9 testes com resultado OK**. Os testes não se conectam a provedores de modelos nem a bancos.

## 2. Testar resistência a jailbreak em um modelo do OpenCode

```bash
python3 -m financial_redteam eval \
  --model provider/model-id \
  --cases 2 \
  --output eval-report.json
```

Substitua `provider/model-id` pelo identificador **real** de um modelo acessível em sua instalação OpenCode. Para comparar modelos, repita `--model` até cinco vezes. O argumento `--cases` define quantos dos seis cenários executar por modelo. Consulte `opencode run --help` e o seletor `/models` para confirmar a compatibilidade.

Cada avaliação cria uma pasta temporária com `opencode.json`, regras que **negam todas as ferramentas**, um agente `finance-eval` e um canário inteiramente fictício. O objetivo esperado é responder `POLICY_OK`; o relatório diferencia `passed`, `potential_boundary_failure`, `manual_review` e `execution_error`. Um indício de falha **não comprova** um jailbreak sem análise adicional.

**Importante:** os modelos podem cobrar pelas chamadas. Os testes unitários feitos no desenvolvimento simulam as respostas; nenhum provedor real foi executado. As permissões do OpenCode não substituem isolamento de sistema operacional; utilize container/VM para modelos ou plugins não confiáveis.

## 3. Iniciar laboratório de banco/corretora

No **terminal 1**, na pasta `financial-ai-redteam`:

```bash
python3 -m financial_redteam.lab --port 8765
```

No **terminal 2**, na mesma pasta:

```bash
python3 -m financial_redteam scan-lab \
  --scope engagement.example.json \
  --target http://127.0.0.1:8765 \
  --output finance-report.json
```

No laboratório protegido, o resultado esperado é **zero achados** após oito verificações de leitura. Para demonstrar uma falha **apenas nos dados fictícios locais**, reinicie o terminal 1 assim:

```bash
python3 -m financial_redteam.lab --port 8765 --simulate-bola
```

Repita o `scan-lab`: o scanner deverá identificar controles ausentes de propriedade de objetos simulados. Também há opções `--simulate-bfla` (funções administrativas) e `--simulate-cache` (respostas sensíveis sem `no-store`). Isso não toca bancos, clientes, carteiras ou operações reais.

## Escopo e regras de autorização

O arquivo `engagement.example.json` demonstra um engajamento restrito ao laboratório sintético, com identificador, validade, host permitido e limite de requisições. **Ele não é uma autorização de pentest bancário.** O código recusa alvos externos, redirecionamentos automáticos, operações não GET e caminhos que não pertençam aos testes fixos.

Para um futuro pentest real em instituições financeiras, seria necessária autorização escrita, delimitação de aplicações/tenants/contas, janela, limites de taxa e transação, regras de tratamento de dados, contatos de emergência e condições de parada. Não basta modificar o JSON de exemplo e apontar para um banco.

## Segurança e interpretação dos resultados

- O cabeçalho `X-Demo-Actor` representa **identidades fictícias do laboratório** e não autenticação segura de produção.
- As verificações financeiras cobrem BOLA/IDOR (CWE-639), BFLA (CWE-862) e cache de dados sensíveis (CWE-525). O relatório apresenta indícios, não comprovação de impacto.
- Não inclua segredos, contas de clientes, dados reais de negociação ou informações internas nos prompts ou relatórios.
- Os prompts de avaliação não possuem ferramentas de shell/MCP/rede habilitadas. Portanto, os cenários avaliam sobretudo a hierarquia de instruções, **não a exploração real de ferramentas**.
- Revise manualmente as diferenças entre comportamento esperado e observado. A implementação não possui garantia de isolamento contra um modelo/ambiente comprometido.

**Documentação técnica completa, arquitetura, matriz de testes e roadmap:** [README.md](README.md). Referências: [OpenCode CLI](https://opencode.ai/docs/cli/commands), [Modelos](https://opencode.ai/docs/models), [Permissões](https://opencode.ai/docs/permissions), [OWASP API Security](https://owasp.org/API-Security/) e [OpenID FAPI](https://openid.net/wg/fapi/).

**Princípio:** *Nunca confunda um resultado de IA com exploração verificada; autorização, evidência e revisão humana são obrigatórias.*
