# Opendal
##  OpendalAzblobReader [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/opendal/#llama_index.readers.opendal.OpendalAzblobReader "Permanent link")
Bases: 
General reader for any Azblob file or directory.
Source code in `llama_index/readers/opendal/azblob/base.py`
```
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
```
| ```
class OpendalAzblobReader(BaseReader):
"""General reader for any Azblob file or directory."""

    def __init__(
        self,
        container: str,
        path: str = "/",
        endpoint: str = "",
        account_name: str = "",
        account_key: str = "",
        file_extractor: Optional[Dict[str, Union[str, BaseReader]]] = None,
    ) -> None:
"""
        Initialize Azblob container, along with credentials if needed.

        If key is not set, the entire bucket (filtered by prefix) is parsed.

        Args:
        container (str): the name of your azblob bucket
        path (str): the path of the data. If none is provided,
            this loader will iterate through the entire bucket. If path is endswith `/`, this loader will iterate through the entire dir. Otherwise, this loeader will load the file.
        endpoint Optional[str]: the endpoint of the azblob service.
        account_name (Optional[str]): provide azblob access key directly.
        account_key (Optional[str]): provide azblob access key directly.
        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file
            extension to a BaseReader class that specifies how to convert that file
            to text. See `SimpleDirectoryReader` for more details.

        """
        super().__init__()

        self.path = path
        self.file_extractor = file_extractor

        # opendal service related config.
        self.options = {
            "container": container,
            "endpoint": endpoint,
            "account_name": account_name,
            "account_key": account_key,
        }

    def load_data(self) -> List[Document]:
"""Load file(s) from OpenDAL."""
        loader = OpendalReader(
            scheme="azblob",
            path=self.path,
            file_extractor=self.file_extractor,
            **self.options,
        )

        return loader.load_data()

```
  
---|---  
###  load_data [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/opendal/#llama_index.readers.opendal.OpendalAzblobReader.load_data "Permanent link")
```
load_data() -> []

```

Load file(s) from OpenDAL.
Source code in `llama_index/readers/opendal/azblob/base.py`
```
57
58
59
60
61
62
63
64
65
66
```
| ```
def load_data(self) -> List[Document]:
"""Load file(s) from OpenDAL."""
    loader = OpendalReader(
        scheme="azblob",
        path=self.path,
        file_extractor=self.file_extractor,
        **self.options,
    )

    return loader.load_data()

```
  
---|---  
##  OpendalReader [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/opendal/#llama_index.readers.opendal.OpendalReader "Permanent link")
Bases: 
General reader for any opendal operator.
Source code in `llama_index/readers/opendal/base.py`
```
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
```
| ```
class OpendalReader(BaseReader):
"""General reader for any opendal operator."""

    def __init__(
        self,
        scheme: str,
        path: str = "/",
        file_extractor: Optional[Dict[str, Union[str, BaseReader]]] = None,
        **kwargs,
    ) -> None:
"""
        Initialize opendal operator, along with credentials if needed.


        Args:
        scheme (str): the scheme of the service
        path (str): the path of the data. If none is provided,
            this loader will iterate through the entire bucket. If path is endswith `/`, this loader will iterate through the entire dir. Otherwise, this loeader will load the file.
        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file
            extension to a BaseReader class that specifies how to convert that file
            to text. See `SimpleDirectoryReader` for more details.

        """
        import opendal

        super().__init__()

        self.path = path
        self.file_extractor = file_extractor

        self.op = opendal.AsyncOperator(scheme, **kwargs)

    def load_data(self) -> List[Document]:
"""Load file(s) from OpenDAL."""
        with tempfile.TemporaryDirectory() as temp_dir:
            if not self.path.endswith("/"):
                asyncio.run(download_file_from_opendal(self.op, temp_dir, self.path))
            else:
                asyncio.run(download_dir_from_opendal(self.op, temp_dir, self.path))

            loader = SimpleDirectoryReader(temp_dir, file_extractor=self.file_extractor)

            return loader.load_data()

```
  
---|---  
###  load_data [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/opendal/#llama_index.readers.opendal.OpendalReader.load_data "Permanent link")
```
load_data() -> []

```

Load file(s) from OpenDAL.
Source code in `llama_index/readers/opendal/base.py`
```
50
51
52
53
54
55
56
57
58
59
60
```
| ```
def load_data(self) -> List[Document]:
"""Load file(s) from OpenDAL."""
    with tempfile.TemporaryDirectory() as temp_dir:
        if not self.path.endswith("/"):
            asyncio.run(download_file_from_opendal(self.op, temp_dir, self.path))
        else:
            asyncio.run(download_dir_from_opendal(self.op, temp_dir, self.path))

        loader = SimpleDirectoryReader(temp_dir, file_extractor=self.file_extractor)

        return loader.load_data()

```
  
