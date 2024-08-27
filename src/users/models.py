from sqlalchemy import Column, Integer, String

from src.application.database import Base


class UserOrm(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    tg_id = Column(Integer)
