"""
Parallel Execution & Result Merging using RunnableParallel
"""
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# Initialize Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)

# Prompts for Parallel Processing
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

# Prompt for Merging Results
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

# Construct Parallel Runnable Chain
parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

# Final Runnable Pipeline
chain = parallel_chain | merge_chain

sample_text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.
Effective in high dimensional spaces and memory efficient using support vectors.
"""

result = chain.invoke({'text': sample_text})
print("--- RunnableParallel Result ---")
print(result)

# Print Visual DAG Graph
chain.get_graph().print_ascii()