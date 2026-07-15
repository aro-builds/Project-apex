from fastapi import APIRouter

from app.api.v1.system.router import router as system_router

from app.api.v1.kernel.router import router as kernel_router

api_router = APIRouter()

api_router.include_router(system_router)

api_router.include_router(kernel_router)