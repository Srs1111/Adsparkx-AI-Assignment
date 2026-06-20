from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma 
from langchain.embeddings import HuggingFaceEmbaddings

loader = DirectoryLoader("docs")

documents = loader.load()

splitter = RecursiveCharactertextSplitter(
          chunk_size = 500,
          chunk_size = 50
)

doc = Chroma.from_documents(
    docs,
    embedding,
    persist_directory= "chroma_db"
)

db.persist()

print("knowledge base created")