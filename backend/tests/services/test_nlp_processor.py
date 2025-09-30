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

def test_removes_html_tags():
    """Verifica se as tags HTML são removidas."""
    input_text = "<p>Olá <b>mundo</b></p>"
    expected_output = "Olá mundo"
    assert preprocess_text(input_text) == expected_output

def test_removes_quoted_reply_lines():
    """Verifica se as linhas de resposta de e-mails antigos são removidas."""
    input_text = "Esta é a nova mensagem.\n> Esta é a mensagem antiga.\n>> E esta é mais antiga ainda."
    expected_output = "Esta é a nova mensagem."
    assert preprocess_text(input_text) == expected_output

def test_consolidates_whitespace():
    """Verifica se múltiplos espaços e quebras de linha são limpos."""
    input_text = "   Olá    mundo\n\n\ncomo vai você?   "
    expected_output = "Olá mundo\n\ncomo vai você?"
    assert preprocess_text(input_text) == expected_output

def test_full_pipeline():
    """Testa a pipeline completa com um exemplo complexo."""
    input_text = """
    <div>
        <p>Confirmado, te vejo na reunião.</p>
        <br><br><br>
        > Em 28 de set. de 2025, às 14:30, Fulano escreveu:
        > <p>Você vem?</p>
    </div>
    """
    expected_output = "Confirmado, te vejo na reunião."
    assert preprocess_text(input_text) == expected_output