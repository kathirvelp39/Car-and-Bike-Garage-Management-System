from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from database.database import get_db
from crud.customer import (
    create_customer,
    delete_customer,
    get_customer,
    get_customers,
    update_customer,
)
from schemas.customer import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate,
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@router.get("/", response_model=list[CustomerResponse])
def get_customers_api(db: Session = Depends(get_db)):
    return get_customers(db)


@router.post("/", response_model=CustomerResponse)
def create_customer_api(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
):
    return create_customer(db, customer)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer_api(
    customer_id: int,
    db: Session = Depends(get_db),
):
    customer = get_customer(db, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return customer


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer_api(
    customer_id: int,
    customer_data: CustomerUpdate,
    db: Session = Depends(get_db),
):
    customer = update_customer(db, customer_id, customer_data)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )

    return customer


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer_api(
    customer_id: int,
    db: Session = Depends(get_db),
):
    customer = delete_customer(db, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found",
        )
        
