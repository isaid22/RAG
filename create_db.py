# Reference
# https://github.com/langchain-ai/langchain/issues/9749#issuecomment-1693039900
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma

from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders.pdf import PyMuPDFLoader
from langchain.document_loaders.xml import UnstructuredXMLLoader
from langchain.document_loaders.csv_loader import CSVLoader
import os
import shutil
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) # Load the .env file.
print('##### find_dotenv(): ', find_dotenv()) # I kept a .env file with OPENAI_API_KEY

#os.environ["OPENAI_API_KEY"] = os.getenv["OPENAI_API_KEY"]
print('##### MY OPENAI_API_KEY: ', os.getenv)

CHROMA_PATH = "chroma"


# Define a dictionary to map file extensions to their respective loaders
loaders = {
    '.pdf': PyMuPDFLoader,
    '.xml': UnstructuredXMLLoader,
    '.csv': CSVLoader,
}

# Define a function to create a DirectoryLoader for a specific file type
def create_directory_loader(file_type, directory_path):
    return DirectoryLoader(
        path=directory_path,
        glob=f"**/*{file_type}",
        loader_cls=loaders[file_type],
    )

# Create DirectoryLoader instances for each file type
pdf_loader = create_directory_loader('.pdf', 'data/pdf')
# xml_loader = create_directory_loader('.xml', '/path/to/your/directory')
# csv_loader = create_directory_loader('.csv', '/path/to/your/directory')

# Load the files
pdf_documents = pdf_loader.load()
# xml_documents = xml_loader.load()
# csv_documents = csv_loader.load()

text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
)

chunks = text_splitter.split_documents(pdf_documents)

print(f"Split {len(pdf_documents)} documents into {len(chunks)} chunks.")

document = chunks[10]
print(document.page_content)
print(document.metadata)

if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)

# Create a new DB from the documents.
db = Chroma.from_documents(
    chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
)
db.persist()
print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")