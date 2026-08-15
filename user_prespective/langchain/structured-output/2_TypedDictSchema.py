from typing import List, Annotated, TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# 1. TypedDict Schema with Annotated hints define karen
class StudentProfile(TypedDict):
    name: Annotated[str, ..., "Student ka pura naam"]
    age: Annotated[int, ..., "Student ki umer saal me"]
    courses: Annotated[List[str], ..., "Enrolled subjects ki list"]
    gpa: Annotated[float, ..., "GPA out of 4.0"]

# 2. Gemini Model initialize karen
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

# 3. Structured output bind karen
structured_llm = llm.with_structured_output(StudentProfile)

# 4. Invoke karen
query = "sabih maqsood ki age 21 saal hai. Wo Computer Science, Data Structures aur AI ke courses parh raha hai aur uska GPA 3.8 hai."
result = structured_llm.invoke(query)

# 5. Results print karen
print("Type of object:", type(result))
print("Extracted Dictionary:", result)
print("Student Name:", result['name'])
print("Student Age:", result['age'])
print("Enrolled Courses:", result['courses'])
print("GPA:", result['gpa'])