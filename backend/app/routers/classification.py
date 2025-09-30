from fastapi import APIRouter, Depends

from ..schemas.classification import ClassificationResponse
from ..controllers import classification as classification_controller

router = APIRouter()

@router.post(
    "/classify-email",
    response_model=ClassificationResponse,
    summary="Classifica o conteúdo de um email",
    description="Recebe o texto de um email via formulário ou upload de arquivo (.txt/.pdf), o classifica e sugere uma resposta."
)

async def classify_email_route(
    response: ClassificationResponse = Depends(classification_controller.create_classification)
):
    return response