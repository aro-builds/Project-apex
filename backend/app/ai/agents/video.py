from app.ai.agents.base import BaseAgent
from app.ai.kernel.models import AgentInfo
from app.ai.kernel.state import ServiceStatus


class VideoAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            AgentInfo(
                name="Video Engine",
                description="Handles video generation and editing.",
                version="0.1.0",
                status=ServiceStatus.OFFLINE,
                capabilities=[
                    "render",
                    "caption",
                    "transition"
                ]
            )
        )