from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator, current_time

# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="qwen3:1.7b", # Specify which model to use
    temperature=0.2,
    keep_alive="10m",
    stop_sequences=["###", "END"],
    options={"top_k": 40}
)

# Create an agent using the Ollama model
agent = Agent(
    model=ollama_model,
    tools=[calculator, current_time]
)

# Use the agent
# agent("Tell me about AWS Strands agents. In a paragraph, explain what AWS Strands agents are and how they work.") # Prints model output to stdout by default
# response = agent("What's the square root of 144 plus the current time?")
agent("Dime el resultado de 1+1. Dime la respuesta en español.") # Prints model output to stdout by default