from fastapi import APIRouter

router = APIRouter(
    prefix="/api/chatbot"
)

@router.post("/get_message")
def get_message_from_chat(promptMessage: str):
    return {"response": f"Hello from backend! as response from {promptMessage}"}