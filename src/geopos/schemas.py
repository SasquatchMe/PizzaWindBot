from pydantic import BaseModel


class SAddGeoPos(BaseModel):
    longitude: float
    latitude: float
    description: str | None = None

class SGeoPos(SAddGeoPos):
    id: int

