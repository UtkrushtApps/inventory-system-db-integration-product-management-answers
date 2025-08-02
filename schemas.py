from pydantic import BaseModel, condecimal, Field
from typing import Optional
from decimal import Decimal
from datetime import datetime

class ProductCreate(BaseModel):
    name: str = Field(..., max_length=128)
    description: Optional[str]
    price: condecimal(gt=0, max_digits=10, decimal_places=2)
    quantity: int = Field(..., ge=0)

class ProductRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Decimal
    quantity: int
    created_at: datetime

    class Config:
        orm_mode = True
