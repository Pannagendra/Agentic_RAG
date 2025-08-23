# RAG + LangGraph + LangSmith + Drift Monitoring (Local with Ollama)

This is a **POC project** that demonstrates a Retrieval-Augmented Generation (RAG) pipeline built with:
- **LangGraph** for orchestration
- **LangSmith** for observability (optional, skip if no API key)
- **EvidentlyAI** for drift monitoring
- **Ollama (llama3.1:8b)** as the local LLM

## 🚀 Quickstart

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Ingest documents into FAISS
```bash
python -m src.ingest data/raw/sample.txt
```

### 3. Run the RAG pipeline (local LLM)
```bash
python -m src.serve query --query "What is this project about?"
```

### 4. Monitor Drift
```bash
python -m src.monitor
```

---
