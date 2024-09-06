from pydantic import BaseModel

from src.answers.schemas import SAnswer


class SAddQuestion(BaseModel):
    text: str
    geopos_id: int


class SQuestion(SAddQuestion):
    id: int
    answers: list[SAnswer] = []

    class Config:
        orm_mode = True
