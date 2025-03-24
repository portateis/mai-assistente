from fastapi import FastAPI, Request, Form
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from mai_chatbot import responder_mensagem, mostrar_menu_inicial

app = FastAPI()

# Permitir chamadas de qualquer origem (útil pra debug/testes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "mensagem": "MAI Assistente Virtual - API online! Use POST /chat ou /twilio-webhook para conversar."
    }

@app.post("/chat")
async def chat(request: Request):
    dados = await request.json()
    mensagem_usuario = dados.get("mensagem", "")
    resposta = responder_mensagem(mensagem_usuario)
    return {"resposta": resposta}

@app.post("/twilio-webhook", response_class=PlainTextResponse)
async def twilio_webhook(Body: str = Form(...), From: str = Form(...)):
    print(f"📥 Mensagem recebida do WhatsApp: {Body}")
    
    if Body.strip().lower() == "menu":
        resposta_final = mostrar_menu_inicial()
    else:
        resposta_final = responder_mensagem(Body)

    print(f"📤 MAI vai responder: {resposta_final}")
    return PlainTextResponse(resposta_final)
