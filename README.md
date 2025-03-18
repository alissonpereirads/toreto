# Chat PDF - Assistente de Manual de Notebook

Bem-vindo ao **Chat PDF**, mais um projeto de estudo que desenvolvi para explorar o poder dos **Large Language Models (LLMs)** e suas aplicações práticas. Este projeto é um assistente virtual capaz de responder perguntas sobre o manual de um notebook, utilizando algumas técnicas de processamento de linguagem natural (NLP) e frameworks.

## 🚀 Sobre o Projeto

Este projeto foi criado como parte do meu portfólio de estudos em **Ciência de Dados** e **Inteligência Artificial**. Atualmente, estou no 3º semestre da faculdade e tenho me dedicado a projetos práticos para consolidar meus conhecimentos e me preparar para oportunidades de estágio na área.

O **Chat PDF** é uma aplicação que permite fazer perguntas sobre o manual de um notebook e receber respostas precisas com base no conteúdo do documento. Utilizei um pdf pre carreagado neste exemplo, mas poderia ser algo mais personalizado e vou pensar em uma ideia para multiplos pdfs ainda.

## 🛠️ Ferramentas e Tecnologias Utilizadas

Aqui estão as principais ferramentas e frameworks que utilizei para desenvolver este projeto:

### Frameworks e Bibliotecas
- **LangChain**: Framework para construção de aplicações com LLMs, utilizado para criar a cadeia de QA (Question-Answering) e integrar o modelo de linguagem.
- **Streamlit**: Biblioteca para criar interfaces web interativas em Python, utilizada para construir a interface do chat.
- **Hugging Face Transformers**: Para embeddings de texto usando o modelo `sentence-transformers/all-MiniLM-L6-v2`.
- **Chroma**: Vector store para armazenar e recuperar embeddings dos documentos.

### Modelo de Linguagem
- **Groq (LLaMA 3 70B)**: Modelo de linguagem avançado utilizado para gerar respostas contextualizadas com base no conteúdo do manual.

### Outras Ferramentas
- **PyPDFLoader**: Para carregar e processar o arquivo PDF.
- **RecursiveCharacterTextSplitter**: Para dividir o documento em partes menores (chunks) e facilitar o processamento.
- **Dotenv**: Para gerenciar variáveis de ambiente, como chaves de API.

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido com os seguintes objetivos:
1. **Aprender na Prática**: Explorar o uso de LLMs e frameworks como LangChain e Streamlit em um projeto real.
2. **Resolver um Problema Real**: Criar uma solução que facilite a consulta de manuais técnicos de forma rápida e eficiente.
3. **Montar um Portfólio**: Demonstrar minhas habilidades em Ciência de Dados e IA para potenciais oportunidades de estágio.

## ⚙️ Como Funciona

O **Chat PDF** funciona em três etapas principais:

1. **Carregamento do PDF**:
   - O manual do notebook é carregado e dividido em partes menores (chunks) para facilitar o processamento.

2. **Criação do Vector Store**:
   - Os chunks são transformados em embeddings (representações numéricas do texto) e armazenados em um vector store usando o **Chroma**.

3. **Geração de Respostas**:
   - Quando o usuário faz uma pergunta, o sistema recupera os chunks mais relevantes do vector store e utiliza o modelo **Groq** para gerar uma resposta contextualizada.


```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o projeto na sua máquina:

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/chat-pdf.git
   cd chat-pdf
   ```

2. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as Variáveis de Ambiente**:
   - Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API Groq:
   ```
   GROQ_API_KEY=sua_chave_aqui
   ```

4. **Execute a Aplicação**:
   ```bash
   streamlit run main.py
   ```

5. **Acesse o Chat**:
   - Abra o navegador e acesse http://localhost:8501.
   - Faça perguntas sobre o manual do notebook e veja as respostas em tempo real!

## 🌟 Destaques do Projeto

- **Interface Amigável**: Desenvolvi uma interface simples e intuitiva usando Streamlit, facilitando a interação do usuário.
- **Eficiência no Processamento**: Utilizei técnicas como chunking e embeddings para garantir que o sistema seja rápido e preciso.
- **Aprendizado Contínuo**: Este projeto me permitiu explorar novas ferramentas e consolidar conhecimentos em LLMs e NLP.

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, pude:
- Aprofundar meu conhecimento em LLMs e suas aplicações práticas.
- Aprender a usar frameworks como LangChain e Streamlit.
- Entender a importância de técnicas como chunking e embeddings no processamento de documentos.
- Melhorar minhas habilidades em Python e no desenvolvimento de soluções de IA.

## 📩 Contato

Estou em busca de uma oportunidade de estágio na área de Ciência de Dados ou Inteligência Artificial. Se você gostou do meu trabalho ou tem alguma dúvida, sinta-se à vontade para entrar em contato:


- **LinkedIn**: [Alisson Pereira](https://www.linkedin.com/in/alisson-pereira-ds/)
- **E-mail**: alissonpereira.contato@gmail.com
- **GitHub**: [alissonpereirads](https://github.com/alissonpereirads)



---

Feito com ❤️ por [Alisson Pereira]  
*Estudante de Ciência de Dados | Apaixonado por IA e Tecnologia*
