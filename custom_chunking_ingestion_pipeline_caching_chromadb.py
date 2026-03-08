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
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore


import os 
from dotenv import load_dotenv 
load_dotenv()

Settings.llm=OpenAI(model="gpt-4o-mini")
Settings.embed_model=OpenAIEmbedding(model="text-embedding-3-small")
Settings.chunk_size=512
Settings.chunk_overlap=50
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
PERSISTENCE_DIR="./pipeline_storage"
CHROMA_DIR="./chroma_db"


def main():
    documents=SimpleDirectoryReader(
    input_dir="llamaindex-docs",
    required_exts=[".md"],
    recursive=False,
    num_files_limit=10
    ).load_data()

    print(f"Loaded docs{len(documents)}")

    chroma_client=chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_collection=chroma_client.get_or_create_collection("llamaindex_docs")
    vector_store=ChromaVectorStore(chroma_collection=chroma_collection)

    #count docs in chroma db
    existing_count=chroma_collection.count()
    print(f"ChromaDB contains {existing_count} embeddings")

    if existing_count >0:
        print(f"using existing embeddings")
    else:
    #create ingestion pipeline
        pipeline=IngestionPipeline(
            transformations=[
                SentenceSplitter(chunk_size=Settings.chunk_size,
                chunk_overlap=Settings.chunk_overlap),
                #TitleExtractor(), #<= add here 
                #SummaryExtractor(),
                OpenAIEmbedding(model="text-embedding-3-small")
            ],
            vector_store=vector_store
            )

        processed_nodes=pipeline.run(documents=documents, show_progress=True)
        print(f"processed into {len(processed_nodes)}")

        #pipeline.docstore.persist(persist_dir=PERSISTANCE_DIR)
        #print("Persisted!")
        if processed_nodes[0].embedding:
           print(f"Embedding dim: {len(processed_nodes[0].embedding)}")

    #create index
    index=VectorStoreIndex.from_vector_store(vector_store)

    print("vectorstore created!")
    query_engine=index.as_query_engine()

    query="what is llamacloud?"
    response=query_engine.query(query)

    print(response)


if __name__=="__main__":
    main()


