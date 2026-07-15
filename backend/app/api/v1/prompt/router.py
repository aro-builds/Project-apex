from fastapi import APIRouter

from app.ai.prompts.router import PromptRouter
from app.ai.prompts.schemas import PromptRequest

router = APIRouter(prefix="/prompt", tags=["Prompt"])

prompt_handler = PromptRouter()

@router.post("/process")
async def process_prompt(request: PromptRequest):

    result = prompt_handler.process(request.prompt)

    return {
        "success": True,
        "data": result
    }
