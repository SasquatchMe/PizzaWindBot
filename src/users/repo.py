from sqlalchemy import select

from src.database import new_session
from src.users.models import UserOrm
from src.users.schemas import SAddUser, SDeleteUser, SGetUserById


class UserRepo:

    @classmethod
    async def add_one(cls, data: SAddUser):
        async with new_session() as session:
            user_dict = data.model_dump()

            user = UserOrm(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models

    @classmethod
    async def get_one(cls, data: SGetUserById):
        async with new_session() as session:
            user_id = data.model_dump()['id']
            query = select(UserOrm).where(UserOrm.id == user_id)
            result = await session.execute(query)
            user = result.scalar_one()
            return user

    @classmethod
    async def delete_user(cls, data: SDeleteUser):
        async with new_session() as session:
            user_id = data.model_dump()['id']
            query = select(UserOrm).where(UserOrm.id == user_id)
            result = await session.execute(query)
            user = result.scalars().first()
            await session.delete(user)
            await session.commit()
            return user.id


