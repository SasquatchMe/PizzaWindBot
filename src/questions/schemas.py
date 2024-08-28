from pydantic import BaseModel

from src.geopos.schemas import SGeoPos


class SAddQuestion(BaseModel):
    text: str
    geopos_id: int

class SQuestion(SAddQuestion):
    id: int
    geopos: SGeoPos

    class Config:
        orm_mode = True

