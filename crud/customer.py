from sqlalchemy import text
from sqlalchemy.orm import Session

from models.customer import Customer
from schemas.customer import CustomerCreate, CustomerUpdate


def create_customer(db: Session, customer: CustomerCreate):
    new_customer = Customer(
        name=customer.name,
        phone=customer.phone,
        email=customer.email,
        address=customer.address,
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def get_customers(db: Session):
    return db.query(Customer).all()


def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()


def update_customer(
    db: Session,
    customer_id: int,
    customer_data: CustomerUpdate,
):
    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if customer:
        customer.name = customer_data.name
        customer.phone = customer_data.phone
        customer.email = customer_data.email
        customer.address = customer_data.address

        db.commit()
        db.refresh(customer)

    return customer


def delete_customer(db: Session, customer_id: int):
    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if customer:
        db.delete(customer)
        db.commit()

        remaining_customers = db.query(Customer).count()

        if remaining_customers == 0:
            db.execute(
                text("ALTER TABLE customers AUTO_INCREMENT = 1")
            )
            db.commit()

    return customer
