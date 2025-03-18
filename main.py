import os
import streamlit as st
from dotenv import load_dotenv
from config import get_groq
from loader import doc_loader
from splitter import split_documents
from embeddings import get_embeddings_function
from vector_store import get_vector_store
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações iniciais
st.set_page_config(page_title="Chat PDF - Manual do Notebook", page_icon="📘")
st.title("Chat PDF - Manual do Notebook")

# Sidebar com link para download do PDF
with st.sidebar:

    st.header("Sobre o Projeto")
    st.info(
        """
        Este é um assistente virtual especializado em responder perguntas
        sobre o manual do notebook. Faça perguntas e obtenha respostas
        precisas com base no conteúdo do manual.
        """
    )
    st.markdown("---")
    st.subheader("Download do Manual")
    st.write("Baixe o manual do notebook utilizado neste projeto:")
    with open("files/manual_notebook.pdf", "rb") as file:
        btn = st.download_button(
            label="📥 Baixar PDF",
            data=file,
            file_name="manual_notebook.pdf",
            mime="application/pdf",
        )
    st.markdown("---")
    st.markdown(
        "**Contato**\n\n"
        "Alisson Pereira: alissonpereira.contato@gmail.com\n"
        "\n(75) 98886-2585\n\n"
    )


# Função para inicializar o vector store e o chat
def initialize_chat():
    llm = get_groq()

    # Caminho para o diretório do vector store
    diretorio_vector_store = "db_vector"

    # Verifica se o vector store já existe
    if os.path.exists(diretorio_vector_store) and os.listdir(diretorio_vector_store):
        with st.spinner("Lendo manual..."):
            vector_db = get_vector_store(
                documents=None,  # Não precisa passar documentos, pois já existe
                embedding=get_embeddings_function(),
                diretorio=diretorio_vector_store,
            )
    else:
        with st.spinner(
            "Criando novo vector store. Isso pode levar alguns instantes..."
        ):
            # Carrega o documento
            arquivo = doc_loader(path="files\\manual_notebook.pdf")

            # Divide o documento em partes menores
            aquivo_split = split_documents(arquivo)

            # Cria o vector store
            vector_db = get_vector_store(
                documents=aquivo_split,
                embedding=get_embeddings_function(),
                diretorio=diretorio_vector_store,
            )

    # Define o prompt personalizado
    prompt_template = """
    Você é um assistente especializado em responder perguntas sobre o manual de um notebook. 
    Responda apenas com base no conteúdo do manual fornecido. Se a pergunta não puder ser respondida com base no manual, responda: "Não consigo encontrar essa informação no manual."

    Exemplos:
    Pergunta: Como faço para ligar o notebook?
    Resposta: Para ligar o notebook, pressione o botão de energia localizado no canto superior direito do teclado.

    Pergunta: Qual é a duração da bateria?
    Resposta: A duração da bateria pode variar dependendo do uso, mas em média dura até 8 horas.

    Agora, responda a seguinte pergunta:
    {context}

    Pergunta: {question}
    Resposta:
    """

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Cria a cadeia de QA
    chat_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_db.as_retriever(search_type="similarity", k=3),
        chain_type_kwargs={"prompt": prompt},
    )

    return chat_chain


# Inicializa o chat
chat_chain = initialize_chat()

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Exibe o histórico de mensagens
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "ai":
        st.chat_message("ai").write(message["content"])

# Entrada do usuário
pergunta = st.chat_input("Faça sua pergunta sobre o manual do notebook:")

if pergunta:
    # Adiciona a pergunta ao histórico
    st.chat_message("user").write(pergunta)
    st.session_state.messages.append({"role": "user", "content": pergunta})

    with st.spinner("Processando sua pergunta..."):
        resposta = chat_chain.invoke({"query": pergunta})
        resposta_texto = resposta["result"]

        # Adiciona a resposta ao histórico
        st.chat_message("ai").write(resposta_texto)
        st.session_state.messages.append({"role": "ai", "content": resposta_texto})
