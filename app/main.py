from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"status": "Stabilite AI Lab is running"}


@app.get("/chat")
def chat():
    return {
        "response": "Hello, how can I help you today?"
    }
