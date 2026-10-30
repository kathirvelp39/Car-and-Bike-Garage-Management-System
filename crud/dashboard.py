from sqlalchemy import func
from sqlalchemy.orm import Session

from models.bill import Bill
from models.customer import Customer
from models.service import Service
from models.spare_part import SparePart
from models.vehicle import Vehicle


def get_dashboard_data(db: Session):

    # Total customers
    total_customers = (
        db.query(Customer)
        .count()
    )

    # Total cars
    total_cars = (
        db.query(Vehicle)
        .filter(Vehicle.vehicle_type == "Car")
        .count()
    )

    # Total bikes
    total_bikes = (
        db.query(Vehicle)
        .filter(Vehicle.vehicle_type == "Bike")
        .count()
    )

    # Vehicles currently under service
    vehicles_under_service = (
        db.query(Service)
        .filter(
            Service.status.in_(
                [
                    "Received",
                    "Inspection",
                    "In Service",
                    "Waiting for Parts",
                ]
            )
        )
        .count()
    )

    # Completed services
    completed_services = (
        db.query(Service)
        .filter(
            Service.status.in_(
                [
                    "Completed",
                    "Delivered",
                ]
            )
        )
        .count()
    )

    # Pending services
    pending_services = (
        db.query(Service)
        .filter(
            Service.status.notin_(
                [
                    "Completed",
                    "Delivered",
                ]
            )
        )
        .count()
    )

    # Total revenue
    total_revenue = (
        db.query(
            func.coalesce(
                func.sum(Bill.final_amount),
                0,
            )
        )
        .scalar()
    )

    # Low-stock spare parts
    low_stock_parts = (
        db.query(SparePart)
        .filter(
            SparePart.available_quantity
            <= SparePart.minimum_stock_level
        )
        .count()
    )

    return {
        "total_customers": total_customers,
        "total_cars": total_cars,
        "total_bikes": total_bikes,
        "vehicles_under_service": vehicles_under_service,
        "completed_services": completed_services,
        "pending_services": pending_services,
        "total_revenue": float(total_revenue),
        "low_stock_parts": low_stock_parts,
    } 