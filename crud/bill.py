from sqlalchemy.orm import Session

from models.bill import Bill
from models.service import Service
from models.service_part import ServicePart
from models.spare_part import SparePart
from schemas.bill import BillCreate, BillUpdate


def calculate_spare_parts_charges(
    db: Session,
    service_id: int,
):
    service_parts = (
        db.query(ServicePart)
        .filter(ServicePart.service_id == service_id)
        .all()
    )

    total = 0

    for service_part in service_parts:
        spare_part = (
            db.query(SparePart)
            .filter(
                SparePart.id
                == service_part.spare_part_id
            )
            .first()
        )

        if spare_part:
            total += (
                service_part.quantity_used
                * spare_part.price
            )

    return total


def create_bill(
    db: Session,
    bill_data: BillCreate,
):
    service = (
        db.query(Service)
        .filter(Service.id == bill_data.service_id)
        .first()
    )

    if service is None:
        return None

    labour_charges = service.labour_charge

    spare_parts_charges = (
        calculate_spare_parts_charges(
            db,
            bill_data.service_id,
        )
    )

    final_amount = (
        labour_charges
        + spare_parts_charges
        + bill_data.tax
        - bill_data.discount
    )

    new_bill = Bill(
        service_id=bill_data.service_id,
        labour_charges=labour_charges,
        spare_parts_charges=spare_parts_charges,
        tax=bill_data.tax,
        discount=bill_data.discount,
        final_amount=final_amount,
        payment_status=bill_data.payment_status,
    )

    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)

    return new_bill


def get_bills(db: Session):
    return db.query(Bill).all()


def get_bill(
    db: Session,
    bill_id: int,
):
    return (
        db.query(Bill)
        .filter(Bill.id == bill_id)
        .first()
    )


def update_bill(
    db: Session,
    bill_id: int,
    bill_data: BillUpdate,
):
    bill = get_bill(db, bill_id)

    if bill is None:
        return None

    bill.tax = bill_data.tax
    bill.discount = bill_data.discount
    bill.payment_status = bill_data.payment_status

    bill.final_amount = (
        bill.labour_charges
        + bill.spare_parts_charges
        + bill.tax
        - bill.discount
    )

    db.commit()
    db.refresh(bill)

    return bill


def delete_bill(
    db: Session,
    bill_id: int,
):
    bill = get_bill(db, bill_id)

    if bill:
        db.delete(bill)
        db.commit()

    return bill 