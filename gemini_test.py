import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini Pro", layout="centered")
st.title(" Gerador de Conteúdo com Gemini Pro")

api_key = st.text_input(" Digite sua chave de API do Google:", type="password")
prompt = st.text_input(" O que você quer perguntar para o Gemini?")
quer_resumo = st.checkbox(" Você quer um resumo da resposta?")

if st.button(" Gerar resposta"):
    if not api_key or not prompt:
        st.warning(" Por favor, insira a chave de API e o prompt.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            with st.spinner(" Gerando resposta..."):
                response = model.generate_content(prompt)
                texto_gerado = response.text

            st.subheader(" Resposta do Gemini:")
            st.write(texto_gerado)

            if quer_resumo:
                with st.spinner(" Gerando resumo..."):
                    resumo_response = model.generate_content(f"Resuma de forma clara e objetiva:\n\n{texto_gerado}")
                    st.subheader(" Resumo:")
                    st.write(resumo_response.text)

        except Exception as e:
            st.error(f" Ocorreu um erro: {e}")
