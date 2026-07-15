from datetime import datetime
from typing import List, Optional

from app.ai.memory.models import MemoryRecord
from app.ai.memory.store import memory_store


class MemoryManager:

    def __init__(self):
        self.store = memory_store

    def save_memory(self, record: MemoryRecord) -> MemoryRecord:
        """
        Save a new memory record.
        If the key already exists, update the timestamp.
        """

        existing = self.store.get(record.key)

        if existing:
            record.created_at = existing.created_at

        record.updated_at = datetime.utcnow()

        self.store.save(record)

        return record

    def get_memory(self, key: str) -> Optional[MemoryRecord]:
        return self.store.get(key)

    def delete_memory(self, key: str):
        self.store.delete(key)

    def clear_memory(self):
        self.store.clear()

    def list_memories(self) -> List[MemoryRecord]:
        return self.store.list_all()

    def memory_exists(self, key: str) -> bool:
        return self.store.exists(key)

    def memory_count(self) -> int:
        return self.store.size()