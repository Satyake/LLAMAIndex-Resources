[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#_top)
# Classify Contract Types
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
In this example, we’ll be classifying various contracts by type, using LlamaClassify, and the `llama-cloud` SDK. When provided with a file, we’ll classify it either as a `co_branding` contract or an `affiliate_agreement`.
As an example, we’ll be making use of the [CUAD](https://zenodo.org/records/4595826) dataset, which includes various contracts such as: Affiliate Agreements, Co-Branding contracts, Franchise contracts and more.
The example we go through below is also replicable within the LlamaCloud as well, where you will also be able to create classification rules via the UI, instead of defining them in code:


```


pip install llama-cloud>=1.0


```

```


npm install @llamaindex/llama-cloud


```

```


pip install llama-cloud-services


```

## Download Contracts
[Section titled “Download Contracts”](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#download-contracts)
To start off, we recommend downloading a few contracts from the ‘Affiliate Agreements’ and ‘Co-Branding’ sections from the [CUAD dataset](https://zenodo.org/records/4595826).
## Connect to Llama Cloud
[Section titled “Connect to Llama Cloud”](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#connect-to-llama-cloud)
To get started, make sure you provide your [Llama Cloud](https://cloud.llamaindex.ai?utm_campaign=extract&utm_medium=recipe) API key.
You can set it as an environment variable `LLAMA_CLOUD_API_KEY` or pass it directly to the SDK at runtime.
## Initialize a LlamaCloud Client
[Section titled “Initialize a LlamaCloud Client”](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#initialize-a-llamacloud-client)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#tab-panel-31)


```


from llama_cloud import AsyncLlamaCloud





project_id ="your-project-id"




organization_id ="your-organization-id"





client =AsyncLlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])


```

```


import LlamaCloud from"@llamaindex/llama-cloud";





const projectId"your-project-id";




const organizationId"your-organization-id";





const clientnewLlamaCloud({




apiKey: process.env.LLAMA_CLOUD_API_KEY!,



```

```


from llama_cloud_services.beta.classifier.client import ClassifyClient




from llama_cloud.client import AsyncLlamaCloud





client =AsyncLlamaCloud(token=os.environ["LLAMA_CLOUD_API_KEY"])




project_id ="your-project-id"




organization_id ="your-organization-id"





classifier =ClassifyClient(client,project_id=project_id,organization_id=organization_id)


```

## Define Classification Rules
[Section titled “Define Classification Rules”](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#define-classification-rules)
For this example, we’ll narrow down the scope to classifying between `co_branding` and `affiliate_agreements` types:
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#tab-panel-34)


```


rules =[





"type": "affiliate_agreements",




"description": "This is a contract that outlines an affiliate agreement",






"type": "co_branding",




"description": "This is a contract that outlines a co-branding deal/agreement",




```

```


const rules = [





type: 'affiliate_agreements',




description: 'This is a contract that outlines an affiliate agreement',






type: 'co_branding',




description: 'This is a contract that outlines a co-branding deal/agreement',




```

```


from llama_cloud.types import ClassifierRule





rules =[




ClassifierRule(




type="affiliate_agreements",




description="This is a contract that outlines an affiliate agreement",





ClassifierRule(




type="co_branding",




description="This is a contract that outlines a co-branding deal/agreement",




```

## Classify Files
[Section titled “Classify Files”](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#classify-files)
Finally, we can classify a file (or files):
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamaclassify/examples/classify_contract_types/#tab-panel-37)


```


file_obj =await client.files.create(




file="CybergyHoldingsInc_Affliate Agreement.pdf",




purpose="classify",





file_id = file_obj.id





result =await client.classifier.classify_file_path(




file_ids=[file_id],




rules=rules,






classification = result.items[0].result




print("Classification Result: "+ classification.type)




print("Classification Reason: "+ classification.reasoning)


```

```

// Upload a file



const fileObj = await client.files.create({




file: fs.createReadStream('CybergyHoldingsInc_Affliate Agreement.pdf'),




purpose: "classify",





const fileIdfileObj.id;





const result = await client.classifier.classifyFilePath({




file_ids: [fileId],




rules: rules,






const classificationresult.items[0].result;




console.log("Classification Result: "+ classification?.type);




console.log("Classification Reason: "+ classification?.reasoning);


```

```


result =await classifier.aclassify_file_path(




rules=rules,




file_input_path="CybergyHoldingsInc_Affliate Agreement.pdf",






classification = result.items[0].result




print("Classification Result: "+ classification.type)




print("Classification Reason: "+ classification.reasoning)


```

Once classification is complete, the results will include not only the contract type the file was classified as, but also the reasoning for this classification by LlamaClassify. For example, in this case this is the result we got:
```

Classification Result: affiliate_agreements


Classification Reason: The document is titled 'MARKETING AFFILIATE AGREEMENT' and repeatedly refers to one party as the 'Marketing Affiliate.' The agreement outlines the rights and obligations of the 'Marketing Affiliate' (MA) to market, sell, and support certain technology products, and details the relationship between the company and the affiliate. There is no mention of joint branding, shared trademarks, or collaborative marketing under both parties' brands, which would be indicative of a co-branding agreement. The content is entirely consistent with an affiliate agreement, where one party (the affiliate) is authorized to market and sell the products of another company, rather than a co-branding arrangement. Therefore, the best match is 'affiliate_agreements' with very high confidence.

```

