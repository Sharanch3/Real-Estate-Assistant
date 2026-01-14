import os
from pathlib import Path
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_classic.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"
TEMPERATURE = 0.5
EMBED_MODEL = "text-embedding-3-small" 
CHUNK_SIZE = 300
CHUNK_OVERLAP = 10
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectore_store"
COLLECTION_NAME = "real_estate"


model = None
vector_store = None


def initialize_components():
    global model, vector_store

    if model is None:
        model = ChatOpenAI(model= "gpt-4o-mini", temperature= TEMPERATURE)

    if vector_store is None:
        embedding = OpenAIEmbeddings(model= EMBED_MODEL, api_key= OPENAI_API_KEY)
        
        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embedding,
            persist_directory=str(VECTORSTORE_DIR)
        )


def process_urls(urls):
    yield " Initializing Components..."
    initialize_components()

    yield "Resetting vector store..."
    vector_store.reset_collection()

    yield "Loading data..."
    loader = WebBaseLoader(urls)
    docs = loader.load()

    yield "Splitting text into chunks..."
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    
    chunks = splitter.split_documents(documents=docs)

    yield "Adding to vector store"
    vector_store.add_documents(chunks)

    yield "Setup is complete. ✅"

def generate_answer(query):
    global model, vector_store
    
    if vector_store is None:
        raise RuntimeError("VectorDB is not initialized. Please process URLs first")
    
    if model is None:
        initialize_components()
    
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 3,
            "fetch_k": 7,
            "lambda_mult": 0.5
        }
    )

    chain = RetrievalQAWithSourcesChain.from_llm(llm= model, retriever = retriever)
    result = chain.invoke({"question": query}, return_only_outputs = True)
    sources = result.get("sources", "")

    
    return result['answer'], sources



if __name__ == "__main__":

    urls = [
        "https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html",
        "https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html"
    ]
    
    query = "Tell me what was the 30 year fixed mortagate rate along with the date"
    
    process_urls(urls)
    
    answer, sources = generate_answer(query= query)
    print(f"Answer: {answer}")
    print(f"Sources: {sources}")