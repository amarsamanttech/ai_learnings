from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading PDFs from ./data...")
loader = PyPDFDirectoryLoader("data")
docs = loader.load()
if not docs:
    print("No PDFs found in ./data/ — add one!")
    exit(1)

print(f"Loaded {len(docs)} document(s)")

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)
print(f"Split into {len(chunks)} chunks")

print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Building FAISS index...")
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("faiss_index")

print("Ingestion complete! FAISS index saved.")