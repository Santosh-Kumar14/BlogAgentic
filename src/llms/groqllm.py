from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()


    def get_llm(self):
        try:
            self.groq_api_key = os.getenv("GROQ_API_KEY")
            if not self.groq_api_key:
                raise ValueError("GROQ_API_KEY environment variable is missing.")
            llm = ChatGroq(api_key=self.groq_api_key, model="openai/gpt-oss-20b", temperature=0, max_tokens=8192,reasoning_effort="low")
            return llm
        except Exception as e:
            raise ValueError(f"Error occurred with exception : {e}")