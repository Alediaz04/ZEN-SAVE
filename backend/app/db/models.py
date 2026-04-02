from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .database import Base

class TransactionType(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    names = Column(String, nullable=False) #Ingresa su nombre
    last_name = Column(String, nullable=False) #ingresa su apellido
    dni = Column(String, unique=True, index=True, nullable=False) #ingresa su DNI
    email = Column(String, unique=True, index=True, nullable=False) #ingresa el gmail
    username = Column(String, unique=True, index=True, nullable=False) #Ingresar nombre de usuario
    hashed_password = Column(String, nullable=False) #Ingresar contraseña
    dob = Column(DateTime, nullable=False)  #Ingresar fecha de nacimiento

#preferencias de aplicacion general
    is_dark_mode = Column(Boolean, default=True) #modo oscuro
    created_at = Column(DateTime, default=datetime.utcnow) #fecha de creacion de la cuenta

    #Relaciones
    sent_transactions = relationship("Transaction", foreign_keys='Transaction.sender_id', back_populates="sender")
    received_transactions = relationship("Transaction", foreign_keys='Transaction.receiver_id', backpopulates="receiver")

    class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False) # Facturas, Auto, Transporte, Salud, etc.
    transaction_type = Column(Enum(TransactionType), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    sender = relationship("User", foreign_keys=[sender_id], back_populates="sent_transactions")
    receiver = relationship("User", foreign_keys=[receiver_id], back_populates="received_transactions")