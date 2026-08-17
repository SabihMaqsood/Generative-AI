"""
Simple LCEL Chain Example
"""

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Initialize Model
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    max_output_tokens=300
) 

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
) 

parser = StrOutputParser()

# Create Simple Chain
chain = prompt | model | parser

result = chain.invoke({'topic': 'cricket'}) 
print(result) 