# scripts/run_pipeline.py
import sys
import os
from scripts.ingest import ingest_and_index

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

processed_files = []
skipped_files = []
unsupported_files = []

def ingest_any(path: str):
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for fname in files:
                fpath = os.path.join(root, fname)
                try:
                    result = ingest_and_index(fpath)
                    if result == 'processed':
                        processed_files.append(fpath)
                    elif result == 'skipped':
                        skipped_files.append(fpath)
                    elif result == 'unsupported':
                        unsupported_files.append(fpath)
                except Exception as e:
                    print(f"❌ {fpath}: {e}")
    else:
        try:
            result = ingest_and_index(path)
            if result == 'processed':
                processed_files.append(path)
            elif result == 'skipped':
                skipped_files.append(path)
            elif result == 'unsupported':
                unsupported_files.append(path)
        except Exception as e:
            print(f"❌ {path}: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.run_pipeline <file_or_folder>")
        sys.exit(1)

    ingest_any(sys.argv[1])

    print("\n🔚 Pipeline Summary")
    print(f"✅ Processed files: {len(processed_files)}")
    print(f"⏭️ Skipped (already processed): {len(skipped_files)}")
    print(f"❌ Unsupported file types: {len(unsupported_files)}")
    print("✅ All done.")

if __name__ == "__main__":
    main()