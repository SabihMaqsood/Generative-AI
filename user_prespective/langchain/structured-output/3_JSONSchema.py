from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# 1. Pure JSON Schema Dictionary define karen
car_schema = {
    "title": "CarDetails",
    "description": "Information about a vehicle",
    "type": "object",
    "properties": {
        "brand": {"type": "string", "description": "Car manufacturer brand"},
        "model": {"type": "string", "description": "Car model name"},
        "year": {"type": "integer", "description": "Manufacturing year"},
        "is_electric": {"type": "boolean", "description": "Is the car 100% electric?"}
    },
    "required": ["brand", "model", "year", "is_electric"]
}

# 2. Gemini Model initialize karen
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

# 3. Structured Output bind karen
structured_llm = llm.with_structured_output(car_schema)

# 4. Invoke karen
query = "Tesla Model 3 electric car hai jo 2023 me manufacture hui."
result = structured_llm.invoke(query)

# 5. Results print karen
print("Type of object:", type(result))
print("Extracted JSON Object:", result)
print("Is Electric Car?:", result['is_electric'])