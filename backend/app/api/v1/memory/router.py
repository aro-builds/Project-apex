from fastapi import APIRouter
from app.ai.memory.router import router as memory_router

router = APIRouter()

router.include_router(memory_router)