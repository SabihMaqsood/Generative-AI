from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)
# Define explicit field schemas
response_schemas = [
    ResponseSchema(name="city", description="Name of the city"),
    ResponseSchema(name="country", description="Country where the city is located"),
    ResponseSchema(name="population_millions", description="Approximate population in millions as a float")
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

prompt = PromptTemplate(
    template="Provide details about the city '{city}'.\n{format_instructions}",
    input_variables=["city"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model | parser
result = chain.invoke({"city": "Tokyo"})

print(result)