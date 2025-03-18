import logging
from langchain_text_splitters import RecursiveCharacterTextSplitter


split = RecursiveCharacterTextSplitter(
    chunk_size=1500, chunk_overlap=300, separators=["\n", "."]
)


def split_documents(document):
    logging.info("Dividindo documento em partes menores.")
    documents = split.split_documents(document)
    logging.info(f"Documento dividido em {len(documents)} partes.")
    return documents
