from fastapi import APIRouter

router = APIRouter()

@router.get("", summary="Perform a system health check")
async def health_check():
    """Checks if the API server is up and responsive."""
    return {"status": "healthy", "message": "API is operational"}

@router.get("/status", summary="Get internal system status metrics")
async def system_status():
    """Returns status metrics of background processing workers."""
    return {"status": "idle", "active_tasks": 0, "queue_depth": 0}
