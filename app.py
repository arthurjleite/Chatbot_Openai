import streamlit as st
import pandas as pd
import openai
import os
from dotenv import load_dotenv
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Assistente de Organização Pessoal", page_icon="📋")

# Carregar API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Inicializar ou carregar a planilha
def carregar_ou_criar_planilha():
    try:
        df = pd.read_excel("tarefas.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=['data', 'titulo', 'descricao', 'status'])
        df.to_excel("tarefas.xlsx", index=False)
    return df

# Função para salvar na planilha
def salvar_tarefa(data, titulo, descricao):
    df = carregar_ou_criar_planilha()
    nova_tarefa = pd.DataFrame({
        'data': [data],
        'titulo': [titulo],
        'descricao': [descricao],
        'status': ['Pendente']
    })
    df = pd.concat([df, nova_tarefa], ignore_index=True)
    df.to_excel("tarefas.xlsx", index=False)
    return df

# Interface principal
st.title("📋 Assistente de Organização Pessoal")

# Tabs para diferentes funcionalidades
tab1, tab2 = st.tabs(["💬 Chat", "➕ Adicionar Tarefa"])

with tab1:
    st.subheader("💬 Converse com seu assistente")
    pergunta = st.text_area("Digite sua pergunta ou comando:", height=100,
                           placeholder="Ex: Quais são minhas tarefas para hoje? ou Mostre minhas tarefas pendentes.")

    if st.button("Enviar"):
        if pergunta:
            df = carregar_ou_criar_planilha()
            prompt = f"""Você é um assistente de organização pessoal. Abaixo está uma tabela de tarefas que você deve usar para responder à pergunta do usuário de forma precisa e útil.
            Dados das tarefas (formato xlsx):

            {df.to_csv(index=False)}

            Pergunta: {pergunta}
            
            Responda de forma clara e profissional em português. Se for uma consulta sobre tarefas,
            organize a resposta de forma estruturada. Se não houver dados relevantes, informe isso educadamente."""

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )
            resposta = response['choices'][0]['message']['content']
            st.markdown(f"**🤖 Resposta:** {resposta}")
        else:
            st.warning("Por favor, digite uma pergunta ou comando.")

with tab2:
    st.subheader("➕ Adicionar Nova Tarefa")
    
    data = st.date_input("Data do compromisso", datetime.now())
    titulo = st.text_input("Título da tarefa")
    descricao = st.text_area("Descrição", height=100)
    
    if st.button("Salvar Tarefa"):
        if titulo and descricao:
            df = salvar_tarefa(data, titulo, descricao)
            st.success("✅ Tarefa adicionada com sucesso!")
            st.dataframe(df.tail(1))
        else:
            st.warning("Por favor, preencha todos os campos.")
