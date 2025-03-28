from fastapi import FastAPI, Request
from mai_chatbot import responder_mensagem
import json

app = FastAPI()

@app.post("/twilio-webhook")
async def webhook(request: Request):
    data = await request.json()
    mensagem = data.get("Body", "").strip()
    resposta = responder_mensagem(mensagem)
    return {"resposta": resposta}
