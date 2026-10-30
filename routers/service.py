from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.service import (
    create_service,
    delete_service,
    get_service,
    get_services,
    get_services_by_customer,
    get_services_by_mechanic,
    get_services_by_vehicle,
    update_service,
)
from database.database import get_db
from schemas.service import (
    ServiceCreate,
    ServiceResponse,
    ServiceUpdate,
)

router = APIRouter(
    prefix="/services",
    tags=["Services"],
)


@router.get("/", response_model=list[ServiceResponse])
def get_services_api(db: Session = Depends(get_db)):
    return get_services(db) 


@router.post("/", response_model=ServiceResponse)
def create_service_api(
    service: ServiceCreate,
    db: Session = Depends(get_db),
):
    return create_service(db, service)


@router.get("/customer/{customer_id}", response_model=list[ServiceResponse])
def get_customer_services_api(
    customer_id: int,
    db: Session = Depends(get_db),
):
    return get_services_by_customer(db, customer_id)


@router.get("/vehicle/{vehicle_id}", response_model=list[ServiceResponse])
def get_vehicle_services_api(
    vehicle_id: int,
    db: Session = Depends(get_db),
):
    return get_services_by_vehicle(db, vehicle_id)


@router.get("/mechanic/{mechanic_id}", response_model=list[ServiceResponse])
def get_mechanic_services_api(
    mechanic_id: int,
    db: Session = Depends(get_db),
):
    return get_services_by_mechanic(db, mechanic_id)


@router.get("/{service_id}", response_model=ServiceResponse)
def get_service_api(
    service_id: int,
    db: Session = Depends(get_db),
):
    service = get_service(db, service_id)

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )

    return service


@router.put("/{service_id}", response_model=ServiceResponse)
def update_service_api(
    service_id: int,
    service_data: ServiceUpdate,
    db: Session = Depends(get_db),
):
    service = update_service(
        db,
        service_id,
        service_data,
    )

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )

    return service


@router.delete("/{service_id}", status_code=204)
def delete_service_api(
    service_id: int,
    db: Session = Depends(get_db),
):
    service = delete_service(db, service_id)

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )