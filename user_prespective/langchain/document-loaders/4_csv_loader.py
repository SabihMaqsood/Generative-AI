import os
from langchain_community.document_loaders import CSVLoader

# Setup Sample CSV File
os.makedirs("sample_docs", exist_ok=True)
csv_path = "sample_docs/sample.csv"

with open(csv_path, "w", encoding="utf-8") as f:
    f.write("Name,Role,City\nAli,AI Engineer,Lahore\nSara,Data Scientist,Karachi\nUsman,MLOps Engineer,Islamabad")

# CSVLoader treats each row as a separate Document object
loader = CSVLoader(csv_path)
documents = loader.load()

print(f"Total Rows Loaded: {len(documents)}\n")

for doc in documents:
    print(f"Row Record:\n{doc.page_content}")
    print(f"Metadata: {doc.metadata}\n" + "-"*30)