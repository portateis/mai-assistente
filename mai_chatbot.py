import json

with open("data/filiais.json", "r", encoding="utf-8") as f:
    base_filiais = json.load(f)

def responder_mensagem(mensagem: str) -> str:
    mensagem = mensagem.lower()
    if "filial" in mensagem or "endereços" in mensagem:
        resposta = "Temos filiais nas seguintes cidades:\n"
        resposta += "\n".join([cidade['cidade'] for cidade in base_filiais])
        return resposta
    return "Olá! Eu sou a MAI, assistente da Massa Fort. Como posso te ajudar hoje?"
