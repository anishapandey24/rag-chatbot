from langchain_core.documents import Document

def handle_txt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return [Document(page_content=content, metadata={"source": str(file_path)})]
    except Exception as e:
        print(f"❌ Error reading TXT: {file_path}: {e}")
        return []
