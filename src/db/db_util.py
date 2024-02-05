from util import chunk_pdf
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

def GetContextFromDb(file_name,query):
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    chunks = chunk_pdf(file_name)

    db = Chroma.from_texts(chunks, embedding_function)
    docs = db.similarity_search(k=10,query=query)

    return "\n\n---\n\n".join([doc.page_content for doc in docs])
    