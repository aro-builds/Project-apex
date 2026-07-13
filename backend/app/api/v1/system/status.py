from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/status", tags=["System"])
async def get_system_status():
    return {
        "success": True,
        "message": "System status retrieved successfully",
        "data": {
            "system": "Project APEX",
            "version": "0.1.0",

            "services": {
                "backend": "online",
                "ollama": "offline",
                "workflow_engine": "offline",
                "video_engine": "offline",
                "voice_engine": "offline"
            }
        },
        "timestamp": datetime.utcnow().isoformat()
    }