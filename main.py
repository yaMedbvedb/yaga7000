from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

def fix_encoding(text: str) -> str:
    try:
        return text.encode("latin1").decode("utf-8")
    except Exception:
        return text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.head("/ask")
def ask_head():
    return Response(status_code=200)

@app.post("/ask")
def ask(q: Question):
    fixed = fix_encoding(q.question)
    return {"answer": f"Yaga heard the question: {fixed}"}
