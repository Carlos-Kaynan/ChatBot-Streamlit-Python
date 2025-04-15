import streamlit as st
import google.generativeai as genai

st.title("Gerador de Conteúdo com Gemini Pro")

 
api_key = st.text_input("Digite sua chave de API do Google:", type="password")

 
prompt = st.text_input("O que você quer perguntar para o Gemini?")

 
quer_resumo = st.checkbox("Você quer um resumo da resposta?")

# Botão para gerar a resposta
if st.button("Gerar resposta"):
    if not api_key or not prompt:
        st.warning("Por favor, insira a chave de API e o prompt.")
    else:
        try:
             
            genai.configure(api_key=api_key)

            
            model = genai.GenerativeModel('gemini-pro')

            # Gera a resposta inicial
            response = model.generate_content(prompt)
            texto_gerado = response.text

            st.subheader("Resposta do Gemini:")
            st.write(texto_gerado)

           
            if quer_resumo:
                st.subheader("Resumo:")
                resumo_response = model.generate_content(f"Resuma o seguinte texto de forma clara e objetiva:\n\n{texto_gerado}")
                st.write(resumo_response.text)

        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
