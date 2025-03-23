import os
from datetime import datetime
from dotenv import load_dotenv
import openai
from filiais import encontrar_filial_mais_proxima, obter_dados_da_filial, filiais_massafort

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

def obter_saudacao():
    hora = datetime.now().hour
    if hora < 12:
        return "Bom dia"
    elif hora < 18:
        return "Boa tarde"
    return "Boa noite"

def mostrar_menu_inicial():
    saudacao = obter_saudacao()
    mensagem = (
        f"{saudacao}! 😊 Eu sou a MAI, assistente da *Massa Fort Concreto*.\n"
        "1️⃣ Fazer orçamento\n"
        "2️⃣ Tipos de concreto\n"
        "3️⃣ Localizar filial\n"
        "4️⃣ Falar com gerente\n\n"
        "❌ Digite 'sair' para encerrar."
    )
    conversation_history.append({"role": "assistant", "content": mensagem})

def responder_mensagem(mensagem):
    global conversation_history
    user_input = mensagem.strip()
    lower_msg = user_input.lower()
    conversation_history.append({"role": "user", "content": user_input})

    if any(k in lower_msg for k in ["cobrança", "diretoria", "reclamação", "jurídico", "juridico", "ti"]):
        resposta = (
            "📢 Para assuntos como cobrança, diretoria, jurídico, TI ou reclamações, entre em contato com nossa Matriz:\n\n"
            "📍 Av. Maria Quitéria n.1445, Feira de Santana, BA\n"
            "📧 massafort@massafort.com\n"
            "📞 (75) 3024-1111\n"
            "🕒 Atendimento: Seg-Sex, 7:30 às 18:00"
        )
        conversation_history.append({"role": "assistant", "content": resposta})
        limitar_historico()
        return resposta

    if lower_msg in ["1", "orçamento"]:
        resposta = "Claro! Me diga a cidade onde será feita a entrega do concreto. 😊"
        return resposta
    elif lower_msg in ["2", "tipos de concreto"]:
        resposta = "Trabalhamos com concreto usinado, bombeável, estrutural e mais. Posso indicar o ideal pra sua obra! 💡"
        return resposta
    elif lower_msg in ["3", "filial"]:
        resposta = "Informe a cidade e localizo a filial mais próxima. 🗺️"
        return resposta
    elif lower_msg in ["4", "gerente"]:
        resposta = "Certo! Qual cidade você está? Vou buscar o contato do gerente responsável. 🤝"
        return resposta
    elif lower_msg in ["sair", "encerrar"]:
        resposta = "Foi um prazer falar com você! Qualquer coisa, é só me chamar. 💙"
        return resposta

    try:
        openai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        resposta = openai_response.choices[0].message.content.strip()
    except Exception:
        resposta = "Desculpe, não consegui processar sua mensagem agora. Tente novamente mais tarde."

    conversation_history.append({"role": "assistant", "content": resposta})
    limitar_historico()
    return resposta

def limitar_historico():
    global conversation_history
    MAX_MSG = 12
    mensagens_uteis = conversation_history[1:]
    if len(mensagens_uteis) > MAX_MSG:
        conversation_history[:] = [conversation_history[0]] + mensagens_uteis[-MAX_MSG:]
