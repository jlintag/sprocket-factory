from fastapi import FastAPI

app = FastAPI()

@app.get("/factories")
def get_factories():
    return {"msg": "Hello World"}
