from typing import Literal

from pydantic import BaseModel, Field


class VehicleCreate(BaseModel):
    registration_number: str = Field(
        min_length=3,
        max_length=20,
    )
    vehicle_type: Literal["Car", "Bike"]
    brand: str = Field(min_length=2, max_length=100)
    model: str = Field(min_length=1, max_length=100)
    manufacturing_year: int = Field(ge=1900, le=2100)
    fuel_type: str = Field(min_length=2, max_length=30)
    mileage: float = Field(ge=0)
    customer_id: int = Field(gt=0)


class VehicleUpdate(BaseModel):
    registration_number: str = Field(
        min_length=3,
        max_length=20,
    )
    vehicle_type: Literal["Car", "Bike"]
    brand: str = Field(min_length=2, max_length=100)
    model: str = Field(min_length=1, max_length=100)
    manufacturing_year: int = Field(ge=1900, le=2100)
    fuel_type: str = Field(min_length=2, max_length=30)
    mileage: float = Field(ge=0)
    customer_id: int = Field(gt=0)


class VehicleResponse(BaseModel):
    id: int
    registration_number: str
    vehicle_type: str
    brand: str
    model: str
    manufacturing_year: int
    fuel_type: str
    mileage: float
    customer_id: int

    class Config:
        from_attributes = True