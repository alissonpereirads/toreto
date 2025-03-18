from langchain_chroma import Chroma
import streamlit as st
import logging

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_vector_store(documents, embedding, diretorio):
    """
    Cria ou carrega um vector store no diretório especificado.

    Args:
        documents: Lista de documentos a serem indexados. Se None, carrega um vector store existente.
        embedding: Função de embedding a ser usada.
        diretorio: Diretório onde o vector store será salvo ou carregado.
    """
    if documents is not None:
        # Cria um novo vector store com os documentos fornecidos
        with st.spinner("Criando vector store. Isso pode levar alguns instantes..."):
            vectordb = Chroma.from_documents(
                documents=documents,
                embedding=embedding,
                persist_directory=diretorio,
            )
    else:
        # Carrega um vector store existente
        vectordb = Chroma(
            persist_directory=diretorio,
            embedding_function=embedding,
        )

    return vectordb
