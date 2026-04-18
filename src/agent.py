import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.sql import SQLTools

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

def get_insurance_agent():
    """
    Cria e configura o Agente de Seguros que pode consultar o SQLite.
    """
    
    # Configuração das ferramentas SQL para o nosso banco de dados
    sql_tools = SQLTools(
        db_url="sqlite:///insurance.db"
    )

    # 2. Inicializa o Agente
    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[sql_tools],
        markdown=True,
        instructions=[
            "Você é um Agente de Seguros Automotivos amigável e profissional.",
            "Sua principal função é ajudar o corretor a entender seus dados de clientes e apólices.",
            "Utilize as tabelas 'brokers', 'clients' e 'policies' do banco de dados.",
            "A tabela 'brokers' contém as informações dos corretores.",
            "Sempre que fizer uma consulta, explique o que encontrou de forma resumida.",
            "Se não encontrar um dado, sugira ao corretor verificar se o nome do cliente está correto.",
            "Nunca invente dados que não existem no banco!"
        ]
    )
    
    return agent

if __name__ == "__main__":
    # Teste rápido do agente via terminal
    agent = get_insurance_agent()
    agent.print_response("Olá! Quem é o corretor cadastrado no sistema?", stream=True)
