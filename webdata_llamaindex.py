
import os 
from dotenv import load_dotenv
load_dotenv()
from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
load_dotenv()
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY
def main():
    url="https://paulgraham.com/greatwork.html"
    documents=SimpleWebPageReader(html_to_text=True)
    docs=documents.load_data([url])
    print(len(docs))

    #preview
    #for i, doc in enumerate(docs):
    #    print(f"doc {i+1} preview:\n{doc.text[:500]}")
    index=VectorStoreIndex.from_documents(docs)
    print("index created \n")

    #queryengine
    qe=index.as_query_engine()

    #question
    query="what does paul gram say on great work?"

    print(query)

    #response
    response=qe.query(query)
    print(f"Response :\n {response}")

if __name__=="__main__":
    main()



