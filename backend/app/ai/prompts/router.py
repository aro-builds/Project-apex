from app.ai.prompts.analyzer import PromptAnalyzer
from app.ai.prompts.planner import ExecutionPlanner


class PromptRouter:

    def __init__(self):

        self.analyzer = PromptAnalyzer()
        self.planner = ExecutionPlanner()

    def process(self, prompt: str):

        intent = self.analyzer.analyze(prompt)

        plan = self.planner.create_plan(intent)

        return {
            "intent": intent,
            "plan": plan
        }