from scripts.ingest import ingest_and_index
from scripts.ingest_directory import ingest_directory
import os

def ingest_any(path: str):
    if os.path.isdir(path):
        ingest_directory(path)
    elif os.path.isfile(path):
        ingest_and_index(path)
    else:
        raise FileNotFoundError(f"❌ Path not found: {path}")
