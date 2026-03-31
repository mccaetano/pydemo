
from fastapi import FastAPI
from customer_api.database.db import engine
from customer_api.database.schema import create_db
from customer_api.routes import customer
create_db(engine)

app = FastAPI()

app.include_router(customer.router)
