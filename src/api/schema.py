from typing import List, Optional
from pydantic import BaseModel


class FactoryBase(BaseModel):
    sprocket_production_actual: List[int]
    sprocket_production_goal: List[int]
    time: List[int]


class FactoryCreate(FactoryBase):
    pass


class Factory(FactoryBase):
    id: int

    class Config:
        orm_mode = True


class SprocketBase(BaseModel):
    teeth: int
    pitch_diameter: int
    outside_diameter: int
    pitch: int


class SprocketCreate(SprocketBase):
    pass


class SprocketUpdate(BaseModel):
    id: Optional[int]
    teeth: Optional[int]
    pitch_diameter: Optional[int]
    outside_diameter: Optional[int]
    pitch: Optional[int]

    class Config:
        orm_mode = True


class Sprocket(SprocketBase):
    id: int

    class Config:
        orm_mode = True
