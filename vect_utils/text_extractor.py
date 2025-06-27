from PyPDF2 import PdfReader
import docx
import csv
import os 
def handle_pdf(file_path):
    reader = PdfReader(file_path)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

def docx_handler(file_path):
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def handle_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return "\n".join([", ".join(row) for row in reader])

def text_extractor(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
