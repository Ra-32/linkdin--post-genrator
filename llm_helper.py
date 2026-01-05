from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

if os.path.exists(".env"):
    load_dotenv()
else:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

groq_token=os.getenv("GROQ_API_KEY")

llm=ChatGroq(api_key=groq_token,temperature=0.7,model="llama-3.1-8b-instant")



