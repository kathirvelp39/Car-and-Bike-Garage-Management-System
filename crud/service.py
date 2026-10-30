from sqlalchemy.orm import Session

from models.service import Service
from schemas.service import ServiceCreate, ServiceUpdate


def create_service(db: Session, service_data: ServiceCreate):
    new_service = Service(
        customer_id=service_data.customer_id,
        vehicle_id=service_data.vehicle_id,
        service_type=service_data.service_type,
        complaint=service_data.complaint,
        arrival_date=service_data.arrival_date,
        expected_delivery_date=service_data.expected_delivery_date,
        status=service_data.status,
        mechanic_id=service_data.mechanic_id,
        labour_charge=service_data.labour_charge,
        additional_notes=service_data.additional_notes,
        total_service_cost=service_data.total_service_cost,
    )

    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


def get_services(db: Session):
    return db.query(Service).all()


def get_service(db: Session, service_id: int):
    return (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )


def update_service(
    db: Session,
    service_id: int,
    service_data: ServiceUpdate,
    
):
    service = (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )

    if service:
        service.customer_id = service_data.customer_id
        service.vehicle_id = service_data.vehicle_id
        service.service_type = service_data.service_type
        service.complaint = service_data.complaint
        service.arrival_date = service_data.arrival_date
        service.expected_delivery_date = (
            service_data.expected_delivery_date
        )
        service.status = service_data.status
        service.mechanic_id = service_data.mechanic_id
        service.labour_charge = service_data.labour_charge
        service.additional_notes = service_data.additional_notes
        service.total_service_cost = service_data.total_service_cost

        db.commit()
        db.refresh(service)

    return service


def delete_service(db: Session, service_id: int):
    service = (
        db.query(Service)
        .filter(Service.id == service_id)
        .first()
    )

    if service:
        db.delete(service)
        db.commit()

    return service


def get_services_by_customer(
    db: Session,
    customer_id: int,
):
    return (
        db.query(Service)
        .filter(Service.customer_id == customer_id)
        .all()
    )


def get_services_by_vehicle(
    db: Session,
    vehicle_id: int,
):
    return (
        db.query(Service)
        .filter(Service.vehicle_id == vehicle_id)
        .all()
    )


def get_services_by_mechanic(
    db: Session,
    mechanic_id: int,
):
    return (
        db.query(Service)
        .filter(Service.mechanic_id == mechanic_id)
        .all()
    )