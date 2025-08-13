# FinWise  
**From finance PDFs to explainable answers with RAG and Concept Graphs**  

FinWise is a **learning-focused** project that explores how to build a **Retrieval-Augmented Generation (RAG)** system for finance knowledge, enriched with **concept graphs** for better explainability.  
The goal is not just to make it work — but to deeply understand each step, compare multiple approaches, and document the reasoning behind every design decision.

---

## 🚀 Features

- **PDF Ingestion & Cleaning**  
  Parse and normalize finance PDFs (Zerodha Varsity, SEBI investor guides, glossaries).
  
- **Multiple Chunking Strategies**  
  Fixed-size, heading-aware, and semantic chunking — with experiments to measure impact on retrieval.

- **Embeddings & Vector Stores**  
  Compare MiniLM, BGE-small, and other models; store vectors in ChromaDB and FAISS.

- **Concept Graph Construction**  
  Extract keywords, cluster related terms, and build graphs using similarity and co-occurrence.

- **RAG Backend with FastAPI**  
  Integrate local LLMs via Ollama (Mistral / LLaMA3) for offline, private generation.

- **Graph Visualization**  
  NetworkX, PyVis, or Plotly for interactive exploration of finance concepts.

- **Experiment-Driven Development**  
  Every module is tested against multiple strategies; metrics and trade-offs are logged.

---

## 📂 Repository Structure

```

FinWise/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env.example
├── Makefile
├── data/
│   ├── raw/          # Original PDFs
│   ├── interim/      # Parsed text/JSON
│   └── processed/    # Chunks + embeddings
├── docs/
│   ├── architecture.md
│   ├── decisions/    # Design decision logs
│   ├── learning_log.md
│   └── api.md
├── notebooks/
│   ├── 01_pdf_extraction.ipynb
│   ├── 02_chunking_experiments.ipynb
│   ├── 03_embeddings_bench.ipynb
│   ├── 04_graph_construction.ipynb
│   └── 05_rag_eval.ipynb
├── src/                    # <-- Python modules go here
│   ├── config.py
│   ├── data/
│   │   ├── pdf_loader.py
│   │   ├── cleaners.py
│   │   └── chunkers.py
│   ├── embeddings/
│   │   ├── base.py
│   │   ├── sentence_transformers_backend.py
│   │   └── ollama_backend.py
│   ├── vectordb/
│   │   ├── chroma_store.py
│   │   └── faiss_store.py
│   ├── graph/
│   │   ├── concepts.py
│   │   ├── graph_builders.py
│   │   └── graph_viz.py
│   ├── rag/
│   │   ├── retriever.py
│   │   ├── rerankers.py
│   │   └── pipeline.py
│   └── api/
│       └── app.py
└── tests/


````

---

## 📊 Project Goals

1. **Learn deeply** — every component is explored through multiple approaches.  
2. **Document decisions** — using `docs/decisions/` with problem, options, decision, reasoning.  
3. **Interview readiness** — be able to explain the system end-to-end with metrics and trade-offs.  
4. **Production-style repo** — modular `src/` code, experiment `notebooks/`, and clear docs.  

---

## 🧪 Planned Experiments

- **Chunking:** 300 vs 500 vs 800 tokens; 10% vs 20% overlap.  
- **Embeddings:** MiniLM vs BGE-small-en vs BGE-m3.  
- **Vector Stores:** Chroma vs FAISS (Flat / IVF).  
- **Graph Edges:** similarity vs co-occurrence vs hybrid.  
- **Reranking:** with vs without cross-encoder.  
- **Graph-Aware Retrieval:** personalized PageRank boosts.

---

## 🛠️ Tech Stack

- **Data Processing:** PyMuPDF, regex-based cleaners  
- **Embeddings:** SentenceTransformers, Ollama  
- **Vector DB:** ChromaDB, FAISS  
- **Graphs:** NetworkX, PyVis, Plotly  
- **Backend:** FastAPI  
- **LLM:** Mistral / LLaMA3 (quantized) via Ollama  
- **Evaluation:** RAGAS, Recall@K, MRR, nDCG  
- **Deployment:** Hugging Face Spaces → Docker

---

## 📖 How to Run (Dev Mode)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create .env from example
cp .env.example .env

# 3. Run FastAPI server
uvicorn src.api.app:app --reload
````

---

## 🗂️ Documentation

* **Architecture Overview:** `docs/architecture.md`
* **Design Decisions:** `docs/decisions/`
* **Learning Log:** `docs/learning_log.md`
* **API Docs:** `docs/api.md`

---

## 📅 Roadmap

* [ ] Build baseline pipeline with fixed chunking + Chroma + MiniLM
* [ ] Add heading-aware chunking
* [ ] Compare MiniLM vs BGE-small embeddings
* [ ] Implement concept graph construction
* [ ] Integrate Ollama LLM backend
* [ ] Add reranking + graph-aware retrieval
* [ ] Deploy demo on Hugging Face Spaces
* [ ] Containerize with Docker

---

## 📜 License

MIT License — see `LICENSE` for details.

---

## ✍️ Author

Created by **Aditya Tejpal** — a hands-on learning project for deep-diving into RAG, graphs, and finance data.


