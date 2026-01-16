from pydantic import BaseModel, Field
from typing import List, Optional


class CatCreate(BaseModel):
    name: str
    years_of_experience: int
    breed: str
    salary: float


class CatUpdate(BaseModel):
    salary: float


class TargetCreate(BaseModel):
    name: str
    country: str
    notes: Optional[str] = None
    is_complete: bool = False


class TargetUpdate(BaseModel):
    notes: Optional[str] = None
    is_complete: Optional[bool] = None


class MissionCreate(BaseModel):
    targets: List[TargetCreate] = Field(..., min_items=1, max_items=3)
