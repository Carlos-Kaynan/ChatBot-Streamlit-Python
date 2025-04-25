import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini Pro", layout="centered")
st.title("Gerador de Conteúdo com Gemini Pro")

api_key = st.text_input("Digite sua chave de API do Google:", type="password")
prompt = st.text_input("O que você quer perguntar para o Gemini?")
quer_resumo = st.checkbox("Você quer um resumo da resposta?")

if st.button("Gerar resposta"):
    if not api_key or not prompt:
        st.warning("Por favor, insira a chave de API e o prompt.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            with st.spinner("Gerando resposta..."):
                response = model.generate_content(prompt)
                texto_gerado = response.text

            st.subheader("Resposta do Gemini:")
            st.write(texto_gerado)

            if quer_resumo:
                with st.spinner("Gerando resumo..."):
                    resumo_response = model.generate_content(f"Resuma de forma clara e objetiva:\n\n{texto_gerado}")
                    st.subheader("Resumo:")
                    st.write(resumo_response.text)

            # Campo para descrição de imagem
            gerar_imagem = st.checkbox("Deseja gerar uma imagem com base na resposta?")
            if gerar_imagem:
                estilo_imagem = st.text_input("Descreva como você quer a imagem (ex: estilo cartoon, realista, etc):")

                if st.button("Gerar Imagem"):
                    if not estilo_imagem:
                        st.warning("Por favor, descreva como deseja a imagem.")
                    else:
                        with st.spinner("Gerando imagem baseada na resposta..."):
                            # Prompt para geração de imagem
                            imagem_prompt = f"Crie uma imagem baseada no seguinte texto: {texto_gerado}. Estilo: {estilo_imagem}."

                            image_model = genai.GenerativeModel('gemini-pro')
                            image_response = image_model.generate_content(imagem_prompt)

                            st.subheader("Imagem Gerada:")
                            st.image(image_response.images[0], use_column_width=True)

        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
