from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")
    return {"answer": f"Yaga heard the question: {question}"}
