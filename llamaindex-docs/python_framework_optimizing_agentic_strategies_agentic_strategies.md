[Skip to content](https://developers.llamaindex.ai/python/framework/optimizing/agentic_strategies/agentic_strategies/#_top)
# Agentic strategies
You can build agents on top of your existing LlamaIndex RAG workflow to empower it with automated decision capabilities. A lot of modules (routing, query transformations, and more) are already agentic in nature in that they use LLMs for decision making.
## Simpler Agentic Strategies
[Section titled “Simpler Agentic Strategies”](https://developers.llamaindex.ai/python/framework/optimizing/agentic_strategies/agentic_strategies/#simpler-agentic-strategies)
These include routing and query transformations.
  * [Query Transformations](https://developers.llamaindex.ai/python/framework/optimizing/advanced_retrieval/query_transformations)
  * [Sub Question Query Engine (Intro)](https://developers.llamaindex.ai/python/examples/query_engine/sub_question_query_engine)


## Data Agents
[Section titled “Data Agents”](https://developers.llamaindex.ai/python/framework/optimizing/agentic_strategies/agentic_strategies/#data-agents)
This guides below show you how to deploy a full agent loop, capable of chain-of-thought and query planning, on top of existing RAG query engines as tools for more advanced decision making.
Make sure to check out our [full module guide on Data Agents](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents), which highlight these use cases and much more.
Our [lower-level agent API](https://developers.llamaindex.ai/python/framework/module_guides/deploying/agents#manual-agents) shows you the internals of how an agent works (with step-wise execution).
Example guides below (using LLM-provider-specific function calling):
  * [Basic Function Agent](https://developers.llamaindex.ai/python/examples/workflow/function_calling_agent)
  * [Function Agent with Query Engine Tools](https://developers.llamaindex.ai/python/examples/agent/openai_agent_with_query_engine)
  * [Function Agent Retrieval](https://developers.llamaindex.ai/python/examples/agent/openai_agent_retrieval)
  * [Function Agent Query Cookbook](https://developers.llamaindex.ai/python/examples/agent/openai_agent_query_cookbook)
  * [Function Agent w/ Context Retrieval](https://developers.llamaindex.ai/python/examples/agent/openai_agent_context_retrieval)


