from app.ai.services.ollama import OllamaService

ollama = OllamaService()

response = ollama.generate("Say hello in one sentence.")

print(response)