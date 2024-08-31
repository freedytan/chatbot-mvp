from pydantic import BaseModel
from typing import List
from app.models import Message

class ConversationCreate(BaseModel):
    user_id: str
    messages: List[Message]
