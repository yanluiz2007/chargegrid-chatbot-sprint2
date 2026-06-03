# ChargeGrid Assistant — Chatbot GoodWe EV Challenge 2026

O ChargeGrid Assistant é um chatbot de inteligência artificial desenvolvido pelo Grupo 5 da turma 1CCPY da FIAP, como parte da Sprint 2 do EV Challenge 2026, em parceria com a GoodWe.

O assistente foi criado para atuar como um especialista virtual no ecossistema de carregamento de veículos elétricos, com foco na plataforma ChargeGrid Intelligence — solução que integra energia solar, armazenamento em bateria e carregadores EV em ambientes comerciais. O modelo de linguagem utilizado é o **Llama 3.3 70B**, acessado gratuitamente via API da Groq.

---

## Para que serve

O ChargeGrid Assistant foi desenvolvido para apoiar três perfis diferentes de usuário:

- **Motoristas de EV**: dúvidas sobre como funciona o carregamento, diferença entre carregadores, tempo estimado de carga e boas práticas de uso.
- **Gestores de frota ou estabelecimentos**: informações sobre tarifas, gestão de demanda, controle de pico e otimização de custo energético.
- **Operadores técnicos**: suporte sobre protocolos de comunicação (OCPP, MODBUS, MQTT), hardware GoodWe HCA G2, integração solar e monitoramento em tempo real.

O chatbot não responde sobre assuntos fora desse escopo. Se o usuário perguntar algo não relacionado ao tema, o assistente informa educadamente que foi desenvolvido exclusivamente para esse contexto.

---

## Tecnologias utilizadas

| Tecnologia | Versão | Para que serve |
|---|---|---|
| Python | 3.10+ | Linguagem principal do projeto |
| Groq API | — | Provedor de inferência do modelo Llama |
| Llama 3.3 70B | — | Modelo de linguagem que gera as respostas |
| python-dotenv | latest | Carrega a API Key com segurança via arquivo `.env` |
| groq (lib) | latest | Cliente oficial para chamadas à API da Groq |

---

## Pré-requisitos

Antes de começar, confirme que você tem o seguinte instalado na máquina:

**Python 3.10 ou superior**

