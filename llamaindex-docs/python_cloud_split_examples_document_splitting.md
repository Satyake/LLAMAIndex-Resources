[Skip to content](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#_top)
# Splitting Concatenated Documents
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
This guide demonstrates how to use the Split API to automatically segment a concatenated PDF into logical document sections based on content categories.
## Use Case
[Section titled “Use Case”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#use-case)
When dealing with large PDFs that contain multiple distinct documents or sections (e.g., a bundle of research papers, a collection of reports), you often need to split them into individual segments. The Split API uses AI to:
  1. Analyze each page’s content
  2. Classify pages into user-defined categories
  3. Group consecutive pages of the same category into segments


## Example Document
[Section titled “Example Document”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#example-document)
We’ll use a PDF containing three concatenated documents:
  * **Alan Turing’s essay** “Intelligent Machinery, A Heretical Theory” (an essay)
  * **ImageNet paper** (a research paper)
  * **“Attention is All You Need”** paper (a research paper)


We’ll split this into segments categorized as either `essay` or `research_paper`.
📄 [Download the example PDF](https://github.com/run-llama/llama_cloud_services/blob/main/examples/split/document_splitting/data/turing%2Bimagenet%2Battention.pdf)
## Setup
[Section titled “Setup”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#setup)
Install the required packages:


Terminal window```


pipinstallllama-cloud=1.0


```

Set up your environment (or pass your API key directly in code later):
Terminal window```


exportLLAMA_CLOUD_API_KEY="your_api_key_here"


```

Terminal window```


npminstall@llamaindex/llama-cloud


```

Set up your environment (or pass your API key directly in code later):
Terminal window```


exportLLAMA_CLOUD_API_KEY="your_api_key_here"


```

## Step 1: Upload the PDF
[Section titled “Step 1: Upload the PDF”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#step-1-upload-the-pdf)
Upload the concatenated PDF to LlamaCloud using the `llama-cloud` SDK:


```


from llama_cloud import LlamaCloud





client =LlamaCloud()





pdf_path ="./data/turing+imagenet+attention.pdf"





uploaded_file = client.files.create(file=pdf_path,purpose="split")





file_id = uploaded_file.id




print(f"✅ File uploaded: {uploaded_file.id}")


```

```


import fs from"fs";




import { LlamaCloud } from"@llamaindex/llama-cloud";





const clientnewLlamaCloud();





const pdfPath"./data/turing+imagenet+attention.pdf";





const uploadedFile = await client.files.create({




file: fs.createReadStream(pdfPath),




purpose: "split",






const fileIduploadedFile.id;




console.log(`✅ File uploaded: ${uploadedFile.id}`);


```

## Step 2: Create a Split Job
[Section titled “Step 2: Create a Split Job”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#step-2-create-a-split-job)
Create a split job with category definitions. Each category needs a `name` and a `description` that helps the AI understand what content belongs to that category:


```


job = client.beta.split.create(




document_input={




"type": "file_id",




"value": file_id,





categories=[





"name": "essay",




"description": "A philosophical or reflective piece of writing that presents personal viewpoints, arguments, or thoughts on a topic without strict formal structure",






"name": "research_paper",




"description": "A formal academic document presenting original research, methodology, experiments, results, and conclusions with citations and references",








print(f"✅ Split job created: {job.id}")




print(f"   Status: {job.status}")


```

```


const job = await client.beta.split.create({




document_input: {




type: "file_id",




value: fileId,





categories: [





name: "essay",




description:




"A philosophical or reflective piece of writing that presents personal viewpoints, arguments, or thoughts on a topic without strict formal structure",






name: "research_paper",




description:




"A formal academic document presenting original research, methodology, experiments, results, and conclusions with citations and references",








console.log(`✅ Split job created: ${job.id}`);




console.log(`   Status: ${job.status}`);


```

## Step 3: Poll for Completion
[Section titled “Step 3: Poll for Completion”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#step-3-poll-for-completion)
The split job runs asynchronously. Poll until it completes:


```


completed_job = client.beta.split.wait_for_completion(job.id,polling_interval=2.0)


```

```


const completedJob = await client.beta.split.waitForCompletion(job.id, { pollingInterval: 2.0 });


```

## Step 4: Analyze Results
[Section titled “Step 4: Analyze Results”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#step-4-analyze-results)
Examine the split results:


```


segments = completed_job.result.segments if completed_job.result else[]





print(f"📊 Total segments found: (segments)}")





for i, segment inenumerate(segments,1):




category = segment.category




pages = segment.pages




confidence = segment.confidence_category





iflen(pages) ==1:




page_range =f"Page {pages[0]}"




else:




page_range =f"Pages (pages)}-(pages)}"





print(f"\nSegment {i}:")




print(f"   Category: {category}")




print(f{page_range} ((pages)} pages)")




print(f"   Confidence: {confidence}")


```

```


const segmentscompletedJob.result?.segments || [];





console.log(`📊 Total segments found: ${segments.length}`);





segments.forEach((segment, index)=> {




const categorysegment.category;




const pagessegment.pages;




const confidencesegment.confidence_category;





const pageRange =




pages.length === 1




?`Page ${pages[0]}`




:`Pages ${Math.min(...pages)}-${Math.max(...pages)}`;





console.log(`\nSegment ${index+1}:`);




console.log(`   Category: ${category}`);




console.log(`${pageRange} (${pages.length} pages)`);




console.log(`   Confidence: ${confidence}`);



});

```

### Expected Output
[Section titled “Expected Output”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#expected-output)
```

📊 Total segments found: 3



Segment 1:



Category: essay




Pages 1-4 (4 pages)




Confidence: high




Segment 2:



Category: research_paper




Pages 5-13 (9 pages)




Confidence: high




Segment 3:



Category: research_paper




Pages 14-24 (11 pages)




Confidence: high


```

The Split API correctly identified:
  * **1 essay segment** : Alan Turing’s “Intelligent Machinery, A Heretical Theory”
  * **2 research paper segments** : ImageNet paper and “Attention is All You Need”


## Using `allow_uncategorized`
[Section titled “Using allow_uncategorized”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#using-allow_uncategorized)
You can use the `allow_uncategorized` strategy when you want to capture pages that don’t match any defined category:


```


job = client.beta.split.create(...,splitting_strategy={"allow_uncategorized": True})


```

```


const job = await client.beta.split.create({..., splitting_strategy: { allow_uncategorized: true } });


```

With this configuration, pages that don’t match `essay` will be grouped as `uncategorized`.
## Next Steps
[Section titled “Next Steps”](https://developers.llamaindex.ai/python/cloud/split/examples/document_splitting/#next-steps)
  * Explore the [REST API reference](https://developers.llamaindex.ai/python/cloud/split/examples/getting_started/api) for all available options
  * Combine Split with [LlamaExtract](https://developers.llamaindex.ai/python/cloud/split/llamaextract/getting_started) to run targeted extraction on each segment
  * Use [LlamaParse](https://developers.llamaindex.ai/python/cloud/split/llamaparse/getting_started) to parse individual segments with optimized settings


