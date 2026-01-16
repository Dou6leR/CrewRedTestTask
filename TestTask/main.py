from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.helpers.database import create_db_and_tables
from api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    pass


app = FastAPI(
    title="Spy Cat Agency",
    lifespan=lifespan
)

app.include_router(router)
