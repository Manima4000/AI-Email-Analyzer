# backend/app/services/ai_client.py
import google.generativeai as genai
import json
from ..config import GOOGLE_API_KEY, MODEL_NAME

# Configura o cliente do Gemini com a nossa chave de API
genai.configure(api_key=GOOGLE_API_KEY)

# --- FUNÇÃO REAL COM GEMINI ---
def get_real_ai_analysis(text: str) -> dict:
    """
    Faz a chamada real para a API do Gemini para análise de email.
    """
    print("AI Service (REAL): Analisando o texto com Gemini...")
    
    model = genai.GenerativeModel(MODEL_NAME)

    prompt = f"""
    Aja como um assistente de produtividade altamente eficiente. Sua tarefa é analisar o conteúdo de um e-mail e retornar uma análise em formato JSON.
    
    Contexto no qual você se encontra: 
        Estamos criando uma solução digital para uma grande empresa do setor financeiro que lida com um alto volume de emails diariamente.
        Esses emails podem ser mensagens solicitando um status atual sobre uma requisição em andamento, compartilhando algum arquivo ou até mesmo mensagens improdutivas, como desejo de feliz natal ou perguntas não relevantes. 
        Nosso objetivo é automatizar a leitura e classificação desses emails e sugerir classificações e respostas automáticas de acordo com o teor de cada email recebido, liberando tempo da equipe para que não seja mais necessário ter uma pessoa fazendo esse trabalho manualmente.


    Siga estritamente as seguintes regras:
        1. Classifique o e-mail em uma de duas categorias: "Produtivo" ou "Improdutivo" - Produtivo: Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema).
            - Improdutivo: Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos).
        2. Com base na categoria e no conteúdo, sugira uma resposta curta/média, profissional e em português.
        3. Sua resposta DEVE ser um objeto JSON válido, sem nenhum texto antes ou depois.
        4. O objeto JSON deve ter exatamente duas chaves: "category" (string) e "suggested_response" (string).
        5. o campo "suggested_response" TEM QUE ser adequada à categoria identificada.


    --- EXEMPLOS ---

    Exemplo 1 de E-mail: "Olá equipe, gostaria de confirmar nossa reunião amanhã às 10h para discutir o relatório trimestral. Por favor, tragam suas anotações."
    Exemplo 1 de Saída JSON Esperada:
    
        {{
            "category": "Produtivo",
            "suggested_response": "Confirmado. Estarei presente na reunião amanhã às 10h com minhas anotações. Até lá."
        }}

    Exemplo 2 de E-mail: "Super oferta imperdível! Compre agora e ganhe 50% de desconto em toda a loja. Clique aqui!"
    Exemplo 2 de Saída JSON Esperada:
    
    {{
        "category": "Improdutivo",
        "suggested_response": "Obrigado pela oferta, mas não tenho interesse no momento. Por favor, remova-me da sua lista de marketing."
    }}
    
    
    O texto do e-mail para analise é: "{text}"  
    """
    
    try:
        response = model.generate_content(prompt)
        if not response.parts:
            return {
                "category": "Bloqueado por Segurança",
                "suggested_response": "O conteúdo do e-mail acionou os filtros de segurança da API de IA e não pôde ser processado. Tente um texto com conteúdo diferente."
            }
        json_response = response.text.strip().replace("```json", "").replace("```", "")
        return json.loads(json_response)
    except Exception as e:
        print(f"Erro ao chamar a API do Gemini ou ao parsear o JSON: {e}")
        return {
            "category": "Erro",
            "suggested_response": "Não foi possível analisar o e-mail no momento. Tente novamente."
        }



