from pydantic import BaseModel

from src.answers.schemas import SAnswer
from src.questions.schemas import SQuestion


class SAddGeoPos(BaseModel):
    latitude: float
    longitude: float
    description: str | None = None

class SGeoPos(SAddGeoPos):
    id: int

    questions: SQuestion | None = None

