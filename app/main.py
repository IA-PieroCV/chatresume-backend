from fastapi import FastAPI
from .routers import chatbot

app = FastAPI()

app.include_router(chatbot.router)