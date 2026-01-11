from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "eco server çalışıyor"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "reply": f"Mesajın alındı: {req.text}"
    }
