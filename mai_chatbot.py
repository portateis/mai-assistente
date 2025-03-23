import os
from datetime import datetime
from dotenv import load_dotenv
import openai

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation_history = [
    {
        "role": "system",
        "content": (
            "Você é MAI, a assistente virtual da MASSA FORT CONCRETO. "
            "Seja gentil, acolhedora, objetiva, profissional e empática. "
            "Entenda mensagens livres do cliente, mesmo fora do menu. "
            "Ofereça informações sobre orçamento, filiais, gerentes e tipos de concreto."
        )
    }
]

def mostrar_menu_inicial():
    mensagem = (
        "Olá! 😊 Eu sou a MAI, assistente da *Massa Fort Concreto*.
"
        "1️⃣ Fazer orçamento
"
        "2️⃣ Tipos de concreto
"
        "3️⃣ Localizar filial
"
        "4️⃣ Falar com gerente

"
        "❌ Digite 'sair' para encerrar."
    )
    conversation_history.append({"role": "assistant", "content": mensagem})

def responder_mensagem(mensagem):
    user_input = mensagem.strip()
    conversation_history.append({"role": "user", "content": user_input})

    try:
        resposta_api = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        resposta = resposta_api.choices[0].message.content.strip()
    except Exception:
        resposta = "Desculpe, não consegui responder agora. Tente novamente em instantes."

    conversation_history.append({"role": "assistant", "content": resposta})
    if len(conversation_history) > 12:
        conversation_history[:] = [conversation_history[0]] + conversation_history[-10:]
    return resposta
