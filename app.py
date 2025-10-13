import asyncio
from mcp_use import MCPAgent, MCPClient
from langchain_ollama import ChatOllama
import yaml


prompt_path = "system_prompt.yaml"
with open(prompt_path, "r", encoding="utf-8") as f:
    prompt_templates = yaml.safe_load(f)

async def main():
  config = {
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y",
               "chrome-devtools-mcp@latest",
               "--browser-url=http://127.0.0.1:9222"
               ]
      }
    }
  }

  client = MCPClient.from_dict(config)

  llm = ChatOllama(model="qwen3:4b")

  agent = MCPAgent(
      llm=llm,
      client=client,
      system_prompt=prompt_templates,
      memory_enabled=True,
      max_steps=5
  )

  result = await agent.run("What component is related to the part number CL10C330JB8NNNC")
  print(result)

asyncio.run(main())