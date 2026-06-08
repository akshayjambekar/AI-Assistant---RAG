from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_services import ask_llm
from app.services.rag_service import RAGService
router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):

    response = await RAGService.ask_question(
    request.message
    )

    return {
        "response": response
    }