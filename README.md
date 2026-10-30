# Car and Bike Garage Management System

A backend application developed using Python, FastAPI, MySQL, and SQLAlchemy to manage daily operations in a car and bike service garage.

## Project Overview

This system helps garage staff manage customers, vehicles, service requests, mechanics, and spare parts inventory through REST APIs.

## Features

### 1. Customer Management
- Create, view, update, and delete customer records.

### 2. Vehicle Management
- Manage cars and bikes.
- Store registration number, vehicle type, brand, model, manufacturing year, fuel type, and mileage.
- Link vehicles with customers.
- Search vehicles by registration number.

### 3. Service Management
- Create and manage service requests.
- Link services with customers and vehicles.
- Maintain service history.
- Manage service statuses:
  - Received
  - Inspection
  - In Service
  - Waiting for Parts
  - Completed
  - Delivered

### 4. Mechanic Management
- Create, view, update, and delete mechanic records.
- Store mechanic details, specialization, and experience.
- Assign mechanics to service requests.
- View services assigned to mechanics.

### 5. Spare Parts and Inventory Management
- Manage spare parts inventory.
- Track part name, part number, category, available quantity, price, and minimum stock level.
- Record spare parts used for services.
- Automatically reduce stock when parts are used.
- Identify low-stock spare parts.

## Technology Stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- uv
- Swagger UI

## Project Structure

```text
Garage_Management_System/
â”œâ”€â”€ crud/
â”œâ”€â”€ database/
â”œâ”€â”€ models/
â”œâ”€â”€ routers/
â”œâ”€â”€ schemas/
â”œâ”€â”€ screenshots/
â”œâ”€â”€ main.py
â”œâ”€â”€ .gitignore
â”œâ”€â”€ .python-version
â”œâ”€â”€ pyproject.toml
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ uv.lock
â””â”€â”€ README.md
