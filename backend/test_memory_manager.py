from app.ai.memory.manager import MemoryManager
from app.ai.memory.models import MemoryRecord

manager = MemoryManager()

record = MemoryRecord(
    key="project",
    value={
        "name": "Project APEX",
        "version": "0.1.0"
    }
)

manager.save_memory(record)

print("Exists:", manager.memory_exists("project"))

print("Count:", manager.memory_count())

print("Record:", manager.get_memory("project"))

print("All:", manager.list_memories())

manager.delete_memory("project")

print("Exists after delete:", manager.memory_exists("project"))