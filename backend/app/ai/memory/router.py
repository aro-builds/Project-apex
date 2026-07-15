from fastapi import APIRouter, HTTPException

from app.ai.memory.models import MemoryRecord
from app.ai.memory.service import MemoryService

router = APIRouter(prefix="/memory", tags=["Memory"])

memory = MemoryService()


@router.post("/save")
def save_memory(record: MemoryRecord):
    return memory.save(record)


@router.get("/list")
def list_memory():
    return memory.list()


@router.get("/{key}")
def get_memory(key: str):

    result = memory.get(key)

    if result is None:
        raise HTTPException(status_code=404, detail="Memory not found")

    return result


@router.delete("/{key}")
def delete_memory(key: str):

    memory.delete(key)

    return {
        "success": True,
        "message": "Memory deleted."
    }


@router.delete("/clear/all")
def clear_memory():

    memory.clear()

    return {
        "success": True,
        "message": "All memory cleared."
    }


@router.get("/stats/count")
def count_memory():

    return {
        "count": memory.count()
    }