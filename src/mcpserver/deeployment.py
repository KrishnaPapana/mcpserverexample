from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server")

@mcp.tool()
def add_two_numbers(a, b):
    """
    Adds two numbers together.
    Args:
    a -- the first number
    b -- the second number
    Returns:
    The sum of a and b 
    """
    
    return a + b
