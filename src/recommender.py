from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.promp_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.retriever = retriever
        self.llm = ChatGroq(
            groq_api_key=api_key,
            model_name=model_name,
            temperature=0
        )
        self.prompt = ChatPromptTemplate.from_template(get_anime_prompt())

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def get_recommendation(self, query: str) -> str:
        # Create a basic RAG chain
        rag_chain = (
            {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        return rag_chain.invoke(query)
