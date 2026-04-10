from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
import ollama
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize API key and credits
API_KEY = os.getenv("API_KEY")
user_credits = {API_KEY: 5}

# Initialize FastAPI app
app = FastAPI()

# In-memory chat storage (session-based memory)
chat_memory = {}

# System prompt (AI personality)
SYSTEM_PROMPT = "You are a helpful AI assistant for students."

# Request body model
class PromptRequest(BaseModel):
    prompt: str

# API key verification
def verify_api_key(x_api_key: str = Header(None)):
    credits = user_credits.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key or no credits left")
    return x_api_key

# Main AI Agent Endpoint
@app.post("/ai-agent")
def ai_agent(request: PromptRequest, x_api_key: str = Depends(verify_api_key)):
    
    # Deduct credit
    user_credits[x_api_key] -= 1

    # Get previous chat history
    history = chat_memory.get(x_api_key, [])

    # Add system prompt only once (if new session)
    if not history:
        history.append({"role": "system", "content": SYSTEM_PROMPT})

    # Add user message
    history.append({"role": "user", "content": request.prompt})

    # Call Ollama LLM
    response = ollama.chat(
        model="mistral",
        messages=history
    )

    ai_reply = response["message"]["content"]

    # Save AI response to memory
    history.append({"role": "assistant", "content": ai_reply})
    chat_memory[x_api_key] = history

    return {
        "status": "success",
        "response": ai_reply,
        "conversation_length": len(history),
        "credits_left": user_credits[x_api_key]
    }