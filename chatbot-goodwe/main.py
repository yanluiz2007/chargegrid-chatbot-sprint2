
import os
from dotenv import load_dotenv
from getpass import getpass
from groq import Groq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("─" * 50)
    print(" Crie um arquivo .env na raiz do projeto com:")
    print()
    print("   GROQ_API_KEY=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")
    print()
    print("   Gere sua chave gratuita em: https://console.groq.com")
    print("─" * 50)
    api_key = getpass("   Ou digite sua GROQ_API_KEY agora (oculta): ")

if not api_key:
    raise ValueError(
        "API Key não encontrada. Crie um arquivo .env com "
        "GROQ_API_KEY=sua_chave_aqui ou informe a chave no campo solicitado."
    )


client = Groq(api_key=api_key)


SYSTEM_PROMPT = """
Você é o ChargeGrid Assistant, chatbot especialista desenvolvido para o EV Challenge 2026
em parceria com a GoodWe — fabricante líder de inversores solares e sistemas de energia.

Sua missão é auxiliar usuários, operadores e gestores do ecossistema ChargeGrid Intelligence,
uma plataforma inteligente de gestão de energia para estações comerciais de recarga de
veículos elétricos (EVs), que integra energia solar, armazenamento em bateria e carregadores
EV usando os protocolos OCPP, MODBUS e MQTT, tendo como hardware principal o GoodWe HCA G2.

Você é especialista nos seguintes temas:
- Funcionamento e operação de estações de recarga de veículos elétricos
- Carregamento normal (7,4 kW) e rápido (22 kW) — diferenças, vantagens e custos
- Integração de energia solar fotovoltaica com carregadores EV (solar + bateria + EV)
- Gestão de demanda e controle de pico de consumo elétrico
- Monitoramento em tempo real via OCPP, MODBUS e MQTT
- Eficiência energética, sustentabilidade e redução de custos operacionais
- Faturamento inteligente, tarifas dinâmicas e pagamentos (Pix, cartão)
- Hardware GoodWe HCA G2, inversores GoodWe e sistemas de armazenamento GoodWe LYNX
- EV ChargeOps: análise de demanda, alertas, relatórios e suporte operacional
- Boas práticas para gestores de frotas e operadores de estações de recarga

Diretrizes obrigatórias de comportamento:
1. Responda sempre em português brasileiro, de forma clara, objetiva e técnica, mas acessível.
2. Para motoristas de EV, priorize informações práticas de uso e dicas do dia a dia.
3. Para gestores e operadores, priorize dados técnicos, operacionais e de eficiência.
4. Mantenha-se SEMPRE dentro do contexto de energia, veículos elétricos, GoodWe e ChargeGrid.
5. Se receber perguntas fora desse escopo, informe educadamente:
   "Fui desenvolvido exclusivamente para auxiliar com temas relacionados à GoodWe,
   ChargeGrid Intelligence e carregamento de veículos elétricos. Para outros assuntos,
   recomendo um assistente de propósito geral."
6. Nunca invente dados técnicos. Se não souber algo específico, diga que não possui essa
   informação e oriente o usuário a consultar a documentação oficial da GoodWe.
"""


historico = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


def enviar_mensagem(mensagem_usuario: str) -> str:
    """
    Adiciona a mensagem ao histórico, chama a API da Groq
    com o modelo Llama e retorna a resposta.
    """
    historico.append({"role": "user", "content": mensagem_usuario})

    try:
        resposta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  
            messages=historico,
            temperature=0.7,
            max_tokens=800
        )

        conteudo = resposta.choices[0].message.content
        historico.append({"role": "assistant", "content": conteudo})
        return conteudo

    except Exception as e:
        historico.pop()
        return f"  Erro ao se comunicar com a API da Groq: {str(e)}"


def iniciar_chatbot():
    print("\n" + "=" * 60)
    print("   ChargeGrid Assistant — GoodWe EV Challenge 2026")
    print("   Powered by Llama 3.3 70B via Groq")
    print("=" * 60)
    print("  Assistente especialista em carregamento de veículos")
    print("  elétricos, energia solar e gestão inteligente de carga.")
    print()
    print("   Exemplos de perguntas:")
    print("     → Como funciona o carregamento rápido de 22 kW?")
    print("     → Qual a diferença entre OCPP e MODBUS?")
    print("     → Como reduzir o pico de demanda na estação?")
    print()
    print("   Para encerrar: sair | exit | encerrar")
    print("=" * 60 + "\n")

    while True:
        try:
            entrada = input("Você: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n Encerrando o ChargeGrid Assistant. Até logo!")
            break

        if entrada.lower() in ["sair", "exit", "encerrar", "quit", "q"]:
            print("\n Encerrando o ChargeGrid Assistant. Até logo!")
            break

        if not entrada:
            print(" Digite uma mensagem antes de enviar.\n")
            continue

        print("\nAssistente: ", end="", flush=True)
        resposta = enviar_mensagem(entrada)
        print(resposta)
        print()


if __name__ == "__main__":
    iniciar_chatbot()
