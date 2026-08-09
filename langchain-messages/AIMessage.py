from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# AIMessage stores the assistant's previous response to build chat memory
chat_history = [
    SystemMessage(content="You are a helpful customer support agent for Daraz Pakistan."),
    HumanMessage(content="Where is my order package?"),
    AIMessage(content="Please provide your tracking ID so I can check your delivery status.")
]

# Adding a follow-up user query using the stored history
chat_history.append(HumanMessage(content="My tracking ID is PK-98765."))

result = model.invoke(chat_history)

print("Updated Chat History with AIMessage:")
print(result.content)