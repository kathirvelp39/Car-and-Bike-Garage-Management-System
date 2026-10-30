from sqlalchemy.orm import Session

from models.service import Service
from models.service_part import ServicePart
from models.spare_part import SparePart
from schemas.spare_part import (
    SparePartCreate,
    SparePartUpdate,
)


def create_spare_part(
    db: Session,
    spare_part_data: SparePartCreate,
):
    new_part = SparePart(
        part_name=spare_part_data.part_name,
        part_number=spare_part_data.part_number,
        category=spare_part_data.category,
        available_quantity=spare_part_data.available_quantity,
        price=spare_part_data.price,
        minimum_stock_level=spare_part_data.minimum_stock_level,
    )

    db.add(new_part)
    db.commit() 
    db.refresh(new_part)

    return new_part


def get_spare_parts(db: Session):
    return db.query(SparePart).all()


def get_spare_part(
    db: Session,
    spare_part_id: int,
):
    return (
        db.query(SparePart)
        .filter(SparePart.id == spare_part_id)
        .first()
    )


def update_spare_part(
    db: Session,
    spare_part_id: int,
    spare_part_data: SparePartUpdate,
):
    part = get_spare_part(db, spare_part_id)

    if part:
        part.part_name = spare_part_data.part_name
        part.part_number = spare_part_data.part_number
        part.category = spare_part_data.category
        part.available_quantity = (
            spare_part_data.available_quantity
        )
        part.price = spare_part_data.price
        part.minimum_stock_level = (
            spare_part_data.minimum_stock_level
        )

        db.commit()
        db.refresh(part)

    return part


def delete_spare_part(
    db: Session,
    spare_part_id: int,
):
    part = get_spare_part(db, spare_part_id)

    if part:
        db.delete(part)
        db.commit()

    return part


def get_low_stock_parts(db: Session):
    return (
        db.query(SparePart)
        .filter(
            SparePart.available_quantity
            <= SparePart.minimum_stock_level
        )
        .all()
    )


def use_spare_part(
    db: Session,
    spare_part_id: int,
    service_id: int,
    quantity_used: int,
):
    # Find spare part
    part = get_spare_part(
        db,
        spare_part_id,
    )

    if part is None:
        return "PART_NOT_FOUND", None

    # Find service
    service = (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )

    if service is None:
        return "SERVICE_NOT_FOUND", None

    # Check stock before reducing quantity
    if part.available_quantity < quantity_used:
        return "INSUFFICIENT_STOCK", None

    # Reduce spare part stock
    part.available_quantity -= quantity_used

    # Check whether this part is already used
    # for this service
    service_part = (
        db.query(ServicePart)
        .filter(
            ServicePart.service_id == service_id,
            ServicePart.spare_part_id == spare_part_id,
        )
        .first()
    )

    if service_part:
        service_part.quantity_used += quantity_used
    else:
        service_part = ServicePart(
            service_id=service_id,
            spare_part_id=spare_part_id,
            quantity_used=quantity_used,
        )

        db.add(service_part)

    # Calculate total spare-parts cost
    service_parts = (
        db.query(ServicePart)
        .filter(
            ServicePart.service_id == service_id
        )
        .all()
    )

    parts_total = 0

    for service_part_item in service_parts:
        spare_part = (
            db.query(SparePart)
            .filter(
                SparePart.id
                == service_part_item.spare_part_id
            )
            .first()
        )

        if spare_part:
            parts_total += (
                service_part_item.quantity_used
                * spare_part.price
            )

    # Calculate total service cost
    service.total_service_cost = (
        service.labour_charge + parts_total
    )

    # Save changes
    db.commit()
    db.refresh(part)

    return "SUCCESS", part