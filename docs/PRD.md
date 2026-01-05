# 📑 PRD: ANTIGRAVITY OS v2.1
**Status:** Baseline | **Data:** 2026-01-04

## 1. Visão Geral
Sistema operacional agêntico para a @willrefrimix, focado em automação técnica de HVAC-R (VRV Daikin), marketing técnico e BI.

## 2. Stack Tecnológica
- **Backend:** FastAPI (Python 3.12 Async) - Porta 8001.
- **Orquestração:** Kestra (Workflows Pesados) + n8n (Webhooks).
- **IA:** crewAI (Agentes) + LangGraph (Estados) + Hugging Face/Ollama.
- **VRAM:** Otimizada para RTX 4090 (24GB).
- **Memória:** Qdrant Vector DB (RAG Técnico).

## 3. Requisitos Core
- **R1:** Diagnóstico técnico via ADB (Pocophone) capturando dados do "Facilita Técnico".
- **R2:** Análise de visão (VLM) para identificar danos em placas eletrônicas.
- **R3:** Automação de SEO: Transformar logs de obra em scripts de YouTube/Reels.
- **R4:** Soberania: 100% dos dados técnicos devem residir no Qdrant local.

## 4. KPIs de Sucesso
- Resposta técnica em < 30s no WhatsApp.
- Zero alucinação em códigos de erro VRV Daikin.
- Sincronização automática entre o campo (Pocophone) e o Data Lake.
