from pydantic import BaseModel, Field


class MechanicCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    phone: str = Field(min_length=10, max_length=15)
    specialization: str = Field(min_length=2, max_length=100)
    experience: int = Field(ge=0)


class MechanicUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    phone: str = Field(min_length=10, max_length=15)
    specialization: str = Field(min_length=2, max_length=100)
    experience: int = Field(ge=0)


class MechanicResponse(BaseModel):
    id: int
    name: str
    phone: str
    specialization: str
    experience: int

    class Config:
        from_attributes = True