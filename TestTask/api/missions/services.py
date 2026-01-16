from fastapi import HTTPException
from sqlmodel import Session, select
from core.models import Mission, Target, Cat
from core.schemas.cat import MissionCreate, TargetUpdate


class MissionService:
    @classmethod
    def create_mission_with_targets(cls, session: Session, data: MissionCreate):
        new_mission = Mission()
        session.add(new_mission)
        session.commit()

        for t_data in data.targets:
            target = Target(**t_data.model_dump(), mission_id=new_mission.id)
            session.add(target)

        session.commit()
        session.refresh(new_mission)
        return new_mission

    @classmethod
    def get_missions(cls, session: Session):
        return session.exec(select(Mission)).all()

    @classmethod
    def get_mission(cls, session: Session, mission_id: int):
        m = session.get(Mission, mission_id)
        if not m:
            raise HTTPException(status_code=404, detail="Mission not found")
        return m

    @classmethod
    def delete_mission(cls, session: Session, mission_id: int):
        mission = cls.get_mission(session, mission_id)
        if mission.cat_id is not None:
            raise HTTPException(status_code=400, detail="Cannot delete mission assigned to a cat")
        session.delete(mission)
        session.commit()
        return {"message": "Mission deleted"}

    @classmethod
    def assign_cat_to_mission(cls, session: Session, mission_id: int, cat_id: int):
        mission = cls.get_mission(session, mission_id)
        cat = session.get(Cat, cat_id)
        if not cat:
            raise HTTPException(status_code=404, detail="Cat not found")

        active_mission = session.exec(
            select(Mission).where(
                Mission.cat_id == cat_id,
                Mission.is_complete == False
            )
        ).first()

        if active_mission:
            raise HTTPException(
                status_code=400,
                detail="This cat already has an active (incomplete) mission"
            )

        mission.cat_id = cat_id
        session.add(mission)
        session.commit()
        session.refresh(mission)
        return mission

    @classmethod
    def update_target(cls, session: Session, target_id: int, data: TargetUpdate):
        target = session.get(Target, target_id)
        if not target:
            raise HTTPException(status_code=404, detail="Target not found")

        mission = session.get(Mission, target.mission_id)

        if data.notes is not None:
            if target.is_complete or (mission and mission.is_complete):
                raise HTTPException(status_code=400, detail="Notes are frozen: target or mission is complete")
            target.notes = data.notes

        if data.is_complete is not None:
            target.is_complete = data.is_complete

        session.add(target)
        session.commit()

        session.refresh(mission)
        if all(t.is_complete for t in mission.targets):
            mission.is_complete = True
            session.add(mission)
            session.commit()

        session.refresh(target)
        return target
