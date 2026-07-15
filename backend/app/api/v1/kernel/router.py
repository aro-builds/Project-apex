from fastapi import APIRouter

from app.ai.kernel.manager import AIKernel
from app.api.v1.kernel.status import router as status_router

router = APIRouter(prefix="/kernel", tags=["Kernel"])

kernel = AIKernel()


@router.get("/agents", summary="Registered Agents")
async def list_agents():
    return kernel.get_agents()


router.include_router(status_router)