# Para executar: streamlit run main2.py

import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="ChatBot com IA", page_icon="🤖")


genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
modelo = genai.GenerativeModel("gemini-2.5-flash")

st.write("### ChatBot com IA") # markdown

# session_state = memoria do streamlit
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA com feedback visual (spinner)
    with st.spinner("A IA está digitando..."):
        try:
            # Converter histórico para o formato do Gemini (user/model)
            historico_gemini = []
            for msg in st.session_state["lista_mensagens"][:-1]:
                role = "user" if msg["role"] == "user" else "model"
                historico_gemini.append({"role": role, "parts": [msg["content"]]})

            chat = modelo.start_chat(history=historico_gemini)
            response = chat.send_message(mensagem_usuario)
            
            resposta_ia = response.text

            # exibir a resposta da IA na tela
            st.chat_message("assistant").write(resposta_ia)
            mensagem_ia = {"role": "assistant", "content": resposta_ia}
            st.session_state["lista_mensagens"].append(mensagem_ia)
        except Exception as e:
            st.error(f"Erro ao conectar com a IA: {e}")
            st.warning("Tentando listar modelos disponíveis para sua chave:")
            try:
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        st.write(f"- {m.name}")
            except Exception as e2:
                st.error(f"Sua chave de API parece inválida. Erro ao listar modelos: {e2}")
