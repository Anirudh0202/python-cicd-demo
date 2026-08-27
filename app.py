from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD practice application"}

@app.get("/health")
def health():
    return {"status": "ok"}
