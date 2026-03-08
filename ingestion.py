#core data structures
from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document
from llama_index.core import Settings

#text_splitter
from llama_index.core.node_parser import SentenceSplitter
#embedding models
from llama_index.embeddings.openai import OpenAIEmbedding
#index
from llama_index.core import VectorStoreIndex
#LLMs config
from llama_index.llms.openai import OpenAI

from dotenv import load_dotenv
import os 
load_dotenv()

OPENAI_API_KEY="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"
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY

Settings.llm=OpenAI(model="gpt-4o-mini")
Settings.embed_model=OpenAIEmbedding(model="text-embedding-3-small")
Settings.chunk_size=512

def main():
    documents=SimpleDirectoryReader(
        input_dir="llamaindex-docs",
        recursive=False,
        required_exts=[".md"],
        num_files_limit=20
    )
    documents=documents.load_data()
    #print(f"loaded{len(documents)} documents")

    #get first document
   # doc=documents[0]
   # print(doc.text[:300])
   # print(doc.metadata)
   # print(doc.doc_id)
    index=VectorStoreIndex.from_documents(
    documents,
    node_parser=SentenceSplitter()
   )
    print("index created {index}")
    query_engine=index.as_query_engine()
    response=query_engine.query("How to integrate Pinecone in vecdb")
    print(response)
if __name__=="__main__":
    main()
