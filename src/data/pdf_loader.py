from pathlib import Path
from datetime import datetime
import json
from langchain_community.document_loaders import PyPDFLoader
from collections import defaultdict

ESSENTIAL_METADATA_KEYS = [
    "source",
    "source_path",
    "category",
    "page_number",
    "page_label"
    "total_pages",
    "text_length",
    "load_date"
]

def load_pdf(file_path: str, category: str):
    """
    Load a single PDF and attach only essential metadata to each page.
    Removes unnecessary fields like producer, creator, creationdate, moddate.
    """
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    num_pages = len(docs)
    
    for i, doc in enumerate(docs, start=1):
        # Overwrite metadata with only essential fields
        doc.metadata = {
            "source": Path(file_path).name,
            "source_path": str(Path(file_path)),
            "category": category,
            "page_number": i,
            "page_label": str(i), 
            "total_pages": num_pages,
            "text_length": len(doc.page_content),
            "load_date": datetime.now().isoformat()
        }
    
    return docs

def load_pdfs_from_folder(folder_path: str):
    """
    Load all PDFs in a folder, detect category from folder name.
    """
    folder = Path(folder_path)
    category = folder.name.lower()
    all_docs = []
    for pdf_file in folder.glob("*.pdf"):
        all_docs.extend(load_pdf(str(pdf_file), category))
    return all_docs

def ingest_all_sources(base_raw_path: str = "data/raw"):
    """
    Load PDFs from multiple sources (varsity, sebi_education) 
    and return a combined list of documents.
    """
    base_folder = Path(base_raw_path)
    all_docs = []

    for source_folder in ["varsity", "sebi_education"]:
        folder_path = base_folder / source_folder
        if folder_path.exists():
            docs = load_pdfs_from_folder(str(folder_path))
            all_docs.extend(docs)
        else:
            print(f"Warning: Folder {folder_path} does not exist, skipping.")

    return all_docs

def save_docs_to_json(docs, output_folder="data/interim/raw/"):
    """
    Save extracted docs with metadata to separate JSON files by source.
    Each page is stored as a separate entry.
    """
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    # Group docs by source
    docs_by_source = defaultdict(list)
    for doc in docs:
        source = doc.metadata.get("category", "unknown")
        docs_by_source[source].append({
            "page_content": doc.page_content,
            "metadata": doc.metadata
        })

    # Save each source separately
    for source, pages in docs_by_source.items():
        file_path = output_path / f"all_pdfs_{source}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(pages, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(pages)} pages to {file_path}")
