class PromptAnalyzer:

    def analyze(self, prompt: str) -> str:

        prompt = prompt.lower()

        if "video" in prompt:
            return "video"

        if "voice" in prompt:
            return "voice"

        if "workflow" in prompt:
            return "workflow"

        return "general"