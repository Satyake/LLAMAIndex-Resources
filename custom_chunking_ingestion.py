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
Settings.chunk_overlap=20

def main():
   documents=SimpleDirectoryReader(
    input_dir="llamaindex-docs",
    required_exts=[".md"],
    recursive=False,
    num_files_limit=10
   ).load_data()
   print(f"loaded {len(documents)}")

   node_parser=SentenceSplitter(
    chunk_size=Settings.chunk_size,
    chunk_overlap=Settings.chunk_overlap
   )
   print("Parsing documents into nodes with custom_chunking..")

   nodes=node_parser.get_nodes_from_documents(documents)
   for i, node in enumerate(nodes[:3]):
    print(f"\nNode{i+1} content: \n{node.get_content()}")
    if node.metadata:
        print(f"-Source: {node.metadata.get('file_name','N/A')}")

   print("Creating Vector store index from nodes")
   #index=VectorStoreIndex.from_documents(documents,node_parser=node_parser)
   index=VectorStoreIndex(nodes)
   print("Created sucessfully")

   #query
   query="What is llama index"
   response=index.as_query_engine().query(query)
   print(response)

if __name__=="__main__":
    main()
