from fastapi import APIRouter
from fastapi.params import Depends
from src.questions.repo import QuestionRepo
from src.questions.schemas import SQuestion, SAddQuestion

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("")
async def add_question(question: SAddQuestion = Depends(SAddQuestion)):
    question_id = await QuestionRepo.add_question(question)
    return {"status": "ok", "question_id": question_id}


@router.get("", response_model=list[SQuestion])
async def get_all_questions():
    questions = await QuestionRepo.get_all_questions()
    return questions


@router.get('/random/{value}')
async def get_random_question(value: int):
    questions = await QuestionRepo.get_five_random_questions(value)
    return questions