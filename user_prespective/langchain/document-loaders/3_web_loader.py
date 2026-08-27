from langchain_community.document_loaders import WebBaseLoader

# Target Web Page URL
target_url = "https://python.langchain.com/"

loader = WebBaseLoader(target_url)
documents = loader.load()

print(f"Total Web Documents Loaded: {len(documents)}")
print(f"Source URL: {documents[0].metadata['source']}")
print("Extracted Content Snippet:")
print(documents[0].page_content[:300].replace('\n', ' '))