# 🤖 MAI - Assistente Virtual Massa Fort Concreto

MAI é uma assistente virtual construída com **FastAPI + OpenAI**, integrada ao WhatsApp via **Twilio**.  
Ideal para atendimento humanizado e inteligente para construtoras, arquitetos e engenheiros.

---

## 🚀 Funcionalidades

- Respostas inteligentes via ChatGPT (OpenAI)
- Menu de atendimento (orçamento, filial, gerente, etc)
- Integração com WhatsApp via Twilio
- API RESTful com endpoints `/chat` e `/twilio-webhook`
- Deploy via Docker / Render

---

## 📦 Arquivos principais

| Arquivo            | Descrição                                 |
|--------------------|-------------------------------------------|
| `main.py`          | API principal com FastAPI                 |
| `mai_chatbot.py`   | Lógica da assistente MAI                  |
| `filiais.py`       | Dados das filiais (mock - substitua!)    |
| `requirements.txt` | Bibliotecas necessárias                   |
| `Dockerfile`       | Empacotamento com Docker                  |

---

## 💬 Endpoints da API

- `POST /chat`  
  Envia uma mensagem para a MAI e recebe uma resposta.

- `POST /twilio-webhook`  
  Endpoint para integrar com Twilio WhatsApp.

---

## 🛠️ Como rodar localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Ou com Docker:

```bash
docker build -t mai-assistente .
docker run -p 8080:8080 mai-assistente
```

---

## 🌍 Deploy com Render (Docker)

1. Crie um repositório no GitHub com estes arquivos
2. Vá até https://render.com
3. Crie um **Web Service** com ambiente `Docker`
4. Deploy automático será feito 🎉

---

## 📲 Integração WhatsApp (Twilio)

1. Ative o sandbox no painel da Twilio
2. No campo `WHEN A MESSAGE COMES IN`, insira:

```
https://<sua-api>.onrender.com/twilio-webhook
```

3. Envie mensagem para o número do sandbox pelo WhatsApp
4. A MAI responderá automaticamente 🤖💬

---

## 🧠 Sobre a MAI

> MAI é gentil, inteligente, objetiva e prestativa.  
> Sua linguagem é acolhedora e adaptada ao cliente final, sem parecer um robô.

---

Desenvolvido com ❤️ por [Você]
