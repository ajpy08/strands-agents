from mcp.server import FastMCP
import logging

# Configure logging
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", 
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

mcp = FastMCP("Calculator Server")

@mcp.tool(description="Add two numbers together")
def add(x: float, y: float) -> float:
    """Add two numbers and return the result."""
    logger.info(f"Tool 'add' invoked with x={x}, y={y}")
    result = x + y
    logger.info(f"Tool 'add' result: {result}")
    return result

@mcp.tool(description="Subtract two numbers")
def subtract(x: float, y: float) -> float:
    """Subtract two numbers and return the result."""
    logger.info(f"Tool 'subtract' invoked with x={x}, y={y}")
    result = x - y
    logger.info(f"Tool 'subtract' result: {result}")
    return result

@mcp.tool(description="Multiply two numbers")
def multiply(x: float, y: float) -> float:
    """Multiply two numbers and return the result."""
    logger.info(f"Tool 'multiply' invoked with x={x}, y={y}")
    result = x * y
    logger.info(f"Tool 'multiply' result: {result}")
    return result

@mcp.tool(description="Divide two numbers")
def divide(x: float, y: float) -> float:
    """Divide two numbers and return the result."""
    logger.info(f"Tool 'divide' invoked with x={x}, y={y}")
    if y == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")
    result = x / y
    logger.info(f"Tool 'divide' result: {result}")
    return result

mcp.run(transport="streamable-http")