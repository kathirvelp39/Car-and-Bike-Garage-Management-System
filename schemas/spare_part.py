from pydantic import BaseModel, Field


class SparePartCreate(BaseModel):
    part_name: str = Field(
        min_length=2,
        max_length=100,
    )

    part_number: str = Field(
        min_length=2,
        max_length=50,
    )

    category: str = Field(
        min_length=2,
        max_length=100,
    )

    available_quantity: int = Field(
        ge=0,
    )

    price: float = Field(
        ge=0,
    )

    minimum_stock_level: int = Field(
        ge=0,
    )


class SparePartUpdate(BaseModel):
    part_name: str = Field(
        min_length=2,
        max_length=100,
    )

    part_number: str = Field(
        min_length=2,
        max_length=50,
    )

    category: str = Field(
        min_length=2,
        max_length=100,
    )

    available_quantity: int = Field(
        ge=0,
    )

    price: float = Field(
        ge=0,
    )

    minimum_stock_level: int = Field(
        ge=0,
    )


class SparePartResponse(BaseModel):
    id: int
    part_name: str
    part_number: str
    category: str
    available_quantity: int
    price: float
    minimum_stock_level: int

    class Config:
        from_attributes = True


class SparePartUsage(BaseModel):
    service_id: int = Field(gt=0)
    quantity_used: int = Field(gt=0)  