from pydantic import BaseModel, EmailStr, Field


class CustomerCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    phone: str = Field(min_length=10, max_length=15)
    email: EmailStr | None = None
    address: str | None = Field(default=None, max_length=255)


class CustomerUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    phone: str = Field(min_length=10, max_length=15)
    email: EmailStr | None = None
    address: str | None = Field(default=None, max_length=255)
    
class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: str | None = None
    address: str | None = None

    class Config:
        from_attributes = True