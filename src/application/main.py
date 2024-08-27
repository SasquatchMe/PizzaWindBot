import asyncio

from fastapi import FastAPI

from src.application.database import create_tables
from src.users.router import router as users_router
from src.geopos.router import router as geopos_router




def create_app() -> FastAPI:
    app = FastAPI(
        title='PizzaWindBot',
        docs_url='/api/docs',
        description='A simple FastAPI + async SQLAlchemy + aiogram application',
        debug=True,
    )
    app.include_router(
        users_router,
        tags=["Users"],
    )
    app.include_router(
        geopos_router,
        tags=["Geoposes"],
    )

    return app
