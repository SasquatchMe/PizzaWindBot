import asyncio

from fastapi import FastAPI

from src.config import settings
from src.database import create_tables
from src.users.router import router as users_router
from src.geopos.router import router as geopos_router

app = FastAPI()

app.include_router(
    users_router,
    tags=["Users"],
)
app.include_router(
    geopos_router,
    tags=["Geoposes"],
)

if __name__ == '__main__':
    asyncio.run(create_tables())
