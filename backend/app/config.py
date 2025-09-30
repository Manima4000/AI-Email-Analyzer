import os
from dotenv import load_dotenv


load_dotenv() #Carrega as variáveis do arquivo .env para o ambiente

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

if not (GOOGLE_API_KEY and MODEL_NAME):
    raise ValueError("As variáveis de ambiente GOOGLE_API_KEY ou MODEL_NAME não foram definidas.")