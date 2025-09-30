# backend/check_models.py
import google.generativeai as genai
from app.config import GOOGLE_API_KEY # Reutiliza nossa config para pegar a chave

print("Tentando configurar a API...")
try:
    genai.configure(api_key=GOOGLE_API_KEY)

    print("\nListando modelos disponíveis que suportam 'generateContent':")

    model_found = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
            model_found = True

    if not model_found:
        print("\nNENHUM modelo encontrado! Isso confirma um problema de configuração no projeto (provavelmente faturamento ou permissões).")

    print("\nScript concluído.")

except Exception as e:
    print(f"\nOcorreu um erro: {e}")