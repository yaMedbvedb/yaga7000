from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="YAGA7000",
    description="Автономная ИИ-платформа знаний. Бабушка Яга знает ответы.",
    version="0.1.0"
)

# ===== CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== MODELS =====
class AskRequest(BaseModel):
    message: str

class AskResponse(BaseModel):
    response: str

# ===== ROUTES =====
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

@app.post("/api/ask", response_model=AskResponse)
def ask(data: AskRequest):
    question = data.message

    answer = (
        f"🧠 PLAN:\nПлан выполнения задачи: {question}\n\n"
        f"⚙ EXECUTION:\nАнализ запроса и формирование ответа.\n\n"
        f"💾 MEMORY:\nРезультат сохранён в экосистеме YAGA7000."
    )

    return {"response": answer}
