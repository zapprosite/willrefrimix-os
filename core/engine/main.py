import os
import asyncio
from crewai import Agent, Task, Crew, Process
from langchain_ollama import ChatOllama
from agents.tech_zappro.tools.hvac_tools import HVACTools

# Configuração do Cérebro Local (RTX 4090)
llm = ChatOllama(
    model="qwen2.5:14b",
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
)

# 1. AGENTES
jarvis = Agent(
    role='Jarvis CEO',
    goal='Gerenciar a Will Refrimix e orquestrar técnicos de campo.',
    backstory='Supervisor administrativo e de autoridade técnica HVAC-R.',
    llm=llm,
    verbose=True
)

zappro = Agent(
    role='ZapPRO Tech',
    goal='Resolver falhas em VRV Daikin e buscar manuais.',
    backstory='Engenheiro HVAC-R especialista em VRV. Usa Qdrant e ADB para diagnóstico real.',
    tools=[HVACTools.query_qdrant_manuals, HVACTools.capture_pocophone_data],
    llm=llm,
    verbose=True
)

# 2. ORQUESTRADOR
async def start_antigravity_os(prompt: str):
    mission = Task(
        description=prompt,
        expected_output="Diagnóstico técnico ou relatório de execução comercial.",
        agent=jarvis
    )

    crew = Crew(
        agents=[jarvis, zappro],
        tasks=[mission],
        process=Process.hierarchical,
        manager_llm=llm,
        verbose=True
    )

    return await crew.kickoff_async()

if __name__ == "__main__":
    import sys
    user_query = sys.argv[1] if len(sys.argv) > 1 else "Checar status do sistema"
    asyncio.run(start_antigravity_os(user_query))
