from sqlalchemy import Column, Float, Integer, String

from database.database import Base


class SparePart(Base):
    __tablename__ = "spare_parts"

    id = Column(Integer, primary_key=True, index=True)

    part_name = Column(String(100), nullable=False)

    part_number = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    category = Column(String(100), nullable=False)

    available_quantity = Column(
        Integer,
        nullable=False,
        default=0,
    )

    price = Column(Float, nullable=False)

    minimum_stock_level = Column(
        Integer,
        nullable=False,
        default=0, 
    )