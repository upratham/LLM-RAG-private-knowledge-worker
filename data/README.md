# Data Directory

This directory contains input and processed data for the RAG system.

## Structure

- **raw/** - Original documents to be ingested
- **processed/** - Processed and chunked documents
  - **pdf_markdown/** - Markdown files converted from PDFs
  - **repo_summaries/** - Repository summaries and documentation

## Adding Documents

1. Place your documents in `raw/` subdirectory
2. Supported formats: `.txt`, `.pdf`, `.docx`
3. Run `python main.py` or use `RAGSystem.ingest_documents()`

### Converting PDFs to Markdown

Use the PDF converter module to convert PDF files to Markdown:

```bash
# Convert all PDFs in data/raw to data/processed/pdf_markdown
python -m src.pdf_converter --input data/raw --output data/processed/pdf_markdown

# Analyze PDFs without converting
python -m src.pdf_converter --input data/raw --analyze-only
```

Or use it programmatically:

```python
from src.pdf_converter import convert_all_pdfs, analyze_pdfs
from pathlib import Path

# Convert PDFs
stats = convert_all_pdfs(Path("data/raw"), Path("data/processed/pdf_markdown"))
print(f"Converted: {stats['success']}, Errors: {stats['errors']}")

# Analyze PDFs
analysis = analyze_pdfs(Path("data/raw"))
print(f"Convertible: {len(analysis['convertible'])}")
print(f"Image-based: {len(analysis['no_text'])}")
print(f"Encrypted: {len(analysis['encrypted'])}")
```

## Examples

```
raw/
├── kb_document_1.txt
├── kb_document_2.txt
├── company_handbook.pdf
└── research_papers/
    ├── paper1.pdf
    └── paper2.txt
```

## Document Best Practices

1. **Format**: Plain text or standard document formats
2. **Size**: Break large files (>1MB) into smaller sections
3. **Language**: Ensure consistent language (preferably English)
4. **Quality**: Clean text without excessive markup or artifacts
5. **Structure**: Organize logically with clear sections

## PDF Notes

- **Text-based PDFs**: Fully supported, text is extracted directly
- **Scanned PDFs**: Not supported without OCR. These files will be skipped (logged as "no text extracted")
- **Encrypted PDFs**: Password-protected PDFs cannot be processed. These will be logged as errors
- **Conversion Details**:
  - 21 PDFs successfully converted to Markdown
  - 15 Image-based PDFs (scanned documents without OCR)
  - 1 Encrypted PDF (password-protected)
  - All output files maintain the original folder structure

## Data Privacy

- Ensure all documents are authorized for processing
- Sensitive information should be redacted
- Follow organizational data policies
- No PII (personally identifiable information) in documents
