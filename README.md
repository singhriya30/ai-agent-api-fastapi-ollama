# 🤖 AI Agent API with Memory & Authentication

A production-style AI backend built using FastAPI and Ollama that supports multi-turn conversations, API key authentication, and credit-based usage control.

---

## 🚀 Features

* 🔹 LLM-powered AI responses using Mistral (via Ollama)
* 🔹 Context-aware conversations (memory support)
* 🔹 API key-based authentication
* 🔹 Credit-based request limiting system
* 🔹 FastAPI backend (high performance)
* 🔹 JSON-based API responses
* 🔹 Scalable and modular design

---

## 🧠 Tech Stack

* **Backend:** FastAPI (Python)
* **LLM:** Ollama (Mistral model)
* **Environment Management:** python-dotenv
* **API Testing:** Requests / Postman

---

## 📁 Project Structure

```
API-For-Your-LLM/
│── main.py              # FastAPI backend with AI agent
│── test-api.py          # Script to test API
│── requirements.txt     # Dependencies
│── .env                 # API key configuration
│── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/singhriya30/ai-agent-api.git
cd ai-agent-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
API_KEY= your_api_key
```

---

### 5️⃣ Install & Run Ollama

Download from: https://ollama.com

Then run:

```bash
ollama run mistral
```

---

### 6️⃣ Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

## 🧪 API Usage

### Endpoint

```
POST /ai-agent
```

### Headers

```
x-api-key: your_api_key
Content-Type: application/json
```

### Request Body

```json
{
  "prompt": "Explain AI in simple terms"
}
```

---

### Response Example

```json
{
  "status": "success",
  "response": "AI is a technology that allows machines to think and learn like humans.",
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
* Enables multi-turn context-aware responses
* Improves AI interaction quality

---

## 📌 Future Improvements

* 🔹 Database integration for persistent memory
* 🔹 Multiple user authentication system
* 🔹 Frontend UI (React / Next.js)
* 🔹 Deployment on cloud (AWS / Render)
