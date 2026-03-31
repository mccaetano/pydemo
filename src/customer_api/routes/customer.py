

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from customer_api.database.db import get_db
from customer_api.database.schema import Customer
from customer_api.models.customer import Customer_request, Customer_response


router = APIRouter(
    prefix="/customer",
    tags=["Customers"]
)

@router.post("", response_model=Customer_response)
async def create(customer: Customer_request, db: Session = Depends(get_db)):
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/{customer_id}", response_model=Customer_response)
async def get_byid(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Id not found")
    return db_customer

@router.get("   ", response_model=List[Customer_response])
async def get_all(db: Session = Depends(get_db)):
    db_customer = db.query(Customer).all()
    return db_customer