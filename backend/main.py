from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "YAGA7000 ONLINE"}
