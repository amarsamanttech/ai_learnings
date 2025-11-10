from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
import os
import time

# Wait for Ollama
print("Connecting to Ollama...")
for i in range(30):
    try:
        test = OllamaLLM(model="phi3:mini", base_url=os.getenv("OLLAMA_HOST"))
        test.invoke("hi")
        break
    except:
        print(f"Waiting for Ollama... ({i+1}/30)")
        time.sleep(5)
else:
    print("Ollama not available!")
    exit(1)

print("Loading vector store...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

llm = OllamaLLM(model="phi3:mini", base_url=os.getenv("OLLAMA_HOST"))

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

print("\nRAG READY! Ask about your document (type 'exit' to quit)\n")

while True:
    q = input("> ").strip()
    if q.lower() == 'exit':
        break
    if not q:
        continue
    try:
        result = qa.invoke({"query": q})
        print(f"\n{result['result']}\n")
    except Exception as e:
        print(f"Error: {e}")