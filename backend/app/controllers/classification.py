from fastapi.concurrency import run_in_threadpool
from fastapi import File, UploadFile, Form, HTTPException, status
from typing import Annotated

from ..schemas.classification import ClassificationResponse
from ..services import text_parser, nlp_processor, ai_client

async def create_classification(
    email_text: Annotated[str | None, Form()] = None,
    email_file: Annotated[UploadFile | None, File()] = None,
):
    """
    Orquestra o processo de classificação de email:
    1. Valida a entrada.
    2. Extrai o texto (de formulário ou arquivo).
    3. Pré-processa o texto.
    4. Obtém a análise da IA.
    5. Retorna a resposta estruturada.
    """
    if not email_text and not email_file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Você deve enviar ou um texto ou um arquivo."
        )
    
    if email_text and email_file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Envie ou texto ou um arquivo, não ambos."
        )

    text_content = ""
    file_name = None

    if email_file:
        if email_file.content_type not in ["text/plain", "application/pdf"]:
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail="Formato de arquivo não suportado. Use apenas .txt ou .pdf."
            )
        file_name = email_file.filename
        text_content = await text_parser.extract_text_from_file(email_file)
    
    elif email_text:
        text_content = email_text

    processed_text = nlp_processor.preprocess_text(text_content)
    
    analysis = await run_in_threadpool(ai_client.get_real_ai_analysis, processed_text)

    return ClassificationResponse(
        file_name=file_name,
        category=analysis["category"],
        suggested_response=analysis["suggested_response"]
    )