import pandas as pd
from langchain_core.documents import Document

def handle_xlsx(file_path: str) -> list[Document]:
    try:
        dfs = pd.read_excel(file_path, sheet_name=None)
        all_rows = []

        for sheet_name, df in dfs.items():
            for idx, row in df.iterrows():
                row_str = "\n".join([f"{col}: {row[col]}" for col in df.columns])
                all_rows.append(f"[Sheet: {sheet_name}, Row: {idx}]\n{row_str}")

        full_text = "\n\n".join(all_rows)
        return [Document(page_content=full_text, metadata={"source": str(file_path)})]
    except Exception as e:
        print(f"❌ Error reading XLSX: {file_path}: {e}")
        return []
