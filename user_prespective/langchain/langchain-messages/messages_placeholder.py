from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini")

# Create ChatPromptTemplate with MessagesPlaceholder for dynamic chat history
chat_template = ChatPromptTemplate([
    ("system", "You are an expert customer support agent for TCS Courier."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_query}")
])

# Simulated existing chat history list
history = [
    HumanMessage(content="Where is my package?"),
    AIMessage(content="Please provide your tracking ID so I can assist you.")
]

# Inject history dynamically along with current query
prompt = chat_template.invoke({
    "chat_history": history,
    "user_query": "My tracking ID is TCS-88990."
})

# Invoke model
result = model.invoke(prompt)

print("--- Response using MessagesPlaceholder ---")
print(result.content)