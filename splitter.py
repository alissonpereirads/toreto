import logging
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Ajustei os parâmetros, mas você pode precisar otimizar
split = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, separators=["\n", "."]  # Alterei os valores
)


def split_documents(document):
    logger.info("Dividindo documento em partes menores.")
    documents = split.split_documents(document)
    logger.info(f"Documento dividido em {len(documents)} partes.")
    return documents
