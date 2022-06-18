from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from .schema import Factory as SchemaFactory
from .schema import Sprocket as SchemaSprocket

from .schema import Factory
from .schema import Sprocket

from .models import Factory as ModelFactory
from .models import Sprocket as ModelSprocket

import os

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


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
    factories = db.session.query(ModelFactory).all()
    return [sanitize_factory_object(var) for var in factories]
