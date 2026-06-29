from app.services.vectorstores import get_vectorstores

def retrieve_docs(query):
    vectorstore = get_vectorstores()

    docs = vectorstore.similarity_search_with_score(query,k=3)
    return docs 