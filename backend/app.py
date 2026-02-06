from fastapi import FastAPI

app = FastAPI(
    title="YAGA7000",
    description="Автономная ИИ-платформа знаний. Бабушка Яга знает ответы.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "project": "YAGA7000",
        "message": "Бабушка Яга здесь. Задай вопрос.",
        "status": "online"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(question: str):
    return {
        "question": question,
        "answer": "Яга думает... (пока заглушка)",
        "confidence": 0.42
    }
