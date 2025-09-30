from fastapi import UploadFile
import fitz  

async def extract_text_from_file(file: UploadFile) -> str:
    """
    Extrai texto de um UploadFile, suportando .txt e .pdf.
    """
    content_type = file.content_type
    
    if content_type == "text/plain":
        contents = await file.read()
        return contents.decode("utf-8")
        
    elif content_type == "application/pdf":
        text = ""
        contents = await file.read()
        with fitz.open(stream=contents, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
        
    else:
        return "Formato de arquivo não suportado."