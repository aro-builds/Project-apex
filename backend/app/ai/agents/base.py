from abc import ABC
from app.ai.kernel.models import AgentInfo


class BaseAgent(ABC):

    def __init__(self, info: AgentInfo):
        self.info = info

    def get_info(self) -> AgentInfo:
        return self.info