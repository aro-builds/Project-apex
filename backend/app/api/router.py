from fastapi import APIRouter
from app.api.v1.prompt.router import router as prompt_router
from app.api.v1.router import api_router as v1_router

router = APIRouter()

router.include_router(v1_router, prefix="/v1")
# This links your prompt endpoints to the main API
router.include_router(prompt_router)