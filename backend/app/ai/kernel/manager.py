from app.ai.kernel.registry import KernelRegistry

from app.ai.agents.video import VideoAgent
from app.ai.agents.voice import VoiceAgent
from app.ai.agents.workflow import WorkflowAgent
from app.ai.agents.system import SystemAgent


class AIKernel:

    def __init__(self):

        self.registry = KernelRegistry()

        self._load_default_agents()

    def _load_default_agents(self):

        agents = [

            VideoAgent(),
            VoiceAgent(),
            WorkflowAgent(),
            SystemAgent()

        ]

        for agent in agents:

            self.registry.register(agent)

    def get_agents(self):

        return self.registry.list_agents()