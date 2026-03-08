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
CHROMA_DIR="./chroma_db_cached"
CACHE_DIR="./pipeline_cache"

Settings.llm=OpenAI(model="gpt-4o-mini")
Settings.embed_model=OpenAIEmbedding(model="text-embedding-3-small")
Settings.chunk_size=512
Settings.chunk_overlap=50
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")


def get_transformations():
    return [SentenceSplitter(
        chunk_size=Settings.chunk_size,
        chunk_overlap=Settings.chunk_overlap
    ),
    TitleExtractor(),
    OpenAIEmbedding(model="text-embedding-3-small")
    ]

def main():

    documents=SimpleDirectoryReader(
    input_dir="llamaindex-docs",
    required_exts=[".md"],
    recursive=False,
    num_files_limit=5
    ).load_data()

    chroma_client=chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_collection=chroma_client.get_or_create_collection("llamaindex_docs")
    vector_store=ChromaVectorStore(chroma_collection=chroma_collection)

    print(f"existing embeddings {chroma_collection.count()}")

    #create pipeline
    pipeline=IngestionPipeline(
        transformations=get_transformations(),
        vector_store=vector_store,
        docstore=SimpleDocumentStore() #track doc hashes
    )

    #load existing cache if available
    if os.path.exists(CACHE_DIR):
        print(f"Loading existing cache from {CACHE_DIR}")
        pipeline.load(persist_dir=CACHE_DIR)
        print("Cache loaded")
    else:
        print("No cache")
    print("cache transformations will be reused")
    processed_nodes=pipeline.run(documents=documents, show_progress=True)
    if processed_nodes:
        if processed_nodes[0].embedding:
            print(f"length of embedding {len(processed_nodes[0].embedding)}")
    pipeline.persist(persist_dir=CACHE_DIR)
    print("cache saved, next run will skip unchanged documents")

    vector_index=VectorStoreIndex.from_vector_store(vector_store)
    query_engine=vector_index.as_query_engine()

    query="what is llamaindex used for?"
    response=query_engine.query(query)
    print(response)

if __name__=="__main__":
    main()











