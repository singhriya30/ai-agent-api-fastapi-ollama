from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
import ollama
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
user_credits = {API_KEY: 5}

app = FastAPI()

chat_memory = {}

SYSTEM_PROMPT = """
You are an AI agent. 
You can decide when to use tools.

Available tools:
1. search: Use for latest information from internet

If needed, respond like:
TOOL: search: <query>

Otherwise, answer normally.
"""

class PromptRequest(BaseModel):
    prompt: str

def verify_api_key(x_api_key: str = Header(None)):
    credits = user_credits.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key or no credits left")
    return x_api_key

# Simple Search Tool
def search_tool(query: str):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    try:
        res = requests.get(url).json()
        return res.get("AbstractText", "No result found")
    except:
        return "Search failed"

@app.post("/ai-agent")
def ai_agent(request: PromptRequest, x_api_key: str = Depends(verify_api_key)):

    user_credits[x_api_key] -= 1

    history = chat_memory.get(x_api_key, [])

    if not history:
        history.append({"role": "system", "content": SYSTEM_PROMPT})

    history.append({"role": "user", "content": request.prompt})

    # First LLM call
    response = ollama.chat(
        model="mistral",
        messages=history
    )

    ai_reply = response["message"]["content"]

    # Check if tool is needed
    if "TOOL: search:" in ai_reply:
        query = ai_reply.split("TOOL: search:")[-1].strip()

        tool_result = search_tool(query)

        history.append({"role": "assistant", "content": f"Tool result: {tool_result}"})

        # Second LLM call with tool result
        response = ollama.chat(
            model="mistral",
            messages=history
        )

        ai_reply = response["message"]["content"]

    history.append({"role": "assistant", "content": ai_reply})
    chat_memory[x_api_key] = history

    return {
        "status": "success",
        "response": ai_reply,
        "conversation_length": len(history),
        "credits_left": user_credits[x_api_key]
    }
