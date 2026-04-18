from database import engine
from models import Base

def init_db():
    print("Iniciando a criação das tabelas...")
    # Este comando cria fisicamente o arquivo .db e as tabelas
    Base.metadata.create_all(bind=engine)
    print("Sucesso! O arquivo 'insurance.db' foi criado e as tabelas estão prontas.")

if __name__ == "__main__":
    init_db()
