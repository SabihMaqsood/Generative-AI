from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Babar Azam is a top Pakistani batter known for his elegant cover drives and consistency.",
    "Shaheen Afridi is a premier Pakistani fast bowler famous for his lethal opening overs and yorkers.",
    "Wasim Akram, known as the Sultan of Swing, is one of the greatest fast bowlers in cricket history.",
    "Mohammad Rizwan is a reliable wicketkeeper-batter known for his grit and partnership building.",
    "Shadab Khan is an all-rounder known for his leg-spin bowling and dynamic fielding."
]

query = 'tell me about shaheen'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)