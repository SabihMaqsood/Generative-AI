from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini")

# Structuring system and human roles with dynamic variable placeholders
chat_template = ChatPromptTemplate([
    ("system", "You are an expert sports analyst specializing in {sport}."),
    ("human", "Explain the concept of {term} in simple terms.")
])

# Filling placeholders with dynamic arguments
prompt = chat_template.invoke({"sport": "Cricket", "term": "Reverse Swing"})

# Invoke model
result = model.invoke(prompt)

print("--- Response using ChatPromptTemplate ---")
print(result.content)