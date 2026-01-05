import os
from crewai import Agent, Task, Crew, Process
from langchain_ollama import ChatOllama

# Configuração do LLM Local (RTX 4090)
llm = ChatOllama(
    model="qwen2.5:16b",
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
)

# Definição do Especialista ZapPRO
zappro_tech = Agent(
    role='Engenheiro de Diagnóstico ZapPRO',
    goal='Resolver alarmes e problemas técnicos em sistemas VRV e Inverter.',
    backstory='Você é a maior autoridade técnica em HVAC-R, focado em performance e manuais Daikin.',
    llm=llm,
    allow_delegation=False
)

async def run_tech_mission(issue_description: str):
    task = Task(
        description=f"Analise o problema técnico: {issue_description}. Use sua base técnica para fornecer uma solução nível engenharia.",
        expected_output="Diagnóstico técnico detalhado com passos de correção.",
        agent=zappro_tech
    )

    crew = Crew(
        agents=[zappro_tech],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    return await crew.kickoff_async()
