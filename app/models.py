# app/models.py

from beanie import Document
from pydantic import Field, BaseModel
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    role: str = Field(default= 'User')
    content: str
    time_created: Optional[datetime] = Field(default_factory=datetime.now)

class Conversation(Document):
    title: str
    messages: List[Message] = Field(default_factory=list)
    
    class Settings:
        collection = "conversations"
