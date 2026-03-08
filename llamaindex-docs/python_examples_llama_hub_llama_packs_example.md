[Skip to content](https://developers.llamaindex.ai/python/examples/llama_hub/llama_packs_example/#_top)
# Llama Packs Example 
This example shows you how to use a simple Llama Pack with VoyageAI. We show the following:
  * How to download a Llama Pack
  * How to inspect its modules
  * How to run it out of the box
  * How to customize it.


You can find all packs on <https://llamahub.ai>
### Setup Data
[Section titled “Setup Data”](https://developers.llamaindex.ai/python/examples/llama_hub/llama_packs_example/#setup-data)
```


!wget "https://www.dropbox.com/s/f6bmb19xdg0xedm/paul_graham_essay.txt?dl=1"-O paul_graham_essay.txt


```

```


from llama_index.core import SimpleDirectoryReader




# load in some sample data



reader =SimpleDirectoryReader(input_files=["paul_graham_essay.txt"])




documents = reader.load_data()


```

### Download and Initialize Pack
[Section titled “Download and Initialize Pack”](https://developers.llamaindex.ai/python/examples/llama_hub/llama_packs_example/#download-and-initialize-pack)
We use `download_llama_pack` to download the pack class, and then we initialize it with documents.
Every pack will have different initialization parameters. You can find more about the initialization parameters for each pack through its [README](https://github.com/logan-markewich/llama-hub/tree/main/llama_hub/llama_packs/voyage_query_engine) (also on LlamaHub).
**NOTE** : You must also specify an output directory. In this case the pack is downloaded to `voyage_pack`. This allows you to customize and make changes to the file, and import it later!
```


from llama_index.core.llama_pack import download_llama_pack





VoyageQueryEnginePack =download_llama_pack(




"VoyageQueryEnginePack","./voyage_pack"



```

```


voyage_pack =VoyageQueryEnginePack(documents)


```

### Inspect Modules
[Section titled “Inspect Modules”](https://developers.llamaindex.ai/python/examples/llama_hub/llama_packs_example/#inspect-modules)
```


modules = voyage_pack.get_modules()




display(modules)


```

```

{'llm': OpenAI(callback_manager=<llama_index.callbacks.base.CallbackManager object at 0x11fdaae90>, model='gpt-4', temperature=0.1, max_tokens=None, additional_kwargs={}, max_retries=3, timeout=60.0, api_key='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', api_base='https://api.openai.com/v1', api_version=''),



'index': <llama_index.indices.vector_store.base.VectorStoreIndex at 0x2bccb3b50>}


```

```


llm = modules["llm"]




vector_index = modules["index"]


```

```

# try out LLM



response = llm.complete("hello world")




print(str(response))


```

```

# try out retriever



retriever = vector_index.as_retriever()




results = retriever.retrieve("What did the author do growing up?")




print(str(results[0].get_content()))


```

### Run Pack
[Section titled “Run Pack”](https://developers.llamaindex.ai/python/examples/llama_hub/llama_packs_example/#run-pack)
Every pack has a `run` function that will accomplish a certain task out of the box. Here we will go through the full RAG pipeline with VoyageAI embeddings.
```

# this will run the full pack



response = voyage_pack.run(




"What did the author do growing up?",similarity_top_k=2



```

```


print(str(response))


```

```

The author spent his time outside of school mainly writing and programming. He wrote short stories and attempted to write programs on an IBM 1401. Later, he started programming on a TRS-80, creating simple games and a word processor. He also painted still lives while studying at the Accademia.

```

### Try Customizing Pack
[Section titled “Try Customizing Pack”](https://developers.llamaindex.ai/python/examples/llama_hub/llama_packs_example/#try-customizing-pack)
A major feature of LlamaPacks is that you can and should inspect and modify the code templates!
In this example we’ll show how to customize the template with a different LLM, while keeping Voyage embeddings, and then re-use it. We’ll use Anthropic instead.
Let’s go into `voyage_pack` and create a copy.
  1. For demo purposes we’ll copy `voyage_pack` into `voyage_pack_copy`.
  2. Go into `voyage_pack_copy/base.py` and look at the `VoyageQueryEnginePack` class definition. This is where all the core logic lives. As you can see the pack class itself is a very light base abstraction. You’re free to copy/paste the code as you wish.
  3. Go into the line in the `__init__` where it do `llm = OpenAI(model="gpt-4")` and instead change it to `llm = Anthropic()` (which defaults to claude-2).
  4. Do `from llama_index.llms import Anthropic` and ensure that `ANTHROPIC_API_KEY` is set in your env variable.
  5. Now you can use!


In the below sections we’ll directly re-import the modified `VoyageQueryEnginePack` and use it.
```


from voyage_pack_copy.base import VoyageQueryEnginePack





voyage_pack =VoyageQueryEnginePack(documents)


```

```


response = voyage_pack.run("What did the author do during his time in RISD?")




print(str(response))


```

```


Unfortunately I do not have enough context in the provided information to definitively state what the author did during his time at RISD. The passage mentions that he learned a lot in a color class he took there, that he was basically teaching himself to paint, and that in 1993 he dropped out. But there are no specific details provided about his activities or course of study during his time enrolled at RISD. I apologize that I cannot provide a more complete response.


```

