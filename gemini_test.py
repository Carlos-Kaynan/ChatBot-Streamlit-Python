import google.generativeai as genai

API_KEY = input("Diga sua chave API do Google")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
imagem = input('Qual imagem você quer?')
response = model.generate_content(f'{imagem}')

print(response.text)