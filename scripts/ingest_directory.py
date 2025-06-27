import os
from scripts.ingest import ingest_and_index

def ingest_directory(folder_path):
    supported_exts = ['.pdf', '.docx', '.txt', '.csv']
    for root, _, files in os.walk(folder_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in supported_exts:
                file_path = os.path.join(root, file)
                try:
                    ingest_and_index(file_path)
                except Exception as e:
                    print(f"❌ Failed on {file_path}: {e}")

if __name__ == "__main__":
    ingest_directory("data/raw")
