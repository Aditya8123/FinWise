from pathlib import Path
import json
from typing import Generator
import ijson
from tqdm import tqdm

def chunk_text_generator(text: str, chunk_size: int = 500, overlap: int = 50) -> Generator[str, None, None]:
    """
    Yield text chunks with optional overlap.
    Ensures start always moves forward to avoid infinite loops.
    """
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")
    
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()
        if chunk:
            yield chunk
        start += chunk_size - overlap  # move forward safely

def chunk_docs_streaming(
    input_folder="data/interim/split",
    output_folder="data/processed",
    chunk_size=500,
    overlap=50,
    jsonl_output=True,  # if True, writes JSONL (faster and safer)
    batch_size=100  # number of chunks to write at once
):
    """
    Stream each cleaned JSON file, create chunks page-by-page,
    and write chunks efficiently to avoid MemoryError.
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    json_files = list(input_path.glob("*.json"))
    if not json_files:
        print(f"No JSON files found in {input_folder}")
        return

    for file in json_files:
        print(f"\nProcessing {file.name} ...")
        if jsonl_output:
            output_file = output_path / f"{file.stem}_chunks.jsonl"
        else:
            output_file = output_path / f"{file.stem}_chunks.json"

        batch = []
        first_chunk = True

        with open(file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
            pages = ijson.items(f_in, "item")
            pages = list(pages)  # if you want total length for tqdm
            for page in tqdm(pages, desc=f"Chunking {file.name}", unit="page"):
                page_content = page.get("page_content", "")
                metadata = page.get("metadata", {})

                for i, chunk in enumerate(chunk_text_generator(page_content, chunk_size, overlap), start=1):
                    chunk_data = {
                        "chunk_id": f"{metadata.get('source', 'unknown')}_page{metadata.get('page_number', '0')}_chunk{i}",
                        "chunk_content": chunk,
                        "metadata": metadata
                    }

                    if jsonl_output:
                        # JSONL: write one line per chunk
                        batch.append(json.dumps(chunk_data, ensure_ascii=False))
                    else:
                        # Array JSON: handle commas
                        if not first_chunk:
                            f_out.write(",\n")
                        f_out.write(json.dumps(chunk_data, ensure_ascii=False))
                        first_chunk = False

                    # Write batch to disk if batch_size reached
                    if jsonl_output and len(batch) >= batch_size:
                        f_out.write("\n".join(batch) + "\n")
                        batch = []

            # write remaining batch
            if jsonl_output and batch:
                f_out.write("\n".join(batch) + "\n")
            
            if not jsonl_output:
                f_out.write("\n]")  # close JSON array

        print(f"Saved chunks to {output_file}")

