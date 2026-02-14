# Contributing to RAG LLM

Thank you for your interest in contributing to RAG LLM! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/LL-RAG-private-knowldge-worker.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/upratham/LL-RAG-private-knowldge-worker.git
cd LL-RAG-private-knowldge-worker

# Run setup script
./setup.sh

# Or manual setup
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small
- Write comments for complex logic

## Testing

Before submitting a PR, ensure all tests pass:

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/unit/test_ingestion.py

# Run with coverage
python -m pytest --cov=src tests/
```

## Adding New Features

1. **Document Loaders**: Add support for new file formats in `src/rag_llm/ingestion/document_loader.py`
2. **Embedding Models**: Add new embedding providers in `src/rag_llm/embeddings/embedding_model.py`
3. **LLM Providers**: Add new LLM integrations in `src/rag_llm/llm/llm_client.py`
4. **Retrieval Methods**: Enhance retrieval strategies in `src/rag_llm/retrieval/retriever.py`

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include tests for new features
- Update documentation as needed
- Ensure all tests pass
- Keep PRs focused on a single feature/fix

## Code Review Process

1. Maintainers will review your PR
2. Address any feedback or requested changes
3. Once approved, your PR will be merged

## Reporting Issues

When reporting issues, please include:

- Description of the issue
- Steps to reproduce
- Expected behavior
- Actual behavior
- System information (OS, Python version, etc.)
- Relevant logs or error messages

## Feature Requests

Feature requests are welcome! Please:

- Check if the feature already exists or is planned
- Provide a clear use case
- Explain the expected behavior
- Consider contributing the feature yourself

## Community Guidelines

- Be respectful and constructive
- Help others learn and grow
- Give credit where it's due
- Focus on what's best for the project

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue for any questions or concerns.
