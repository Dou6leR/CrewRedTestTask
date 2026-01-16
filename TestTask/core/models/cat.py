from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class Cat(SQLModel, table=True):
    __tablename__ = "cat"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    years_of_experience: int
    breed: str
    salary: float

    mission: Optional["Mission"] = Relationship(back_populates="cat")


class Target(SQLModel, table=True):
    __tablename__ = "target"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str
    notes: Optional[str] = None
    is_complete: bool = Field(default=False)

    mission_id: Optional[int] = Field(
        default=None,
        foreign_key="mission.id"
    )
    mission: "Mission" = Relationship(back_populates="targets")


class Mission(SQLModel, table=True):
    __tablename__ = "mission"

    id: Optional[int] = Field(default=None, primary_key=True)
    is_complete: bool = Field(default=False)

    cat_id: Optional[int] = Field(
        default=None,
        foreign_key="cat.id"
    )
    cat: Optional[Cat] = Relationship(back_populates="mission")

    targets: List[Target] = Relationship(back_populates="mission")
