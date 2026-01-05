# 🚀 ANTIGRAVITY OS v2.1

Repositório central de inteligência da Will Refrimix.

## 📂 Estrutura
- `/agents/`: Lógica, ferramentas e prompts dos agentes (Jarvis, ZapPRO).
- `/api/`: Endpoints FastAPI para integração externa.
- `/core/`: Engine de supervisão (LangGraph) e orquestração.
- `/docs/`: PRD, Taskmaster e Planos de Obra.
- `/infrastructure/`: Docker, Kestra flows e Cloudflared.
- `/memory/`: Qdrant schemas e armazenamento de imagens/PDFs.

## 🛠️ Setup Rápido
1. Ative o venv: `source .venv/bin/activate`
2. Instale dependências: `pip install -r requirements.txt`
3. Configure o .env: `cp .env.example .env`
4. Execute o Supervisor: `python core/engine/main.py "missão"`

## 🌐 Governança de Rede
- **API v2:** Porta 8001
- **Kestra:** Porta 8081
- **Qdrant:** Porta 6333
