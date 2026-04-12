# 🤖 AI Agent API with Memory & Authentication (FastAPI + Ollama)

A production-style AI backend built using FastAPI and Ollama that supports multi-turn conversations, API key authentication, and credit-based usage control. This project demonstrates how to build a custom AI agent system without relying on external LLM frameworks.

---

## 🚀 Features

* 🧠 LLM-powered AI responses using Mistral (via Ollama)
* 💬 Context-aware conversations (session-based memory)
* 🔐 API key-based authentication system
* 🎯 Credit-based request limiting system
* ⚡ High-performance FastAPI backend
* 📦 JSON-based API responses
* 🏗️ Clean and modular backend architecture

---

## 🧠 Tech Stack

* **Backend:** FastAPI (Python)
* **LLM Runtime:** Ollama (Mistral model)
* **Environment Management:** python-dotenv
* **API Testing:** Postman / Requests

---

## 🏗️ Architecture

```id="s8n21z"
User → FastAPI → Custom AI Agent → Ollama → Response
```

---

## 📁 Project Structure

```id="y0jtxd"
ai-agent-api/
│── main.py            # FastAPI backend with AI agent logic
│── testapi.py         # API testing script
│── requirements.txt
│── .env               # API key configuration
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash id="3g3n2k"
git clone https://github.com/your-username/your-repo-name.git
cd ai-agent-api
```

---

### 2️⃣ Create Virtual Environment

```bash id="8dntvd"
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash id="qgq4n6"
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```id="o8u7yx"
API_KEY=your_api_key
```

---

### 5️⃣ Install & Run Ollama

Download and install from: https://ollama.com

Run the model:

```bash id="r8rx1c"
ollama run mistral
```

---

### 6️⃣ Run FastAPI Server

```bash id="0x9p7r"
uvicorn main:app --reload
```

---

## 🧪 API Usage

### Endpoint

```id="q6w7jv"
POST /ai-agent
```

---

### Headers

```id="qf6a6j"
x-api-key: your_api_key
Content-Type: application/json
```

---

### Request Body

```json id="y9y6kx"
{
  "prompt": "Explain AI in simple terms"
}
```

---

### Response Example

```json id="e2z6mn"
{
  "status": "success",
  "response": "AI is a technology that enables machines to learn and make decisions like humans.",
  "conversation_length": 3,
  "credits_left": 4
}
```

---

## 🔐 Authentication & Credits

* Each API key starts with **5 credits**
* Each request consumes **1 credit**
* Requests are blocked after credits are exhausted

---

## 🧠 Memory Feature

* Stores conversation per API key
* Enables multi-turn conversations
* Improves response quality with context

---

## ⚠️ Limitations

* Requires local setup of Ollama
* Not directly deployable to cloud without modification

---

## 📈 Future Improvements

* Add database for persistent memory
* Multi-user authentication system
* Admin dashboard for API usage tracking
* Cloud deployment support
* Integration with external tools (search, APIs)
