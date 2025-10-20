from mcp2py import load
import dspy

lm = dspy.LM('ollama_chat/qwen3:4b', api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm)

browser =load("npx chrome-devtools-mcp@latest --headless")

browser_agent = dspy.ReAct("command -> results", tools=browser.tools)

res = browser_agent(command="Go on https://www.findchips.com/detail/CL10C330JB8NNNC/Samsung-Electro--Mechanics and tell me what is this product")

res

print(res.results)