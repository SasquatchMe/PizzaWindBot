from sqlalchemy import select
from sqlalchemy.util import await_only

from src.application.database import new_session
from src.promocodes.models import PromocodeORM
from src.promocodes.schemas import SPromocodeAdd
from src.questions.models import QuestionOrm
from src.questions.repo import QuestionRepo


class PromocodesRepo:

    @classmethod
    async def get_one_by_code(cls, code: str):
        async with new_session() as session:
            stmt = select(PromocodeORM).where(PromocodeORM.code == code)

            result = await session.execute(stmt)

            promocode = result.scalar_one_or_none()

            if promocode:
                return promocode
            return None

    @classmethod
    async def add_one(cls, data: SPromocodeAdd):
        async with new_session() as session:
            promocode_data = data.model_dump()
            promocode = PromocodeORM(**promocode_data)
            session.add(promocode)
            await session.flush()
            await session.commit()
            return promocode.id

    @classmethod
    async def deactivate_promocode(cls, promocode_id):
        async with new_session() as session:
            # Выполняем запрос для получения объекта промокода
            stmt = select(PromocodeORM).where(PromocodeORM.id == promocode_id)
            result = await session.execute(stmt)
            promocode = result.scalar_one_or_none()

            if promocode:
                # Меняем значение поля is_active
                promocode.is_active = False
                # Сохраняем изменения
                await session.commit()
                return promocode

            return None
