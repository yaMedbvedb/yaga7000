from fastapi import FastAPI, Request
import base64

app = FastAPI()

def fix_mojibake(text: str) -> str:
    try:
        return text.encode("latin1").decode("utf-8")
    except Exception:
        return text

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

    if question:
        question = fix_mojibake(question)

    return {
        "answer": f"Yaga heard the question: {question}"
    }
