from app.ai.memory.models import MemoryRecord
from app.ai.memory.store import MemoryStore

store = MemoryStore()

record = MemoryRecord(
    key="project",
    value={
        "name": "Project APEX",
        "status": "Development"
    }
)

store.save(record)

print(store.get("project"))

print(store.exists("project"))

print(store.size())

print(store.list_all())

store.delete("project")

print(store.exists("project"))