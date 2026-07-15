from typing import Dict

from app.ai.agents.base import BaseAgent


class KernelRegistry:

    def __init__(self):

        self._agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent):

        self._agents[agent.get_info().name] = agent

    def get(self, name: str):

        return self._agents.get(name)

    def list_agents(self):

        return [

            agent.get_info()

            for agent in self._agents.values()

        ]