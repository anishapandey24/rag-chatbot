import os
from pathlib import Path
from vect_utils.handle_pdf import handle_pdf
from vect_utils.docx_handler import handle_docx
from vect_utils.xlsx_handler import handle_xlsx
from vect_utils.handle_csv import handle_csv
from vect_utils.image_handler import handle_image
from vect_utils.txt_handler import handle_txt

def extract_text(file_path):
    file_path = Path(file_path)
    suffix = file_path.suffix.lower()
    docs = []

    if suffix == ".pdf":
        print(f"🔍 Processing PDF: {file_path.name}")
        docs = handle_pdf(file_path)
        if docs:
            print(f"✅ PDF processed: {file_path.name} ({len(docs)} documents)")
        else:
            print(f"⚠️ PDF skipped or empty: {file_path.name}")

    elif suffix == ".docx":
        print(f"🔍 Processing DOCX: {file_path.name}")
        docs = handle_docx(file_path)
        if docs:
            print(f"✅ DOCX processed: {file_path.name} ({len(docs)} documents)")
        else:
            print(f"⚠️ DOCX skipped or empty: {file_path.name}")

    elif suffix == ".xlsx":
        print(f"🔍 Processing Excel: {file_path.name}")
        docs = handle_xlsx(file_path)
        if docs:
            print(f"✅ Excel processed: {file_path.name} ({len(docs)} documents)")
        else:
            print(f"⚠️ Excel skipped or empty: {file_path.name}")

    elif suffix == ".csv":
        print(f"🔍 Processing CSV: {file_path.name}")
        docs = handle_csv(file_path)
        if docs:
            print(f"✅ CSV processed: {file_path.name} ({len(docs)} documents)")
        else:
            print(f"⚠️ CSV skipped or empty: {file_path.name}")

    elif suffix in [".jpg", ".jpeg", ".png"]:
        print(f"🖼️ Processing Image: {file_path.name}")
        docs = handle_image(file_path)
        if docs:
            print(f"✅ Image processed: {file_path.name} ({len(docs)} documents)")
        else:
            print(f"⚠️ Image skipped or OCR failed: {file_path.name}")

    elif suffix == ".txt":
        print(f"🔍 Processing TXT: {file_path.name}")
        docs = handle_txt(file_path)
        if docs:
            print(f"✅ TXT processed: {file_path.name} ({len(docs)} documents)")
        else:
            print(f"⚠️ TXT skipped or empty: {file_path.name}")

    else:
        print(f"❌ Unsupported file type: {file_path.name} ({suffix})")
        return 'unsupported'

    return docs if docs else 'skipped'

