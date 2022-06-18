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


@app.get("/factories")
def get_factories():
    factories = db.session.query(ModelFactory).all()
    return factories
