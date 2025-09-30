import re
from bs4 import BeautifulSoup

def _strip_html_tags(text: str) -> str:
    """Remove tags HTML do texto."""
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def _remove_quoted_lines(text: str) -> str:
    """Remove linhas de citação (que começam com '>') de e-mails."""
    lines = text.split('\n')
    unquoted_lines = [line for line in lines if not line.strip().startswith('>')]
    return '\n'.join(unquoted_lines)

def _consolidate_whitespace(text: str) -> str:
    """Substitui múltiplos espaços e quebras de linha por um único espaço/quebra de linha."""
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    return text.strip()

def preprocess_text(text: str) -> str:
    """
    Executa uma pipeline de pré-processamento para limpar o texto de um e-mail
    antes de enviá-lo para a IA.
    """
    print("NLP Service: Executando limpeza inteligente do texto...")
    clean_text = _strip_html_tags(text)
    
    clean_text = _remove_quoted_lines(clean_text)
    
    clean_text = _consolidate_whitespace(clean_text)
    
    return clean_text