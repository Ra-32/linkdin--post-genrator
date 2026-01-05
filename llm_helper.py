from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

groq_token=os.getenv("GROQ_API_KEY")

llm=ChatGroq(api_key=groq_token,temperature=0.7,model="llama-3.1-8b-instant")



