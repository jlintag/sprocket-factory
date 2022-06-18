from typing import List
from pydantic import BaseModel


class Factory(BaseModel):
    sprocket_production_actual: List[int]
    sprocket_production_goal: List[int]
    time: List[int]

    class Config:
        orm_mode = True


class Sprocket(BaseModel):
    teeth: int
    pitch_diameter: int
    outside_diameter: int
    pitch: int

    class Config:
        orm_mode = True
