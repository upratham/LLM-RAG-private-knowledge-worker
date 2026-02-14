# API Usage Guide

## Table of Contents
1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Component APIs](#component-apis)
4. [Advanced Usage](#advanced-usage)
5. [Configuration](#configuration)

## Installation

```bash
pip install -r requirements.txt
```

## Basic Usage

### Quick Start

```python
from rag_llm.ingestion import DocumentLoader, TextSplitter
from rag_llm.embeddings import EmbeddingModel, VectorStore
from rag_llm.retrieval import Retriever
from rag_llm.llm import LLMClient
from rag_llm.query_processor import QueryProcessor

# 1. Load and process documents
loader = DocumentLoader("path/to/documents")
documents = loader.load()

splitter = TextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# 2. Create embeddings and vector store
embedding_model = EmbeddingModel()
embeddings = embedding_model.embed_texts([c['content'] for c in chunks])

vector_store = VectorStore()
vector_store.add_documents(chunks, embeddings)

# 3. Query the system
retriever = Retriever(vector_store, embedding_model)
llm_client = LLMClient()
processor = QueryProcessor(retriever, llm_client)

result = processor.process_query("Your question here")
print(result['answer'])
```

## Component APIs

### DocumentLoader

```python
from rag_llm.ingestion import DocumentLoader

# Load from file
loader = DocumentLoader("document.pdf")
docs = loader.load()

# Load from directory
loader = DocumentLoader("documents/")
docs = loader.load()

# Supported formats: .txt, .pdf, .docx, .md, .html
```

### TextSplitter

```python
from rag_llm.ingestion import TextSplitter

splitter = TextSplitter(
    chunk_size=1000,      # Max characters per chunk
    chunk_overlap=200     # Overlap between chunks
)

# Split documents
chunks = splitter.split_documents(documents)

# Split single text
text_chunks = splitter.split_text("Long text here...")
```

### EmbeddingModel

```python
from rag_llm.embeddings import EmbeddingModel

# Initialize with default model
model = EmbeddingModel()

# Use specific model
model = EmbeddingModel("sentence-transformers/all-mpnet-base-v2")

# Embed single text
embedding = model.embed_text("Sample text")

# Embed multiple texts
embeddings = model.embed_texts(["Text 1", "Text 2"])

# Get dimension
dim = model.get_embedding_dimension()
```

### VectorStore

```python
from rag_llm.embeddings import VectorStore

# Initialize
store = VectorStore(
    storage_path="data/vector_store",
    use_faiss=True  # Use FAISS for fast search
)

# Add documents
store.add_documents(chunks, embeddings)

# Save to disk
store.save("my_knowledge_base")

# Load from disk
store.load("my_knowledge_base")

# Search
results = store.search(query_embedding, k=5)

# Clear all data
store.clear()
```

### Retriever

```python
from rag_llm.retrieval import Retriever

retriever = Retriever(vector_store, embedding_model)

# Retrieve documents
docs = retriever.retrieve(
    query="What is RAG?",
    k=5,                          # Number of results
    score_threshold=0.7           # Optional minimum score
)

# Get formatted context
context = retriever.retrieve_with_context("What is RAG?", k=5)
```

### LLMClient

```python
from rag_llm.llm import LLMClient

# OpenAI
llm = LLMClient(
    model_name="gpt-3.5-turbo",
    provider="openai",
    api_key="your-api-key",
    temperature=0.7,
    max_tokens=1000
)

# Anthropic
llm = LLMClient(
    model_name="claude-3-sonnet-20240229",
    provider="anthropic",
    api_key="your-api-key"
)

# Generate response
response = llm.generate(
    prompt="Your question",
    context="Retrieved context",
    system_message="Custom system message"
)
```

### QueryProcessor

```python
from rag_llm.query_processor import QueryProcessor

processor = QueryProcessor(
    retriever=retriever,
    llm_client=llm_client,
    k=5,
    system_message="Custom instructions"
)

# Process query
result = processor.process_query(
    query="What is this about?",
    return_sources=True
)

print(result['answer'])
print(result['sources'])
```

## Advanced Usage

### Custom System Messages

```python
custom_message = """
You are an expert assistant specializing in technical documentation.
Answer questions concisely and cite specific document sections.
If information is not in the context, say so clearly.
"""

processor = QueryProcessor(
    retriever=retriever,
    llm_client=llm_client,
    system_message=custom_message
)
```

### Batch Processing

```python
# Process multiple documents
for doc_path in document_paths:
    loader = DocumentLoader(doc_path)
    docs = loader.load()
    chunks = splitter.split_documents(docs)
    
    embeddings = embedding_model.embed_texts([c['content'] for c in chunks])
    vector_store.add_documents(chunks, embeddings)

vector_store.save()
```

### Score Filtering

```python
# Only retrieve highly relevant documents
docs = retriever.retrieve(
    query="Specific technical question",
    k=10,
    score_threshold=0.8  # Higher threshold = more selective
)
```

### Multiple Vector Stores

```python
# Technical docs
tech_store = VectorStore(storage_path="data/technical")
tech_store.load("technical_kb")

# Business docs
business_store = VectorStore(storage_path="data/business")
business_store.load("business_kb")

# Query different stores
tech_retriever = Retriever(tech_store, embedding_model)
business_retriever = Retriever(business_store, embedding_model)
```

## Configuration

### Environment Variables

```bash
# .env file
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
LLM_PROVIDER=openai
LLM_MODEL=gpt-3.5-turbo
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

### YAML Configuration

```python
from rag_llm.utils import load_config

config = load_config("config/config.yaml")

# Use config values
embedding_model = EmbeddingModel(config['embedding']['model_name'])
splitter = TextSplitter(
    chunk_size=config['document_processing']['chunk_size'],
    chunk_overlap=config['document_processing']['chunk_overlap']
)
```

## Error Handling

```python
try:
    loader = DocumentLoader("documents/")
    documents = loader.load()
    
    if not documents:
        print("No documents found")
    else:
        # Process documents
        pass
        
except FileNotFoundError:
    print("Document path not found")
except Exception as e:
    print(f"Error: {str(e)}")
```

## Logging

```python
from rag_llm.utils import setup_logger

logger = setup_logger(
    name="my_app",
    level=logging.INFO,
    log_file="logs/app.log"
)

logger.info("Starting document processing")
logger.error("Failed to load document")
```
