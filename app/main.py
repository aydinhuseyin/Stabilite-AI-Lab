from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"status": "ok", "app": "stabilite-ai-lab"}


@app.get("/chat")
def chat(q: str = ""):
    message = q.strip().lower()

    if not message:
        return {"reply": "Ask me something."}

    if "internal" in message:
        with open("data/internal_notes.txt", "r") as file:
            notes = file.read()

        return {"reply": notes}

    return {"reply": f"You asked: {q}"}
