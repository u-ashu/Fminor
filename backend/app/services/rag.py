from app.services.retriever import retrieve_docs
from app.services.llm import llm
from app.services.memory import chat_history
def ask_questions(session_id,question):
    docs = retrieve_docs(question)
    context = "\n\n".join(
        doc.page_content
        for doc in docs 
    )

    history = "\n".join(chat_history.get(session_id,[]))

    prompt =  f"""
        You are an expert document assistant.

        Use the provided context and chat history.

        If the answer is not available in the context,
        say:
        "I could not find this information in the uploaded documents."

        Chat History:
        {history}

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    response = llm.invoke(prompt)
    answer = response.content
    chat_history[session_id].append(f"User:{question}")
    chat_history[session_id].append(f"Assistant:{answer}")

    sources = []

    if len(chat_history[session_id]) > 20:
        chat_history[session_id] = chat_history[session_id][-20:]

    for doc in docs:
        sources.append(
            {
                "source":doc.metadata.get("source"),
                "content":doc.page_content[:250]

            }
        
    )
    return {
            "answer":answer,
            "sources":sources
        }



    