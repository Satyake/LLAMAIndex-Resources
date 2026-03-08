[Skip to content](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#_top)
# Azure Blob Storage Data Source
Copy as Markdown
MCP Server
Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude config  Copy Codex config 
Load data from Azure Blob Storage.
## Configure via UI
[Section titled “Configure via UI”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#configure-via-ui)
We can load data by using two different types of authentication methods:
## 1. Account Key Authentication Mechanism
[Section titled “1. Account Key Authentication Mechanism”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#1-account-key-authentication-mechanism)
## 2. Service Principal Authentication Mechanism
[Section titled “2. Service Principal Authentication Mechanism”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#2-service-principal-authentication-mechanism)
## 3. SAS URL Authentication Mechanism
[Section titled “3. SAS URL Authentication Mechanism”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#3-sas-url-authentication-mechanism)
## Configure via API / Client
[Section titled “Configure via API / Client”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#configure-via-api--client)
#### 1. Account Key Authentication Mechanism
[Section titled “1. Account Key Authentication Mechanism”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#1-account-key-authentication-mechanism-1)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#tab-panel-294)
  * [ TypeScript (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#tab-panel-295)


```


from llama_cloud.types.data_source_create_params import (




CloudAzStorageBlobDataSource,






data_source = client.data_sources.create(




name="my-data-source",




component=CloudAzStorageBlobDataSource(




container_name='<container_name>',




account_url='<account_url>',




blob='<blob>',# optional




prefix='<prefix>',# optional




account_name='<account_name>',




account_key='<account_key>',





source_type="AZURE_STORAGE_BLOB",




project_id="my-project-id",



```

```


const dataSource = await client.dataSources.create({




name: 'my-data-source',




component: {




container_name: '<container_name>',




account_url: '<account_url>',




blob: '<blob>'// optional




prefix: '<prefix>'// optional




account_name: '<account_name>',




account_key: '<account_key>',





source_type: 'AZURE_STORAGE_BLOB',




project_id: 'my-project-id',



```

```


from llama_cloud.types import CloudAzStorageBlobDataSource





ds = {




'name': '<your-name>',




'source_type': 'AZURE_STORAGE_BLOB',




'component': CloudAzStorageBlobDataSource(




container_name='<container_name>',




account_url='<account_url>',




blob='<blob>',# optional




prefix='<prefix>',# optional




account_name='<account_name>',




account_key='<account_key>',






data_source = client.data_sources.create_data_source(request=ds)


```

```


const ds = {




'name': '<your-name>',




'sourceType': 'AZURE_STORAGE_BLOB',




'component': {




'container_name': '<container_name>',




'account_url': '<account_url>',




'blob': '<blob>'// optional




'prefix': '<prefix>'// optional




'account_name': '<account_name>',




'account_key': '<account_key>',







data_source =await client.dataSources.createDataSource({




body: ds



```

#### 2. Service Principal Authentication Mechanism
[Section titled “2. Service Principal Authentication Mechanism”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#2-service-principal-authentication-mechanism-1)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#tab-panel-298)
  * [ TypeScript (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#tab-panel-299)


```


from llama_cloud.types.data_source_create_params import (




CloudAzStorageBlobDataSource,






data_source = client.data_sources.create(




name="my-data-source",




component=CloudAzStorageBlobDataSource(




container_name='<container_name>',




account_url='<account_url>',




blob='<blob>',# optional




prefix='<prefix>',# optional




client_id='<client_id>',




client_secret='<client_secret>',




tenant_id='<tenant_id>',





source_type="AZURE_STORAGE_BLOB",




project_id="my-project-id",



```

```


const dataSource = await client.dataSources.create({




name: 'my-data-source',




component: {




container_name: '<container_name>',




account_url: '<account_url>',




blob: '<blob>'// optional




prefix: '<prefix>'// optional




client_id: '<client_id>',




client_secret: '<client_secret>',




tenant_id: '<tenant_id>',





source_type: 'AZURE_STORAGE_BLOB',




project_id: 'my-project-id',



```

```


from llama_cloud.types import CloudAzStorageBlobDataSource





ds = {




'name': '<your-name>',




'source_type': 'AZURE_STORAGE_BLOB',




'component': CloudAzStorageBlobDataSource(




container_name='<container_name>',




account_url='<account_url>',




blob='<blob>',# optional




prefix='<prefix>',# optional




client_id='<client_id>',




client_secret='<client_secret>',




tenant_id='<tenant_id>',






data_source = client.data_sources.create_data_source(request=ds)


```

```


const ds = {




'name': '<your-name>',




'sourceType': 'AZURE_STORAGE_BLOB',




'component': {




'container_name'='<container_name>',




'account_url'='<account_url>',




'blob'='<blob>'// optional




'prefix'='<prefix>'// optional




'client_id'='<client_id>',




'client_secret'='<client_secret>',




'tenant_id'='<tenant_id>',







data_source =await client.dataSources.createDataSource({




body: ds



```

#### 3. SAS URL Authentication Mechanism
[Section titled “3. SAS URL Authentication Mechanism”](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#3-sas-url-authentication-mechanism-1)
  * [ Python (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#tab-panel-302)
  * [ TypeScript (legacy) ](https://developers.llamaindex.ai/python/cloud/llamacloud/integrations/data_sources/azure_blob/#tab-panel-303)


```


from llama_cloud.types.data_source_create_params import (




CloudAzStorageBlobDataSource,





data_source = client.data_sources.create(




name="my-data-source",




component=CloudAzStorageBlobDataSource(




container_name='<container_name>',




account_url='<account_url>/?<SAS_TOKEN>',




blob='<blob>',# optional




prefix='<prefix>',# optional





source_type="AZURE_STORAGE_BLOB",




project_id="my-project-id",



```

```


const dataSource = await client.dataSources.create({




name: 'my-data-source',




component: {




container_name: '<container_name>',




account_url: '<account_url>/?<SAS_TOKEN>',




blob: '<blob>'// optional




prefix: '<prefix>'// optional





source_type: 'AZURE_STORAGE_BLOB',




project_id: 'my-project-id',



```

```


from llama_cloud.types import CloudAzStorageBlobDataSource





ds = {




'name': '<your-name>',




'source_type': 'AZURE_STORAGE_BLOB',




'component': CloudAzStorageBlobDataSource(




container_name='<container_name>',




account_url='<account_url>/?<SAS_TOKEN>',




blob='<blob>',# optional




prefix='<prefix>',# optional






data_source = client.data_sources.create_data_source(request=ds)


```

```


const ds = {




'name': '<your-name>',




'sourceType': 'AZURE_STORAGE_BLOB',




'component': {




'container_name': '<container_name>',




'account_url': '<account_url>/?<SAS_TOKEN>',




'blob': '<blob>'// optional




'prefix': '<prefix>'// optional







data_source =await client.dataSources.createDataSource({




body: ds



```

