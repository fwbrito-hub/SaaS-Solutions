import streamlit as st
from agent import get_insurance_agent
from database import SessionLocal
from models import Broker, Client, Policy
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="AutoInsure AI | Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Premium (Custom CSS)
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stSecondary {
        background-color: #1a1c24;
    }
    div.stButton > button:first-child {
        background-color: #00f2fe;
        color: #000;
        border: none;
        border-radius: 8px;
        font-weight: bold;
    }
    .chat-container {
        border: 1px solid #2d2d2d;
        border-radius: 12px;
        padding: 20px;
        background-color: #161b22;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização de Estado da Sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- BARRA LATERAL (Métricas e Info) ---
with st.sidebar:
    st.image("assets/header.png")
    st.title("🛡️ AutoInsure AI")
    st.markdown("---")
    
    st.subheader("Métricas do Corretor")
    session = SessionLocal()
    try:
        total_clients = session.query(Client).count()
        total_policies = session.query(Policy).count()
        broker = session.query(Broker).first()
        
        st.metric("Usuário Ativo", broker.name if broker else "Nenhum")
        st.metric("Total de Clientes", total_clients)
        st.metric("Apólices Ativas", total_policies)
    finally:
        session.close()
    
    st.markdown("---")
    if st.button("Limpar Histórico de Chat"):
        st.session_state.messages = []
        st.rerun()

# --- ÁREA PRINCIPAL (Dashboard & Chat) ---
st.title("Dashboard Inteligente")
st.write("Bem-vindo ao centro de comando da sua corretora.")

# Layout em Colunas para Dados
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🤖 Falar com Assistente IA")
    
    # Exibir histórico de chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input do Chat
    if prompt := st.chat_input("Pergunte algo (ex: 'Quem é o melhor cliente?')"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Resposta do Agente Agno
        with st.chat_message("assistant"):
            agent = get_insurance_agent()
            response_container = st.empty()
            
            # Streaming da resposta
            full_response = ""
            for chunk in agent.run(prompt, stream=True):
                if hasattr(chunk, 'content') and chunk.content:
                    full_response += chunk.content
                    response_container.markdown(full_response + "▌")
            
            response_container.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

with col2:
    st.subheader("📊 Visão Geral dos Dados")
    # Aqui poderíamos colocar gráficos do Plotly futuramente
    st.info("💡 Dica: Peça para a IA listar seus clientes para ver os dados aparecerem no chat.")
    
    tab1, tab2 = st.tabs(["Instruções", "Segurança"])
    with tab1:
        st.markdown("""
        1. Pergunte sobre seus clientes.
        2. Peça relatórios de apólices vencendo.
        3. A IA consulta o banco em tempo real.
        """)
    with tab2:
        st.warning("Este sistema usa SQLite local. Seus dados estão protegidos na sua máquina.")
