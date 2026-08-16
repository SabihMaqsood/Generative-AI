from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

# Define Pydantic Schema
class ActorInfo(BaseModel):
    name: str = Field(description="Name of the actor")
    famous_movies: list[str] = Field(description="List of top 3 famous movies")
    oscar_winner: bool = Field(description="True if actor won an Oscar, else False")

# Instantiate Parser
parser = PydanticOutputParser(pydantic_object=ActorInfo)

# Inject Format Instructions into Prompt
prompt = PromptTemplate(
    template="Provide details about the actor '{actor}'.\n{format_instructions}",
    input_variables=["actor"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Chain Execution via LCEL
chain = prompt | model | parser
result: ActorInfo = chain.invoke({"actor": "Leonardo DiCaprio"})

print(f"Actor: {result.name}")
print(f"Oscar Winner: {result.oscar_winner}")
print(f"Top Movies: {result.famous_movies}")