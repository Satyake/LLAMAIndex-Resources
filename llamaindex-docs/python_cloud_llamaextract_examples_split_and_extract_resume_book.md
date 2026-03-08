[Skip to content](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#_top)
# Resume Book Processing Agent
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Processing resume books can be time-consuming when you need to extract structured information from hundreds of resumes. This notebook demonstrates how to build an intelligent agent that automatically processes resume books using [LlamaAgent Workflows](https://developers.llamaindex.ai/python/llamaagents/workflows/), [LlamaSplit](https://developers.llamaindex.ai/python/cloud/split/getting_started/) and [LlamaExtract](https://developers.llamaindex.ai/python/cloud/llamaextract/getting_started/). The agent:
  1. **Uploads** PDF documents to LlamaCloud
  2. **Splits** the document into logical segments (resumes vs. curriculum/index)
  3. **Extracts** structured data from each resume
  4. **Orchestrates** the entire process using LlamaIndex workflows


## Getting the Resume Book
[Section titled “Getting the Resume Book”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#getting-the-resume-book)
For this example, we’ll use the NYU Math-Finance Full-Time Resume Book. You can download it from:
Save the file locally (e.g., as `resume_book.pdf`) before proceeding.
## Overview
[Section titled “Overview”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#overview)
The workflow uses two key LlamaCloud services:
  * : Categorizes document pages into different types (resumes, curriculum pages, cover pages, etc.)
  * : Extracts structured data from documents using AI


Let’s start by installing the required dependencies.
```


pip install llama-cloud>=1.0 requests llama-index-workflows


```

```


import os




from getpass import getpass





if"OPENAI_API_KEY"notin os.environ:




os.environ["OPENAI_API_KEY"] =getpass("OPENAI_API_KEY")




if"LLAMA_CLOUD_API_KEY"notin os.environ:




os.environ["LLAMA_CLOUD_API_KEY"] =getpass("LLAMA_CLOUD_API_KEY")


```

## Step 1: Upload File to LlamaCloud
[Section titled “Step 1: Upload File to LlamaCloud”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#step-1-upload-file-to-llamacloud)
Before we can process the document, we need to upload it to LlamaCloud. This gives us a `file_id` that we can use with other LlamaCloud APIs.
The `LlamaCloud` client provides a convenient `upload_file()` method that handles the upload and returns metadata including the file ID.
```


from llama_cloud import LlamaCloud, AsyncLlamaCloud





client =AsyncLlamaCloud(api_key=os.getenv("LLAMA_CLOUD_API_KEY"))




# Update this path to where you saved the resume book



pdf_path ="resume_book.pdf"# or "/content/resume_book.pdf" in Colab





uploaded_file =await client.files.create(file=pdf_path,purpose="extract")





file_id = uploaded_file.id




print(f"✅ File uploaded: {file_id}")


```

## Step 2: Split Document into Categories
[Section titled “Step 2: Split Document into Categories”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#step-2-split-document-into-categories)
Now we’ll use LlamaCloud’s to automatically categorize pages in the document. This is useful when a document contains multiple types of content.
We define categories:
  * **`resume`**: Individual resume pages from candidates
  * **`curriculum`**: The overall student curriculum page listing the program curriculum
  * **`cover_page`**: Cover page or title page (optional, depending on document structure)


The Split API uses AI to analyze each page and assign it to the appropriate category. This creates a job that runs asynchronously, so we’ll need to poll for results.
```

# Split the document and wait for completion


# Each category needs a name and a description that helps the AI


# understand what content belongs to that category



response =await client.beta.split.split(




categories=[





"name": "resume",




"description": "A resume page from an individual candidate containing their professional information, education, and experience",






"name": "curriculum",




"description": "The overall student curriculum page listing the program curriculum",






"name": "cover_page",




"description": "Cover page, title page, or introductory page of the resume book",






document_input={"type": "file_id", "value": file_id},





# Print the splitting results



print(f"Split job completed with status: {result.status}")




print()





if response.result:




print(f"📊 Total segments found: (response.result.segments)}")




for i, segment inenumerate(response.result.segments,1):




pages = segment.pages




iflen(pages) ==1:




page_range =f"Page {pages[0]}"




else:




page_range =f"Pages (pages)}-(pages)}"





print(f"\nSegment {i}:")




print(f"   Category: {segment.category}")




print(f{page_range} ((pages)} pages)")




print(f"   Confidence: {segment.confidence_category}")


```

## Step 3: Define Extraction Schema and Extract Data
[Section titled “Step 3: Define Extraction Schema and Extract Data”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#step-3-define-extraction-schema-and-extract-data)
is a service that extracts structured data from documents. We’ll use it to extract resume information from each candidate’s resume.
The extractor will use a Pydantic schema to define the structure of data we want to extract.
We define a **Pydantic schema** (`ResumeSchema`) that describes the structure of data we want to extract from each resume:
  * Candidate name
  * Contact information (email, phone)
  * Education (degrees, institutions, dates)
  * Work experience (companies, roles, dates, descriptions)
  * Skills (technical skills, programming languages, etc.)
  * Additional information (certifications, languages, etc.)


The `ExtractConfig` specifies:
  * **`extraction_mode`**:`PREMIUM` for highest quality extraction
  * **`page_range`**: Extract from specific pages (e.g., “5” for the resume on page 5)
  * **`confidence_scores`**: Include confidence scores in results


We then call `extract()` to extract data from the specified page range.
```


from pydantic import BaseModel, Field




from typing import Optional, List





classEducation(BaseModel):




degree: str=Field(description="Degree type (e.g., B.S., M.S., Ph.D.)")




institution: str=Field(description="Name of the educational institution")




field_of_study: Optional[str] =Field(None,description="Field of study or major")




graduation_date: Optional[str] =Field(None,description="Graduation date or year")




gpa: Optional[str] =Field(None,description="GPA if mentioned")





classWorkExperience(BaseModel):




company: str=Field(description="Company or organization name")




position: str=Field(description="Job title or position")




start_date: Optional[str] =Field(None,description="Start date")




end_date: Optional[str] =Field(None,description="End date (or 'Present' if current)")




description: Optional[str] =Field(None,description="Job description or key responsibilities")





classResumeSchema(BaseModel):




name: str=Field(description="Full name of the candidate")




email: Optional[str] =Field(None,description="Email address")




phone: Optional[str] =Field(None,description="Phone number")




location: Optional[str] =Field(None,description="Location or address")




education: List[Education] =Field(description="List of educational qualifications")




work_experience: List[WorkExperience] =Field(description="List of work experiences")




skills: List[str] =Field(description="List of skills, programming languages, or technical competencies")




certifications: Optional[List[str]] =Field(None,description="Certifications or licenses")




languages: Optional[List[str]] =Field(None,description="Languages spoken")




summary: Optional[str] =Field(None,description="Professional summary or objective")





result =await client.extraction.extract(




file_id=file_id,




config={




"extraction_mode": "PREMIUM",




"use_reasoning": False,




"cite_sources": False,




"confidence_scores": True,




"page_range": "5"





data_schema=ResumeSchema.model_json_schema(),






extracted_result = ResumeSchema.model_validate(result.data)


```

### View Extracted Data
[Section titled “View Extracted Data”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#view-extracted-data)
Let’s see what data was extracted from the document. The result is a dictionary matching our `ResumeSchema`.
```

extracted_result.data

```

```

{'name': 'Quanquan (Lydia) Chen',



'email': 'q.chen@nyu.edu',




'phone': '(201) 626-0959',




'location': 'New York, NY',




'education': [{'degree': 'M.S.',




'institution': 'New York University',




'field_of_study': 'Mathematics in Finance',




'graduation_date': '12/24',




'gpa': None},




{'degree': 'B.S.',




'institution': 'Zhejiang University',




'field_of_study': 'Mathematics and Applied Mathematics',




'graduation_date': '06/23',




'gpa': None}],




'work_experience': [{'company': 'Numerix',




'position': 'Financial Engineering Intern',




'start_date': '07/24',




'end_date': 'Present',




'description': 'Developed models (e.g., Black-Scholes, Heston, Bates), applied market data and wrote payoff scripts to price exotic instruments (e.g., barrier options, variance swaps, cliquets, corridors). Conducted calibrations for equity and FX models with pricing and Greeks, considered different cases (e.g., time-dependent yield, projection rate, day-count conventions) to ensure accuracy. Researched and applied pricing algorithms (e.g., backward Monte Carlo for American options) in literature review from academic papers on financial products pricing.'},




{'company': 'Shenwan Hongyuan Securities Research Co., Ltd.',




'position': 'Financial Engineering Intern',




'start_date': '06/22',




'end_date': '11/22',




'description': 'Extracted fund data, manipulated and validated data through detecting outliers, dropping duplicates values, completed missing values with imputers, and reduce data dimensions. Applied PCA on portfolio, based on principal components and risk budgeting to build a new one, backtested it and obtained annualized return 7.16% and winning percentage nearly 85%. Anatomized low-cost fund data, summarized competitive advantages and background as well as business strategies of investment companies; researched other products, produced client reports.'}],




'skills': ['Python (Pandas, Numpy, Scipy, Matplotlib, Sklearn)',




'LaTeX',




'Excel'],




'certifications': None,




'languages': ['English (fluent)', 'Mandarin (native)'],




'summary': None}


```

## Step 4: Build a Workflow to Automate Everything
[Section titled “Step 4: Build a Workflow to Automate Everything”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#step-4-build-a-workflow-to-automate-everything)
Now we’ll orchestrate the entire process as a **LlamaIndex Workflow**
  1. **`split_document`step** :
     * Uploads the file
     * Creates a split job
     * Polls for completion
     * Emits an `ExtractResume` event for each segment
  2. **`extract_resume`step** :
     * Waits for all segments to be collected (fan-in pattern)
     * Extracts data from each “resume” segment
     * Returns all extracted resumes


### Key Workflow Concepts:
[Section titled “Key Workflow Concepts:”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#key-workflow-concepts)
  * **Events** : Custom event types (`ExtractResume`) to pass data between steps
  * **Fan-out/Fan-in** : The `split_document` step emits multiple events (one per segment), and `extract_resume` collects them all before proceeding
  * **Context Store** : Used to track how many segments we expect to collect
  * **Parallel Processing** : Multiple extraction events can be processed concurrently


```


from workflows import Workflow, step, Context




from workflows.events import StartEvent, StopEvent, Event





classExtractResume(Event):




file_path: str




category: str




pages: list[int]





classResumeBookAgent(Workflow):





def__init__(self, *args, **kwargs):




super().__init__(*args,**kwargs)




self.client =LlamaCloud(api_key=os.getenv("LLAMA_CLOUD_API_KEY"))





classResumeSchema(BaseModel):




name: str=Field(description="Full name of the candidate")




email: Optional[str] =Field(None,description="Email address")




phone: Optional[str] =Field(None,description="Phone number")




location: Optional[str] =Field(None,description="Location or address")




education: List[Education] =Field(description="List of educational qualifications")




work_experience: List[WorkExperience] =Field(description="List of work experiences")




skills: List[str] =Field(description="List of skills, programming languages, or technical competencies")




certifications: Optional[List[str]] =Field(None,description="Certifications or licenses")




languages: Optional[List[str]] =Field(None,description="Languages spoken")




summary: Optional[str] =Field(None,description="Professional summary or objective")





self.extract_schema = ResumeSchema




self.categories =[





"name": "resume",




"description": "A resume page from an individual candidate containing their professional information, education, and experience",






"name": "curriculum",




"description": "The overall student curriculum page listing the program curriculum",






"name": "cover_page",




"description": "Cover page, title page, or introductory page of the resume book",







@step




asyncdefsplit_document(self, ev: StartEvent, ctx: Context) -> ExtractResume:




uploaded_file =awaitself.client.files.create(file=ev.file_path,purpose="extract")





file_id = uploaded_file.id




await ctx.store.set("file_id", file_id)




print(f"✅ File uploaded: {uploaded_file.name}",flush=True)





response =awaitself.client.beta.split.split(




categories=self.categories,




document_input={"type": "file_id", "value": file_id},






segments = response.result.segments if response.result else[]




await ctx.store.set("segments_count",(segments))




for segment in segments:




ctx.send_event(ExtractResume(file_path=ev.file_path,category=segment.category,pages=segment.pages))





@step




asyncdefextract_resume(self, ev: ExtractResume, ctx: Context) -> StopEvent:




ready = ctx.collect_events(




ev,[ExtractResume]*await ctx.store.get("segments_count")





if ready isNone:




returnNone




extraction_result =[]




for event in ready:




if event.category =="resume":




file_id =await ctx.store.get("file_id")




extracted_result =awaitself.client.extraction.extract(




data_schema=self.extract_schema.model_json_schema(),




file_id=file_id,




config={"page_range": f"(event.pages)}-(event.pages)}"}





extraction_result.append(extracted_result.data)




returnStopEvent(result=extraction_result)


```

Running the agent end-to-end will look like this:
```


agent =ResumeBookAgent(timeout=1000)





resp =await agent.run(start_event=StartEvent(file_path="resume_book.pdf"))


```

✅ File uploaded: resume_book.pdf Status: pending (elapsed: 0s) Status: processing (elapsed: 5s) Status: processing (elapsed: 10s) Status: completed (elapsed: 15s)
```


for resume in resp[1:3]:




print(f"\n{'='*60}")




print(f"Name: {resume.get('name','N/A')}")




print(f"Education: {resume.get('education','N/A')}")




print(f"Skills: {', '.join(resume.get('skills',[]))}")




print(f"{'='*60}")


```

```

============================================================


Name: Shengjun (James) Guan


Education: [{'degree': 'M.S.', 'institution': 'New York University', 'field_of_study': 'Mathematics in Finance', 'graduation_date': '12/24', 'gpa': None}, {'degree': 'B.S.', 'institution': 'Rose-Hulman Institute of Technology', 'field_of_study': 'Mathematics and Data Science', 'graduation_date': '05/23', 'gpa': None}]


Skills: Python, Java, R, MongoDB, NoSQL, MATLAB, Maple


============================================================



============================================================


Name: Shupeng (Wayne) Guan


Education: [{'degree': 'M.S.', 'institution': 'New York University', 'field_of_study': 'Mathematics in Finance', 'graduation_date': '01/25', 'gpa': None}, {'degree': 'B.S.', 'institution': 'University of Birmingham', 'field_of_study': 'Mathematics With Honours (First Class)', 'graduation_date': '07/23', 'gpa': None}, {'degree': 'B.S.', 'institution': 'Huazhong University of Science and Technology', 'field_of_study': 'Finance', 'graduation_date': '06/21', 'gpa': '3.8/4'}]


Skills: Python, R, MATLAB, SQL, LaTex

```

## Next Steps
[Section titled “Next Steps”](https://developers.llamaindex.ai/python/cloud/llamaextract/examples/split_and_extract_resume_book/#next-steps)
Now that you have structured resume data, you can:
  * **Filter candidates** by skills, education, or experience
  * **Search** for specific qualifications
  * **Build a candidate matching system** based on job requirements
  * **Generate reports** on candidate demographics and qualifications