---|---  
##  OpendalGcsReader [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/opendal/#llama_index.readers.opendal.OpendalGcsReader "Permanent link")
Bases: 
General reader for any Gcs file or directory.
Source code in `llama_index/readers/opendal/gcs/base.py`
```
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
```
| ```
class OpendalGcsReader(BaseReader):
"""General reader for any Gcs file or directory."""

    def __init__(
        self,
        bucket: str,
        path: str = "/",
        endpoint: str = "",
        credentials: str = "",
        file_extractor: Optional[Dict[str, Union[str, BaseReader]]] = None,
    ) -> None:
"""
        Initialize Gcs container, along with credentials if needed.

        If key is not set, the entire bucket (filtered by prefix) is parsed.

        Args:
        bucket (str): the name of your gcs bucket
        path (str): the path of the data. If none is provided,
            this loader will iterate through the entire bucket. If path is endswith `/`, this loader will iterate through the entire dir. Otherwise, this loeader will load the file.
        endpoint Optional[str]: the endpoint of the azblob service.
        credentials (Optional[str]): provide credential string for GCS OAuth2 directly.
        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file
            extension to a BaseReader class that specifies how to convert that file
            to text. See `SimpleDirectoryReader` for more details.

        """
        super().__init__()

        self.path = path
        self.file_extractor = file_extractor

        # opendal service related config.
        self.options = {
            "bucket": bucket,
            "endpoint": endpoint,
            "credentials": credentials,
        }

    def load_data(self) -> List[Document]:
"""Load file(s) from OpenDAL."""
        loader = OpendalReader(
            scheme="gcs",
            path=self.path,
            file_extractor=self.file_extractor,
            **self.options,
        )

        return loader.load_data()

```
  
---|---  
###  load_data [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/opendal/#llama_index.readers.opendal.OpendalGcsReader.load_data "Permanent link")
```
load_data() -> []

```

Load file(s) from OpenDAL.
Source code in `llama_index/readers/opendal/gcs/base.py`
```
54
55
56
57
58
59
60
61
62
63
```
| ```
def load_data(self) -> List[Document]:
"""Load file(s) from OpenDAL."""
    loader = OpendalReader(
        scheme="gcs",
        path=self.path,
        file_extractor=self.file_extractor,
        **self.options,
    )

    return loader.load_data()

```
  
---|---  
##  OpendalS3Reader [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/opendal/#llama_index.readers.opendal.OpendalS3Reader "Permanent link")
Bases: 
General reader for any S3 file or directory.
Source code in `llama_index/readers/opendal/s3/base.py`
```
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
```
| ```
class OpendalS3Reader(BaseReader):
"""General reader for any S3 file or directory."""

    def __init__(
        self,
        bucket: str,
        path: str = "/",
        endpoint: str = "",
        region: str = "",
        access_key_id: str = "",
        secret_access_key: str = "",
        file_extractor: Optional[Dict[str, Union[str, BaseReader]]] = None,
    ) -> None:
"""
        Initialize S3 bucket and key, along with credentials if needed.

        If key is not set, the entire bucket (filtered by prefix) is parsed.

        Args:
        bucket (str): the name of your S3 bucket
        path (str): the path of the data. If none is provided,
            this loader will iterate through the entire bucket. If path is endswith `/`, this loader will iterate through the entire dir. Otherwise, this loeader will load the file.
        endpoint Optional[str]: the endpoint of the S3 service.
        region: Optional[str]: the region of the S3 service.
        access_key_id (Optional[str]): provide AWS access key directly.
        secret_access_key (Optional[str]): provide AWS access key directly.
        file_extractor (Optional[Dict[str, BaseReader]]): A mapping of file
            extension to a BaseReader class that specifies how to convert that file
            to text. See `SimpleDirectoryReader` for more details.

        """
        super().__init__()

        self.path = path
        self.file_extractor = file_extractor

        # opendal service related config.
        self.options = {
            "access_key": access_key_id,
            "secret_key": secret_access_key,
            "endpoint": endpoint,
            "region": region,
            "bucket": bucket,
        }

    def load_data(self) -> List[Document]:
"""Load file(s) from OpenDAL."""
        loader = OpendalReader(
            scheme="s3",
            path=self.path,
            file_extractor=self.file_extractor,
            **self.options,
        )

        return loader.load_data()

```
  
---|---  
###  load_data [#](https://developers.llamaindex.ai/python/framework-api-reference/readers/opendal/#llama_index.readers.opendal.OpendalS3Reader.load_data "Permanent link")
```
load_data() -> []

```

Load file(s) from OpenDAL.
Source code in `llama_index/readers/opendal/s3/base.py`
```
60
61
62
63
64
65
66
67
68
69
```
| ```
def load_data(self) -> List[Document]:
"""Load file(s) from OpenDAL."""
    loader = OpendalReader(
        scheme="s3",
        path=self.path,
        file_extractor=self.file_extractor,
        **self.options,
    )

    return loader.load_data()

```
  
---|---  
options: members: - OpendalAzblobReader - OpendalGcsReader - OpendalReader - OpendalS3Reader
