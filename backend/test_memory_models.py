from app.ai.memory.models import MemoryRecord

memory = MemoryRecord(
    key="project",
    value={
        "name": "Project APEX"
    }
)

print(memory.model_dump())