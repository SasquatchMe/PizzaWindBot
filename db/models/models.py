from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL
from sqlalchemy import Column, Integer, String, Engine

import asyncio

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)




