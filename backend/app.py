from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="YAGA7000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "YAGA7000 online"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/ask")
def ask(req: AskRequest):
    return {
        "response": (
            f"🧠 PLAN:\nлан: {req.message}\n\n"
            f"⚙ EXECUTION:\nнализ и рассуждение.\n\n"
            f"💾 MEMORY:\nСохранено в экосистеме YAGA7000."
        )
    }
