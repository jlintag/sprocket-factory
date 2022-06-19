from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from typing import List
from . import schema
from .models import Factory, Sprocket

import os

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def sanitize_factory_objects(factories: List[Factory]):
    return [sanitize_factory_object(var) for var in factories]


def sanitize_factory_object(factory: Factory):
    return {
        "chart_data": {
            "sprocket_production_actual": factory.sprocket_production_actual,
            "sprocket_production_goal": factory.sprocket_production_goal,
            "time": factory.time,
        },
        "id": factory.id,
    }


@app.get("/factories")
def get_factories():
    factories = db.session.query(Factory).all()
    return sanitize_factory_objects(factories)


@app.get("/factories/{factory_id}")
def get_factories(factory_id):
    factory = db.session.query(Factory).get(factory_id)
    return sanitize_factory_object(factory)


@app.get("/sprockets/{sprocket_id}")
def get_sprocket(sprocket_id):
    sprocket = db.session.query(Sprocket).get(sprocket_id)
    return sprocket


@app.post("/sprockets/", status_code=201, response_model=schema.Sprocket)
def post_sprocket(sprocket: schema.SprocketCreate):
    db_sprocket = Sprocket(
        teeth=sprocket.teeth,
        pitch_diameter=sprocket.pitch_diameter,
        outside_diameter=sprocket.outside_diameter,
        pitch=sprocket.pitch,
    )
    db.session.add(db_sprocket)
    db.session.commit()
    db.session.refresh(db_sprocket)
    return db_sprocket


@app.patch("/sprockets/{sprocket_id}", status_code=202, response_model=schema.Sprocket)
def patch_sprocket(sprocket_id: int, sprocket: schema.SprocketUpdate):
    stored_sprocket = db.session.query(Sprocket).get(sprocket_id)
    for key, value in vars(sprocket).items():
        setattr(stored_sprocket, key, value) if value else None

    db.session.add(stored_sprocket)
    db.session.commit()
    db.session.refresh(stored_sprocket)

    return stored_sprocket
