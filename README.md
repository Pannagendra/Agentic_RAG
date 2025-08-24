# Agentic RAG: RAG + LangGraph + LangSmith + Drift Monitoring (Local with Ollama)

This is a **Proof of Concept (POC)** for an agentic Retrieval-Augmented Generation (RAG) pipeline, combining orchestration, observability, monitoring, and local LLM inference.

---

##  Key Features

- **LangGraph orchestration**: Modular flow control, fine-grained task coordination  
- **LangSmith observability**: Detailed logging & tracing of requests and prompts (optional; requires API key)  
- **Drift Monitoring via EvidentlyAI**: Automatic detection of embedding or performance drift over time  
- **Local LLM Execution**: Powered by **Ollama (llama3.1:8b)** — efficient and private  
- **Vector Store with FAISS**: Fast, scalable similarity search for retrieval  
- **Agentic Design**: Supports chaining, context-aware agents, and dynamic response strategies

---

##  Architecture (Diagram)

```
graph TB
    subgraph Ingestion
        A[Raw Documents] --> B[Document Chunking]
        B --> C[Embedding Generation]
        C --> D[FAISS Vector Store]
    end

    subgraph Query Flow
        U[User Query] --> E[LangGraph Orchestrator]
        E -->|Retrieve| D
        D --> F[Retrieve Top Context]
        E -->|Invoke| G[Ollama LLM]
        F --> G
        G --> H[LangSmith Logger]
        H --> I[Response Returned]
        H --> J[EvidentlyAI Monitor]
    end
```

---

##  Quick Start

### 1. Prerequisites

- Python 3.11+  
- Ollama installed and running (`llama3.1:8b`)  
- Access to LangSmith (optional – for advanced observability)  
- Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Ingest Documents

```bash
python -m src.ingest data/raw/sample.txt
```

This prepares document embeddings and populates the FAISS store.

### 3. Run the Agentic RAG Pipeline

```bash
python -m src.serve query --query "What is this project about?"
```

### 4. Monitor Drift (Optional)

```bash
python -m src.monitor
```

Track embedding consistency and query-response behavior over time.

---

##  Usage: LangGraph & LangSmith Highlights

- **LangGraph** enables structured orchestration: define directed agent workflows, handle fallback paths, and combine tools dynamically.
- Use `langgraph.yml` (or similar) to define your orchestration logic: multi-step reasoning, inter-agent handoffs, parallel retrieval + reasoning.
- **LangSmith** (if configured via `LANGSMITH_API_KEY`) captures:
  - Full prompt history
  - Latency metrics for each component
  - Error traces and retries  
- Ideal for debugging complex agentic behavior and performance profiling.

---

##  Future Enhancements Roadmap

| Milestone           | Deliverables |
|---------------------|--------------|
| **GPU Acceleration**     | CUDA support for Ollama models (faster inference) |
| **Dockerization / Cloud** | Containerized deployment, optional GPU instances |
| **Agentic Extensions**    | Support for external tool integration—e.g., web search, calculator agents |
| **Advanced RAG Features** | Re-ranking, query expansion, prompt chaining |
| **API Layer**             | REST endpoints for querying, ingestion, and monitoring |
| **UI Dashboard**          | Interactive Streamlit or React UI with visual metrics, config controls |
| **Prometheus / Metrics**  | Export observability data (LangSmith/Evidently) to external dashboards |
| **Multi-Agent Mode**      | Parallel agent invocation, agent arbitration, dynamic orchestration |

---

##  Project Structure

```
Agentic_RAG/
├── src/
│   ├── ingest.py
│   ├── serve.py
│   ├── monitor.py
│   └── langgraph.yml  # pipeline orchestration config
├── data/
│   └── raw/
│       └── sample.txt
├── requirements.txt
├── README.md
└── .env.example        # sample env vars for configuration
```

---

##  Configuration

Create a `.env` file and configure these settings:

```env
OLLAMA_MODEL=llama3.1:8b
OLLAMA_HOST=http://localhost:11434

# FAISS
VECTOR_DB_PATH=./faiss_index/
MAX_RETRIEVALS=5

# LangSmith (optional)
LANGSMITH_API_KEY=your_api_key_here

# Drift Monitoring
MONITORING_ENABLED=true
DRIFT_THRESHOLD=0.1

# LangGraph config file
LANGGRAPH_CONFIG=./src/langgraph.yml
```

---

##  Troubleshooting

- **Ollama not running**?  
  Ensure it's active:
  ```bash
  ollama serve
  ollama run llama3.1:8b "Hello"
  ```

- **LangSmith integration failing**?  
  Confirm `${LANGSMITH_API_KEY}` is set correctly and valid.

- **High drift alerts**?  
  Investigate embedding consistency, data changes, or model shifts.

---

##  Contributing

1. **Fork** the repository  
2. Create a branch: `git checkout -b feature/my-cool-agent`  
3. Implement and **test thoroughly**  
4. Push: `git push origin feature/my-cool-agent`  
5. Open a **Pull Request** — describe your enhancements or fixes

---

##  License

MIT License — see the [LICENSE](LICENSE) file.

---

##  Acknowledgments

- **LangGraph** for orchestration capabilities  
- **LangSmith** for observability  
- **EvidentlyAI** for drift monitoring  
- **Ollama** for local LLM execution  
- **FAISS** for efficient vector search

---

**Built with ❤️ for the AI community**

⭐ **Star this repo if it helped you build better RAG systems!**

---
## 📬 Contact

Made with ❤️ by [Pannagendra KL](https://github.com/Pannagendra)
