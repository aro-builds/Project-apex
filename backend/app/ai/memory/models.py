from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class MemoryRecord(BaseModel):
    key: str
    value: Dict[str, Any]

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class MemoryResponse(BaseModel):
    success: bool
    message: str


class ConversationContext(BaseModel):
    session_id: str
    last_prompt: Optional[str] = None
    last_intent: Optional[str] = None
    active_agent: Optional[str] = None


class UserPreferences(BaseModel):
    preferred_voice: Optional[str] = None
    preferred_language: Optional[str] = "English"
    preferred_resolution: Optional[str] = "1080x1920"