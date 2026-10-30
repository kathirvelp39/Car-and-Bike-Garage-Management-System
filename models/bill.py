from sqlalchemy import Column, Float, ForeignKey, Integer, String

from database.database import Base


class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)

    service_id = Column(
        Integer,
        ForeignKey("services.id"),
        nullable=False,
    )

    labour_charges = Column(
        Float,
        nullable=False,
        default=0,
    )

    spare_parts_charges = Column(
        Float,
        nullable=False,
        default=0,
    )

    tax = Column(
        Float,
        nullable=False,
        default=0,
    )

    discount = Column(
        Float,
        nullable=False,
        default=0,
    )

    final_amount = Column(
        Float,
        nullable=False,
        default=0,
    )

    payment_status = Column(
        String(30),
        nullable=False,
        default="Pending",
    ) 