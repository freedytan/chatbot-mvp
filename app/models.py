from beanie import Document
from pydantic import Field, BaseModel
from typing import List

class Message(BaseModel):
    content: str

class Conversation(Document):
    title: str
    messages: List[Message] = Field(default_factory=list)
    
    class Settings:
        collection = "conversations"
