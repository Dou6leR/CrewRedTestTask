#  Spy Cat Agency (SCA) - Management System

This is a RESTful API for the Spy Cat Agency to manage their feline operatives, missions, and targets. Built with **FastAPI**, **SQLModel**, and **PostgreSQL**.

## 🛠 Tech Stack
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** [PostgreSQL](https://www.postgresql.org/) (via [SQLModel](https://sqlmodel.tiangolo.com/))
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (modern & fast Python package manager)
- **Validation:** Pydantic v2
- **Containerization:** Docker & Docker Compose
- **External API:** [TheCatAPI](https://thecatapi.com/) for breed validation

---

## 🚀 How to Run

### Option 1: Using Docker (Recommended)
This will automatically set up the Python application and a PostgreSQL database.

1.  Make sure you have **Docker** and **Docker Compose** installed.
2.  In the root directory (`TestTask`), run:
    ```bash
    docker-compose up --build
    ```
3.  The API will be available at: `http://localhost:8000`
4.  Interactive API docs (Swagger): `http://localhost:8000/docs`

---

### Option 2: Local Development (Manual)
1.  **Install `uv`**:
    ```bash
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
2.  **Sync dependencies**:
    ```bash
    uv sync
    ```
3.  **Set Environment Variables**:
    Create a `.env` file or set the `DATABASE_URL`:
    `DATABASE_URL=postgresql://user:password@localhost:5432/spy_cat_agency`
4.  **Run the application**:
    ```bash
    uv run uvicorn main:app --reload
    ```

---

## 📬 API Documentation & Postman

### Postman Collection
- **[🔗 Link to Public Postman Collection](https://www.postman.com/rostyslawoo-1959159/crewredtesttask/collection/47391324-b479e740-2e56-4fd6-82f4-f015643f2a23/?action=share&creator=47391324)**
- Alternatively, you can find the exported JSON file in the root directory: `SpyCatAgency.postman_collection.json`.

**Setup:** Ensure the `baseUrl` variable in Postman is set to `http://localhost:8000`.

---

## 🏗 Project Structure
```text
TestTask/
├── api/
│   ├── cats/           # Controller & Service for Cat management
│   └── missions/       # Controller & Service for Missions & Targets
├── core/
│   ├── helpers/        # Database connection & setup
│   ├── models/         # SQLModel database models
│   └── schemas/        # Pydantic validation schemas
├── main.py             # Entry point & Lifespan configuration
├── Dockerfile          # Container configuration
└── docker-compose.yml  # Multi-container orchestration
