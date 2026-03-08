# Oracleai
##  OracleEmbeddings [#](https://developers.llamaindex.ai/python/framework-api-reference/embeddings/oracleai/#llama_index.embeddings.oracleai.OracleEmbeddings "Permanent link")
Bases: 
Get Embeddings.
Source code in `llama_index/embeddings/oracleai/base.py`
```
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
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
```
| ```
class OracleEmbeddings(BaseEmbedding):
"""Get Embeddings."""

    _conn: Any = PrivateAttr()
    _params: Dict[str, Any] = PrivateAttr()
    _proxy: Optional[str] = PrivateAttr()

    def __init__(
        self,
        conn: Connection,
        params: Dict[str, Any],
        proxy: Optional[str] = None,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self._conn = conn
        self._proxy = proxy
        self._params = params

    @classmethod
    def class_name(self) -> str:
        return "OracleEmbeddings"

    @staticmethod
    def load_onnx_model(conn: Connection, dir: str, onnx_file: str, model_name: str):
"""
        Load an ONNX model to Oracle Database.

        Args:
            conn: Oracle Connection,
            dir: Oracle Directory,
            onnx_file: ONNX file name,
            model_name: Name of the model.
            Note: user needs to have create procedure,
                  create mining model, create any directory privilege.

        """
        try:
            if conn is None or dir is None or onnx_file is None or model_name is None:
                raise Exception("Invalid input")

            cursor = conn.cursor()
            cursor.execute(
"""
                begin
                    dbms_data_mining.drop_model(model_name => :model, force => true);
                    SYS.DBMS_VECTOR.load_onnx_model(:path, :filename, :model, json('{"function" : "embedding", "embeddingOutput" : "embedding" , "input": {"input": ["DATA"]}}'));
                end;""",
                path=dir,
                filename=onnx_file,
                model=model_name,
            )

            cursor.close()

        except Exception as ex:
            print(f"An exception occurred :: {ex}")
            cursor.close()
            raise

    def _get_embedding(self, text: str) -> List[float]:
        try:
            import oracledb
        except ImportError as e:
            raise ImportError(
                "Unable to import oracledb, please install with "
                "`pip install -U oracledb`."
            ) from e

        if text is None:
            return None

        embedding = None
        try:
            oracledb.defaults.fetch_lobs = False
            cursor = self._conn.cursor()

            if self._proxy:
                cursor.execute(
                    "begin utl_http.set_proxy(:proxy); end;", proxy=self._proxy
                )

            cursor.execute(
                "select t.* from dbms_vector_chain.utl_to_embeddings(:content, json(:params)) t",
                content=text,
                params=json.dumps(self._params),
            )

            row = cursor.fetchone()
            if row is None:
                embedding = []
            else:
                rdata = json.loads(row[0])
                # dereference string as array
                embedding = json.loads(rdata["embed_vector"])

            cursor.close()
            return embedding
        except Exception as ex:
            print(f"An exception occurred :: {ex}")
            cursor.close()
            raise

    def _get_embeddings(self, texts: List[str]) -> List[List[float]]:
"""
        Compute doc embeddings using an OracleEmbeddings.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each input text.

        """
        try:
            import oracledb
        except ImportError as e:
            raise ImportError(
                "Unable to import oracledb, please install with "
                "`pip install -U oracledb`."
            ) from e

        if texts is None:
            return None

        embeddings: List[List[float]] = []
        try:
            # returns strings or bytes instead of a locator
            oracledb.defaults.fetch_lobs = False
            cursor = self._conn.cursor()

            if self._proxy:
                cursor.execute(
                    "begin utl_http.set_proxy(:proxy); end;", proxy=self._proxy
                )

            chunks = []
            for i, text in enumerate(texts, start=1):
                chunk = {"chunk_id": i, "chunk_data": text}
                chunks.append(json.dumps(chunk))

            vector_array_type = self._conn.gettype("SYS.VECTOR_ARRAY_T")
            inputs = vector_array_type.newobject(chunks)
            cursor.execute(
                "select t.* "
                + "from dbms_vector_chain.utl_to_embeddings(:content, "
                + "json(:params)) t",
                content=inputs,
                params=json.dumps(self._params),
            )

            for row in cursor:
                if row is None:
                    embeddings.append([])
                else:
                    rdata = json.loads(row[0])
                    # dereference string as array
                    vec = json.loads(rdata["embed_vector"])
                    embeddings.append(vec)

            cursor.close()
            return embeddings
        except Exception as ex:
            print(f"An exception occurred :: {ex}")
            cursor.close()
            raise

    def _get_query_embedding(self, query: str) -> List[float]:
        return self._get_embedding(query)

    async def _aget_query_embedding(self, query: str) -> List[float]:
        return self._get_query_embedding(query)

    def _get_text_embedding(self, text: str) -> List[float]:
        return self._get_embedding(text)

    async def _aget_text_embedding(self, text: str) -> List[float]:
        return self._get_text_embedding(text)

    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self._get_embeddings(texts)

    async def _aget_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self._get_text_embeddings(texts)

```
  
---|---  
###  load_onnx_model `staticmethod` [#](https://developers.llamaindex.ai/python/framework-api-reference/embeddings/oracleai/#llama_index.embeddings.oracleai.OracleEmbeddings.load_onnx_model "Permanent link")
```
load_onnx_model(conn: Connection, dir: , onnx_file: , model_name: )

```

Load an ONNX model to Oracle Database.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`conn` |  `Connection` |  Oracle Connection, |  _required_  
`dir` |  Oracle Directory, |  _required_  
`onnx_file` |  ONNX file name, |  _required_  
`model_name` |  Name of the model. |  _required_  
`Note` |  user needs to have create procedure, create mining model, create any directory privilege. |  _required_  
Source code in `llama_index/embeddings/oracleai/base.py`
```
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
70
71
72
73
74
75
76
77
78
79
80
81
82
83
```
| ```
@staticmethod
def load_onnx_model(conn: Connection, dir: str, onnx_file: str, model_name: str):
"""
    Load an ONNX model to Oracle Database.

    Args:
        conn: Oracle Connection,
        dir: Oracle Directory,
        onnx_file: ONNX file name,
        model_name: Name of the model.
        Note: user needs to have create procedure,
              create mining model, create any directory privilege.

    """
    try:
        if conn is None or dir is None or onnx_file is None or model_name is None:
            raise Exception("Invalid input")

        cursor = conn.cursor()
        cursor.execute(
"""
            begin
                dbms_data_mining.drop_model(model_name => :model, force => true);
                SYS.DBMS_VECTOR.load_onnx_model(:path, :filename, :model, json('{"function" : "embedding", "embeddingOutput" : "embedding" , "input": {"input": ["DATA"]}}'));
            end;""",
            path=dir,
            filename=onnx_file,
            model=model_name,
        )

        cursor.close()

    except Exception as ex:
        print(f"An exception occurred :: {ex}")
        cursor.close()
        raise

```
  
---|---  
options: members: - OracleEmbeddings
