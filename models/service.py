from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Text

from database.database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)

    service_type = Column(String(100), nullable=False)
    complaint = Column(Text, nullable=False)

    arrival_date = Column(Date, nullable=False)
    expected_delivery_date = Column(Date, nullable=False)
    status = Column(String(30), nullable=False, default="Received")

    mechanic_id = Column(Integer, ForeignKey("mechanics.id"), nullable=True)

    labour_charge = Column(Float, nullable=False, default=0)
    additional_notes = Column(Text, nullable=True)
    total_service_cost = Column(Float, nullable=False, default=0) 