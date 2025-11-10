# 🚀 RAG POC with Docker, Ollama, and ChromaDB

This project demonstrates a **fully containerized Retrieval-Augmented Generation (RAG)** pipeline using:
- **Ollama** – Local LLMs (e.g., `mistral`)
- **ChromaDB** – Vector database
- **Docker Compose** – Orchestrates everything
- **Python App** – Ingestion & querying

**Tested on Windows/Linux/macOS with Docker Desktop.**

## Quick Start
1. `docker compose up --build -d`
2. `docker compose exec rag_app python ingestion_script.py`
3. `docker compose exec rag_app python query_app.py`

## Files
- `docker-compose.yaml`: Services config
- `Dockerfile`: Python app build
- `requirements.txt`: Dependencies
- `.env.example`: Config (copy to `.env`)
- `ingestion_script.py`: Load PDF to ChromaDB
- `query_app.py`: Interactive RAG queries
- `data/my_docs.pdf`: Sample PDF

## Stop
`docker compose down -v`

*Built for local AI – November 07, 2025*