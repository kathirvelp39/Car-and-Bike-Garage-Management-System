from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_customers: int
    total_cars: int
    total_bikes: int
    vehicles_under_service: int
    completed_services: int
    pending_services: int
    total_revenue: float
    low_stock_parts: int