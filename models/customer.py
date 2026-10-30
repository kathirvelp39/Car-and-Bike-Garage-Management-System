from sqlalchemy import Column, Integer, String

from database.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100), nullable=True)
    address = Column(String(255), nullable=True)
