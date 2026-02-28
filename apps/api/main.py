from core import hello
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/health")
def read_root():
    return {"status": "healthy"}


@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": hello(name)}


def dev():
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)


def start():
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
