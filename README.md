cat > README.md << 'EOF'
# 🚀 Mini RAG System (Retrieval-Augmented Generation)

An end-to-end **RAG system** that ingests PDFs, stores embeddings in a vector database, retrieves relevant context, and generates answers using a local LLM.

---

## ⚡ Quick Start (Recommended)

docker compose up --build

Then:

1. Install Ollama → https://ollama.com  
2. Run:
ollama serve  
ollama pull tinyllama  

3. Open API docs:
http://localhost:8000/docs

---

## 📌 Features

- Multi-PDF ingestion  
- Semantic search with embeddings  
- Context-aware responses  
- Chat history using MongoDB  
- Dockerized services  
- CI/CD using GitHub Actions  
- Local LLM using Ollama  

---

## 🏗️ Tech Stack

- Backend: FastAPI  
- Vector DB: Qdrant  
- Database: MongoDB  
- LLM: Ollama  
- Frontend: React (Vite)  
- DevOps: Docker, GitHub Actions  

---

## 📂 Project Structure

rag-system/
├── app/
│   ├── ingestion/
│   ├── retrieval/
│   ├── llm/
├── docker-compose.yml
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md

---

## ⚙️ Setup

git clone https://github.com/yashdpatel16-max/mini-rag.git  
cd mini-rag  
docker compose up --build  

---

## 🤖 Ollama Setup

ollama serve  
ollama pull tinyllama  

In code:

MODEL_NAME = "tinyllama"  

For Docker:

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

---

## 🔄 API

POST /ingest  
POST /rag-query  

---

## 🧠 Flow

Query → Embedding → Qdrant → Context → LLM → Response

---

## 👨‍💻 Author

Yash Patel

---

## ⭐ Highlights

- End-to-end RAG pipeline  
- Docker microservices  
- CI/CD automation  
EOF
