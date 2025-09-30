from pydantic import BaseModel, Field

class ClassificationResponse(BaseModel):
    """
    Define o formato da resposta JSON para a classificação de email.
    """
    file_name: str | None = Field(
        default=None, 
        description="O nome do arquivo enviado, se houver.",
        examples=["meu_documento.pdf"]
    )
    category: str = Field(
        ..., 
        description="A categoria do email.",
        examples=["Produtivo", "Improdutivo"]
    )
    suggested_response: str = Field(
        ...,
        description="A sugestão de resposta gerada pela IA.",
        examples=["Entendido. Irei priorizar esta tarefa."]
    )

    class Config:
        from_attributes = True