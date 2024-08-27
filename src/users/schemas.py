from pydantic import BaseModel



class SUser(BaseModel):
    id: int
    first_name: str
    tg_id: int


class SAddUser(BaseModel):
    first_name: str
    tg_id: int

class SDeleteUser(BaseModel):
    id: int


class SGetUserById(BaseModel):
    id: int
