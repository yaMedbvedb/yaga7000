from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import base64

app = FastAPI()

# ✅ равильный CORS без credentials
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()

    question = None

    if "question_b64" in data:
        question = base64.b64decode(data["question_b64"]).decode("utf-8")
    elif "question" in data:
        question = data["question"]

    return {
        "answer": f"Яга услышала: {question}"
    }
