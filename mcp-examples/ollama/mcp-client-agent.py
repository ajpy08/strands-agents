from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from strands.models.ollama import OllamaModel

def create_streamable_http_transport():
   return streamablehttp_client("http://localhost:8000/mcp/")

streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

# Use the MCP server in a context manager
with streamable_http_mcp_client:
    # Get the tools from the MCP server
    tools = streamable_http_mcp_client.list_tools_sync()

    ollama_model = OllamaModel(
        host="http://localhost:11434",  # Ollama server address
        model_id="qwen3:1.7b", # Specify which model to use
        temperature=0.2,
        keep_alive="10m",
        stop_sequences=["###", "END"],
        options={"top_k": 40}
    )

    # Create an agent with the MCP tools
    agent = Agent(
        model=ollama_model,
        tools=tools
    )

    # Use the agent within the MCP context
    # response = agent("What is 125 plus 375?")
    response = agent("What is 125 plus 375? Then multiply the result by 2 and divide by 3. Finally, subtract 100 from the result. Use only the mcp tools to do this.")