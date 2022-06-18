from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ARRAY

Base = declarative_base()


class Factory(Base):
    __tablename__ = "chartdata"
    id = Column(Integer, primary_key=True, index=True)
    sprocket_production_actual = Column(ARRAY(Integer))
    sprocket_production_goal = Column(ARRAY(Integer))
    time = Column(ARRAY(Integer))


class Sprocket(Base):
    __tablename__ = "sprockets"
    id = Column(Integer, primary_key=True, index=True)
    teeth = Column(Integer)
    pitch_diameter = Column(Integer)
    outside_diameter = Column(Integer)
    pitch = Column(Integer)
