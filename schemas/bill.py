from typing import Literal

from pydantic import BaseModel, Field


PaymentStatus = Literal[
    "Pending",
    "Paid",
    "Partially Paid",
]


class BillCreate(BaseModel):
    service_id: int = Field(gt=0)
    tax: float = Field(ge=0, default=0)
    discount: float = Field(ge=0, default=0)
    payment_status: PaymentStatus = "Pending"


class BillUpdate(BaseModel):
    tax: float = Field(ge=0, default=0)
    discount: float = Field(ge=0, default=0)
    payment_status: PaymentStatus


class BillResponse(BaseModel):
    id: int
    service_id: int
    labour_charges: float
    spare_parts_charges: float
    tax: float
    discount: float
    final_amount: float
    payment_status: str

    class Config:
        from_attributes = True 