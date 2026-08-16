from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# Dynamic prompt: Reusable string with variable placeholder {country}
dynamic_template = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"]
)

# Pass variable value dynamically at execution
prompt = dynamic_template.invoke({"country": "Pakistan"})

result = model.invoke(prompt)

print("Dynamic Prompt Output:")
print(result.content)