from app import crud, schemas, database
from app.database import init_db
from app.models import Conversation, Message
from beanie import init_beanie
from fastapi import FastAPI, HTTPException
import uvicorn

# Initialize FastAPI application
app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/")
async def read_root():
    return {"message": "Welcome to my Beanie-powered Chatbot API!"}

# Route to create a new conversation with the first message
@app.post("/conversations/", response_description="Conversation created")
async def create_conversation_with_message(message: Message):
    new_conversation = await crud.create_conversation_with_message(message)
    return new_conversation

# Route to add message to conversation
@app.post("/conversations/{conversation_id}/messages/", response_description="Message added to the conversation")
async def add_message(conversation_id: str, message: Message):
    updated_conversation = await crud.add_message_to_conversation(conversation_id, message)
    return updated_conversation

# Run the server using Uvicorn
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
