# 🚀 RAG POC with Docker, Ollama, and ChromaDB


This folder contains the README and instructions for the RAG (Retrieval-Augmented Generation) proof-of-concept that uses Ollama in Docker and a simple ingestion/query app.

## Overview

This project shows a minimal RAG PoC using a Docker Compose stack that runs Ollama and an application container (rag_app) that ingests documents and answers queries.

## Folder structure (expected)

- docker-compose.yml              # Compose file that defines services (ollama, rag_app, etc.)
- rag-poc/                        # This folder (project root for RAG PoC)
  - README.md                     # This file
  - rag_app/
    - ingestion_script.py         # Script to ingest documents into the vector DB / store
    - query_app.py                # Script to query the app / interact with the model
    - Dockerfile                  # Dockerfile for rag_app (if present)
    - requirements.txt            # Python dependencies for rag_app (if present)
  - data/                         # Source documents, or pointers to them
  - models/                       # Local model artifacts (if used)
  - notebooks/                    # Optional notebooks for experimentation
  - configs/                      # Config files (e.g., llm/config.yaml, ingest settings)

Adjust the exact layout to match the repository contents. If a file from the list above is missing, check the repo and add it as needed.

## Prerequisites

- Docker (latest recommended)
- Docker Compose (v2+ integrated with docker as `docker compose`)
- Python 3.8+ (for local scripts inside rag_app)
- git

## RUN (Copy-Paste)

Open PowerShell in the repository root and run the following commands (copy-paste):

```powershell
cd rag-poc

# 1. FULL CLEAN
docker compose down -v
docker system prune -f

# 2. START
docker compose up --build -d

# 3. WATCH OLLAMA
docker compose logs -f ollama


Wait for:
textOllama ready!
Press Ctrl+C
```

Then run ingestion and query steps:

```powershell
# 4. INGEST
docker compose exec rag_app python ingestion_script.py

# 5. QUERY
docker compose exec rag_app python query_app.py
Ask:
> What is this document about?
```

Notes:
- The exact container name (`rag_app`) and script names (`ingestion_script.py`, `query_app.py`) are based on a common layout. If your repository uses different names, update the commands accordingly.
- If the rag_app container needs environment variables or mounted volumes, verify them in docker-compose.yml before running the ingestion step.
- For large datasets, the ingestion step may take time and may require more memory; consider running locally with adequate resources.

## Troubleshooting

- If docker compose fails to start, run `docker compose up` without `-d` to see logs.
- If the ollama service does not reach the "Ollama ready!" message, inspect its logs and ensure any model downloads or license steps finish.
- If ingestion fails due to missing dependencies, exec into the container to inspect or add a requirements.txt and rebuild the image.

## Next steps

- Update this README with exact file names and arguments from your repository after confirming the real layout.
- Add example config files and a sample dataset under data/ so new users can run the PoC end-to-end.

---