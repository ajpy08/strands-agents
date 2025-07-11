import os
from dotenv import load_dotenv
from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.models.openai import OpenAIModel
from strands.tools.mcp.mcp_client import MCPClient

# Cargar variables de entorno desde archivo .env
load_dotenv()


def create_streamable_http_transport():
    return streamablehttp_client("http://localhost:8000/mcp/")


streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

# Use the MCP server in a context manager
with streamable_http_mcp_client:
    # Get the tools from the MCP server
    tools = streamable_http_mcp_client.list_tools_sync()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada")

    model = OpenAIModel(
        client_args={
            "api_key": api_key,
        },
        # **model_config
        model_id="gpt-3.5-turbo",
        params={
            "max_tokens": 1000,
            "temperature": 0.7,
        },
    )

    # Create an agent with the MCP tools
    agent = Agent(model=model, tools=tools)

    message = """
I have 4 requests:

1. What is 10 + 50?
2. The last result multiplied by 2
3. Then divide by 3
4. Finally substract 32
   Use only mcp tools to confirm that the script works before outputting it
"""

    response = agent(message)
