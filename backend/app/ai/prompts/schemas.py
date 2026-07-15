from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str


class PromptResponse(BaseModel):
    success: bool
    intent: str
    selected_agents: list[str]
    execution_plan: list[str]