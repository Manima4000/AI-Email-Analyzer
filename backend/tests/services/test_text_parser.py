import pytest
from unittest.mock import MagicMock # Usaremos MagicMock para criar nosso dublê

from app.services.text_parser import extract_text_from_file


@pytest.mark.asyncio
async def test_extract_text_from_txt_file():
    """
    Verifica se a função extrai corretamente o texto de um mock de arquivo .txt.
    """

    mock_content = b"Este eh um conteudo de teste de um arquivo txt."
    
    mock_file = MagicMock()
    mock_file.content_type = "text/plain" 
    
    async def mock_read():
        return mock_content
    mock_file.read = mock_read 
    extracted_text = await extract_text_from_file(mock_file)

    assert extracted_text == "Este eh um conteudo de teste de um arquivo txt."

@pytest.mark.asyncio
async def test_extract_text_from_unsupported_file():
    """
    Verifica se a função lida com tipos de arquivo não suportados.
    """
    mock_file = MagicMock()
    mock_file.content_type = "image/png" 

    extracted_text = await extract_text_from_file(mock_file)

    assert extracted_text == "Formato de arquivo não suportado."