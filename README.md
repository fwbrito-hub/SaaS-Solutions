![AutoInsure Header](assets/header.png)

# 🚗 AutoInsure AI: SaaS de Seguros com Agentes de IA

Este repositório contém o curso prático para a construção de um **SaaS (Software as a Service)** para corretores de seguros de automóveis e motos, utilizando **Python**, **Agno Framework** e **Streamlit**.

---

## 📚 Jornada de Aprendizado

Acompanhe os módulos do curso através dos Notebooks interativos abaixo. Cada aula pode ser aberta diretamente no **Google Colab** clicando no botão correspondente.

| Módulo | Conteúdo | Notebook |
| :--- | :--- | :--- |
| **01** | **Base do SaaS (Banco de Dados)** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fwbrito-hub/SaaS-Solutions/blob/main/notebooks/01_database.ipynb) |
| **02** | **Cérebro (IA com Agno)** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fwbrito-hub/SaaS-Solutions/blob/main/notebooks/02_agents_ia.ipynb) |
| **03** | **Interface (Streamlit Dashboard)** | ⏳ Em construção... |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**: Linguagem base.
- **SQLAlchemy + SQLite**: Persistência de dados local e robusta.
- **Agno (Phidata)**: Orquestração de agentes de IA inteligentes.
- **Llama 3 (via Groq)**: Motor de inteligência artificial open-source.
- **Streamlit**: Criação de interfaces web rápidas e modernas.

---

## 🚀 Como Iniciar Localmente

Para rodar este projeto na sua máquina:

1. Clone o repositório:
```bash
git clone https://github.com/fwbrito-hub/SaaS-Solutions.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o banco de dados:
```bash
python src/init_db.py
```

4. Rode o Dashboard:
```bash
streamlit run src/app.py
```

---
*Este curso foi desenvolvido para fins didáticos, focado na criação de aplicações reais e escaláveis.*
