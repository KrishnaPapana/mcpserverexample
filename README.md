# MCP Server Deepdive Deployment

## Installation Steps

### 1. Clone the Repository
```
git clone https://github.com/KrishnaPapana/mcpserverexample.git
cd mcpserverexample
```

### 2. Set Up Python Environment
- Ensure you have Python 3.12 or higher installed.
- (Recommended) Create and activate a virtual environment:
```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -U pip
pip install .
```

### 4. Run the MCP Server
```
mcp-server
```

This will start the MCP server using the entry point defined in `pyproject.toml`.

---

For more details, see the project documentation or source code.

---

## MCP Client Configuration

You can add the following to your MCP client config file to automatically install and run the server:

```json
{
    "mcpserver":{
        "server":{
            "command": "uv",
            "args":[
                "--from",
                "git+https://github.com/KrishnaPapana/mcpserverexample.git",
                "mcp-server"
            ]
        }
    }
}
```
