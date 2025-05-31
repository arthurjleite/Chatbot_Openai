# 📋 Assistente de Organização Pessoal

Um chatbot inteligente para gerenciar suas tarefas e compromissos, desenvolvido com Streamlit e GPT-4.

## 🚀 Funcionalidades

- Adicionar novas tarefas e compromissos
- Consultar tarefas existentes através de chat natural
- Armazenamento automático em planilha Excel
- Interface amigável e intuitiva

## 📋 Requisitos

- Python 3.7+
- Streamlit
- Pandas
- OpenAI
- python-dotenv

## 🛠️ Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install streamlit pandas openai python-dotenv
```
3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API OpenAI:
```
OPENAI_API_KEY=sua_chave_aqui
```

## 💻 Como Usar

1. Execute o aplicativo:
```bash
streamlit run app.py
```

2. Acesse através do navegador (geralmente em http://localhost:8501)

3. Use a aba "Chat" para consultar suas tarefas ou a aba "Adicionar Tarefa" para criar novos compromissos

## 📝 Exemplos de Perguntas

- "Quais são minhas tarefas para hoje?"
- "Mostre minhas tarefas pendentes"
- "Quais compromissos tenho esta semana?" 