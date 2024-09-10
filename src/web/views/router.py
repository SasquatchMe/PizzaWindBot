from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse

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
    return RedirectResponse(url="/site/questions")


@router.get("/geoposes")
async def geoposes_list(request: Request):
    geopoeses = await GeoPosRepo.get_all()
    return templates.TemplateResponse(
        "geoposes.html", {"request": request, "geoposes": geopoeses}
    )


@router.get("/questions/add")
async def questions_add_form(request: Request):
    geoposes = await GeoPosRepo.get_only_geos()
    return templates.TemplateResponse(
        "question_add.html", {"request": request, "geoposes": geoposes}
    )


@router.post("/questions/add")
async def questions_add(
    request: Request,
    questionText: str = Form(...),
    answer1: str = Form(...),
    answer2: str = Form(...),
    answer3: str = Form(...),
    answer4: str = Form(...),
    correctAnswer: int = Form(...),
    geopos_id: int = Form(...),
):

    async with new_session() as db:
        # Создание вопроса
        question = QuestionOrm(text=questionText, geopos_id=geopos_id)
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


@router.get("/geoposes/add")
async def geoposes_add_form(request: Request):
    return templates.TemplateResponse("geopose_add.html", {"request": request})


@router.post("/geoposes/add")
async def geoposes_add(
    request: Request,
    latitude: float = Form(...),
    longitude: float = Form(...),
    desc: str = Form(...),
):
    with new_session() as session:
        geopos = GeoPosOrm(
            latitude=latitude,
            longitude=longitude,
            description=desc,
        )
        session.add(geopos)
        await session.commit()

    return RedirectResponse(url="/site/geoposes", status_code=303)


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


@router.get("/questions/{question_id}/edit")
async def question_edit_form(request: Request, question_id: int):
    # Получаем вопрос и геопозиции
    question = await QuestionRepo.get_one(question_id)
    geoposes = await GeoPosRepo.get_only_geos()  # Список всех геопозиций
    return templates.TemplateResponse(
        "question_edit.html",
        {"request": request, "question": question, "geoposes": geoposes},
    )


@router.post("/questions/{question_id}/update")
async def question_update(
    request: Request,
    question_id: int,
    questionText: str = Form(...),
    answer1: str = Form(...),
    answer2: str = Form(...),
    answer3: str = Form(...),
    answer4: str = Form(...),
    correctAnswer: int = Form(...),
    geopos_id: int = Form(...),
):
    async with new_session() as db:
        # Получаем текущий вопрос
        question = await db.get(QuestionOrm, question_id)

        if not question:
            return RedirectResponse(url="/site/questions", status_code=404)

        # Обновляем текст вопроса и геопозицию
        question.text = questionText
        question.geopos_id = geopos_id

        # Сначала удаляем старые ответы
        await db.execute(
            AnswerOrm.__table__.delete().where(AnswerOrm.question_id == question_id)
        )

        # Создаем новые ответы
        answers = [answer1, answer2, answer3, answer4]
        for i, answer_text in enumerate(answers):
            is_correct = i == correctAnswer
            answer = AnswerOrm(
                text=answer_text, is_correct=is_correct, question_id=question.id
            )
            db.add(answer)

        await db.commit()

    return RedirectResponse(url=f"/site/questions/{question_id}", status_code=303)


@router.post("/questions/{question_id}")
async def delete_question(request: Request, question_id: int, method: str = Form(...)):
    if method == "DELETE":
        await QuestionRepo.delete_question(question_id)
        return RedirectResponse(url="/site/questions", status_code=303)
    return RedirectResponse(
        url=f"/site/questions/{question_id}", status_code=400
    )  # На случай ошибки


@router.post("/geoposes/{geopos_id}/delete")
async def delete_geopos(request: Request, geopos_id: int, method: str = Form(...)):
    if method == "DELETE":
        async with new_session() as db:
            geopos = await db.get(GeoPosOrm, geopos_id)
            if geopos:
                await db.delete(geopos)
                await db.commit()
                return RedirectResponse(url="/site/geoposes", status_code=303)
            return RedirectResponse(url="/site/geoposes", status_code=404)
    return RedirectResponse(url="/site/geoposes", status_code=400)  # В случае ошибки
