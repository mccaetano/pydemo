

from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class Customer_request(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str]
    birth_date: Optional[date]

class Customer_response(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str]
    birth_date: Optional[date]

    class Config:
        from_attributes = True
