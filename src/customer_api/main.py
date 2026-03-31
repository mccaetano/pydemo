
from fastapi import FastAPI
from customer_api.database.db import engine
from customer_api.database.schema import create_db
from customer_api.routes.customer import router as customer_router
create_db(engine)

app = FastAPI()

app.add_route(customer_router)
