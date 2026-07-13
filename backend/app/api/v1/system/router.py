from fastapi import APIRouter
from app.api.v1.system.status import router as status_router

router = APIRouter(prefix="/system", tags=["System"])

router.include_router(status_router)