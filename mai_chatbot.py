# mai_chatbot.py
import os
from datetime import datetime
from dotenv import load_dotenv
import openai
from filiais import encontrar_filial_mais_proxima, obter_dados_da_filial, filiais_massafort

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = [
    {
        "role": "system",
        "content": (
            "Você é MAI, a assistente virtual da MASSA FORT CONCRETO. "
            "Seja gentil, acolhedora, empática e objetiva. Interprete mensagens livres do cliente com inteligência. "
            "Forneça informações sobre orçamento, tipos de concreto, localização de filiais e contatos de gerente."
        )
    }
]

brand_info = (
    "Massa Fort Concreto: Mais de 17 Anos de Excelência na Construção\n"
    "Construindo bases sólidas para o futuro\n\n"
    "Somos referência no setor com uma rede de 27 filiais, dedicados a fornecer concreto de alta qualidade, "
    "serviços confiáveis e soluções sob medida para cada projeto."
)

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
        f"{saudacao}! 😊 Eu sou a MAI, a assistente virtual da *Massa Fort Concreto*.\n"
        f"{brand_info}\n\n"
        "Como posso te ajudar hoje?\n\n"
        "1️⃣ Fazer orçamento\n"
        "2️⃣ Saber sobre tipos de concreto\n"
        "3️⃣ Localizar filial mais próxima\n"
        "4️⃣ Falar com um gerente\n\n"
        "❌ Digite 'sair' para encerrar."
    )
    print(mensagem)
    conversation_history.append({"role": "assistant", "content": mensagem})

def responder_mensagem(mensagem):
    global conversation_history
    user_input = mensagem.strip()
    lower_msg = user_input.lower()
    conversation_history.append({"role": "user", "content": user_input})

    # Ações diretas por palavras-chave
    if any(k in lower_msg for k in ["cobrança", "diretoria", "reclamação", "jurídico", "juridico", "ti"]):
        resposta = (
            "Para assuntos como cobrança, diretoria, jurídico, TI ou reclamações, por favor entre em contato com nossa Matriz:\n\n"
            "📍 Av. Maria Quitéria n.1445, Feira de Santana, BA\n"
            "📧 massafort@massafort.com\n"
            "📞 (75) 3024-1111\n"
            "🕒 Atendimento: Seg-Sex, 7:30 às 18:00"
        )
        conversation_history.append({"role": "assistant", "content": resposta})
        return resposta

    if lower_msg in ["1", "orçamento"]:
        resposta = "Claro! Me informe a cidade onde será feita a entrega do concreto. 😊"
    elif lower_msg in ["2", "tipos de concreto"]:
        resposta = "Temos concreto usinado, bombeável, estrutural, entre outros. Quer ajuda para escolher o ideal? 💡"
    elif lower_msg in ["3", "filial"]:
        resposta = "Me diga o nome da sua cidade, e eu localizo a filial mais próxima pra você. 🗺️"
    elif lower_msg in ["4", "gerente"]:
        resposta = "Me informe a cidade para eu passar o contato do gerente responsável. 🤝"
    elif lower_msg in ["sair", "encerrar"]:
        resposta = "Foi um prazer falar com você! Se precisar, estarei por aqui. 💙"
    elif "feira de santana" in lower_msg or "salvador" in lower_msg:
        cidade_alvo = "feira de santana" if "feira de santana" in lower_msg else "salvador"
        opcoes = [nome for nome in filiais_massafort.keys() if cidade_alvo in nome.lower()]
        resposta = "Encontrei mais de uma filial nessa cidade:\n\n"
        for filial in opcoes:
            dados = filiais_massafort[filial]
            resposta += f"🏢 *{filial}*\n👤 {dados['gerente']} - 📞 https://wa.me/{dados['whatsapp_gerente']}\n\n"
    else:
        # Tenta identificar filial pela mensagem
        filial = encontrar_filial_mais_proxima(lower_msg)
        if filial:
            dados = obter_dados_da_filial(filial)
            if dados:
                resposta = (
                    f"A filial mais próxima é *{filial}*.\n"
                    f"👤 Gerente: {dados['gerente']}\n📞 WhatsApp: https://wa.me/{dados['whatsapp_gerente']}\n"
                    f"📧 E-mail: {dados['email_gerente']}\n"
                )
                conversation_history.append({"role": "assistant", "content": resposta})
                return resposta

        # Fallback: envia para OpenAI
        try:
            openai_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation_history
            )
            resposta = openai_response.choices[0].message.content.strip()
        except Exception:
            resposta = "Desculpe, não consegui processar sua mensagem agora. Tente novamente mais tarde."

    conversation_history.append({"role": "assistant", "content": resposta})
    return resposta
