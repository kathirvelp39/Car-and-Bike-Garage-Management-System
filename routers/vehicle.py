from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud.vehicle import (
    create_vehicle,
    delete_vehicle,
    get_vehicle,
    get_vehicle_by_registration_number,
    get_vehicles,
    update_vehicle,
)
from database.database import get_db
from schemas.vehicle import (
    VehicleCreate,
    VehicleResponse,
    VehicleUpdate,
)

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
)


@router.get("/", response_model=list[VehicleResponse])
def get_vehicles_api(db: Session = Depends(get_db)):
    return get_vehicles(db)


@router.post("/", response_model=VehicleResponse)
def create_vehicle_api(
    vehicle: VehicleCreate,
    db: Session = Depends(get_db),
):
    return create_vehicle(db, vehicle)


@router.get("/search", response_model=VehicleResponse)
def search_vehicle_api(
    registration_number: str,
    db: Session = Depends(get_db),
):
    vehicle = get_vehicle_by_registration_number(
        db,
        registration_number,
    )

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found",
        )

    return vehicle


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle_api(
    vehicle_id: int,
    db: Session = Depends(get_db),
):
    vehicle = get_vehicle(db, vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found",
        )

    return vehicle


@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle_api(
    vehicle_id: int,
    vehicle_data: VehicleUpdate,
    db: Session = Depends(get_db),
):
    vehicle = update_vehicle(
        db,
        vehicle_id,
        vehicle_data,
    )

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found",
        )

    return vehicle


@router.delete(
    "/{vehicle_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_vehicle_api(
    vehicle_id: int,
    db: Session = Depends(get_db),
):
    vehicle = delete_vehicle(db, vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found",
        )