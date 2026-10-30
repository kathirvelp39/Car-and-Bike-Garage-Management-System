GARAGE MANAGEMENT SYSTEM

Project Description
-------------------
This is a FastAPI-based Garage Management System for managing customer details in a garage.

Technologies Used
-----------------
- Python
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Pydantic
- Uvicorn

Project Structure
-----------------
models/
schemas/
database/
routers/
screenshots/
main.py
requirements.txt
README.txt

Features
--------
- Create Customer
- View All Customers
- View Customer by ID
- Update Customer
- Delete Customer
- Input Validation
- Error Handling
- MySQL Database Integration

Database Setup
--------------
1. Install MySQL.
2. Create a database named:

garage_Management_db

3. Create a .env file in the project root.
4. Add the database connection:

DATABASE_URL=mysql+pymysql://root:root@localhost:3306/garage_Management_db

Setup Instructions
------------------
1. Create and activate the virtual environment.
2. Install the required packages:

uv sync

3. Start the FastAPI server:

uv run uvicorn main:app --reload

4. Open Swagger UI:

http://127.0.0.1:8000/docs

API Endpoints
-------------
POST   /customers/
GET    /customers/
GET    /customers/{customer_id}
PUT    /customers/{customer_id}
DELETE /customers/{customer_id}

Testing
-------
All APIs can be tested using FastAPI Swagger UI.

Note
----
The .env file contains database credentials and should not be included in the submitted ZIP file.