Para verificar a versão instalada, abra o terminal e rode:
```bash
python --version
```
Se retornar algo como `Python 3.10.x` ou superior, está ok. Caso não tenha, baixe em [python.org/downloads](https://www.python.org/downloads).

**pip**

O pip é o gerenciador de pacotes do Python e normalmente já vem instalado junto. Para verificar:
```bash
pip --version
```

**Conta na Groq**

A API da Groq é gratuita e não exige cartão de crédito. Acesse [console.groq.com](https://console.groq.com), crie uma conta e gere uma chave de API. O passo a passo está detalhado na seção abaixo.

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-goodwe.git
cd chatbot-goodwe
```

Ou baixe o projeto como `.zip` pelo GitHub e extraia na sua máquina.

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Esse comando instala automaticamente as duas bibliotecas necessárias para o projeto funcionar:

- **groq**: cliente oficial da API da Groq, responsável por enviar as mensagens para o modelo Llama e receber as respostas.
- **python-dotenv**: lê o arquivo `.env` e carrega a API Key como variável de ambiente, sem que você precise expô-la no código.

Sem essa etapa, o projeto não vai rodar.

---

## Configurando a API Key

Esse é o passo mais importante de toda a configuração. Leia com atenção.

### Gerando a chave na Groq

1. Acesse [console.groq.com](https://console.groq.com) e faça login
2. No menu lateral, clique em **API Keys**
3. Clique em **Create API Key**
4. Dê um nome para identificar a chave (pode ser `chatbot-goodwe` ou qualquer outro)
5. Copie a chave gerada — ela começa com `gsk_` e aparece **apenas uma vez**

### Criando o arquivo `.env`

Na raiz do projeto (mesma pasta onde está o `main.py`), crie um arquivo chamado **`.env`** com o seguinte conteúdo:

```
GROQ_API_KEY=cole_sua_chave_aqui
```

Substitua `cole_sua_chave_aqui` pela chave real que você copiou da Groq.

> **Referência**: já existe um arquivo `.env.example` no projeto que mostra exatamente esse formato. Ele serve de modelo — não coloque a chave real nele, pois esse arquivo vai para o GitHub.

### Por que o `.env` não vai para o GitHub

O arquivo `.env` contém sua chave de API, que é pessoal e intransferível. Se ela for exposta num repositório público, qualquer pessoa pode utilizá-la e consumir seus créditos. Por isso, o `.env` já está listado no `.gitignore` do projeto, o que impede automaticamente que ele seja enviado ao repositório.

---

## Como executar

Com as dependências instaladas e o `.env` configurado, abra o terminal na pasta do projeto e rode:

```bash
python main.py
```

O chatbot vai inicializar e exibir uma tela de boas-vindas com exemplos de perguntas. A partir daí, basta digitar sua pergunta e pressionar Enter.

**Comandos disponíveis durante a conversa:**

| Comando | O que faz |
|---|---|
| `sair` | Encerra o chatbot |
| `exit` | Encerra o chatbot |
| `encerrar` | Encerra o chatbot |

**E se o `.env` não estiver configurado?**

Nesse caso, o chatbot exibe um aviso e solicita que você digite a chave diretamente no terminal. Por segurança, ela não aparece na tela enquanto você digita — esse comportamento é intencional e usa a função `getpass` do Python.

---

## Executando no Google Colab

Caso prefira rodar pelo Colab em vez do terminal local, siga os passos abaixo:

```python
# Célula 1 — Instalar dependências
!pip install groq python-dotenv

# Célula 2 — Clonar o repositório
!git clone https://github.com/seu-usuario/chatbot-goodwe.git
%cd chatbot-goodwe

# Célula 3 — Rodar o chatbot
!python main.py
```

No Colab, como não há arquivo `.env`, o chatbot vai pedir a API Key no campo de input ao iniciar.

---

## Como o chatbot funciona por dentro

### System Prompt

O system prompt é o conjunto de instruções que define o comportamento do assistente antes de qualquer interação com o usuário. Ele é enviado para o modelo como a primeira mensagem de toda sessão, com o papel `system`.

Nele estão definidos: a identidade do assistente, os temas que ele pode e não pode responder, o perfil esperado do usuário, e as diretrizes de tom e linguagem. É o system prompt que garante que o chatbot se mantenha dentro do escopo do EV Challenge — sem ele, o modelo responderia qualquer coisa.

### Histórico de mensagens

A memória de contexto do chatbot funciona através de uma lista Python chamada `historico`. A cada troca de mensagem, tanto a pergunta do usuário quanto a resposta do assistente são adicionadas a essa lista.

Quando o usuário faz uma nova pergunta, a lista inteira — desde o system prompt até a última resposta — é enviada para a API. É assim que o modelo consegue manter coerência ao longo da conversa e fazer referência ao que foi dito anteriormente.

---

## Casos de teste

Os 5 casos de teste completos estão documentados em `tests/casos_teste.md`, com espaço para registrar a resposta obtida e a avaliação qualitativa. Resumo abaixo:

| # | Pergunta enviada | Avaliação esperada |
|---|---|---|
| 1 | Diferença entre carregamento de 7,4 kW e 22 kW | Adequada — resposta técnica e clara |
| 2 | Como a energia solar reduz o custo de recarga? | Adequada — explica o fluxo solar → EV |
| 3 | O que é controle de pico de demanda? | Adequada — conceito e gestão pelo ChargeGrid |
| 4 | Quais protocolos o ChargeGrid usa e para quê? | Adequada — OCPP, MODBUS e MQTT explicados |
| 5 | Previsão do campeonato brasileiro de futebol | Adequada — recusa educada fora do escopo |

---

## Grupo 5 — Turma 1CCPY | FIAP | EV Challenge 2026

Jair Ferreira Dos Santos Neto — RM 569682  
Matheus da Costa Gonçalves — RM 570756  
Yan Luiz Neves Lemos — RM 571717  
Arthur dos Santos Bezerra — RM 569721  
Carlos Henrique Fratezi — RM 571792
