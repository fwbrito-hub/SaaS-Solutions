from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, declarative_base

# A Base é a classe de onde todas as nossas tabelas vão herdar
Base = declarative_base()

class Broker(Base):
    """
    Representa o Corretor (Inquilino/Tenant).
    Cada corretor terá seus próprios clientes e apólices.
    """
    __tablename__ = 'brokers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    # Relação: Um corretor tem muitos clientes
    clients = relationship("Client", back_populates="broker")

class Client(Base):
    """
    Representa o Segurado (o cliente do corretor).
    """
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True)
    broker_id = Column(Integer, ForeignKey('brokers.id'))
    
    # Relação: Um cliente pertence a um corretor
    broker = relationship("Broker", back_populates="clients")
    # Relação: Um cliente pode ter várias apólices (ex: carro e moto)
    policies = relationship("Policy", back_populates="client")

class Policy(Base):
    """
    Representa a Apólice de Seguro.
    """
    __tablename__ = 'policies'
    
    id = Column(Integer, primary_key=True)
    policy_number = Column(String, unique=True)
    vehicle_plate = Column(String)
    vehicle_model = Column(String)
    expiration_date = Column(Date) # Data de vencimento - Crucial para renovações!
    premium_amount = Column(Float) # Valor pago pelo seguro
    
    client_id = Column(Integer, ForeignKey('clients.id'))
    
    # Relação: Uma apólice pertence a um cliente
    client = relationship("Client", back_populates="policies")
