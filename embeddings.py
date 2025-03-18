import logging
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

load_dotenv()


def get_embeddings_function():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    hf = HuggingFaceEmbeddings(model_name=model_name)
    logger.info("Função de embeddings configurada com sucesso.")
    return hf
