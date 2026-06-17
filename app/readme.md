
# AI Knowledge Assistant (RAG)

## Overview

AI Knowledge Assistant is a Retrieval Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions in natural language.

The system extracts text from PDFs, creates embeddings, stores them in ChromaDB, retrieves relevant content, and uses a local Mistral LLM to generate context-aware answers.


## Features

- PDF Upload
- PDF Text Extraction
- Text Chunking with Overlap
- Embedding Generation
- ChromaDB Vector Storage
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Metadata Support
- Source Citations
- Logging
- Local LLM Integration (Mistral)


## Architecture

PDF Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Semantic Search
    ↓
Mistral LLM
    ↓
Answer + Citations



## Tech Stack

- Python
- FastAPI
- Mistral 7B
- llama.cpp
- Sentence Transformers
- ChromaDB
- PyPDF



## Project Structure

app/
│
├── routes/
│   ├── upload.py
│   └── chat.py
│
├── services/
│   ├── pdf_service.py
│   ├── chunk_service.py
│   ├── embedding_service.py
│   ├── vector_service.py
│   ├── rag_service.py
│   └── llm_service.py
│
├── main.py
│
data/
chroma_db/



## Installation

### Clone Repository

git clone <repo-url>

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt


## Run Application

uvicorn app.main:app --reload

http://127.0.0.1:8000/docs




