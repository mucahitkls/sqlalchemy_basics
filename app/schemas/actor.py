from pydantic import BaseModel
from datetime import date


class ActorSchema(BaseModel):
    id: int
    name: str
    birthday: date

    class Config:
        orm_mode = True
