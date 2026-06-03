# 🧪 Casos de Teste — ChargeGrid Assistant
## Sprint 2 | GoodWe EV Challenge 2026 | Grupo 5 — Turma 1CCPY | FIAP

---

## Instruções de preenchimento

Após executar o chatbot, copie as respostas obtidas na coluna **Resposta Obtida** e preencha a **Avaliação Qualitativa** com uma das opções:

- ✅ **Adequada** — resposta correta, dentro do escopo, clara e útil
- ⚠️ **Parcialmente adequada** — resposta relevante, mas incompleta ou imprecisa
- ❌ **Inadequada** — resposta errada, fora do escopo ou sem utilidade

---

## Tabela de Casos de Teste

| # | Pergunta Enviada | Resposta Esperada (resumo) | Resposta Obtida | Avaliação Qualitativa |
|---|---|---|---|---|
| 1 | Qual a diferença entre o carregamento normal de 7,4 kW e o rápido de 22 kW? | O carregador de 7,4 kW (Modo 2/3, AC) é mais lento e mais barato. O de 22 kW (AC trifásico) carrega em menor tempo, mas tem custo maior por kWh na plataforma ChargeGrid. A escolha depende do tempo disponível e do tipo de veículo. | *(preencher após teste)* | *(preencher após teste)* |
| 2 | Como a integração solar reduz o custo de recarga dos veículos? | A energia gerada pelos painéis solares é usada diretamente para carregar os EVs, reduzindo o consumo da rede elétrica. Em horários de alta geração solar, o custo por kWh cai significativamente. O ChargeGrid Intelligence gerencia automaticamente essa priorização. | *(preencher após teste)* | *(preencher após teste)* |
| 3 | O que é controle de pico de demanda e por que ele é importante numa estação de recarga? | Controle de pico limita a potência máxima consumida simultaneamente para evitar multas da distribuidora por ultrapassagem de demanda contratada. No ChargeGrid, a demanda máxima é distribuída dinamicamente entre os carregadores ativos (cap de 50 kW, por exemplo). | *(preencher após teste)* | *(preencher após teste)* |
| 4 | Quais protocolos de comunicação o ChargeGrid Intelligence utiliza e para que serve cada um? | OCPP: comunicação entre software e carregadores EV (autenticação, início/fim de sessão, status). MODBUS: leitura de dados do inversor solar GoodWe (potência gerada, tensão, frequência). MQTT: troca de mensagens em tempo real entre sensores, BMS e a plataforma de monitoramento. | *(preencher após teste)* | *(preencher após teste)* |
| 5 | Quero saber a previsão do campeonato brasileiro de futebol deste ano. Você pode me ajudar? | O chatbot deve recusar educadamente, explicando que foi criado exclusivamente para temas relacionados à GoodWe, ChargeGrid Intelligence e carregamento de veículos elétricos. Deve sugerir um assistente de propósito geral para outros assuntos. | *(preencher após teste)* | *(preencher após teste)* |

---

## Observações Gerais

*(espaço para o grupo registrar observações sobre o comportamento geral do chatbot durante os testes)*

- Comportamento dentro do escopo:
- Comportamento fora do escopo:
- Qualidade do histórico de conversa:
- Sugestões de melhoria no system prompt:
