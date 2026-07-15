from app.ai.agents.base import BaseAgent
from app.ai.kernel.models import AgentInfo
from app.ai.kernel.state import ServiceStatus


class WorkflowAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            AgentInfo(
                name="Workflow Engine",
                description="Handles workflow planning and execution.",
                version="0.1.0",
                status=ServiceStatus.OFFLINE,
                capabilities=[
                    "schedule",
                    "execute",
                    "pipeline"
                ]
            )
        )