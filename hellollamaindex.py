import os 
from dotenv import load_dotenv
OPENAI_API_KEY="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"
load_dotenv()
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY

from llama_index.llms.openai import OpenAI

def main():
    response=OpenAI().complete("What is LlamaIndex?")
    print(response)

if __name__=='__main__':
    main()


