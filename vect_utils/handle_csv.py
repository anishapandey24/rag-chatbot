import pandas as pd
from langchain_core.documents import Document

def handle_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        text = df.astype(str).replace("nan", "").to_string(index=False)
        return [Document(page_content=text, metadata={"source": str(file_path)})]
    except Exception as e:
        print(f"❌ Error reading CSV: {file_path}: {e}")
        return []
