from fastapi import FastAPI, Request

app = FastAPI()

def fix_mojibake(text: str) -> str:
    try:
        # если текст был прочитан как latin1 вместо utf-8
        return text.encode("latin1").decode("utf-8")
    except Exception:
        return text

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    question = fix_mojibake(question)

    return {"answer": f"Yaga heard the question: {question}"}
