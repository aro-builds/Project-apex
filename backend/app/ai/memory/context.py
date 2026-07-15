from pydantic import BaseModel


class MemoryContext(BaseModel):
    prompt: str
    intent: str
    response: str | None = None