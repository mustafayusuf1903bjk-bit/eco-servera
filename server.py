from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "Eco server çalışıyor 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Kısa, net ve Türkçe cevap ver."},
            {"role": "user", "content": req.text}
        ]
    )
    return {"reply": response.choices[0].message.content}
