# app/database.py

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import Conversation

async def init_db():
    # Initialize MongoDB client 
    client = AsyncIOMotorClient(
        "mongodb://localhost:27017/chatbot_db"
    )
    
    # Initialize Beanie with the 'chatbot_db' database
    await init_beanie(database=client['chatbot_db'], document_models=[Conversation])

