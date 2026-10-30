from sqlalchemy import Column, ForeignKey, Integer

from database.database import Base


class ServicePart(Base):
    __tablename__ = "service_parts"

    id = Column(Integer, primary_key=True, index=True)

    service_id = Column(
        Integer,
        ForeignKey("services.id"),
        nullable=False,
    )

    spare_part_id = Column(
        Integer,
        ForeignKey("spare_parts.id"),
        nullable=False,
    )

    quantity_used = Column(
        Integer,
        nullable=False,
    ) 