from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud.mechanic import (
    create_mechanic,
    delete_mechanic,
    get_mechanic,
    get_mechanics,
    update_mechanic,
)
from database.database import get_db
from schemas.mechanic import (
    MechanicCreate,
    MechanicResponse,
    MechanicUpdate,
)

router = APIRouter(
    prefix="/mechanics",
    tags=["Mechanics"],
)


@router.get("/", response_model=list[MechanicResponse])
def get_mechanics_api(db: Session = Depends(get_db)):
    return get_mechanics(db)


@router.post("/", response_model=MechanicResponse)
def create_mechanic_api(
    mechanic: MechanicCreate,
    db: Session = Depends(get_db),
):
    return create_mechanic(db, mechanic)


@router.get("/{mechanic_id}", response_model=MechanicResponse)
def get_mechanic_api(
    mechanic_id: int,
    db: Session = Depends(get_db),
):
    mechanic = get_mechanic(db, mechanic_id)

    if mechanic is None:
        raise HTTPException(
            status_code=404,
            detail="Mechanic not found",
        )

    return mechanic


@router.put("/{mechanic_id}", response_model=MechanicResponse)
def update_mechanic_api(
    mechanic_id: int,
    mechanic_data: MechanicUpdate,
    db: Session = Depends(get_db),
):
    mechanic = update_mechanic(
        db,
        mechanic_id,
        mechanic_data,
    )

    if mechanic is None:
        raise HTTPException(
            status_code=404,
            detail="Mechanic not found",
        )

    return mechanic


@router.delete(
    "/{mechanic_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_mechanic_api(
    mechanic_id: int,
    db: Session = Depends(get_db),
):
    mechanic = delete_mechanic(db, mechanic_id)

    if mechanic is None:
        raise HTTPException(
            status_code=404,
            detail="Mechanic not found",
        )