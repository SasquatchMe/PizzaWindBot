from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.answers.router import router as answers_router
from src.geopos.router import router as geopos_router
from src.questions.router import router as questions_router
from src.users.router import router as users_router
from src.web.views.router import router as pages_router
from src.promocodes.router import router as promocodes_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="PizzaWindBot",
        docs_url="/api/docs",
        description="A simple FastAPI + async SQLAlchemy + aiogram application",
        debug=False,
    )

    app.mount(
        "/static",
        StaticFiles(directory="src/web/static"),
        name="static",
    )

    app.include_router(
        users_router,
        tags=["Users"],
    )
    app.include_router(
        geopos_router,
        tags=["Geoposes"],
    )
    app.include_router(
        questions_router,
    )

    app.include_router(
        answers_router,
    )

    app.include_router(
        pages_router,
    )
    app.include_router(
        promocodes_router,
    )
    return app
