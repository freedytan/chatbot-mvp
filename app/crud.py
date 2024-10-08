# app/crud.py

from app.models import Conversation, Message
from app.llm_service import llm_generate
from app.anonymizer import anonymize_text
from bson import ObjectId
from fastapi import HTTPException

async def create_conversation_with_message(message: Message) -> Conversation:
    # Anonymize only the content of the user's message
    message.content = anonymize_text(message.content)

    # Create a new conversation with the initial user message
    conversation = Conversation(
        title="New Conversation",  
        messages=[message] #Anonymize
    )
    
    # Generate the LLM response based on the initial user message
    llm_response_content = llm_generate(message.content)
    llm_response_content = anonymize_text(llm_response_content) # Anonymize
    llm_response = Message(role="Chatbot", content=llm_response_content)
    
    # Append the LLM's response to the messages list
    conversation.messages.append(llm_response)
    
    # Save the conversation to the database
    await conversation.insert()
    
    return conversation

async def add_message_to_conversation(conversation_id: str, message: Message) -> Conversation:
    # Retrieve the conversation by ID
    conversation = await Conversation.get(ObjectId(conversation_id))
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    # Append the new user message to the messages list
    conversation.messages.append(message)
    
    # Generate the full chat history as a string
    chat_history = "\n".join([f"{msg.role}: {msg.content}" for msg in conversation.messages])
    
    # Generate the LLM response based on the entire conversation history
    llm_response_content = llm_generate(chat_history)
    llm_response = Message(role="Chatbot", content=llm_response_content)
    
    # Append the LLM's response to the messages list
    conversation.messages.append(llm_response)
    
    # Save the updated conversation back to the database
    await conversation.save()

    return llm_response

# Read a conversation by ID
async def read_conversation(conversation_id: str) -> Conversation:
    conversation = await Conversation.get(ObjectId(conversation_id))
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation

# Delete a conversation by ID
async def delete_conversation(conversation_id: str):
    conversation = await Conversation.get(ObjectId(conversation_id))
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    await conversation.delete()
    return {"message": "Conversation deleted successfully"}
