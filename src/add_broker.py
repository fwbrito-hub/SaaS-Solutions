from database import SessionLocal
from models import Broker

def add_test_data():
    session = SessionLocal()
    try:
        # Verifica se ja existe um corretor
        if session.query(Broker).count() == 0:
            new_broker = Broker(
                name="Francisco Brito",
                email="contato@fwbrito.com.br"
            )
            session.add(new_broker)
            session.commit()
            print("Corretor de teste cadastrado com sucesso!")
        else:
            print("O corretor ja estava cadastrado.")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    add_test_data()
