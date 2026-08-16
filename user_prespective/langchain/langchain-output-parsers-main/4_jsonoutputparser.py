from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="Generate a profile for a fictional software engineer in JSON format with keys 'name', 'tech_stack', and 'experience_years'.\n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model | parser
result = chain.invoke({})

print(result)
print(f"Parsed Type: {type(result)}")