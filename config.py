import logging
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


def get_groq(model_name="llama3-70b-8192"):  # Corrigi o nome do modelo aqui
    logger.info("Configurando o modelo Groq.")
    llm = ChatGroq(model=model_name, api_key=api_key)
    logger.info("Modelo Groq configurado com sucesso.")
    return llm
