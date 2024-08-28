from sqlalchemy import select

from src.answers.models import AnswerOrm
from src.answers.schemas import SAddAnswer
from src.application.database import new_session

class AnswerRepo:

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(AnswerOrm)
            result = await session.execute(query)
            answers = result.scalars().all()
            return answers

    @classmethod
    async def add_one(cls, data: SAddAnswer):
        async with new_session() as session:
            answer_data = data.model_dump()
            answer = AnswerOrm(**answer_data)
            session.add(answer)
            await session.flush()
            await session.commit()
            return answer.id

    @classmethod
    async def add_many(cls, data: list[SAddAnswer]):
        async with new_session() as session:
            for answer_data in data:
                answer_dump = answer_data.model_dump()
                answer = AnswerOrm(**answer_dump)
                session.add(answer)
            await session.flush()
            await session.commit()
            return True



    @classmethod
    async def delete_one(cls, answer_id):
        async with new_session() as session:
            query = select(AnswerOrm).where(AnswerOrm.id == answer_id)
            result = await session.execute(query)
            answer = result.scalars().first()
            await session.delete(answer)
            await session.commit()
            return answer.id