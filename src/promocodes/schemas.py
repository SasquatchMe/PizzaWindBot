from pydantic import BaseModel


class SPromocodeAdd(BaseModel):
    code: str
    corrects: int
    is_active: bool
