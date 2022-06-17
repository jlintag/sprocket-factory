import json
from jsonschema import validate
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def get_schema():
    with open("src/test/schemas/factory.json", "r") as file:
        schema = json.load(file)
    return schema


def test_get_factories():
    response = client.get("/factories")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_validate_get_factories_structure():
    json_data = {"chart_data": {}}
    validate(instance=json_data, schema=get_schema())
