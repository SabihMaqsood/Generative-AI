"""
Conditional Dynamic Routing using RunnableBranch & RunnableLambda
"""
import os
from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)

# Output Schema for Sentiment
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser_pydantic = PydanticOutputParser(pydantic_object=Feedback)
parser_str = StrOutputParser()

# Classifier Prompt
classifier_prompt = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser_pydantic.get_format_instructions()}
)

classifier_chain = classifier_prompt | model | parser_pydantic

# Branch Response Prompts
positive_prompt = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

negative_prompt = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Dynamic Branch Definition
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', positive_prompt | model | parser_str),
    (lambda x: x.sentiment == 'negative', negative_prompt | model | parser_str),
    RunnableLambda(lambda x: "Could not classify sentiment properly.")
)

# End-to-End Dynamic Routing Chain
chain = classifier_chain | branch_chain

response = chain.invoke({'feedback': 'This is a beautiful phone'})
print("--- RunnableBranch Result ---")
print(response)