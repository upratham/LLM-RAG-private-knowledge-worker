# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-02-15

### Added

#### Advanced RAG Features
- **LLM-Based Re-ranking**: Implemented `rerank()` function in `src/rag_system.py` that uses Ollama with structured outputs to intelligently re-order retrieved chunks by relevance
- **Query Rewriting**: Added `rewrite_query()` function that optimizes user queries for better semantic search results
- **Chunk Merging**: Implemented `merge_chunks()` utility to combine and deduplicate results from multiple retrieval strategies
- **Pydantic Models**: Added `RankOrder` BaseModel for structured LLM outputs using OpenAI-compatible API

#### Ollama Integration
- **Dual Client Setup**: 
  - OpenAI-compatible client for structured outputs at `http://localhost:11434/v1`
  - LangChain Ollama client for standard chat at `http://localhost:11434`
- **Local LLM Support**: Full integration with Ollama for privacy-first, local LLM inference
- **Model**: Using `llama3.2` as default model

#### System Prompts
- **Personal Knowledge Base Template**: Pre-configured system prompt for answering questions about user profiles, education, experience, and achievements
- **Document Reference Rules**: Instructions to avoid mentioning document names or knowledge base references in responses

### Changed

#### Configuration Updates
- **config.json**:
  - Updated `chunk_size` from 1000 to 700 characters
  - Updated `chunk_overlap` from 100 to 200 characters
  - Changed default LLM provider from "openai" to "ollama"
  - Changed model from "gpt-3.5-turbo" to "llama3.2"
  - Set temperature to 0 (was 0.7) for deterministic outputs
  - Added `ollama` configuration section with host URLs and API key
  - Added `advanced_rag` section with feature flags for query rewriting and re-ranking
  - Added `enable_reranking` flag to retrieval settings

#### Documentation
- **README.md**:
  - Added "LLM-Based Re-ranking" and "Query Rewriting" to features list
  - Updated Technology Stack to include Ollama and structured outputs
  - Added "Advanced RAG System" component section
  - Added Ollama setup instructions
  - Updated configuration examples to reflect current settings
  - Clarified project structure with updated file descriptions

- **docs/API_REFERENCE.md**:
  - Added comprehensive "RAG System Module" section
  - Documented all new functions: `rerank()`, `rewrite_query()`, `merge_chunks()`, `fetch_unranked_chunks()`
  - Added `RankOrder` Pydantic model documentation
  - Added system prompt template documentation
  - Added "Advanced RAG Pipeline Example" with complete workflow
  - Added Ollama setup instructions in configuration section
  - Updated OpenAI-compatible API usage examples

#### Dependencies
- **requirements.txt**:
  - Added `pydantic` for structured data validation and parsing

### Technical Details

#### API Changes
- `src/rag_system.py` now uses `chat.completions.parse()` instead of `chat.completions.create()` for structured outputs
- Re-ranking requires OpenAI-compatible endpoint at `/v1` path (Ollama provides this)

#### Notebook Updates
- `notebooks/pipeline.ipynb`:
  - Updated cell 17 with proper Ollama client configuration
  - Updated cell 18 with `rerank()` function using structured outputs
  - Updated cell 27 with refined query rewriting prompt
  - Fixed typo: "lamma3.2" → "llama3.2"

### Fixed
- **TypeError**: Fixed "You tried to pass a `BaseModel` class to `chat.completions.create()`" by switching to `parse()` method
- **NotFoundError**: Fixed 404 errors by correctly configuring Ollama OpenAI-compatible endpoint URL
- **API Compatibility**: Ensured proper use of Ollama's `/v1` endpoint for OpenAI compatibility

### Breaking Changes
- Default LLM provider changed from OpenAI to Ollama (requires local Ollama installation)
- Chunk size reduced from 1000 to 700 characters (may require re-indexing)
- Temperature changed to 0 for deterministic behavior

### Migration Guide

#### For Existing Users
1. **Install Ollama**:
   ```bash
   # Visit https://ollama.ai for installation
   ollama serve
   ollama pull llama3.2
   ```

2. **Update Configuration**:
   - Your existing `config.json` will work, but consider updating to new defaults
   - Or keep OpenAI by setting `"provider": "openai"` in config

3. **Re-index Documents** (optional but recommended):
   ```python
   # With updated chunk_size=700, chunk_overlap=200
   chunks = chunking(documents, chunk_size=700, chunk_overlap=200)
   vectorstore = embedder("./vectors", chunks)
   ```

4. **Install Pydantic**:
   ```bash
   pip install pydantic
   ```

### Notes
- Ollama provides privacy-first LLM inference (no data leaves your machine)
- OpenAI integration still available by changing provider in config
- Re-ranking feature is optional and can be disabled via config
- Query rewriting improves retrieval quality for conversational queries

---

## [Previous Versions]
See Git history for changes prior to 2026-02-15.
