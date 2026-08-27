import os
from langchain_community.document_loaders import PyPDFLoader

# Build path relative to this script's location, not the terminal's cwd
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, "sample_docs", "sample.pdf")

if not os.path.exists(pdf_path):
    print(f"Error: Please place a PDF file at '{pdf_path}' before running this script.")
else:
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    print(docs)