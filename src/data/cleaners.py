from pathlib import Path
import json
import re

def clean_text(text: str) -> str:
    """
    Perform basic text cleaning:
    - Remove extra spaces, newlines, tabs
    - Remove repeated headers/footers (simple heuristic)
    - Normalize quotes and hyphens
    """
    text = re.sub(r'\s+', ' ', text)
    text = text.replace("“", '"').replace("”", '"').replace("–", "-")
    text = re.sub(r'Page \d+ of \d+', '', text, flags=re.IGNORECASE)
    return text.strip()

def clean_docs(input_folder="data/interim/raw/", output_folder="data/interim/cleaned/"):
    """
    Load all JSON files in input_folder, clean text, and save one cleaned JSON per file.
    Metadata is preserved.
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    json_files = list(input_path.glob("*.json"))
    if not json_files:
        print(f"No JSON files found in {input_folder}")
        return

    for json_file in json_files:
        with open(json_file, "r", encoding="utf-8") as f:
            pages = json.load(f)
        
        cleaned_pages = []
        for page in pages:
            cleaned_text = clean_text(page['page_content'])
            cleaned_pages.append({
                "page_content": cleaned_text,
                "metadata": page['metadata']
            })
        
        output_file = output_path / f"{json_file.stem}_cleaned.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(cleaned_pages, f, ensure_ascii=False, indent=2)
        
        print(f"Saved {len(cleaned_pages)} cleaned pages to {output_file}")

def split_all_cleaned_jsons(
    input_folder: str = "data/interim/cleaned/",
    output_folder: str = "data/interim/split/",
    pages_per_file: int = 500
) -> None:
    """
    Scan a folder for all *_cleaned.json files and split them into smaller JSON files.
    Each split file will have _partX appended to the name.

    Args:
        input_folder: Folder containing *_cleaned.json files.
        output_folder: Folder where split JSON files will be saved.
        pages_per_file: Number of pages per split file.
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise FileNotFoundError(f"Folder {input_folder} does not exist.")

    cleaned_files = list(input_path.glob("*_cleaned.json"))
    if not cleaned_files:
        print("No *_cleaned.json files found in folder.")
        return

    for file_path in cleaned_files:
        with open(file_path, "r", encoding="utf-8") as f:
            pages = json.load(f)

        total_pages = len(pages)
        num_files = (total_pages + pages_per_file - 1) // pages_per_file  # ceil division

        for i in range(num_files):
            start_idx = i * pages_per_file
            end_idx = min(start_idx + pages_per_file, total_pages)
            chunk_pages = pages[start_idx:end_idx]

            split_file_name = f"{file_path.stem}_part{i+1}.json"
            split_file_path = output_path / split_file_name

            with open(split_file_path, "w", encoding="utf-8") as f:
                json.dump(chunk_pages, f, ensure_ascii=False, indent=2)

            print(f"Saved {len(chunk_pages)} pages to {split_file_path}")

    print("\n✅ All *_cleaned.json files have been split.")
