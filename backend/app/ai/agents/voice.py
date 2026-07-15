from app.ai.agents.base import BaseAgent
from app.ai.kernel.models import AgentInfo
from app.ai.kernel.state import ServiceStatus


class VoiceAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            AgentInfo(
                name="Voice Engine",
                description="Handles speech generation and audio processing.",
                version="0.1.0",
                status=ServiceStatus.OFFLINE,
                capabilities=[
                    "tts",
                    "mix",
                    "noise_removal"
                ]
            )
        )