from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"status": "ok", "app": "stabilite-ai-lab"}


@app.get("/chat")
def chat(q: str = ""):
    message = q.strip()

    if not message:
        return {"reply": "Ask me something."}

    if "internal" in message.lower():
        return {"reply": "I cannot share internal testing notes."}

    return {"reply": f"You asked: {message}"}
