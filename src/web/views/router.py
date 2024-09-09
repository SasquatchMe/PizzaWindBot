from fastapi import APIRouter, Request, Depends, Form
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.answers.models import AnswerOrm
from src.application.database import new_session
from src.geopos.models import GeoPosOrm
from src.geopos.repo import GeoPosRepo
from src.questions.models import QuestionOrm
from src.questions.repo import QuestionRepo

router = APIRouter(prefix="/site")

templates = Jinja2Templates(directory="src/web/templates")


@router.get("/")
async def index():
    return RedirectResponse(url="/questions")


@router.get("/questions/add")
async def questions_add(request: Request):
    return templates.TemplateResponse("question_add.html", {"request": request})


@router.post("/questions/add")
async def questions_add(
    request: Request,
    questionText: str = Form(...),
    answer1: str = Form(...),
    answer2: str = Form(...),
    answer3: str = Form(...),
    answer4: str = Form(...),
    correctAnswer: int = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
):

    async with new_session() as db:
        # Создание геопозиции
        geopos = GeoPosOrm(latitude=latitude, longitude=longitude)
        db.add(geopos)
        await db.commit()

        # Создание вопроса
        question = QuestionOrm(text=questionText, geopos_id=geopos.id)
        db.add(question)
        await db.commit()

        answers = [answer1, answer2, answer3, answer4]

        # Создание ответов
        for i, answer_text in enumerate(answers):
            is_correct = i == correctAnswer
            answer = AnswerOrm(
                text=answer_text, is_correct=is_correct, question_id=question.id
            )
            db.add(answer)
        await db.commit()

    return RedirectResponse(url="/site/questions", status_code=303)


@router.get("/questions/{question_id}")
async def question_detail(request: Request, question_id: int):
    question = await QuestionRepo.get_one(question_id)
    geopos = await GeoPosRepo.get_one(question.geopos_id)
    return templates.TemplateResponse(
        "question.html",
        {
            "request": request,
            "question": question,
            "geopos": geopos,
        },
    )


@router.get("/questions", response_class=HTMLResponse)
async def home(request: Request):
    questions = await QuestionRepo.get_all_questions()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "questions": questions,
        },
    )
