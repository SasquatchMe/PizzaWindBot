from fastapi import APIRouter, Depends

from src.answers.repo import AnswerRepo
from src.answers.schemas import SAddAnswer

router = APIRouter(prefix="/answers", tags=["Answers"])


@router.post('')
async def add_answer(answer: SAddAnswer = Depends(SAddAnswer)):
    answer_id = await AnswerRepo.add_one(answer)
    return {'status': True, 'answer_id': answer_id}

@router.get('')
async def get_all_answers():
    answers = await AnswerRepo.get_all()
    return {'answers': answers}

@router.delete('/{answer_id}')
async def delete_answer(answer_id: int):
    await AnswerRepo.delete_one(answer_id)
    return {'status': True}

@router.post('/add_many')
async def add_many(answers: list[SAddAnswer]):
    answers_added = await AnswerRepo.add_many(answers)
    return {"status": answers_added}
