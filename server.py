from mcp import MCPServer
from agent import agent

server = MCPServer(
    agents=[agent]
)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8001)
