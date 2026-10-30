from sqlalchemy.orm import Session

from models.vehicle import Vehicle
from schemas.vehicle import VehicleCreate, VehicleUpdate


def create_vehicle(db: Session, vehicle_data: VehicleCreate):
    new_vehicle = Vehicle(
        registration_number=vehicle_data.registration_number,
        vehicle_type=vehicle_data.vehicle_type,
        brand=vehicle_data.brand,
        model=vehicle_data.model,
        manufacturing_year=vehicle_data.manufacturing_year,
        fuel_type=vehicle_data.fuel_type,
        mileage=vehicle_data.mileage,
        customer_id=vehicle_data.customer_id,
    )

    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)

    return new_vehicle


def get_vehicles(db: Session):
    return db.query(Vehicle).all()


def get_vehicle(db: Session, vehicle_id: int):
    return (
        db.query(Vehicle)
        .filter(Vehicle.id == vehicle_id)
        .first()
    )


def get_vehicle_by_registration_number(
    db: Session,
    registration_number: str,
):
    return (
        db.query(Vehicle)
        .filter(
            Vehicle.registration_number == registration_number
        )
        .first()
    )


def update_vehicle(
    db: Session,
    vehicle_id: int,
    vehicle_data: VehicleUpdate,
):
    vehicle = (
        db.query(Vehicle)
        .filter(Vehicle.id == vehicle_id)
        .first()
    )

    if vehicle:
        vehicle.registration_number = (
            vehicle_data.registration_number
        )
        vehicle.vehicle_type = vehicle_data.vehicle_type
        vehicle.brand = vehicle_data.brand
        vehicle.model = vehicle_data.model
        vehicle.manufacturing_year = (
            vehicle_data.manufacturing_year
        )
        vehicle.fuel_type = vehicle_data.fuel_type
        vehicle.mileage = vehicle_data.mileage
        vehicle.customer_id = vehicle_data.customer_id

        db.commit()
        db.refresh(vehicle)

    return vehicle


def delete_vehicle(db: Session, vehicle_id: int):
    vehicle = (
        db.query(Vehicle)
        .filter(Vehicle.id == vehicle_id)
        .first()
    )

    if vehicle:
        db.delete(vehicle)
        db.commit()

    return vehicle