import os
from dotenv import load_dotenv
from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.models.openai import OpenAIModel
from strands.models.ollama import OllamaModel
from strands.models import BedrockModel

from strands.tools.mcp.mcp_client import MCPClient

# Cargar variables de entorno desde archivo .env
load_dotenv(override=True)


def create_streamable_http_transport():
    return streamablehttp_client("http://localhost:8000/mcp/")


def create_model_from_env():
    """
    Crea el modelo basado en la variable de entorno MODEL_TYPE.
    Opciones: 'openai', 'ollama', 'bedrock' (default)
    """
    model_type = os.getenv("MODEL_TYPE", "bedrock").lower()
    if not model_type:
        raise ValueError("La variable de entorno MODEL_TYPE no está configurada")

    print(f"Using {model_type} model")

    if model_type == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "La variable de entorno OPENAI_API_KEY no está configurada para el modelo OpenAI"
            )

        return OpenAIModel(
            client_args={"api_key": api_key},
            model_id=os.getenv("OPENAI_MODEL_ID", "gpt-3.5-turbo"),
            params={
                "max_tokens": int(os.getenv("OPENAI_MAX_TOKENS", "1000")),
                "temperature": float(os.getenv("OPENAI_TEMPERATURE", "0.7")),
            },
        )

    elif model_type == "ollama":
        return OllamaModel(
            host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            model_id=os.getenv("OLLAMA_MODEL_ID", "qwen3:1.7b"),
            temperature=float(os.getenv("OLLAMA_TEMPERATURE", "0.2")),
            keep_alive=os.getenv("OLLAMA_KEEP_ALIVE", "10m"),
            stop_sequences=os.getenv("OLLAMA_STOP_SEQUENCES", "###,END").split(","),
            options={"top_k": int(os.getenv("OLLAMA_TOP_K", "40"))},
        )

    elif model_type == "bedrock":
        return BedrockModel(
            # model_id="anthropic.claude-sonnet-4-20250514-v1:0",
            temperature=0.3,
            top_p=0.8,
            region_name="us-west-2"
        )

    else:
        raise ValueError(
            f"Tipo de modelo no soportado: {model_type}. Opciones válidas: 'openai', 'ollama', 'bedrock'"
        )


streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

# Use the MCP server in a context manager
with streamable_http_mcp_client:
    # Get the tools from the MCP server
    tools = streamable_http_mcp_client.list_tools_sync()

    # Crear modelo basado en variables de entorno
    model = create_model_from_env()

    # Create an agent with the MCP tools
    agent = Agent(model=model, tools=tools)

    message = """
I have 4 sequential math operations to perform. Use only mcp tools to confirm the script works before outputting it.

1. Add 10 and 50.
2. Take the result from step 1 and multiply it by 2.
3. Take the result from step 2 and divide it by 3.
4. Take the result from step 3 and subtract 32 from it.

print the final result from step 4 in JSON format
"""

    response = agent(message)
