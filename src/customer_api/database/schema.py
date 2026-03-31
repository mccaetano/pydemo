
from sqlalchemy import Column, Date, Integer, String
from customer_api.database.db import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    birth_date = Column("birthDate", Date)

def create_db(engine):
    Base.metadata.create_all(bind = engine)