from fastapi import APIRouter, Depends
from sqlmodel import Session
from core.helpers.database import get_session
from core.schemas.cat import MissionCreate, TargetUpdate
from api.missions.services import MissionService

router = APIRouter(tags=["Missions & Targets"])


@router.post("/missions")
def create_mission(data: MissionCreate, session: Session = Depends(get_session)):
    return MissionService.create_mission_with_targets(session, data)


@router.get("/missions")
def list_missions(session: Session = Depends(get_session)):
    return MissionService.get_missions(session)


@router.delete("/missions/{id}")
def delete_mission(id: int, session: Session = Depends(get_session)):
    return MissionService.delete_mission(session, id)


@router.patch("/missions/{id}/assign/{cat_id}")
def assign_cat(id: int, cat_id: int, session: Session = Depends(get_session)):
    return MissionService.assign_cat_to_mission(session, id, cat_id)


@router.patch("/targets/{id}")
def update_target(id: int, data: TargetUpdate, session: Session = Depends(get_session)):
    return MissionService.update_target(session, id, data)
