from typing import List
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# 1. Pydantic Schema define karen
class MovieDetails(BaseModel):
    title: str = Field(description="Movie ka exact title")
    release_year: int = Field(description="Movie ki release ka saal")
    director: str = Field(description="Director ka naam")
    genres: List[str] = Field(description="Movie ke genres ki list")
    rating: float = Field(description="IMDb ya general rating out of 10")

# 2. Gemini Model initialize karen
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

# 3. Model ko structured output ke sath bind karen
structured_llm = llm.with_structured_output(MovieDetails)

# 4. Prompt invoke karen
query = "Inception movie 2010 me release hui thi, jisko Christopher Nolan ne direct kiya tha. Ye Sci-Fi aur Action genre ki film hai jiski rating 8.8 hai."
result = structured_llm.invoke(query)

# 5. Results print karen
print("Type of object:", type(result))
print("Movie Title:", result.title)
print("Release Year:", result.release_year)
print("Director:", result.director)
print("Genres:", result.genres)
print("Rating:", result.rating)

