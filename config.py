import logging
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


def get_groq(model_name="llama-3.3-70b-versatile"):
    logging.info("Configurando o modelo Groq.")
    llm = ChatGroq(model=model_name, api_key=api_key)
    logging.info("Modelo Groq configurado com sucesso.")
    return llm
