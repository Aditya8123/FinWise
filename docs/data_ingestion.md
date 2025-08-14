# Data Ingestion Documentation

## Overview
This document describes the **data ingestion pipeline** for processing PDFs into chunked JSON/JSONL files for further analysis or NLP tasks. The pipeline handles **raw PDF extraction, cleaning, splitting into pages, and chunking text**.

---

## Project Structure

```

FinWise/
├── data/                  # Raw and processed data (ignored by git)
│   ├── raw/               # Original PDF files
│   ├── interim/           # Intermediate JSON files
│   │   ├── raw/
│   │   ├── cleaned/
│   │   └── split/
│   └── processed/         # Chunked JSONL files
├── src/                   # Python modules
│   ├── config.py
│   ├── data/
│   │   ├── pdf_loader.py  # Extract PDFs to JSON pages
│   │   ├── cleaners.py    # Clean page content
│   │   └── chunkers.py    # Chunk pages into smaller pieces
├── notebooks/             # Jupyter notebooks
│   └── 01_pdf_extraction.ipynb   # Notebook for interactive extraction and testing
├── .gitignore
├── README.md
└── requirements.txt

````

---

## Pipeline Steps

### 1. Raw PDF Extraction
- PDFs are stored in `data/raw/`.
- Extracted to **page-level JSON** using `src/data/pdf_loader.py` or interactively via `notebooks/01_pdf_extraction.ipynb`.
- Each page object contains:
  ```json
  {
    "page_content": "Text of the page",
    "metadata": {
        "source": "filename.pdf",
        "source_path": "...",
        "category": "category_name",
        "page_number": 1,
        "page_label": "1",
        "total_pages": 32,
        "text_length": 1000,
        "load_date": "2025-08-14T16:18:13"
    }
  }
````

### 2. Cleaning

* `src/data/cleaners.py` removes unwanted characters, whitespace, and formatting issues.
* Cleaned JSON files are saved in `data/interim/cleaned/`.
* File naming convention: `all_pdfs_<source>_cleaned_partX.json`

### 3. Splitting

* Optional splitting for large files into smaller JSONs.
* Stored in `data/interim/split/`.
* File naming convention: `all_pdfs_<source>_cleaned_partX.json`

### 4. Chunking

* `src/data/chunkers.py` splits page content into smaller chunks.
* Parameters:

  * `chunk_size` (e.g., 800 characters)
  * `overlap` (e.g., 100 characters)
* Uses **streaming + batch writing** to generate `.jsonl` files efficiently.
* Chunk JSON structure:

  ```json
  {
    "chunk_id": "filename_page1_chunk1",
    "chunk_content": "Chunked text content",
    "metadata": {
        "source": "filename.pdf",
        "page_number": 1,
        ...
    }
  }
  ```
* Stored in `data/processed/` with naming: `<original_file_stem>_chunks.jsonl`.

---

## Jupyter Notebook

* `notebooks/01_pdf_extraction.ipynb` allows **interactive exploration** of the pipeline.
* Can be used for:

  * Loading PDFs
  * Inspecting page extraction
  * Running cleaning and chunking in a step-by-step manner
  * Debugging or testing on smaller PDF subsets

---

## Summary Statistics

* Total raw pages extracted
* Total cleaned pages
* Total split pages
* Number of chunks per file
* Total chunks across all files

Scripts in `src/data/` provide automatic summary generation.

---

## Notes

* `.jsonl` is preferred for chunked files to enable **streaming reads** and **faster writes**.
* Large PDFs or intermediate JSON are ignored in GitHub via `.gitignore`.
* Ensure `chunk_size > overlap` to avoid infinite loops.

---

## References

* Python libraries: `pathlib`, `json`, `ijson`, `tqdm`
* Scripts: `src/data/pdf_loader.py`, `src/data/cleaners.py`, `src/data/chunkers.py`
* Notebook: `notebooks/01_pdf_extraction.ipynb`

```



