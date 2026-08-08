from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=20)

result = model.invoke("Write a short poem on PSL cricket in Lahore")

print(result.content)