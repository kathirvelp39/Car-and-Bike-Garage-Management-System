from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.spare_part import (
    create_spare_part,
    delete_spare_part,
    get_low_stock_parts,
    get_spare_part,
    get_spare_parts,
    update_spare_part,
    use_spare_part,
)
from database.database import get_db
from schemas.spare_part import (
    SparePartCreate,
    SparePartResponse,
    SparePartUpdate,
    SparePartUsage,
)


router = APIRouter(
    prefix="/spare-parts",
    tags=["Spare Parts"],
)


@router.get(
    "/",
    response_model=list[SparePartResponse],
)
def get_spare_parts_api(
    db: Session = Depends(get_db),
):
    return get_spare_parts(db)


@router.post(
    "/",
    response_model=SparePartResponse,
)
def create_spare_part_api(
    spare_part: SparePartCreate,
    db: Session = Depends(get_db),
):
    return create_spare_part(db, spare_part)


@router.get(
    "/low-stock",
    response_model=list[SparePartResponse],
)
def get_low_stock_parts_api(
    db: Session = Depends(get_db),
):
    return get_low_stock_parts(db)


@router.get(
    "/{spare_part_id}",
    response_model=SparePartResponse,
)
def get_spare_part_api(
    spare_part_id: int,
    db: Session = Depends(get_db),
):
    part = get_spare_part(db, spare_part_id)

    if part is None:
        raise HTTPException(
            status_code=404,
            detail="Spare part not found",
        )

    return part


@router.put(
    "/{spare_part_id}",
    response_model=SparePartResponse,
)
def update_spare_part_api(
    spare_part_id: int,
    spare_part_data: SparePartUpdate,
    db: Session = Depends(get_db),
):
    part = update_spare_part(
        db,
        spare_part_id,
        spare_part_data,
    )

    if part is None:
        raise HTTPException(
            status_code=404,
            detail="Spare part not found",
        )

    return part


@router.delete(
    "/{spare_part_id}",
    status_code=204,
)
def delete_spare_part_api(
    spare_part_id: int,
    db: Session = Depends(get_db),
):
    part = delete_spare_part(
        db,
        spare_part_id,
    )

    if part is None:
        raise HTTPException(
            status_code=404,
            detail="Spare part not found",
        )


@router.post(
    "/{spare_part_id}/use",
    response_model=SparePartResponse,
)
def use_spare_part_api(
    spare_part_id: int,
    usage: SparePartUsage,
    db: Session = Depends(get_db),
):
    result, part = use_spare_part(
        db,
        spare_part_id,
        usage.service_id,
        usage.quantity_used,
    )

    if result == "PART_NOT_FOUND":
        raise HTTPException(
            status_code=404,
            detail="Spare part not found",
        )

    if result == "SERVICE_NOT_FOUND":
        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )

    if result == "INSUFFICIENT_STOCK":
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock",
        )

    return part 