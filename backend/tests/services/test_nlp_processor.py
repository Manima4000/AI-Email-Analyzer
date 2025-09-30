# Importa a função que queremos testar
from app.services.nlp_processor import preprocess_text

def test_preprocess_text_removes_leading_whitespace():
    """
    Verifica se a função remove corretamente os espaços em branco no início do texto.
    """
    input_text = "   Olá mundo"
    expected_output = "Olá mundo"
    
    actual_output = preprocess_text(input_text)
    
    assert actual_output == expected_output

def test_preprocess_text_removes_trailing_whitespace():
    """
    Verifica se a função remove corretamente os espaços em branco no final do texto.
    """
    input_text = "Olá mundo   "
    expected_output = "Olá mundo"
    
    actual_output = preprocess_text(input_text)
    
    assert actual_output == expected_output

def test_preprocess_text_does_not_change_clean_string():
    """
    Verifica se a função não altera um texto que já está limpo.
    """
    input_text = "Texto limpo sem espaços extras"
    
    actual_output = preprocess_text(input_text)
    
    assert actual_output == input_text