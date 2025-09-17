from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from app.config import GROQ_API_KEY, GROQ_MODEL, get_vectorstore


def build_rag_chain(groq_api_key: str | None = None, groq_model: str | None = None):
    api_key = groq_api_key or GROQ_API_KEY
    model_name = groq_model or GROQ_MODEL
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set. Provide it via env or parameter.")

    vectordb = get_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    system_instructions = (
        "You are a supportive, empathetic mental health assistant. "
        "Offer coping strategies, reflective questions, and resources. "
        "Be non-judgmental and concise. Avoid clinical diagnoses. "
        "Always include a brief disclaimer that you're not a substitute for professional care. "
        "If the user indicates crisis or self-harm, urge contacting local emergency services or a crisis hotline immediately."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_instructions + "\n\nRelevant Context:\n{context}"),
        ("human", "{question}")
    ])

    llm = ChatGroq(groq_api_key=api_key, model_name=model_name, temperature=0.2)

    def join_docs(docs: list) -> str:
        return "\n\n".join(d.page_content for d in docs)

    chain = {
        "context": retriever | join_docs,
        "question": RunnablePassthrough(),
    } | prompt | llm | StrOutputParser()

    return chain


def get_retriever():
    return get_vectorstore().as_retriever(search_kwargs={"k": 4})

