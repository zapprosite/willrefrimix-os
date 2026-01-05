# 🧠 Antigravity Knowledge Base & Governance (2026)
> **Contexto:** Will Refrimix - Automação HVAC-R | **Hardware:** RTX 4090 Twin
> **Paradigma:** Agente Soberano (Executor) vs Copilot (Assistente)

---

## 🛡️ 1. PROTOCOLOS DE GOVERNANÇA E IDENTIDADE (IAM)

### 🤖 Perfil: Agente Jarvis (Core Orchestrator)
- **Escopo:** Orquestração geral, manutenção do OS, gestão de Docker.
- **Permissões de Escrita:** 
  - ✅ `/srv-2/willrefrimix-os/` (Configs, Docs, Scripts)
  - ✅ `/srv-2/willrefrimix-backend/` (Core Logic)
- **Restrições:** 
  - ⛔ Não deletar volumes de dados persistentes sem flag `--force-confirmed`.

### ⚡ Perfil: Agente ZapPRO (Vendas & Triagem)
- **Escopo:** Interação WhatsApp, triagem de leads, consulta de peças.
- **Permissões de Escrita:** 
  - ✅ `/srv-2/willrefrimix-backend/data/memory/` (Logs de conversa)
  - ✅ `/srv-2/willrefrimix-backend/agents/zappro/` (Lógica específica)
- **Restrições Críticas:** 
  - ⛔ **PROIBIDO:** Acesso de escrita na raiz do servidor (`/`).
  - ⛔ **PROIBIDO:** Alterar configurações de rede ou firewall.

---

## 🏗️ 2. CICLO DE VERIFICAÇÃO DE ARTEFATOS (TRUST, BUT VERIFY)

**REGRA DE OURO:** Nenhuma execução complexa é aprovada sem o ciclo de 3 fases.

1.  **Fase 1: Implementation Plan Review**
    *   O Agente deve gerar um arquivo `.md` ou comentário detalhado descrevendo os passos.
    *   *Check:* A lógica faz sentido para HVAC? O modelo físico (peça) está correto?

2.  **Fase 2: Check-point Visual (50%)**
    *   Solicitar screenshot do Browser ou output parcial do Terminal.
    *   *Check:* O seletor CSS do scraper pegou o preço correto? O login no site da Elgin funcionou?

3.  **Fase 3: Validation & Testing**
    *   Execução de testes unitários ou simulação controlada ("Dry Run").
    *   *Check:* O script de automação não está em loop infinito?

---

## 🧠 3. ESTRATÉGIA DE SELEÇÃO DE MODELOS (ROTEAMENTO INTELIGENTE)

| Tarefa / Contexto | Modelo Primário | Fallback | Justificativa |
| :--- | :--- | :--- | :--- |
| **Raciocínio Complexo / Engenharia** | **Gemini 3 Pro** | Claude 4.5 | Capacidade superior de correlacionar manuais técnicos longos (VRV Daikin) e lógica de fluido refrigerante. |
| **Dados Sensíveis (Clientes/Finanças)** | **GPT-OSS (Local - RTX 4090)** | N/A | **Soberania de Dados.** Nenhuma informação PII sai do servidor local. |
| **Coding Simples / Refatoração** | **Gemini Flash 2.0** | Qwen 2.5 Coder | Velocidade e eficiência de custo para tarefas triviais. |
| **Scraping / Visão Computacional** | **Gemini 3 Pro (Vision)** | GPT-4o | Análise de screenshots de catálogos PDF mal formatados. |

---

## 📚 4. NORMAS TÉCNICAS E CONTEXTO HVAC-R (PRIORIDADE ABSOLUTA)

O Agente **DEVE** consultar esta base antes de sugerir manutenção ou peças:

1.  **Daikin VRV/VRF:**
    *   Sempre verificar códigos de erro no manual de serviço atualizado.
    *   Protocolo de comunicação: P1/P2 (Não polarizado).
    *   Sensores Típicos: R1T (Ar), R2T (Líquido), R3T (Gás).

2.  **Elgin & Carrier:**
    *   Priorizar tabelas de pressão x temperatura para diagnósticos de superaquecimento/subresfriamento.
    *   Consultar disponibilidade de peças em fornecedores homologados antes de orçar.

3.  **Boas Práticas de Refrigeração:**
    *   Nunca sugerir "completar gás" sem teste de estanqueidade (nitrogênio).
    *   Vácuo é obrigatório (< 500 microns).

---

## 🛠️ 5. PADRÕES DE PROMPT (ANTIGRAVITY WORKFLOW)

**Template de Objetivo:**
> "Atuando como **[Identidade]**, utilize a ferramenta **[Tool]** para **[Ação]** no contexto **[Contexto HVAC]**. O resultado esperado é **[Output]**."

*Exemplo:*
> "Atuando como **ZapPRO**, utilize o **Browser Agent** para **extrair o preço do Compressor Scroll** no site da Totaline. O resultado esperado é um **JSON com SKU, Preço e Prazo**."
