from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from mai_chatbot import responder_mensagem, mostrar_menu_inicial, conversation_history

app = FastAPI(title="MAI - Massa Fort Assistente Virtual")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mostrar_menu_inicial()

class MensagemEntrada(BaseModel):
    mensagem: str

@app.post("/chat")
async def chat_com_mai(entrada: MensagemEntrada):
    resposta = responder_mensagem(entrada.mensagem)
    return {"resposta": resposta}

@app.post("/twilio-webhook", response_class=PlainTextResponse)
async def receber_twilio(Body: str = Form(...)):
    print("📥 Mensagem recebida do WhatsApp:", Body)
    resposta = responder_mensagem(Body)
    if not resposta or not resposta.strip():
        resposta = "Desculpe, não entendi. Pode repetir?"
    print("📤 MAI vai responder:", resposta)
    return PlainTextResponse(content=resposta)

@app.get("/")
async def root():
    return {"MAI": "online"}
