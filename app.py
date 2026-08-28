from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CI/CD practice application"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "1.1.0"}
