from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

prompt = ChatPromptTemplate.from_template("Explain quantum computing in one simple sentence.")

# StrOutputParser converts AIMessage into clean text string
chain = prompt | model | StrOutputParser()
response = chain.invoke({})

print(response)