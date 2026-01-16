import httpx
from fastapi import HTTPException
from sqlmodel import Session, select
from core.models import Cat
from core.schemas.cat import CatCreate


class CatService:
    @classmethod
    async def validate_breed(cls, breed_name: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get("https://api.thecatapi.com/v1/breeds")
                response.raise_for_status()
                breeds = response.json()
                if not any(b['name'].lower() == breed_name.lower() for b in breeds):
                    raise HTTPException(status_code=400, detail=f"Breed '{breed_name}' is not recognized by TheCatAPI")
            except httpx.HTTPError:
                raise HTTPException(status_code=503, detail="Breed validation service unavailable")

    @classmethod
    def create_cat(cls, session: Session, cat_data: CatCreate):
        db_cat = Cat.model_validate(cat_data)
        session.add(db_cat)
        session.commit()
        session.refresh(db_cat)
        return cat_data

    @classmethod
    def get_all_cats(cls, session: Session):
        return session.exec(select(Cat)).all()

    @classmethod
    def get_cat_by_id(cls, session: Session, cat_id: int):
        cat = session.get(Cat, cat_id)
        if not cat:
            raise HTTPException(status_code=404, detail="Cat not found")
        return cat

    @classmethod
    def update_cat_salary(cls, session: Session, cat_id: int, new_salary: float):
        cat = cls.get_cat_by_id(session, cat_id)
        cat.salary = new_salary
        session.add(cat)
        session.commit()
        session.refresh(cat)
        return cat

    @classmethod
    def delete_cat(cls, session: Session, cat_id: int):
        cat = cls.get_cat_by_id(session, cat_id)
        session.delete(cat)
        session.commit()
        return {"message": "Cat removed"}
