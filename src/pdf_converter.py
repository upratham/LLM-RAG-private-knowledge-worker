"""
PDF to Markdown Converter Module

This module provides functionality to convert PDF files to Markdown format.
It handles text extraction from PDFs with error handling for encrypted and image-based PDFs.

Usage:
    python pdf_converter.py --input data/raw --output data/processed/pdf_markdown
    or import and use directly:
    from src.pdf_converter import convert_all_pdfs
"""

import argparse
from pathlib import Path
from typing import Dict, List, Tuple
import pdfplumber
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def pdf_to_text(pdf_path: Path) -> str:
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Extracted text from all pages joined with double newlines
        
    Raises:
        Exception: If PDF is encrypted or cannot be read
    """
    text_parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text_parts.append(page_text)
    return "\n\n".join(text_parts).strip()


def convert_all_pdfs(input_dir: Path, output_dir: Path) -> Dict[str, int]:
    """
    Convert all PDFs in input directory to Markdown files.
    
    Recursively processes PDFs while maintaining folder structure.
    Errors are logged but do not halt processing.
    
    Args:
        input_dir: Root directory containing PDFs
        output_dir: Root directory for output Markdown files
        
    Returns:
        Dictionary with conversion statistics:
        {
            "success": int,      # Successfully converted
            "no_text": int,      # Image-based PDFs (no extractable text)
            "errors": int        # Encrypted or other errors
        }
    """
    pdf_files = sorted(input_dir.rglob("*.pdf"))
    if not pdf_files:
        logger.warning("No PDF files found in input directory.")
        return {"success": 0, "no_text": 0, "errors": 0}

    output_dir.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    no_text_count = 0
    error_count = 0
    
    logger.info(f"Found {len(pdf_files)} PDF(s) to process...")
    
    for pdf_path in pdf_files:
        rel_path = pdf_path.relative_to(input_dir)
        out_path = output_dir / rel_path.with_suffix(".md")
        out_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            text = pdf_to_text(pdf_path)
            if not text:
                logger.warning(f"[SKIP] No text extracted: {rel_path}")
                no_text_count += 1
                continue

            out_path.write_text(text, encoding="utf-8")
            logger.info(f"[OK] {rel_path}")
            success_count += 1
            
        except Exception as e:
            logger.error(f"[ERROR] {rel_path}: {type(e).__name__}")
            error_count += 1

    return {
        "success": success_count,
        "no_text": no_text_count,
        "errors": error_count
    }


def analyze_pdfs(input_dir: Path) -> Dict[str, any]:
    """
    Analyze all PDFs and categorize them by conversion status.
    
    Args:
        input_dir: Root directory containing PDFs
        
    Returns:
        Dictionary with categorized PDF paths:
        {
            "convertible": List[str],     # Successfully converts to Markdown
            "no_text": List[str],         # Image-based PDFs (no text)
            "encrypted": List[Tuple]      # Encrypted or error PDFs with error type
        }
    """
    pdf_files = sorted(input_dir.rglob("*.pdf"))
    results = {
        "convertible": [],
        "no_text": [],
        "encrypted": []
    }
    
    if not pdf_files:
        logger.warning("No PDF files found.")
        return results
    
    logger.info(f"Analyzing {len(pdf_files)} PDF(s)...")
    
    for pdf_path in pdf_files:
        rel_path = pdf_path.relative_to(input_dir)
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = "\n\n".join([page.extract_text() or "" for page in pdf.pages]).strip()
                if text:
                    results["convertible"].append(str(rel_path))
                else:
                    results["no_text"].append(str(rel_path))
        except Exception as e:
            results["encrypted"].append((str(rel_path), type(e).__name__))
    
    return results


def print_analysis_report(input_dir: Path, analysis: Dict) -> None:
    """
    Print a formatted analysis report of PDFs.
    
    Args:
        input_dir: Root directory for relative path display
        analysis: Analysis results from analyze_pdfs()
    """
    print("\n" + "=" * 70)
    print("PDF ANALYSIS REPORT")
    print("=" * 70)
    
    if analysis["no_text"]:
        print("\nIMAGE-BASED PDFs (No extractable text):")
        print("-" * 70)
        for path in sorted(analysis["no_text"]):
            print(f"  {input_dir / path}")
    
    if analysis["encrypted"]:
        print("\nENCRYPTED/ERROR PDFs:")
        print("-" * 70)
        for path, error in sorted(analysis["encrypted"]):
            print(f"  {input_dir / path} [{error}]")
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Convertible:  {len(analysis['convertible'])}")
    print(f"  Image-based:  {len(analysis['no_text'])}")
    print(f"  Encrypted:    {len(analysis['encrypted'])}")
    print(f"  Total:        {len(analysis['convertible']) + len(analysis['no_text']) + len(analysis['encrypted'])}")
    print("=" * 70 + "\n")


def main():
    """Command-line interface for PDF conversion."""
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown format"
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/raw"),
        help="Input directory containing PDFs (default: data/raw)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/pdf_markdown"),
        help="Output directory for Markdown files (default: data/processed/pdf_markdown)"
    )
    parser.add_argument(
        "--analyze-only",
        action="store_true",
        help="Only analyze PDFs without converting"
    )
    
    args = parser.parse_args()
    input_dir = args.input.resolve()
    output_dir = args.output.resolve()
    
    if not input_dir.exists():
        logger.error(f"Input directory not found: {input_dir}")
        return
    
    if args.analyze_only:
        logger.info("Analyzing PDFs...")
        analysis = analyze_pdfs(input_dir)
        print_analysis_report(input_dir, analysis)
    else:
        logger.info(f"Converting PDFs from {input_dir} to {output_dir}...")
        stats = convert_all_pdfs(input_dir, output_dir)
        print(f"\nConversion Summary:")
        print(f"  Successfully converted: {stats['success']}")
        print(f"  Image-based (no text):  {stats['no_text']}")
        print(f"  Errors/Encrypted:       {stats['errors']}")
        print(f"  Total processed:        {sum(stats.values())}")


if __name__ == "__main__":
    main()
