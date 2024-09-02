# app/crud.py

from app.models import Conversation, Message
from bson import ObjectId
from fastapi import HTTPException

async def create_conversation_with_message(message: Message) -> Conversation:
    conversation = Conversation(
        title="New Conversation",  
        messages=[message]
    )
    await conversation.insert()  # This saves the conversation to the database
    return conversation

async def add_message_to_conversation(conversation_id: str, message: Message) -> Conversation:
    conversation = await Conversation.get(ObjectId(conversation_id))
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    # Append the new message to the messages list
    conversation.messages.append(message)
    
    # Save the updated conversation back to the database
    await conversation.save()
    return conversation