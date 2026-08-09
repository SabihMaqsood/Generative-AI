from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# HumanMessage represents the user's input/question
messages = [
    SystemMessage(content="You are a helpful customer support agent for Daraz Pakistan."),
    HumanMessage(content="Where is my order package?")
]

result = model.invoke(messages)

print("User Question Sent!")
print("Model Response:", result.content)