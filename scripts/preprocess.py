from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import os
from scripts.utils.utils import setup_logging, ensure_dir
from scripts.utils.extractors import extract_text_from_pdf, extract_text_from_docx, extract_text_from_xlsx

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed_texts"

def run_preprocessing(skip_files=None):
    setup_logging()
    ensure_dir(PROCESSED_DIR)

    if skip_files is None:
        skip_files = set()

    processed = []

    for filename in os.listdir(RAW_DIR):
        if filename in skip_files:
            print(f"⏭️ Skipping already processed: {filename}")
            continue

        file_path = os.path.join(RAW_DIR, filename)
        name, ext = os.path.splitext(filename)

        try:
            if ext.lower() == ".pdf":
                text = extract_text_from_pdf(file_path)
            elif ext.lower() == ".docx":
                text = extract_text_from_docx(file_path)
            elif ext.lower() in [".xlsx", ".xls"]:
                text = extract_text_from_xlsx(file_path)
            else:
                print(f"🚫 Skipping unsupported file: {filename}")
                continue

            output_path = os.path.join(PROCESSED_DIR, f"{name}.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)

            processed.append(filename)
            print(f"✅ Processed: {filename}")

        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

    return processed


