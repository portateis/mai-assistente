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

brand_info = (
    "Massa Fort Concreto: Mais de 17 Anos de Excelência na Construção\n"
    "Construindo bases sólidas para o futuro\n\n"
    "Somos referência no setor com uma rede de 27 filiais, fornecendo concreto de alta qualidade, "
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
        f"{saudacao}! 😊 Eu sou a MAI, assistente da *Massa Fort Concreto*.\n"
        f"{brand_info}\n\n"
        "Como posso te ajudar hoje?\n\n"
        "1️⃣ Fazer orçamento\n"
        "2️⃣ Tipos de concreto\n"
        "3️⃣ Localizar filial\n"
        "4️⃣ Falar com gerente\n\n"
        "❌ Digite 'sair' para encerrar."
    )
    print(mensagem)
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
        return resposta

    if lower_msg in ["1", "orçamento"]:
        return "Claro! Me diga a cidade onde será feita a entrega do concreto. 😊"
    elif lower_msg in ["2", "tipos de concreto"]:
        return "Trabalhamos com concreto usinado, bombeável, estrutural e mais. Posso indicar o ideal pra sua obra! 💡"
    elif lower_msg in ["3", "filial"]:
        return "Informe a cidade e localizo a filial mais próxima. 🗺️"
    elif lower_msg in ["4", "gerente"]:
        return "Certo! Qual cidade você está? Vou buscar o contato do gerente responsável. 🤝"
    elif lower_msg in ["sair", "encerrar"]:
        return "Foi um prazer falar com você! Qualquer coisa, é só me chamar. 💙"

    if "feira de santana" in lower_msg or "salvador" in lower_msg:
        cidade_alvo = "feira de santana" if "feira de santana" in lower_msg else "salvador"
        opcoes = [nome for nome in filiais_massafort.keys() if cidade_alvo in nome.lower()]
        resposta = "Encontrei mais de uma filial nessa cidade:\n\n"
        for filial in opcoes:
            dados = filiais_massafort[filial]
            resposta += f"🏢 *{filial}*\n👤 {dados['gerente']} - 📞 https://wa.me/{dados['whatsapp_gerente']}\n\n"
        conversation_history.append({"role": "assistant", "content": resposta})
        return resposta

    filial = encontrar_filial_mais_proxima(lower_msg)
    if filial:
        dados = obter_dados_da_filial(filial)
        if dados:
            resposta = (
                f"A filial mais próxima é *{filial}*.\n"
                f"👤 Gerente: {dados['gerente']}\n"
                f"📞 WhatsApp: https://wa.me/{dados['whatsapp_gerente']}\n"
                f"📧 E-mail: {dados['email_gerente']}"
            )
            conversation_history.append({"role": "assistant", "content": resposta})
            return resposta

    try:
        openai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        resposta = openai_response.choices[0].message.content.strip()
    except Exception as e:
        resposta = "Desculpe, não consegui processar sua mensagem agora. Tente novamente mais tarde."

    conversation_history.append({"role": "assistant", "content": resposta})
    return resposta
