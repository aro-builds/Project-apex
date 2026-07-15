from app.ai.memory.manager import MemoryManager
from app.ai.memory.models import MemoryRecord
from app.ai.memory.context import MemoryContext


class MemoryService:

    def __init__(self):
        self.manager = MemoryManager()

    def save(self, record: MemoryRecord):
        return self.manager.save_memory(record)

    def get(self, key: str):
        return self.manager.get_memory(key)

    def list(self):
        return self.manager.list_memories()

    def delete(self, key: str):
        self.manager.delete_memory(key)

    def clear(self):
        self.manager.clear_memory()

    def exists(self, key: str):
        return self.manager.memory_exists(key)

    def count(self):
        return self.manager.memory_count()

    def save_prompt(
        self,
        prompt: str,
        intent: str,
        response: str | None = None,
    ):
        record = MemoryRecord(
            key=f"prompt:{self.count()+1}",
            value=MemoryContext(
                prompt=prompt,
                intent=intent,
                response=response,
            ).model_dump(),
        )

        return self.save(record)