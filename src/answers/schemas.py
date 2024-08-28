from pydantic import BaseModel


class SAddAnswer(BaseModel):
    text: str
    question_id: int
    is_correct: bool


class SAnswer(SAddAnswer):
    id: int

    class Config:
        orm_mode = True



