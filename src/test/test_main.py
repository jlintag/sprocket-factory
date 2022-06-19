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
    assert len(response.json()) == 3
    assert response.json() == return_hardcoded_factory_values_as_json()


def test_get_single_factory():
    expected = return_single_hardcoded_factory_value(1)
    response = client.get("/factories/1")
    result = json.dumps(response.json())
    assert response.status_code == 200
    assert result == expected


def test_get_single_sprocket():
    expected = return_sprocket_id_1()
    response = client.get("/sprockets/1")
    result = response.json()
    assert response.status_code == 200
    assert result == expected


def test_post_single_sprocket():
    response = client.post(
        "/sprockets/",
        json={"teeth": 9, "outside_diameter": 8, "pitch": 7, "pitch_diameter": 6},
    )
    result = response.json()
    assert response.status_code == 201
    assert result["teeth"] == 9
    assert result["outside_diameter"] == 8
    assert result["pitch"] == 7
    assert result["pitch_diameter"] == 6


def test_patch_single_sprocket():
    expected = return_sprocket_id_2_with_updated_values()
    response = client.patch(
        "/sprockets/2",
        json={"outside_diameter": 10, "pitch_diameter": 12},
    )
    result = response.json()
    assert response.status_code == 202
    assert result["teeth"] == expected["teeth"]
    assert result["outside_diameter"] == expected["outside_diameter"]
    assert result["pitch"] == expected["pitch"]
    assert result["pitch_diameter"] == expected["pitch_diameter"]


def test_validate_get_factories_structure():
    json_data = {"chart_data": {}}
    validate(instance=json_data, schema=get_schema())


def return_hardcoded_factory_values_as_json():
    json_as_string = '[{"chart_data":{"sprocket_production_actual":[32,29,31,30,32,32,29,31,30,32,32,29,31,30,32,32,29,31,30,32],"sprocket_production_goal":[32,30,31,29,32,32,30,31,29,32,32,30,31,29,32,32,30,31,29,32],"time":[1611194818,1611194878,1611194938,1611194998,1611195058,1611195118,1611195178,1611195238,1611195298,1611195358,1611195418,1611195478,1611195538,1611195598,1611195658,1611195718,1611195778,1611195838,1611195898,1611195958]},"id":1},{"chart_data":{"sprocket_production_actual":[32,28,31,30,30,32,29,28,30,32,32,29,31,30,31,32,29,29,33,30],"sprocket_production_goal":[31,33,29,29,32,30,30,31,29,31,31,30,28,29,32,29,30,31,28,32],"time":[1611204818,1611204878,1611204938,1611204998,1611205058,1611205118,1611205178,1611205238,1611205298,1611205358,1611205418,1611205478,1611205538,1611205598,1611205658,1611205718,1611205778,1611205838,1611205898,1611205958]},"id":2},{"chart_data":{"sprocket_production_actual":[32,29,31,30,30,32,29,29,30,32,32,29,31,30,30,32,29,29,33,31],"sprocket_production_goal":[31,31,29,30,32,30,30,31,29,31,30,30,28,29,32,29,31,31,28,32],"time":[1611304818,1611304878,1611304938,1611304998,1611305058,1611305118,1611305178,1611305238,1611305298,1611305358,1611305418,1611305478,1611305538,1611305598,1611305658,1611305718,1611305778,1611305838,1611305898,1611305958]},"id":3}]'
    return json.loads(json_as_string)


def return_single_hardcoded_factory_value(id: int):
    factories_as_json = return_hardcoded_factory_values_as_json()
    factory = [x for x in factories_as_json if x["id"] == id][0]
    return json.dumps(factory)


def return_sprocket_id_1():
    return json.loads(
        '{"id":1,"pitch_diameter":5,"pitch":1,"outside_diameter":6,"teeth":5}'
    )


def return_sprocket_id_2_with_updated_values():
    return json.loads(
        '{"id":2,"pitch_diameter":12,"pitch":1,"outside_diameter":10,"teeth":5}'
    )
