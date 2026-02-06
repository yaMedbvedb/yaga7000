from fastapi import FastAPI
from app.core.team import AutoTeam

app = FastAPI(title="YAGA7000")

team = AutoTeam()

@app.get("/")
def root():
    return {"status": "YAGA7000 online"}

@app.post("/run")
def run(goal: str):
    return team.run(goal)
