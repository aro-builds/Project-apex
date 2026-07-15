from ollama import Client


class OllamaService:

    def __init__(self):
        self.client = Client(host="http://127.0.0.1:11434")

    def generate(self, prompt: str, model: str = "qwen2.5-coder:1.5b") -> str:

        response = self.client.generate(
            model=model,
            prompt=prompt
        )

        return response["response"]