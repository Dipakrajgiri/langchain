from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

class review(TypedDict):
    titel:str
    review:str
    rating:int 

 
structured_model=model.with_structured_output(review)

print(structured_model.invoke("Write a review for the movie Inception"))