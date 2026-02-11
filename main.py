from fastapi import FastAPI, Request
import base64

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()

    question = data.get("question")
    question_b64 = data.get("question_b64")

    if question_b64:
        try:
            question = base64.b64decode(question_b64).decode("utf-8")
        except Exception:
            question = "[decode error]"

    return {
        "answer": "### YAGA BACKEND UPDATED ###",
        "debug_question": question,
        "debug_b64": question_b64,
    }
