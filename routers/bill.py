from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.bill import (
    create_bill,
    delete_bill,
    get_bill,
    get_bills,
    update_bill,
)
from database.database import get_db
from schemas.bill import (
    BillCreate,
    BillResponse,
    BillUpdate,
)


router = APIRouter(
    prefix="/bills",
    tags=["Billing"],
)
 

@router.get(
    "/",
    response_model=list[BillResponse],
)
def get_bills_api(
    db: Session = Depends(get_db),
):
    return get_bills(db)


@router.post(
    "/",
    response_model=BillResponse,
)
def create_bill_api(
    bill_data: BillCreate,
    db: Session = Depends(get_db),
):
    bill = create_bill(db, bill_data)

    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found",
        )

    return bill


@router.get(
    "/{bill_id}",
    response_model=BillResponse,
)
def get_bill_api(
    bill_id: int,
    db: Session = Depends(get_db),
):
    bill = get_bill(db, bill_id)

    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not found",
        )

    return bill


@router.put(
    "/{bill_id}",
    response_model=BillResponse,
)
def update_bill_api(
    bill_id: int,
    bill_data: BillUpdate,
    db: Session = Depends(get_db),
):
    bill = update_bill(
        db,
        bill_id,
        bill_data,
    )

    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not found",
        )

    return bill


@router.delete(
    "/{bill_id}",
    status_code=204,
)
def delete_bill_api(
    bill_id: int,
    db: Session = Depends(get_db),
):
    bill = delete_bill(db, bill_id)

    if bill is None:
        raise HTTPException(
            status_code=404,
            detail="Bill not found",
        )