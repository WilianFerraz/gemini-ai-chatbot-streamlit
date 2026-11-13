# Generative AI Chatbot (Streamlit + Gemini API)

*[Leia em Português](#chatbot-com-ia-generativa-streamlit--api-gemini)*

An interactive web chatbot application built with Python and Streamlit, integrated with Google's **Gemini** model via the OpenAI-compatible SDK. The app manages real-time conversation history using session state to provide contextualized AI responses.

## Technologies Used
- **Python 3**
- **Streamlit** (Interactive Web UI & Session State Management)
- **OpenAI Python SDK** (API Client configured for Google Gemini endpoint)
- **Gemini API** (`gemini-flash-lite-latest`)

## Project Structure
- `main.py`: Core application script containing the Streamlit chat interface, session memory management, and LLM API integration.
- `requirements.txt`: Project dependencies list.

## How to Run

1. Install the dependencies:

    pip install -r requirements.txt

2. Add your Google Gemini API key in `main.py` (replace `"YOUR_GEMINI_API_KEY"` with your actual key from Google AI Studio).

3. Start the Streamlit web server:

    streamlit run main.py

---

# ChatBot com IA Generativa (Streamlit + API Gemini)

*[Read in English](#generative-ai-chatbot-streamlit--gemini-api)*

Aplicação web de chat interativo desenvolvida com Python e Streamlit, integrada ao modelo **Gemini** do Google através do SDK compatível com OpenAI. A aplicação gerencia o histórico da conversa em tempo real utilizando estado de sessão para fornecer respostas contextualizadas.

## Tecnologias Utilizadas
- **Python 3**
- **Streamlit** (Interface Web Interativa e Gerenciamento de Estado de Sessão)
- **OpenAI Python SDK** (Cliente de API configurado para o endpoint do Google Gemini)
- **API Gemini** (`gemini-flash-lite-latest`)

## Estrutura do Projeto
- `main.py`: Script principal contendo a interface de chat em Streamlit, gerenciamento de memória da sessão e integração com a API do modelo de linguagem.
- `requirements.txt`: Lista de dependências do projeto.

## Como Executar

1. Instale as dependências:

    pip install -r requirements.txt

2. Insira sua chave da API do Google Gemini no arquivo `main.py` (substitua `"YOUR_GEMINI_API_KEY"` pela sua chave gerada no Google AI Studio).

3. Inicie o servidor web do Streamlit:

    streamlit run main.py
