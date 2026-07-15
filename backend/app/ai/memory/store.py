from threading import Lock
from typing import Dict, Optional

from app.ai.memory.models import MemoryRecord


class MemoryStore:
    """
    Thread-safe in-memory storage.

    Future implementations:
    - SQLite
    - PostgreSQL
    - Redis
    - ChromaDB
    """

    def __init__(self):
        self._lock = Lock()

        self._memory: Dict[str, MemoryRecord] = {}

    def save(self, record: MemoryRecord):

        with self._lock:
            self._memory[record.key] = record

    def get(self, key: str) -> Optional[MemoryRecord]:

        with self._lock:
            return self._memory.get(key)

    def delete(self, key: str):

        with self._lock:
            self._memory.pop(key, None)

    def clear(self):

        with self._lock:
            self._memory.clear()

    def exists(self, key: str) -> bool:

        with self._lock:
            return key in self._memory

    def list_all(self):

        with self._lock:
            return list(self._memory.values())

    def size(self):

        with self._lock:
            return len(self._memory)
        

# Shared memory store (module-level instance)
memory_store = MemoryStore()