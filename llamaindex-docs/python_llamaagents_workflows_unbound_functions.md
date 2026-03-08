[Skip to content](https://developers.llamaindex.ai/python/llamaagents/workflows/unbound_functions/#_top)
# Workflows from unbound functions
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Throughout these docs, we have been showing workflows defined as classes. However, this is not the only way to define a workflow: you can also define the steps in your workflow through independent or “unbound” functions and assign them to a workflow using the `@step()` decorator. Let’s see how that works.
First we create an empty class to hold the steps:
```


from workflows import Workflow





classTestWorkflow(Workflow):




pass


```

Now we can add steps to the workflow by defining functions and decorating them with the `@step()` decorator:
```


from workflows import step




from workflows.events import StartEvent, StopEvent





@step(workflow=TestWorkflow)




defsome_step(ev: StartEvent) -> StopEvent:




returnStopEvent()


```

In this example, we’re adding a starting step to the `TestWorkflow` class. The `@step()` decorator takes the `workflow` argument, which is the class to which the step will be added. The function signature is the same as for a regular step, with the exception of the `workflow` argument.
You can also add steps this way to any existing workflow class! This can be handy if you just need one extra step in your workflow and don’t want to subclass an entire workflow to do it.
