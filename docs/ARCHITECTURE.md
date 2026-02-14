# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         RAG LLM System                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      1. Document Ingestion                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ DocumentLoader│  │ TextSplitter │  │   Metadata   │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         │                 │                  │                  │
│         └─────────────────┴──────────────────┘                  │
│                           │                                     │
│                     Documents + Chunks                          │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     2. Embedding Generation                      │
│  ┌──────────────────────────────────────────────────┐           │
│  │              EmbeddingModel                      │           │
│  │  (Sentence Transformers / OpenAI / Custom)       │           │
│  └──────────────────────────────────────────────────┘           │
│                           │                                     │
│                    Vector Embeddings                            │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      3. Vector Storage                           │
│  ┌──────────────────────────────────────────────────┐           │
│  │               VectorStore                        │           │
│  │        (FAISS / Numpy-based Search)              │           │
│  └──────────────────────────────────────────────────┘           │
│                                                                 │
│  Index: [doc1_vec, doc2_vec, ..., docN_vec]                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                       4. Query Processing                        │
└─────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
            │                               │
            ▼                               ▼
    ┌─────────────┐               ┌─────────────┐
    │  Retriever  │               │ LLM Client  │
    └─────────────┘               └─────────────┘
            │                               │
            │ Similarity Search             │ Context + Query
            ▼                               ▼
    ┌─────────────┐               ┌─────────────┐
    │Top-K Docs   │───────────────>│  Response   │
    └─────────────┘               └─────────────┘

## Data Flow

1. **Ingestion Phase** (Offline)
   - User adds documents to data/documents/
   - DocumentLoader reads files (PDF, DOCX, TXT, etc.)
   - TextSplitter chunks documents with overlap
   - EmbeddingModel generates vector embeddings
   - VectorStore indexes and saves embeddings

2. **Query Phase** (Online)
   - User submits query via CLI or API
   - EmbeddingModel encodes query to vector
   - Retriever searches VectorStore for similar documents
   - Top-K most relevant chunks are retrieved
   - QueryProcessor formats context for LLM
   - LLMClient generates response with context
   - Response returned to user with sources

## Component Responsibilities

### Document Ingestion (`src/rag_llm/ingestion/`)
- Load documents from various formats
- Split text into semantic chunks
- Preserve metadata (source, filename, etc.)

### Embeddings (`src/rag_llm/embeddings/`)
- Generate vector representations
- Manage embedding models
- Store and retrieve vectors efficiently

### Retrieval (`src/rag_llm/retrieval/`)
- Semantic similarity search
- Rank and filter results
- Format context for LLM

### LLM Integration (`src/rag_llm/llm/`)
- Connect to various LLM providers
- Handle API calls and responses
- Manage prompts and context

### Query Processor (`src/rag_llm/query_processor/`)
- Orchestrate the complete pipeline
- Combine retrieval and generation
- Return formatted responses

### Utils (`src/rag_llm/utils/`)
- Logging and monitoring
- Configuration management
- Helper functions

## Design Principles

1. **Modularity**: Each component is independent and reusable
2. **Extensibility**: Easy to add new providers and formats
3. **Configurability**: YAML/ENV configuration for flexibility
4. **Testability**: Clear interfaces for unit and integration tests
5. **Scalability**: Support for large document collections

## Technology Stack

- **Python 3.8+**: Core language
- **Sentence Transformers**: Embedding generation
- **FAISS**: Vector similarity search
- **OpenAI/Anthropic/HuggingFace**: LLM providers
- **PyPDF2/python-docx/BeautifulSoup**: Document parsing
- **PyYAML**: Configuration management
- **pytest**: Testing framework
