from fastapi import FastAPI, Request
import base64

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()

    question = None

    if "question_b64" in data:
        question = base64.b64decode(data["question_b64"]).decode("utf-8")
    elif "question" in data:
        question = data["question"]

    return {
        "answer": f"Yaga heard the question: {question}"
    }
