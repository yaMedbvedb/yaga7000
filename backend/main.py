from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="YAGA7000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "YAGA7000 online"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/ask")
def ask(data: dict):
    message = data.get("message", "")
    return {
        "response": f"🧙‍♀️ Яга услышала: {message}"
    }
