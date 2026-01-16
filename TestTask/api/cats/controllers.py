from fastapi import APIRouter, Depends
from sqlmodel import Session
from core.helpers.database import get_session
from core.schemas.cat import CatUpdate, CatCreate
from api.cats.services import CatService

router = APIRouter(prefix="/cats", tags=["Cats"])


@router.post("/")
async def create_cat(cat: CatCreate, session: Session = Depends(get_session)):
    await CatService.validate_breed(cat.breed)
    return CatService.create_cat(session, cat)


@router.get("/")
def list_cats(session: Session = Depends(get_session)):
    return CatService.get_all_cats(session)


@router.get("/{cat_id}")
def get_cat(cat_id: int, session: Session = Depends(get_session)):
    return CatService.get_cat_by_id(session, cat_id)


@router.patch("/{cat_id}/salary")
def update_salary(cat_id: int, data: CatUpdate, session: Session = Depends(get_session)):
    return CatService.update_cat_salary(session, cat_id, data.salary)


@router.delete("/{cat_id}")
def delete_cat(cat_id: int, session: Session = Depends(get_session)):
    return CatService.delete_cat(session, cat_id)
