from sqlalchemy import select

from src.application.database import new_session
from src.geopos.models import GeoPosOrm
from src.geopos.schemas import SAddGeoPos, SGeoPos


class GeoPosRepo:

    @classmethod
    async def get_one(cls, data: SGeoPos):
        async with new_session() as session:
            geopos_data = data.model_dump()
            geopos_id = geopos_data['id']

            query = select(GeoPosOrm).where(GeoPosOrm.id == geopos_id)
            result = await session.execute(query)
            geopos = result.scalar_one()
            return geopos

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(GeoPosOrm)
            result = await session.execute(query)
            geopos_models = result.scalars().all()
            return geopos_models

    @classmethod
    async def add_one(cls, data: SAddGeoPos):
        async with new_session() as session:
            geopos_data = data.model_dump()
            geopos = GeoPosOrm(**geopos_data)
            session.add(geopos)
            await session.flush()
            await session.commit()
            return geopos.id

