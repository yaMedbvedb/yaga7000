from fastapi import FastAPI
from pydantic import BaseModel
from agents import run_agent

app = FastAPI()

class Request(BaseModel):
    message: str

@app.post("/api/ask")
def ask(req: Request):
    result = run_agent(req.message)
    return {"response": result}
