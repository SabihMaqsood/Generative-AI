import os
from langchain_community.document_loaders import TextLoader

# Setup Sample Directory & File
os.makedirs("sample_docs", exist_ok=True)
file_path = "sample_docs/sample.txt"

with open(file_path, "w", encoding="utf-8") as f:
    f.write("LangChain simplifies the process of building LLM-powered applications using modular components.")

# Load Document
loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

# Display Results
print(f"Total Documents Loaded: {len(documents)}")
print(f"Content: {documents[0].page_content}")
print(f"Metadata: {documents[0].metadata}")