from fastapi import APIRouter
from .missions import router as missions_router
from .cats import router as cats_router

router = APIRouter()

router.include_router(missions_router)
router.include_router(cats_router)
