import os
from sqlmodel import create_engine, SQLModel, Session
from typing import Generator
from core.models import *

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
