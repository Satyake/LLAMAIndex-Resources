
import os 
from dotenv import load_dotenv
load_dotenv()
from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
OPENAI_API_KEY="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"
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



