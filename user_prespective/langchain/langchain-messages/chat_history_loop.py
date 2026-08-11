from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

# Chat history list initialized with SystemMessage
chat_history = [
    SystemMessage(content="You are a helpful customer support agent for TCS courier.")
]

print("--- Chatbot Initialized (Type 'exit' to stop) ---")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    # Append user prompt to history
    chat_history.append(HumanMessage(content=user_input))

    # Get model response with full conversation memory
    response = model.invoke(chat_history)

    # Append AI response to history
    chat_history.append(AIMessage(content=response.content))

    print(f"AI: {response.content}\n")