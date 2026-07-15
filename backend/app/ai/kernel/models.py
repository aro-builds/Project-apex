from dataclasses import dataclass
from typing import List


@dataclass
class AgentInfo:
    name: str
    description: str
    version: str
    status: str
    capabilities: List[str]