from sqlalchemy import Column, Integer, String

from database.database import Base


class Mechanic(Base):
    __tablename__ = "mechanics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    specialization = Column(String(100), nullable=False)
    experience = Column(Integer, nullable=False)