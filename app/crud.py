from app.models import Conversation, Message
from app.schemas import ConversationCreate

async def create_conversation_with_message(message: Message) -> Conversation:
    conversation = Conversation(
        title="New Conversation",  
        messages=[message]
    )
    await conversation.insert()  # This saves the conversation to the database
    return conversation
