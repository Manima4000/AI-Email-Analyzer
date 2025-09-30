from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- Verifique este import
from .routers import classification

app = FastAPI(
    title="API de Classificação de Email",
    description="Uma API para classificar emails como produtivos ou improdutivos e sugerir respostas.",
    version="1.0.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],         
)


app.include_router(classification.router, prefix="/api/v1", tags=["Classification"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API de Classificação de Email!"}