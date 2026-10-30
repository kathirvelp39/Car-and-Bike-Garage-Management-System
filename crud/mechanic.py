from sqlalchemy.orm import Session

from models.mechanic import Mechanic
from schemas.mechanic import MechanicCreate, MechanicUpdate


def create_mechanic(db: Session, mechanic_data: MechanicCreate):
    new_mechanic = Mechanic(
        name=mechanic_data.name,
        phone=mechanic_data.phone,
        specialization=mechanic_data.specialization,
        experience=mechanic_data.experience,
    )

    db.add(new_mechanic)
    db.commit()
    db.refresh(new_mechanic)

    return new_mechanic


def get_mechanics(db: Session):
    return db.query(Mechanic).all()


def get_mechanic(db: Session, mechanic_id: int):
    return (
        db.query(Mechanic)
        .filter(Mechanic.id == mechanic_id)
        .first()
    )


def update_mechanic(
    db: Session,
    mechanic_id: int,
    mechanic_data: MechanicUpdate,
):
    mechanic = (
        db.query(Mechanic)
        .filter(Mechanic.id == mechanic_id)
        .first()
    )

    if mechanic:
        mechanic.name = mechanic_data.name
        mechanic.phone = mechanic_data.phone
        mechanic.specialization = mechanic_data.specialization
        mechanic.experience = mechanic_data.experience

        db.commit()
        db.refresh(mechanic)

    return mechanic


def delete_mechanic(db: Session, mechanic_id: int):
    mechanic = (
        db.query(Mechanic)
        .filter(Mechanic.id == mechanic_id)
        .first()
    )

    if mechanic:
        db.delete(mechanic)
        db.commit()

    return mechanic