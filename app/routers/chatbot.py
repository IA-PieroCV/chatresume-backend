from fastapi import APIRouter
from pydantic import BaseModel

from ..core.inference_chat import ask_llm

class PromptMessageData(BaseModel):
    promptMessage: str

router = APIRouter(
    prefix="/api/chatbot"
)



@router.post("/get_message")
def get_message_from_chat(data: PromptMessageData):
    output = ask_llm(data.promptMessage)
    return {"response": f"{output}"}