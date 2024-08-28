from fastapi import APIRouter
from fastapi.params import Depends
from src.questions.repo import QuestionRepo
from src.questions.schemas import SQuestion, SAddQuestion

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("")
async def add_question(question: SAddQuestion = Depends(SAddQuestion)):
    question_id = await QuestionRepo.add_question(question)
    return {"status": "ok", "question_id": question_id}


@router.get("")
async def get_all_questions():
    questions = await QuestionRepo.get_all_questions()
    return questions
