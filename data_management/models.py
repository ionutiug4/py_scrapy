from psycopg2 import DATETIME
from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email_address = Column(String, unique=True, index=True, nullable=False)
    last_name = Column(String, unique=False, index=True, nullable=False)
    first_name = Column(String, unique=False, index=True, nullable=False)
    phone_number = Column(String, unique=False, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, unique=False, index=True)
    description = Column(String, unique=False, index=True)
    services = Column(String, unique=False, index=True)
    created_at = Column(DATETIME(), unique=False, index=True)
    status = Column(String, unique=False, index=True)