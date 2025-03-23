# FastAPI Product Catalog API

This is a RESTful API built with **FastAPI** that allows you to manage products and their characteristics.  
The app is fully asynchronous and uses **PostgreSQL** as the database, **SQLAlchemy** for ORM, and **Alembic** for migrations. The project is containerized with **Docker** and ready for deployment (e.g. to AWS).

---

## 📦 Features

- Create, Read, Update, and Delete (CRUD) operations for:
  - `Products`: with fields `id`, `name`, `quantity`, `sku`
  - `Characteristics`: with fields `id`, `name`, `value`, `product_id`
- Fully async via `asyncpg` and `SQLAlchemy 2.0`
- Automatic schema validation using **Pydantic**
- OpenAPI auto-generated documentation (Swagger UI)
- Dockerized PostgreSQL and FastAPI app
- Alembic for database migrations
- `.env` support for environment configuration

---

## 🛠 Technologies

- Python 3.11+
- FastAPI
- SQLAlchemy (async)
- Alembic
- PostgreSQL
- asyncpg
- Docker & Docker Compose
- Pydantic
- Python-dotenv

---

## 📂 Project Structure
. ├── app/ │ ├── main.py # Entry point │ ├── models.py # SQLAlchemy models │ ├── schemas.py # Pydantic schemas │ ├── crud.py # Database logic │ ├── database.py # DB session & engine ├── alembic/ # Alembic migrations │ ├── versions/ │ └── env.py ├── .env.local # Environment variables ├── requirements.txt ├── docker-compose.yml ├── Dockerfile └── README.md

---

## 🚀 Getting Started

### 1. Clone the project

bash
git clone https://github.com/yourusername/fastapi-product-api.git
cd fastapi-product-api

### 2. Add your .env.local file
env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres

### 3. Run with Docker
docker-compose up --build

Swagger UI: http://localhost:8000/docs

### 4. Apply Alembic Migrations
alembic upgrade head

### Example: Create a product (via Swagger UI)
<pre> ```json { "name": "Laptop", "quantity": 10, "sku": "ABC123", "characteristics": [ {"name": "RAM", "value": "16GB"}, {"name": "Color", "value": "Silver"} ] } ``` </pre>