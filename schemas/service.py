from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


ServiceStatus = Literal[
    "Received",
    "Inspection",
    "In Service",
    "Waiting for Parts",
    "Completed",
    "Delivered",
]


class ServiceCreate(BaseModel):
    customer_id: int = Field(gt=0)
    vehicle_id: int = Field(gt=0)
    service_type: str = Field(min_length=2, max_length=100)
    complaint: str = Field(min_length=2)
    arrival_date: date
    expected_delivery_date: date
    status: ServiceStatus = "Received"
    mechanic_id: int | None = Field(default=None, gt=0)
    
    labour_charge: float = Field(ge=0)
    additional_notes: str | None = None
    total_service_cost: float = Field(ge=0)


class ServiceUpdate(BaseModel):
    customer_id: int = Field(gt=0)
    vehicle_id: int = Field(gt=0)
    service_type: str = Field(min_length=2, max_length=100)
    complaint: str = Field(min_length=2)
    arrival_date: date
    expected_delivery_date: date
    status: ServiceStatus
    mechanic_id: int | None = Field(default=None, gt=0)
    
    labour_charge: float = Field(ge=0)
    additional_notes: str | None = None
    total_service_cost: float = Field(ge=0)


class ServiceResponse(BaseModel):
    id: int
    customer_id: int
    vehicle_id: int
    service_type: str
    complaint: str 
    arrival_date: date
    expected_delivery_date: date
    status: str
    mechanic_id: int | None = None
    
    labour_charge: float
    additional_notes: str | None = None
    total_service_cost: float

    class Config:
        from_attributes = True 