# Import FastMCP server framework used to expose functions as tools
# that can be consumed by LLMs/agents via the Model Context Protocol (MCP)
from mcp.server.fastmcp import FastMCP

# Initialize MCP server instance with a name (used for identification/logging)
mcp = FastMCP('Chess.com')

# Import helper functions that interact with Chess.com public API
# (These functions handle actual HTTP requests and data retrieval)
from .chess_api import get_player_profile, get_player_stats


# Register this function as an MCP tool
# Tools are callable functions that LLM agents can invoke dynamically
@mcp.tool()
def get_chess_player_profile(username: str):
    """
    MCP Tool: Fetch public profile of a Chess.com player by username.

    Args:
        username (str): Chess.com username

    Returns:
        dict: Player profile data retrieved from Chess.com API

    Purpose:
        Exposes player profile retrieval as a callable tool
        for LLM agents (e.g., in agentic workflows or toolchains)
    """
    return get_player_profile(username)


# Register another MCP tool for fetching player statistics
@mcp.tool()
def get_chess_player_stats(username: str):
    """
    MCP Tool: Fetch game statistics of a Chess.com player by username..

    Args:
        username (str): Chess.com username

    Returns:
        dict: Player statistics including ratings, game history, etc.

    Purpose:
        Allows LLM agents to query player performance data dynamically
    """
    return get_player_stats(username)


def main():
    """
    Entry point for running the MCP server.

    transport="stdio":
        - Uses standard input/output for communication
        - Commonly used when integrating with local LLM runtimes,
          CLI tools, or agent frameworks

    The server will listen for incoming tool calls and execute
    the registered functions accordingly.
    """
    mcp.run(transport="stdio")


# Standard Python entry point check
# Ensures main() runs only when this script is executed directly
if __name__ == "__main__":
    main()