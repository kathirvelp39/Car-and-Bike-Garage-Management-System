from sqlalchemy import Column, Float, ForeignKey, Integer, String

from database.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    registration_number = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )
    vehicle_type = Column(String(10), nullable=False)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    manufacturing_year = Column(Integer, nullable=False)
    fuel_type = Column(String(30), nullable=False)
    mileage = Column(Float, nullable=False)
    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False,
    )