from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_factories():
    return {"msg": "Hello World"}
