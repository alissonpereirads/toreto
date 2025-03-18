import logging
from langchain_community.document_loaders import PyPDFLoader

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def doc_loader(path: str):
    logger.info(f"Carregando documento do caminho: {path}")
    loader = PyPDFLoader(path)
    document = loader.load()
    logger.info(f"Documento carregado com {len(document)} páginas.")
    for i, page in enumerate(document):
        logger.info(
            f"Página {i + 1}: {page.page_content[:200]}..."
        )  # Mostra os primeiros 200 caracteres de cada página
    return document
