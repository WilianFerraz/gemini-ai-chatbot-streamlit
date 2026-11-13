import streamlit as st
from openai import OpenAI

# Initialize Gemini API client using OpenAI-compatible SDK
client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

st.write("### ChatBot com IA")

# Initialize conversation history in Streamlit session state
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Render existing chat history
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# Handle new user input
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # Display and store user message
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # Request response from Gemini model
    resposta_modelo = client.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )
    resposta_ia = resposta_modelo.choices[0].message.content

    # Display and store AI response
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
