# 🏛️ MASTER TASKMASTER: ANTIGRAVITY OS v2.1 (SOBERANIA TOTAL)
**Visão:** Full Stack Automation para Engenharia HVAC-R & Marketing de Autoridade.
**Data de Início:** 2026-01-04 | **Hardware:** RTX 4090 (24GB VRAM)

---

## 🏗️ PILAR 1: INFRAESTRUTURA & GOVERNANÇA (SRE MODE)
- [x] **Setup de Raiz:** Estrutura monorepo e ambiente virtual `.venv`.
- [x] **Documentação de Soberania:** README.md, PRD.md e AGENTS.md consolidados.
- [ ] **Orquestração Kestra:** Subir container Kestra (Porta 8081) para gerenciar fluxos pesados.
- [ ] **Gateway n8n:** Configurar n8n em modo "Webhook Only" para recebimento de leads/mensagens.
- [ ] **Network Mesh:** Validar túneis Cloudflare para `v2.zappro.site` e `api.zappro.site`.

---

## 🧠 PILAR 2: DATA LAKE & MEMÓRIA TÉCNICA (RAG)
- [ ] **Qdrant Schema:** Criar coleções `manuais_daikin`, `manuais_elgin` e `historico_manutencao`.
- [ ] **ADB Sniper Pipeline:** Implementar script `pocophone_sniper.py` para extração de dados do Facilita Técnico via Kestra.
- [ ] **Hugging Face Embeddings:** Configurar `sentence-transformers` locais para indexação semântica sem latência de nuvem.

---

## 🤖 PILAR 3: ENGINE DE AGENTES (CREWAI + LANGGRAPH)
- [ ] **Jarvis CEO (Supervisor):** - Implementar roteador de intenções (Comercial vs. Técnico).
    - Gestão de orçamentos e CRM via n8n.
- [ ] **ZapPRO Tech (Expert):**
    - Lógica de diagnóstico de erro (Protocolo de Teste Placa Inversora).
    - Integração com Qdrant para consulta de manuais em tempo real.
- [ ] **ZapPRO Vision (VLM):**
    - Pipeline de visão via Qwen2-VL para análise de fotos de campo e diagramas.
- [ ] **LangGraph State Machine:** Definir o fluxo de "loop de correção" onde o Jarvis valida o diagnóstico do ZapPRO.

---

## 📱 PILAR 4: INTEGRAÇÃO DE CAMPO & MOBILE
- [ ] **Evolution API Bridge:** Sincronizar instâncias do WhatsApp Business com o Antigravity OS.
- [ ] **Async Response Loop:** n8n -> Kestra (Processamento IA) -> Resposta WhatsApp.
- [ ] **Pocophone Sync:** Automação de ADB Wireless para coleta de evidências fotográficas de obras.

---

## 📈 PILAR 5: SEO TÉCNICO & CONTENT FACTORY
- [ ] **Metadata Generator:** Automação de extração de palavras-chave HVAC-R dos atendimentos diários.
- [ ] **Script Factory:** Gerar roteiros de YouTube/Reels com base nas resoluções de problemas técnicos reais.
- [ ] **CTR Optimizer:** Sugestão de títulos e tags via LLM focado em público de alto padrão.

---

## 🛡️ PILAR 6: MONITORAMENTO & OPS SENTINEL
- [ ] **GPU Watchdog:** Monitorar uso de VRAM da RTX 4090 durante inferência paralela.
- [ ] **Logs de Auditoria:** Centralizar logs de execução dos agentes em `/memory/logs/`.
- [ ] **Health Check API:** Endpoint `/health` para monitorar status dos containers via Coolify.

## 🛰️ FASE HUGGING FACE 2026 (OTIMIZAÇÃO DE MODELOS)
- [ ] Implementar Reranker (BGE-Reranker-v2) para melhorar a precisão do ZapPRO no Qdrant.
- [ ] Configurar 'Speculative Decoding' para aumentar a velocidade de resposta do Jarvis.
- [ ] Validar a integração do Qwen2-VL no workflow de recebimento de fotos do n8n.

## ✅ RELATÓRIO DE PURGA (2026-01-04)
- [x] Remoção física do repositório /srv-2/willrefrimix-backend/.
- [x] Purga de volumes e imagens do legado (VRAM & Disk liberados).
- [ ] PENDÊNCIA: Estabilizar o túnel Cloudflare v2 (v2.zappro.site).

## 🧹 RELATÓRIO DE SOBERANIA DE VRAM (2026-01-04)
- [x] Expurgo de containers `willrefrimix-*` e `jarvis-pessoal-*`.
- [x] Purga de volumes órfãos e imagens legadas.
- [x] Reset de VRAM do Ollama (Pronto para Qwen 2.5 14B).
- [ ] STATUS: RTX 4090 com VRAM livre para o Clã de Agentes.

## 🛠️ DEBUG DE INFRA (2026-01-04)
- [x] Correção do ModuleNotFoundError via PYTHONPATH=/app no Docker.
- [x] Recriação dos containers Core (API & Qdrant).
- [ ] PENDÊNCIA: Primeiro teste de "End-to-End" (Input -> Jarvis -> ZapPRO).
