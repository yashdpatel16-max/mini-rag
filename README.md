# 🚀 RAG System (Retrieval-Augmented Generation)

An end-to-end **Retrieval-Augmented Generation (RAG)** system that ingests multiple PDFs, stores embeddings in a vector database, retrieves relevant context, and generates intelligent responses using an LLM.

---

## 📌 Features

- 📄 Multi-PDF ingestion
- 🔍 Semantic search using embeddings
- 🧠 Context-aware response generation
- 💬 Chat history stored in MongoDB
- 🐳 Fully containerized with Docker
- ⚙️ CI/CD using GitHub Actions
- ⚡ FastAPI backend with REST endpoints
- 🤖 Local LLM inference using Ollama

---

## 🏗️ Tech Stack

| Layer        | Technology            |
|-------------|----------------------|
| Backend     | FastAPI              |
| Vector DB   | Qdrant               |
| Database    | MongoDB              |
| LLM         | Ollama (local)       |
| Frontend    | React (Vite)         |
| DevOps      | Docker, GitHub Actions |

---

## 📂 Project Structure
rag-system/
│
├── app/
│ ├── ingestion/ # PDF loading & chunking
│ ├── retrieval/ # Embeddings + Qdrant
│ ├── llm/ # Ollama client
│
├── docker-compose.yml
├── Dockerfile
├── main.py
├── requirements.txt
├── README.md


---

## ⚙️ Setup Instructions

1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/mini-rag.git
cd mini-rag

2️⃣ Run with Docker
docker compose up --build

3️⃣ Access API
http://localhost:8000

Swagger Docs:
http://localhost:8000/docs

🔄 API Endpoints
📥 Ingest Documents
POST /ingest
Loads and processes PDFs into the vector database.

💬 Query RAG System
POST /rag-query?query=your_question&user_id=xyz
Returns context-aware response based on stored documents.

🤖 LLM Setup (Ollama)
This project uses Ollama to run a local LLM.

1️⃣ Install Ollama

Download and install from:
https://ollama.com

---

2️⃣ Start Ollama
```bash
ollama serve

3️⃣ Pull a model

For low-resource systems (recommended):
ollama pull tinyllama

4️⃣ Configure model in code

Open:

app/llm/ollama_client.py
Update model name:
MODEL_NAME = "tinyllama"

5️⃣ Important for Docker users

If running inside Docker, update URL:
OLLAMA_URL = "http://host.docker.internal:11434/api/generate

⚠️ Notes
Ollama must be running before querying the API
Ensure port 11434 is accessible
Use smaller models if system has limited RAM

---




🧪 CI/CD Pipeline
✅ Automatic Docker build on every push
✅ Container startup validation
✅ API health check using curl

Implemented using GitHub Actions

🐳 Docker Services
FastAPI (backend)
Qdrant (vector DB)
MongoDB (chat history)

📊 System Flow
User Query
   ↓
Embedding Generation
   ↓
Qdrant Vector Search
   ↓
Context Retrieval
   ↓
LLM (Ollama)
   ↓
Final Response

📌 Future Improvements
🌐 Cloud deployment (Render / AWS)
💬 Chat UI improvements
🔐 Authentication system
📈 Performance optimization

👨‍💻 Author

Yash Patel

⭐ Notes

This project demonstrates:

End-to-end RAG pipeline
Vector database integration
LLM orchestration
Docker-based microservices
CI/CD automation
