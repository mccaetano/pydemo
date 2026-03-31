

from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class Customer_request(BaseModel):
    name = str
    email = EmailStr
    phone = Optional[str]
    birth_date = Optional[date]
