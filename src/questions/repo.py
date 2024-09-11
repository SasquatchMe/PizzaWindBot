from typing import Any

from sqlalchemy import select, Result, func
from sqlalchemy.orm import selectinload

from src.application.database import new_session
from src.geopos.models import GeoPosOrm
from src.questions.models import QuestionOrm
from src.questions.schemas import SAddQuestion


class QuestionRepo:

    @classmethod
    async def get_all_questions(cls):
        async with new_session() as session:
            query = select(QuestionOrm).options(selectinload(QuestionOrm.answers))
            result: Result[Any] = await session.execute(query)
            questions_models = result.scalars().all()
            return questions_models

    @classmethod
    async def add_question(cls, data: SAddQuestion):
        async with new_session() as session:
            question_data = data.model_dump()
            question: QuestionOrm = QuestionOrm(**question_data)
            session.add(question)
            await session.flush()
            await session.commit()
            return question.id

    @classmethod
    async def get_one(cls, question_id):
        async with new_session() as session:
            query = (
                select(QuestionOrm)
                .options(selectinload(QuestionOrm.answers))
                .where(QuestionOrm.id == question_id)
            )
            result: Result[Any] = await session.execute(query)
            question = result.scalars().first()
            return question

    @classmethod
    async def delete_question(cls, question_id):
        async with new_session() as session:
            query = select(QuestionOrm).where(QuestionOrm.id == question_id)
            result: Result[Any] = await session.execute(query)
            question = result.scalars().first()
            await session.delete(question)
            await session.commit()
            return question.id

    @classmethod
    async def get_random_questions(cls, value: int):
        async with new_session() as session:
            query = (
                select(QuestionOrm)
                .options(
                    selectinload(QuestionOrm.answers), selectinload(QuestionOrm.geopos)
                )
                .order_by(func.random())
                .limit(value)
            )

            result: Result[Any] = await session.execute(query)
            questions = result.scalars().all()
            return questions
