from PIL import Image
import pytesseract
from langchain_core.documents import Document

def handle_image(file_path):
    try:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        if text.strip():
            print(f"📸 OCR success for image: {file_path}")
            return [Document(page_content=text, metadata={"source": str(file_path)})]
        else:
            print(f"⚠️ No text found in image: {file_path}")
            return []
    except Exception as e:
        print(f"❌ Failed to process image {file_path}: {e}")
        return []
