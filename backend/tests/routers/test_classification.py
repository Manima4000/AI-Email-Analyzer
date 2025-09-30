from fastapi.testclient import TestClient
from unittest.mock import patch 
import io

from app.main import app 

client = TestClient(app)

def test_classify_email_with_text_successful():
    """
    Testa o endpoint de classificação enviando um texto.
    Verifica se a resposta é 200 OK e se o corpo da resposta está correto.
    """
    form_data = {"email_text": "Este é um e-mail de teste para a reunião."}

    mock_ai_response = {
        "category": "Produtivo (Mocked)",
        "suggested_response": "Resposta gerada pelo teste."
    }


    with patch("app.services.ai_client.get_real_ai_analysis", return_value=mock_ai_response):
        response = client.post("/api/v1/classify-email", data=form_data)

    assert response.status_code == 200
    

    assert response.json() == {
        "file_name": None,
        "category": "Produtivo (Mocked)",
        "suggested_response": "Resposta gerada pelo teste."
    }

def test_classify_email_without_data_fails():
    """
    Testa se o endpoint retorna um erro 400 (Bad Request) quando nenhum dado é enviado.
    """
    response = client.post("/api/v1/classify-email")

    assert response.status_code == 400
    assert response.json() == {"detail": "Você deve enviar ou um texto ou um arquivo."}
    
# Adicione este import no topo do arquivo
import io

# ... (outros imports e o 'client = TestClient(app)')

# Adicione esta nova função de teste ao arquivo
def test_classify_email_with_file_successful():
    """
    Testa o endpoint de classificação enviando um arquivo .txt.
    """

    mock_file_content = b"Este eh um conteudo de teste de um arquivo."
    

    file_payload = {
        "email_file": ("test.txt", mock_file_content, "text/plain")
    }

    mock_ai_response = {
        "category": "Produtivo (Mocked)",
        "suggested_response": "Resposta do arquivo de teste."
    }

    with patch("app.services.ai_client.get_real_ai_analysis", return_value=mock_ai_response):
        response = client.post("/api/v1/classify-email", files=file_payload)

    assert response.status_code == 200
    assert response.json() == {
        "file_name": "test.txt",
        "category": "Produtivo (Mocked)",
        "suggested_response": "Resposta do arquivo de teste."
    }


def test_classify_email_with_both_inputs_fails():
    """
    Testa se o endpoint retorna um erro 400 se texto e arquivo forem enviados juntos.
    """
    form_data = {"email_text": "Texto de teste."}
    file_payload = {"email_file": ("test.txt", b"conteudo", "text/plain")}

    response = client.post("/api/v1/classify-email", data=form_data, files=file_payload)

    assert response.status_code == 400
    assert response.json() == {"detail": "Envie ou texto ou um arquivo, não ambos."}