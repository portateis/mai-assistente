# 🤖 MAI - Assistente Virtual Massa Fort

Assistente virtual construída com **FastAPI**, integrada à **OpenAI** e pronta para usar com **Twilio WhatsApp API**.

---

## 🚀 Funcionalidades

- Atende clientes via WhatsApp (Twilio)
- Responde com empatia e inteligência (GPT-3.5)
- Localiza filiais com base na cidade
- Encaminha para gerente responsável
- Fallback para IA quando necessário

---

## 📦 Estrutura do Projeto

```
mai-assistente/
│
├── main.py               # API FastAPI com endpoints /chat e /twilio-webhook
├── mai_chatbot.py        # Lógica da assistente MAI
├── filiais.py            # Módulo para buscar dados das filiais
├── requirements.txt      # Dependências
├── Dockerfile            # Container Docker
└── README.md             # Instruções e documentação
```

---

## 🛠️ Requisitos

- Python 3.11+
- Conta OpenAI com API Key (`OPENAI_API_KEY`)
- Conta Twilio com sandbox WhatsApp
- GitHub e Render.com para deploy

---

## 🧪 Teste local

1. Crie um `.env` com sua chave:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode local:

```bash
uvicorn main:app --reload
```

---

## ☁️ Deploy no Render

1. Crie um repositório no GitHub
2. Faça upload de todos os arquivos
3. No Render:
   - Crie um novo **Web Service**
   - Link com seu repositório
   - Adicione a variável `OPENAI_API_KEY` nas **Environment Variables**
4. Deploy automático será iniciado

---

## 💡 Dica: Atualizar o repositório no GitHub

### Opção 1: Substituir arquivos (simples)
- Vá no repositório → "Add file" → "Upload files"
- Arraste todos os novos arquivos
- O GitHub vai sobrescrever os antigos

### Opção 2: Limpeza completa (recomendada)
- Delete os arquivos antigos diretamente no GitHub
- Depois envie os arquivos atualizados

---

## 💬 Suporte

Para dúvidas, melhorias ou integração com banco de dados, dashboards e relatórios, entre em contato com o desenvolvedor.

---

Feito com ❤️ para o time Massa Fort.
