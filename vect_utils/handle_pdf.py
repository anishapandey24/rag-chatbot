import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from langchain_core.documents import Document

def handle_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        pages = []

        for i, page in enumerate(doc):
            try:
                text = page.get_text()
                if text.strip():  # only keep non-empty pages
                    pages.append(text)
            except Exception as e:
                print(f"⚠️ Could not extract text from page {i} in {file_path}: {e}")

        if pages:
            combined_text = "\n".join(pages)
            return [Document(page_content=combined_text, metadata={"source": file_path, "method": "fitz"})]

        print(f"📄 Falling back to OCR for PDF: {file_path}")

    except Exception as e:
        print(f"❌ Error opening PDF with fitz: {file_path}: {e}")

    # --- OCR fallback ---
    try:
        images = convert_from_path(file_path)
        ocr_pages = []

        for i, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            if text.strip():
                ocr_pages.append(f"[Page {i+1}]\n{text.strip()}")

        if ocr_pages:
            combined_text = "\n\n".join(ocr_pages)
            return [Document(page_content=combined_text, metadata={"source": file_path, "method": "ocr"})]
        else:
            print(f"⚠️ OCR found no extractable text in PDF: {file_path}")
            return []

    except Exception as e:
        print(f"❌ OCR processing failed for {file_path}: {e}")
        return []
