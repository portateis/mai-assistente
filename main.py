from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/twilio-webhook", response_class=PlainTextResponse)
async def receber_twilio(Body: str = Form(...)):
    print("📥 Mensagem recebida do WhatsApp:", Body)
    return PlainTextResponse(content="Mensagem recebida com sucesso.")
    
@app.get("/")
def root():
    return {"status": "MAI simples online"}
