from fastapi import APIRouter

from app.ai.kernel.manager import AIKernel

router = APIRouter()

kernel = AIKernel()


@router.get("/status", summary="Kernel Status")
async def kernel_status():

    agents = kernel.get_agents()

    services = {}

    for agent in agents:
        services[agent.name] = agent.status

    return {
        "success": True,
        "data": {
            "kernel": "running",
            "registered_agents": len(agents),
            "services": services,
        },
    }