from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )

    chunks = text_splitter.split_text(text)

    return chunks

def chunk_pdf(fileName):
    reader = PdfReader(f"src/resources/{fileName}")
    subset = reader.pages[11:]
    id = 1
    chunks = []
    chunk_ids = []

    for page in subset:
        chunks_to_append = chunk_text(page.extract_text())
        for chunk in chunks_to_append:
            chunks.append(chunk)
            chunk_ids.append(f"id{id}")
            id += 1

    return chunks