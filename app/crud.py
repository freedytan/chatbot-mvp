# app/crud.py

from app.models import Conversation, Message
from app.llm_service import llm_generate
from bson import ObjectId
from fastapi import HTTPException

async def create_conversation_with_message(message: Message) -> Conversation:
    # Create a new conversation with the initial user message
    conversation = Conversation(
        title="New Conversation",  
        messages=[message]
    )
    
    # Generate the LLM response based on the initial user message
    llm_response_content = llm_generate(message.content)
    llm_response = Message(role="Chatbot", content=llm_response_content)
    
    # Append the LLM's response to the messages list
    conversation.messages.append(llm_response)
    
    # Save the conversation to the database
    await conversation.insert()
    
    return conversation

async def add_message_to_conversation(conversation_id: str, message: Message) -> Conversation:
    conversation = await Conversation.get(ObjectId(conversation_id))
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    # Append the new user message to the messages list
    conversation.messages.append(message)
    
    # Generate the LLM response based on the user's message
    llm_response_content = llm_generate(message.content)
    llm_response = Message(role="Chatbot", content=llm_response_content)
    
    # Append the LLM's response to the messages list
    conversation.messages.append(llm_response)
    
    # Save the updated conversation back to the database
    await conversation.save()
    
    return conversation