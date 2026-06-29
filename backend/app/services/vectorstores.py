from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

def get_embeddings():
    return  HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

VECTOR_DB_PATH = 'chroma_db'

def get_vectorstores():
    embedding_models = get_embeddings()
    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_models
    )

def save_chunks(chunks,filename):
    embedding_models = get_embeddings()
    metadatas = [
        {
            "source":filename
        }
        for _ in chunks 
    ]
    vectorstore = Chroma.from_texts(
        texts = chunks,
        embedding=embedding_models,
        persist_directory=VECTOR_DB_PATH,
        metadatas=metadatas
    )

    vectorstore.persist()

