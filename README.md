# ♟️ Chess.com MCP Server

An **MCP (Model Context Protocol) server** that exposes public Chess.com APIs as callable tools for LLMs and agent-based systems.

This project enables **AI agents, MCP clients, and agentic platforms** to fetch real-time chess player data such as profiles and game statistics.

---

## 🚀 Features

- 🔎 Fetch player profile data
- 📊 Retrieve player statistics (ratings, win/loss, etc.)
- 🤖 Fully compatible with MCP-based LLM tool calling
- ⚡ Lightweight and easy to integrate with agent frameworks

---

## 🧠 Why this project?

Modern **Agentic AI systems** rely on:

- Tool calling
- External API integrations
- Structured data retrieval

This project demonstrates how to:

- Wrap real-world APIs as **LLM tools**
- Build an **MCP server from scratch**
- Enable **AI agents to interact with external systems**

---

## 🔌 APIs Used

This server uses the official Chess.com public APIs:

### 1. Player Profile

- **Endpoint:**
  `https://api.chess.com/pub/player/{username}`
- **Description:**
  Returns public profile details of a player

### 2. Player Stats

- **Endpoint:**
  `https://api.chess.com/pub/player/{username}/stats`
- **Description:**
  Returns ratings, win/loss stats, and performance data

---

## 🛠️ Installation & Usage

You can connect this MCP server to any MCP-compatible host (e.g., Claude Desktop, VS Code, custom agents).

### Add to MCP Config

```json
{
  "mcpServers": {
    "chess": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/devaraganesh999/mcp-chess.git",
        "chess"
      ]
    }
  }
}
```

---

## ▶️ Available Tools

### `get_chess_player_profile`

Fetches public profile data for a given username.

**Input:**

```json
{
  "username": "hikaru"
}
```

---

### `get_chess_player_stats`

Fetches player statistics including ratings and game performance.

**Input:**

```json
{
  "username": "hikaru"
}
```

---

## 🧪 Tested With

- Claude Desktop
- Visual Studio Code (MCP integrations)

---

## 🏗️ Project Structure

```bash
mcp-chess/
│── chess/
│   ├── server.py        # MCP server with tool definitions
│   ├── chess_api.py    # Chess.com API integration
│── pyproject.toml       # Project configuration
│── README.md
```

---

## 🎯 Use Cases

- AI agents fetching real-time chess data
- LLM-based analytics or assistants
- Learning MCP and tool-based AI systems
- Building blocks for **agent orchestration systems**

---

## 👨‍💻 Author

**Ganesh**

Aspiring **AI Engineer / Agentic AI Engineer** focused on:

- LLM systems
- MCP & tool integration
- Scalable AI architectures

---

## 📌 Notes

- Uses only public APIs (no authentication required)
- Designed to be lightweight and easily extensible
- Can be expanded with more Chess.com endpoints

---

## ⭐ If you find this useful

Give it a star ⭐ and feel free to contribute!

Thanks to Chess.com

---
