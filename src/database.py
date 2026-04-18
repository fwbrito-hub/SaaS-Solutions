from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Mudamos de .models para models

# Define onde o banco será salvo (na mesma pasta do projeto)
SQLALCHEMY_DATABASE_URL = "sqlite:///./insurance.db"

# O 'engine' é o motor que traduz Python para SQL
# O argumento 'check_same_thread' é necessário apenas para o SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# A 'SessionLocal' é a fábrica de conexões. Cada vez que precisarmos
# mexer no banco, pediremos uma sessão para ela.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
