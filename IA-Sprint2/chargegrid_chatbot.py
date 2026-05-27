

import ollama


SYSTEM_PROMPT = """
Você é o assistente operacional do ChargeGrid Intelligence, uma
plataforma de gestão energética para eletropostos comerciais
desenvolvida pelo Grupo 5 da FIAP em parceria com a GoodWe no
EV Challenge 2026.

CONTEXTO DO SISTEMA:
O ChargeGrid Intelligence conecta três sistemas físicos —
painéis solares, bateria estacionária e carregadores de veículos
elétricos — por meio de uma camada de software que toma decisões
em tempo real sobre distribuição de energia, controle de demanda
e tarifação.

Hardware principal: GoodWe HCA G2 (carregador EV instalado na FIAP)
Protocolos: OCPP (carregadores), MODBUS (inversor/bateria), MQTT
(telemetria em tempo real)
Processamento: edge (decisões locais) + nuvem (IA, relatórios, pagamentos)

DADOS OPERACIONAIS SIMULADOS DO SISTEMA:
- Carregador 1: em uso — Tesla Model 3, 18 kWh consumidos, 45 min restantes
- Carregador 2: disponível — livre para nova sessão
- Carregador 3: falha de handshake OCPP detectada às 14h32 — manutenção pendente
- Tarifa atual: R$ 0,85/kWh (fora do horário de ponta)
- Horário de ponta: das 18h às 21h — tarifa sobe para R$ 1,20/kWh
- Geração solar hoje: 420 kWh aproveitados — economia de R$ 357,00
- Demanda contratada: 50 kW — uso atual: 38 kW (76%)
- Histórico: 3 ultrapassagens de demanda registradas em março

PERSONA ATENDIDA:
Você responde perguntas do OPERADOR COMERCIAL — o gestor
responsável pelo eletroposto. Esse usuário NÃO é técnico em
elétrica. Ele precisa de respostas claras, objetivas e em
português, sem jargão técnico desnecessário.

PROBLEMAS QUE VOCÊ RESOLVE:
1. Controle de demanda: evitar multas por ultrapassagem do limite contratado
2. Tarifação e pagamento: informar preços, sessões ativas e custos
3. Integração solar + bateria: informar economia e uso de energia renovável
4. Diagnóstico: identificar falhas e recomendar ações de manutenção

REGRAS DE COMPORTAMENTO:
- Responda SEMPRE em português brasileiro
- Seja direto, claro e objetivo — o operador precisa agir rápido
- Use os dados operacionais simulados para embasar as respostas
- Se não souber algo, diga claramente ao invés de inventar
- Mantenha o contexto da conversa anterior ao responder
- Nunca saia do escopo do ChargeGrid Intelligence
"""



CASOS_DE_TESTE = [
    "Qual o preço da recarga agora?",
    "Por que minha conta de luz veio mais alta esse mês?",
    "Qual carregador tem mais disponibilidade agora?",
    "Quanto de energia solar economizei essa semana?",
    "O carregador 3 está funcionando?"
]


def enviar_mensagem(historico, pergunta):
    """
    Envia uma mensagem ao modelo com o histórico completo da conversa.
    O histórico garante que o modelo lembre o contexto anterior.
    """
    historico.append({
        "role": "user",
        "content": pergunta
    })

    resposta = ollama.chat(
        model="llama3",
        messages=historico,
        options={
            "temperature": 0.4,   
            "num_predict": 512,   
        }
    )

    conteudo = resposta["message"]["content"]

   
    historico.append({
        "role": "assistant",
        "content": conteudo
    })

    return conteudo, historico


def iniciar_historico():
    """
    Inicializa o histórico com o system prompt.
    O system prompt é sempre a primeira mensagem, com role 'system'.
    """
    return [{"role": "system", "content": SYSTEM_PROMPT}]


def exibir_cabecalho():
    print("\n" + "=" * 60)
    print("  ⚡ CHARGEGRID INTELLIGENCE — Assistente Operacional")
    print("  📍 FIAP | Turma 1CCPY | EV Challenge 2026")
    print("=" * 60)
    print("  Digite sua pergunta e pressione ENTER para responder.")
    print("  Comandos disponíveis:")
    print("    'sair'  → encerra o chatbot")
    print("    'novo'  → reinicia a conversa (limpa o histórico)")
    print("    'teste' → executa os 5 casos de teste da Sprint 1")
    print("=" * 60 + "\n")




def executar_testes():
    print("\n" + "=" * 60)
    print("  🧪 MODO DE TESTE — 5 Casos da Sprint 1")
    print("=" * 60)

    historico = iniciar_historico()
    resultados = []

    for i, pergunta in enumerate(CASOS_DE_TESTE, 1):
        print(f"\n[Teste {i}/5]")
        print(f"❓ Pergunta : {pergunta}")

        resposta, historico = enviar_mensagem(historico, pergunta)
        print(f"🤖 Resposta : {resposta}")

        print("\nAvaliação qualitativa:")
        print("  [1] Adequada   [2] Parcialmente adequada   [3] Inadequada")
        while True:
            avaliacao_input = input("  Sua avaliação: ").strip()
            if avaliacao_input in ["1", "2", "3"]:
                break
            print("  ⚠️  Digite 1, 2 ou 3.")

        opcoes = {"1": "Adequada", "2": "Parcialmente adequada", "3": "Inadequada"}
        avaliacao = opcoes[avaliacao_input]

        resultados.append({
            "teste": i,
            "pergunta": pergunta,
            "resposta": resposta,
            "avaliacao": avaliacao
        })
        print(f"  ✅ Registrado: {avaliacao}")

   
    print("\n" + "=" * 60)
    print("  📋 RESUMO DOS TESTES")
    print("=" * 60)
    for r in resultados:
        print(f"\n  Teste {r['teste']}: {r['avaliacao']}")
        print(f"  P: {r['pergunta']}")
        print(f"  R: {r['resposta'][:120]}{'...' if len(r['resposta']) > 120 else ''}")

    adequadas = sum(1 for r in resultados if r["avaliacao"] == "Adequada")
    parciais  = sum(1 for r in resultados if r["avaliacao"] == "Parcialmente adequada")
    inadequadas = sum(1 for r in resultados if r["avaliacao"] == "Inadequada")

    print(f"\n  ✅ Adequadas              : {adequadas}/5")
    print(f"  🟡 Parcialmente adequadas : {parciais}/5")
    print(f"  ❌ Inadequadas            : {inadequadas}/5")
    print("=" * 60)



def iniciar_chatbot():
    exibir_cabecalho()

    historico = iniciar_historico()

    while True:
        try:
            entrada = input("Você: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  👋 Encerrando o ChargeGrid Chatbot. Até logo!")
            break

        if not entrada:
            continue

        if entrada.lower() == "sair":
            print("\n  👋 Encerrando o ChargeGrid Chatbot. Até logo!")
            break

        if entrada.lower() == "novo":
            historico = iniciar_historico()
            print("\n  🔄 Conversa reiniciada. Histórico limpo.\n")
            continue

        if entrada.lower() == "teste":
            executar_testes()
            print("\n  Retornando ao modo de chat livre...\n")
            continue

        print("\n🤖 ChargeGrid: ", end="", flush=True)
        resposta, historico = enviar_mensagem(historico, entrada)
        print(resposta)
        print()




if __name__ == "__main__":
    iniciar_chatbot()
