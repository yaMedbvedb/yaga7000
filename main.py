from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.head("/ask")
def ask_head():
    return Response(status_code=200)

@app.post("/ask")
async def ask(request: Request):
    raw = await request.body()

    #   Т
    try:
        text = raw.decode("utf-16-le")
    except UnicodeDecodeError:
        text = raw.decode("utf-8")

    data = json.loads(text)
    question = data.get("question", "")

    return {"answer": f"Yaga heard the question: {question}"}
