from app.ai.prompts.analyzer import PromptAnalyzer
from app.ai.prompts.planner import ExecutionPlanner
from app.ai.memory.service import MemoryService


class PromptRouter:

    def __init__(self):
        self.analyzer = PromptAnalyzer()
        self.planner = ExecutionPlanner()
        self.memory = MemoryService()

    def process(self, prompt: str):

        intent = self.analyzer.analyze(prompt)

        self.memory.save_prompt(
            prompt=prompt,
            intent=intent,
        )

        plan = self.planner.create_plan(intent)

        return {
            "intent": intent,
            "plan": plan,
        }