from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-powered prompt-driven automation platform for YouTube Shorts.",
)

app.include_router(router, prefix="/api")