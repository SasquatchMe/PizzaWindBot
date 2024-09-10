from sqlalchemy import select, func
from sqlalchemy.orm import selectinload

from src.application.database import new_session
from src.geopos.models import GeoPosOrm
from src.geopos.schemas import SAddGeoPos, SGeoPos
from src.questions.models import QuestionOrm


class GeoPosRepo:

    @classmethod
    async def get_one(cls, geopos_id):
        async with new_session() as session:

            query = select(GeoPosOrm).where(GeoPosOrm.id == geopos_id)
            result = await session.execute(query)
            geopos = result.scalar_one()
            return geopos

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(GeoPosOrm).options(
                selectinload(GeoPosOrm.questions).selectinload(QuestionOrm.answers)
            )
            result = await session.execute(query)
            geopos_models = result.scalars().all()
            return geopos_models

    @classmethod
    async def get_only_geos(cls):
        async with new_session() as session:
            query = select(GeoPosOrm)
            result = await session.execute(query)
            geoposes = result.scalars().all()
            return geoposes

    @classmethod
    async def add_one(cls, data: SAddGeoPos):
        async with new_session() as session:
            geopos_data = data.model_dump()
            geopos = GeoPosOrm(**geopos_data)
            session.add(geopos)
            await session.flush()
            await session.commit()
            return geopos.id

    @classmethod
    async def get_random_geopos(cls, value):
        async with new_session() as session:
            stmt = (
                select(GeoPosOrm)
                .options(
                    selectinload(GeoPosOrm.questions).selectinload(QuestionOrm.answers)
                )
                .order_by(func.random())
                .limit(value)
            )
            result = await session.execute(stmt)
            geopos_models = result.scalars().all()
            return geopos_models
