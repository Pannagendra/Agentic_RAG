# src/ingest.py
import os
import sys
import argparse
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

def ingest(input_path, out_path):
    docs = []

    if os.path.isdir(input_path):
        for file in os.listdir(input_path):
            if file.endswith(".txt"):
                loader = TextLoader(os.path.join(input_path, file))
                docs.extend(loader.load())
    else:
        loader = TextLoader(input_path)
        docs = loader.load()

    # Split
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    # Store embeddings
    embeddings = OllamaEmbeddings(model="llama3.1:8b")
    vectorstore = FAISS.from_documents(splits, embeddings)
    vectorstore.save_local(out_path)

    print(f"✅ Ingest complete. Saved to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to file or folder with .txt docs")
    parser.add_argument("--out", default="data/processed", help="Where to save vector index")
    args = parser.parse_args()

    ingest(args.input, args.out)
