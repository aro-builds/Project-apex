from app.ai.services.ollama import OllamaService


class PromptAnalyzer:

    def __init__(self):
        self.ollama = OllamaService()

    def analyze(self, prompt: str) -> str:

        system_prompt = f"""
You are an AI intent classifier.

Your task is to classify the user's request into exactly ONE of these categories:

video
voice
workflow
general

Examples:

User: Create a YouTube Short about space.
Answer: video

User: Generate a deep male narration.
Answer: voice

User: Execute the automation workflow.
Answer: workflow

User: Hello
Answer: general

Now classify this request.

    User: {prompt}
    Answer:
    """

        response = self.ollama.generate(system_prompt)

        print("===== OLLAMA RESPONSE =====")
        print(response)
        print("===========================")

        return response.strip().lower() 