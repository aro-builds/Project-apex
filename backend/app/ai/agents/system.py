from app.ai.agents.base import BaseAgent
from app.ai.kernel.models import AgentInfo
from app.ai.kernel.state import ServiceStatus


class SystemAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            AgentInfo(
                name="System Agent",
                description="Handles monitoring and system management.",
                version="0.1.0",
                status=ServiceStatus.ONLINE,
                capabilities=[
                    "health",
                    "restart",
                    "monitor"
                ]
            )
        )