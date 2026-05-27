# ⚡ ChargeGrid Intelligence — Chatbot Operacional
### Assistente Inteligente para Gestão de Eletropostos Comerciais

> *"A mobilidade elétrica do futuro depende do código que orquestra e distribui a energia."*

**EV Challenge 2026 · FIAP + GoodWe · Turma 1CCPY**
**Disciplina: Prompt and Artificial Intelligence · Sprint 2**

---

## 👥 Equipe

| Nome | RM |
|---|---|
| Jair Ferreira dos Santos Neto | 569682 |
| Matheus da Costa Gonçalves | 570756 |
| Yan Luiz Neves Lemos | 571717 |
| Arthur dos Santos Bezerra | 569721 |
| Carlos Henrique Fratezi | 571792 |

---

## 📌 Problema Abordado

Eletropostos comerciais carecem de uma interface inteligente de comunicação com gestores. Operadores precisam consultar status de carregadores, tarifas, consumo solar e alertas de demanda — mas não têm acesso a essas informações de forma simples e em linguagem natural.

O ChargeGrid Intelligence resolve isso com um chatbot operacional que responde perguntas do gestor em português, com contexto completo do sistema de energia do eletroposto.

---

## 🤖 Proposta do Chatbot

O chatbot atua como assistente do **operador comercial** do eletroposto, respondendo perguntas sobre:

- Status e disponibilidade dos carregadores
- Tarifas atuais e horário de ponta
- Economia gerada pela energia solar
- Alertas de demanda e risco de multa
- Diagnóstico de falhas nos equipamentos

O modelo é instruído via **system prompt** com contexto completo do ChargeGrid Intelligence, dados operacionais simulados e regras de comportamento — garantindo respostas coerentes e dentro do escopo GoodWe.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Justificativa |
|---|---|
| Python 3.x | Linguagem principal do projeto |
| Llama 3 (8B) | Modelo de linguagem open-source, roda localmente sem custo |
| Ollama | Runtime local para o Llama — sem necessidade de API Key |
| Biblioteca `ollama` (Python) | Interface Python para comunicação com o modelo |

**Por que Llama + Ollama?**
O Llama 3 via Ollama permite execução 100% local, sem expor chaves de API, sem limite de requisições e com controle total sobre os parâmetros do modelo. Isso garante privacidade dos dados operacionais e viabilidade para um ambiente de produção real.

---

## ⚙️ Instalação e Execução

### Pré-requisitos

- Python 3.8 ou superior
- Windows 10 ou superior / macOS / Linux

### Passo 1 — Instalar o Ollama

Acesse [ollama.com](https://ollama.com) e baixe o instalador para o seu sistema operacional.

### Passo 2 — Baixar o modelo Llama 3

```bash
ollama pull llama3
```

> O download é de aproximadamente 4.7 GB.

### Passo 3 — Instalar a dependência Python

```bash
pip install ollama
```

### Passo 4 — Executar o chatbot

```bash
python chargegrid_chatbot.py
```

---

## 💬 Exemplos de Uso

```
Você: Qual o preço da recarga agora?
🤖 ChargeGrid: O preço atual é R$ 0,85/kWh pois estamos fora do
horário de ponta. A partir das 18h a tarifa sobe para R$ 1,20/kWh.

Você: O carregador 3 está funcionando?
🤖 ChargeGrid: O carregador 3 apresentou falha de handshake OCPP
às 14h32. A manutenção está pendente. Recomendo acionar o suporte
técnico antes do horário de ponta.

Você: Quanto economizei com solar hoje?
🤖 ChargeGrid: Hoje foram aproveitados 420 kWh de energia solar,
equivalente a R$ 357,00 de economia na conta de energia.
```

---

## 🧪 Comandos Disponíveis

| Comando | Função |
|---|---|
| *(qualquer pergunta)* | O chatbot responde com contexto ChargeGrid |
| `teste` | Executa os 5 casos de teste da Sprint 1 automaticamente |
| `novo` | Reinicia a conversa e limpa o histórico |
| `sair` | Encerra o chatbot |

---

## 🧠 Destaques Técnicos

- **System Prompt com contexto rico** — dados operacionais simulados injetados diretamente no prompt
- **Memória de contexto** — histórico completo de mensagens mantido durante toda a conversa
- **Parâmetros controlados** — `temperature=0.4` para respostas consistentes e naturais; `num_predict=512` para respostas objetivas
- **Few-shot implícito** — exemplos de comportamento esperado embutidos no system prompt

---

## 📋 Modelo de Teste — Sprint 1

| # | Pergunta | Avaliação |
|---|---|---|
| 1 | Qual o preço da recarga agora? | Adequada |
| 2 | Por que minha conta de luz veio mais alta esse mês? | Adequada |
| 3 | Qual carregador tem mais disponibilidade agora? | Adequada |
| 4 | Quanto de energia solar economizei essa semana? | Adequada |
| 5 | O carregador 3 está funcionando? | Adequada |

---

## 🗂️ Estrutura do Repositório

```
chargegrid-chatbot-sprint2/
│
├── chargegrid_chatbot.py   # Código principal do chatbot
└── README.md               # Documentação do projeto
```
