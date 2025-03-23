from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse
from mai_chatbot import responder_mensagem, mostrar_menu_inicial, conversation_history
from fastapi.middleware.cors import CORSMiddleware

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
    resposta = responder_mensagem(Body)
    return resposta

@app.get("/")
async def root():
    return {"mensagem": "MAI Assistente Virtual - API online! Use POST /chat ou /twilio-webhook para conversar."}
