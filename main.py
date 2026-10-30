from fastapi import FastAPI

from database.database import Base, engine

from models.customer import Customer
from models.vehicle import Vehicle
from models.mechanic import Mechanic
from models.service import Service
from models.spare_part import SparePart
from models.service_part import ServicePart
from models.bill import Bill

from routers.customer import router as customer_router
from routers.vehicle import router as vehicle_router
from routers.mechanic import router as mechanic_router
from routers.service import router as service_router
from routers.spare_part import router as spare_part_router
from routers.bill import router as bill_router
from routers.dashboard import router as dashboard_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Garage Management System")

app.include_router(customer_router)
app.include_router(vehicle_router)
app.include_router(mechanic_router)
app.include_router(service_router)
app.include_router(spare_part_router)
app.include_router(bill_router)
app.include_router(dashboard_router)