#can add title extraction , summary extraction
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

from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.extractors import TitleExtractor, SummaryExtractor
from llama_index.core.storage.docstore import SimpleDocumentStore 



import os 
from dotenv import load_dotenv 
load_dotenv()

Settings.llm=OpenAI(model="gpt-4o-mini")
Settings.embed_model=OpenAIEmbedding(model="text-embedding-3-small")
Settings.chunk_size=512
Settings.chunk_overlap=50
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
PERSISTENCE_DIR="./pipeline_storage"




def main():
    documents=SimpleDirectoryReader(
    input_dir="llamaindex-docs",
    required_exts=[".md"],
    recursive=False,
    num_files_limit=10
    ).load_data()

    print(f"Loaded docs{len(documents)}")

    #create ingestion pipeline
    pipeline=IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=Settings.chunk_size,
            chunk_overlap=Settings.chunk_overlap),
            TitleExtractor(), #<= add here 
            SummaryExtractor(),
            OpenAIEmbedding(model="text-embedding-3-small")
        ],
        docstore=SimpleDocumentStore()
        )

    if os.path.exists(PERSISTENCE_DIR):
            print("Loading persisted doc store")
            pipeline.docstore.load(persist_dir=PERSISTENCE_DIR)
            print("Loaded!")

    processed_nodes=pipeline.run(documents=documents, show_progress=True)
    print(f"processed into {len(processed_nodes)}")

    pipeline.docstore.persist(persist_dir=PERSISTANCE_DIR)
    print("Persisted!")

    first_node_metadata=processed_nodes[0].metadata

    print("First Node metadata")
    for key, value in first_node_metadata.items():
        print(f"{key}:{value}")

    if processed_nodes[0].embedding:
        print(f"Embedding dim: {len(processed_nodes[0].embedding)}")

    #create index
    index=VectorStoreIndex(processed_nodes)
    query_engine=index.as_query_engine()

    query="what is llamacloud?"
    response=query_engine.query(query)

    print(response)


if __name__=="__main__":
    main()


