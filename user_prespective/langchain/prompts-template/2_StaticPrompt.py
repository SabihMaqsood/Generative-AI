from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# Static prompt: Hardcoded string without placeholders
static_template = PromptTemplate.from_template("What is the capital of Pakistan?")

prompt = static_template.invoke({})

result = model.invoke(prompt)

print("Static Prompt Output:")
print(result.content)