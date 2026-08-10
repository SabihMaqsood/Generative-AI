from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# SystemMessage sets the rules and persona for the AI
messages = [
    SystemMessage(content="You are a helpful customer support agent for Daraz Pakistan.")
]

print("System Message set successfully:")
print(messages)