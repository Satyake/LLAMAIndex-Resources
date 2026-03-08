# Google
##  GoogleCalendarToolSpec [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GoogleCalendarToolSpec "Permanent link")
Bases: 
Google Calendar tool spec.
Currently a simple wrapper around the data loader. TODO: add more methods to the Google Calendar spec.
Source code in `llama_index/tools/google/calendar/base.py`
```
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
209
210
211
212
213
214
215
216
217
218
219
220
221
222
```
| ```
class GoogleCalendarToolSpec(BaseToolSpec):
"""
    Google Calendar tool spec.

    Currently a simple wrapper around the data loader.
    TODO: add more methods to the Google Calendar spec.

    """

    spec_functions = ["load_data", "create_event", "get_date"]

    def __init__(self, creds: Optional[Any] = None):
"""
        Initialize the GoogleCalendarToolSpec.

        Args:
            creds (Optional[Any]): Pre-configured credentials to use for authentication.
                                 If provided, these will be used instead of the OAuth flow.

        """
        self.creds = creds

    def load_data(
        self,
        number_of_results: Optional[int] = 100,
        start_date: Optional[Union[str, datetime.date]] = None,
    ) -> List[Document]:
"""
        Load data from user's calendar.

        Args:
            number_of_results (Optional[int]): the number of events to return. Defaults to 100.
            start_date (Optional[Union[str, datetime.date]]): the start date to return events from in date isoformat. Defaults to today.

        """
        from googleapiclient.discovery import build

        credentials = self._get_credentials()
        service = build("calendar", "v3", credentials=credentials)

        if start_date is None:
            start_date = datetime.date.today()
        elif isinstance(start_date, str):
            start_date = datetime.date.fromisoformat(start_date)

        start_datetime = datetime.datetime.combine(start_date, datetime.time.min)
        start_datetime_utc = start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=start_datetime_utc,
                maxResults=number_of_results,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = events_result.get("items", [])

        if not events:
            return []

        results = []
        for event in events:
            if "dateTime" in event["start"]:
                start_time = event["start"]["dateTime"]
            else:
                start_time = event["start"]["date"]

            if "dateTime" in event["end"]:
                end_time = event["end"]["dateTime"]
            else:
                end_time = event["end"]["date"]

            event_string = f"Status: {event['status']}, "
            event_string += f"Summary: {event['summary']}, "
            event_string += f"Start time: {start_time}, "
            event_string += f"End time: {end_time}, "

            organizer = event.get("organizer", {})
            display_name = organizer.get("displayName", "N/A")
            email = organizer.get("email", "N/A")
            if display_name != "N/A":
                event_string += f"Organizer: {display_name} ({email})"
            else:
                event_string += f"Organizer: {email}"

            results.append(Document(text=event_string))

        return results

    def _get_credentials(self) -> Any:
"""
        Get valid user credentials from storage.

        The file token.json stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first
        time.

        Returns:
            Credentials, the obtained credential.

        """
        if self.creds is not None:
            return self.creds

        from google_auth_oauthlib.flow import InstalledAppFlow

        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials

        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=8080)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return creds

    def create_event(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        location: Optional[str] = None,
        start_datetime: Optional[Union[str, datetime.datetime]] = None,
        end_datetime: Optional[Union[str, datetime.datetime]] = None,
        attendees: Optional[List[str]] = None,
    ) -> str:
"""
            Create an event on the users calendar.

        Args:
            title (Optional[str]): The title for the event
            description (Optional[str]): The description for the event
            location (Optional[str]): The location for the event
            start_datetime Optional[Union[str, datetime.datetime]]: The start datetime for the event
            end_datetime Optional[Union[str, datetime.datetime]]: The end datetime for the event
            attendees Optional[List[str]]: A list of email address to invite to the event

        """
        from googleapiclient.discovery import build

        credentials = self._get_credentials()
        service = build("calendar", "v3", credentials=credentials)

        attendees_list = (
            [{"email": attendee} for attendee in attendees] if attendees else []
        )

        start_time = (
            datetime.datetime.strptime(start_datetime, "%Y-%m-%dT%H:%M:%S%z")
            .astimezone()
            .strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        )
        end_time = (
            datetime.datetime.strptime(end_datetime, "%Y-%m-%dT%H:%M:%S%z")
            .astimezone()
            .strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        )

        event = {
            "summary": title,
            "location": location,
            "description": description,
            "start": {
                "dateTime": start_time,
            },
            "end": {
                "dateTime": end_time,
            },
            "attendees": attendees_list,
        }
        event = service.events().insert(calendarId="primary", body=event).execute()
        return (
            "Your calendar event has been created successfully! You can move on to the"
            " next step."
        )

    def get_date(self):
"""
        A function to return todays date. Call this before any other functions if you are unaware of the date.
        """
        return datetime.date.today()

```
  
---|---  
###  load_data [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GoogleCalendarToolSpec.load_data "Permanent link")
```
load_data(number_of_results: Optional[] = 100, start_date: Optional[Union[, ]] = None) -> []

```

Load data from user's calendar.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`number_of_results` |  `Optional[int]` |  the number of events to return. Defaults to 100. |  `100`  
`start_date` |  `Optional[Union[str, date]]` |  the start date to return events from in date isoformat. Defaults to today. |  `None`  
Source code in `llama_index/tools/google/calendar/base.py`
```
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
```
| ```
def load_data(
    self,
    number_of_results: Optional[int] = 100,
    start_date: Optional[Union[str, datetime.date]] = None,
) -> List[Document]:
"""
    Load data from user's calendar.

    Args:
        number_of_results (Optional[int]): the number of events to return. Defaults to 100.
        start_date (Optional[Union[str, datetime.date]]): the start date to return events from in date isoformat. Defaults to today.

    """
    from googleapiclient.discovery import build

    credentials = self._get_credentials()
    service = build("calendar", "v3", credentials=credentials)

    if start_date is None:
        start_date = datetime.date.today()
    elif isinstance(start_date, str):
        start_date = datetime.date.fromisoformat(start_date)

    start_datetime = datetime.datetime.combine(start_date, datetime.time.min)
    start_datetime_utc = start_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_datetime_utc,
            maxResults=number_of_results,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])

    if not events:
        return []

    results = []
    for event in events:
        if "dateTime" in event["start"]:
            start_time = event["start"]["dateTime"]
        else:
            start_time = event["start"]["date"]

        if "dateTime" in event["end"]:
            end_time = event["end"]["dateTime"]
        else:
            end_time = event["end"]["date"]

        event_string = f"Status: {event['status']}, "
        event_string += f"Summary: {event['summary']}, "
        event_string += f"Start time: {start_time}, "
        event_string += f"End time: {end_time}, "

        organizer = event.get("organizer", {})
        display_name = organizer.get("displayName", "N/A")
        email = organizer.get("email", "N/A")
        if display_name != "N/A":
            event_string += f"Organizer: {display_name} ({email})"
        else:
            event_string += f"Organizer: {email}"

        results.append(Document(text=event_string))

    return results

```
  
---|---  
###  create_event [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GoogleCalendarToolSpec.create_event "Permanent link")
```
create_event(title: Optional[] = None, description: Optional[] = None, location: Optional[] = None, start_datetime: Optional[Union[, datetime]] = None, end_datetime: Optional[Union[, datetime]] = None, attendees: Optional[[]] = None) -> 

```

```
Create an event on the users calendar.

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`title` |  `Optional[str]` |  The title for the event |  `None`  
`description` |  `Optional[str]` |  The description for the event |  `None`  
`location` |  `Optional[str]` |  The location for the event |  `None`  
`start_datetime Optional[Union[str, datetime.datetime]]` |  The start datetime for the event |  _required_  
`end_datetime Optional[Union[str, datetime.datetime]]` |  The end datetime for the event |  _required_  
`attendees Optional[List[str]]` |  A list of email address to invite to the event |  _required_  
Source code in `llama_index/tools/google/calendar/base.py`
```
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
209
210
211
212
213
214
215
216
```
| ```
def create_event(
    self,
    title: Optional[str] = None,
    description: Optional[str] = None,
    location: Optional[str] = None,
    start_datetime: Optional[Union[str, datetime.datetime]] = None,
    end_datetime: Optional[Union[str, datetime.datetime]] = None,
    attendees: Optional[List[str]] = None,
) -> str:
"""
        Create an event on the users calendar.

    Args:
        title (Optional[str]): The title for the event
        description (Optional[str]): The description for the event
        location (Optional[str]): The location for the event
        start_datetime Optional[Union[str, datetime.datetime]]: The start datetime for the event
        end_datetime Optional[Union[str, datetime.datetime]]: The end datetime for the event
        attendees Optional[List[str]]: A list of email address to invite to the event

    """
    from googleapiclient.discovery import build

    credentials = self._get_credentials()
    service = build("calendar", "v3", credentials=credentials)

    attendees_list = (
        [{"email": attendee} for attendee in attendees] if attendees else []
    )

    start_time = (
        datetime.datetime.strptime(start_datetime, "%Y-%m-%dT%H:%M:%S%z")
        .astimezone()
        .strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    )
    end_time = (
        datetime.datetime.strptime(end_datetime, "%Y-%m-%dT%H:%M:%S%z")
        .astimezone()
        .strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    )

    event = {
        "summary": title,
        "location": location,
        "description": description,
        "start": {
            "dateTime": start_time,
        },
        "end": {
            "dateTime": end_time,
        },
        "attendees": attendees_list,
    }
    event = service.events().insert(calendarId="primary", body=event).execute()
    return (
        "Your calendar event has been created successfully! You can move on to the"
        " next step."
    )

```
  
---|---  
###  get_date [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GoogleCalendarToolSpec.get_date "Permanent link")
```
get_date()

```

A function to return todays date. Call this before any other functions if you are unaware of the date.
Source code in `llama_index/tools/google/calendar/base.py`
```
218
219
220
221
222
```
| ```
def get_date(self):
"""
    A function to return todays date. Call this before any other functions if you are unaware of the date.
    """
    return datetime.date.today()

```
  
---|---  
##  GmailToolSpec [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GmailToolSpec "Permanent link")
Bases: 
GMail tool spec.
Gives the agent the ability to read, draft and send gmail messages
Source code in `llama_index/tools/google/gmail/base.py`
```
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
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
```
| ```
class GmailToolSpec(BaseToolSpec):
"""
    GMail tool spec.

    Gives the agent the ability to read, draft and send gmail messages

    """

    spec_functions = [
        "load_data",
        "search_messages",
        "create_draft",
        "update_draft",
        "get_draft",
        "send_draft",
    ]
    query: str = None
    use_iterative_parser: bool = False
    max_results: int = 10
    service: Any = None

    def _cache_service(self) -> None:
        from googleapiclient.discovery import build

        credentials = self._get_credentials()
        if not self.service:
            self.service = build("gmail", "v1", credentials=credentials)

    def load_data(self) -> List[Document]:
"""Load emails from the user's account."""
        self._cache_service()

        return self.search_messages(query="")

    def _get_credentials(self) -> Any:
"""
        Get valid user credentials from storage.

        The file token.json stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first
        time.

        Returns:
            Credentials, the obtained credential.

        """
        import os

        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow

        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=8080)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return creds

    def search_messages(self, query: str, max_results: Optional[int] = None):
"""
        Searches email messages given a query string and the maximum number
        of results requested by the user
           Returns: List of relevant message objects up to the maximum number of results.

        Args:
            query (str): The user's query
            max_results (Optional[int]): The maximum number of search results
            to return.

        """
        if not max_results:
            max_results = self.max_results

        self._cache_service()

        messages = (
            self.service.users()
            .messages()
            .list(userId="me", q=query or None, maxResults=int(max_results))
            .execute()
            .get("messages", [])
        )

        results = []
        try:
            for message in messages:
                message_data = self.get_message_data(message)
                text = message_data.pop("body")
                metadata = message_data
                results.append(Document(text=text, metadata=metadata))
        except Exception as e:
            raise Exception("Can't get message data" + str(e))

        return results

    def get_message_data(self, message):
        message_id = message["id"]
        message_data = (
            self.service.users()
            .messages()
            .get(format="raw", userId="me", id=message_id)
            .execute()
        )
        if self.use_iterative_parser:
            body = self.extract_message_body_iterative(message_data)
        else:
            body = self.extract_message_body(message_data)

        if not body:
            return None

        return {
            "id": message_data["id"],
            "threadId": message_data["threadId"],
            "snippet": message_data["snippet"],
            "body": body,
        }

    def extract_message_body_iterative(self, message: dict):
        if message["raw"]:
            body = base64.urlsafe_b64decode(message["raw"].encode("utf8"))
            mime_msg = email.message_from_bytes(body)
        else:
            mime_msg = message

        body_text = ""
        if mime_msg.get_content_type() == "text/plain":
            plain_text = mime_msg.get_payload(decode=True)
            charset = mime_msg.get_content_charset("utf-8")
            body_text = plain_text.decode(charset).encode("utf-8").decode("utf-8")

        elif mime_msg.get_content_maintype() == "multipart":
            msg_parts = mime_msg.get_payload()
            for msg_part in msg_parts:
                body_text += self.extract_message_body_iterative(msg_part)

        return body_text

    def extract_message_body(self, message: dict):
        from bs4 import BeautifulSoup

        try:
            body = base64.urlsafe_b64decode(message["raw"].encode("utf-8"))
            mime_msg = email.message_from_bytes(body)

            # If the message body contains HTML, parse it with BeautifulSoup
            if "text/html" in mime_msg:
                soup = BeautifulSoup(body, "html.parser")
                body = soup.get_text()
            return body.decode("utf-8")
        except Exception as e:
            raise Exception("Can't parse message body" + str(e))

    def _build_draft(
        self,
        to: Optional[List[str]] = None,
        subject: Optional[str] = None,
        message: Optional[str] = None,
    ) -> str:
        email_message = EmailMessage()

        email_message.set_content(message)

        email_message["To"] = to
        email_message["Subject"] = subject

        encoded_message = base64.urlsafe_b64encode(email_message.as_bytes()).decode()

        return {"message": {"raw": encoded_message}}

    def create_draft(
        self,
        to: Optional[List[str]] = None,
        subject: Optional[str] = None,
        message: Optional[str] = None,
    ) -> str:
"""
        Create and insert a draft email.
           Print the returned draft's message and id.
           Returns: Draft object, including draft id and message meta data.

        Args:
            to (Optional[str]): The email addresses to send the message to
            subject (Optional[str]): The subject for the event
            message (Optional[str]): The message for the event

        """
        self._cache_service()
        service = self.service

        return (
            service.users()
            .drafts()
            .create(userId="me", body=self._build_draft(to, subject, message))
            .execute()
        )

    def update_draft(
        self,
        to: Optional[List[str]] = None,
        subject: Optional[str] = None,
        message: Optional[str] = None,
        draft_id: str = None,
    ) -> str:
"""
        Update a draft email.
           Print the returned draft's message and id.
           This function is required to be passed a draft_id that is obtained when creating messages
           Returns: Draft object, including draft id and message meta data.

        Args:
            to (Optional[str]): The email addresses to send the message to
            subject (Optional[str]): The subject for the event
            message (Optional[str]): The message for the event
            draft_id (str): the id of the draft to be updated

        """
        self._cache_service()
        service = self.service

        if draft_id is None:
            return (
                "You did not provide a draft id when calling this function. If you"
                " previously created or retrieved the draft, the id is available in"
                " context"
            )

        draft = self.get_draft(draft_id)
        headers = draft["message"]["payload"]["headers"]
        for header in headers:
            if header["name"] == "To" and not to:
                to = header["value"]
            elif header["name"] == "Subject" and not subject:
                subject = header["value"]

        return (
            service.users()
            .drafts()
            .update(
                userId="me", id=draft_id, body=self._build_draft(to, subject, message)
            )
            .execute()
        )

    def get_draft(self, draft_id: str = None) -> str:
"""
        Get a draft email.
           Print the returned draft's message and id.
           Returns: Draft object, including draft id and message meta data.

        Args:
            draft_id (str): the id of the draft to be updated

        """
        self._cache_service()
        service = self.service
        return service.users().drafts().get(userId="me", id=draft_id).execute()

    def send_draft(self, draft_id: str = None) -> str:
"""
        Sends a draft email.
           Print the returned draft's message and id.
           Returns: Draft object, including draft id and message meta data.

        Args:
            draft_id (str): the id of the draft to be updated

        """
        self._cache_service()
        service = self.service
        return (
            service.users().drafts().send(userId="me", body={"id": draft_id}).execute()
        )

```
  
---|---  
###  load_data [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GmailToolSpec.load_data "Permanent link")
```
load_data() -> []

```

Load emails from the user's account.
Source code in `llama_index/tools/google/gmail/base.py`
```
45
46
47
48
49
```
| ```
def load_data(self) -> List[Document]:
"""Load emails from the user's account."""
    self._cache_service()

    return self.search_messages(query="")

```
  
---|---  
###  search_messages [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GmailToolSpec.search_messages "Permanent link")
```
search_messages(query: , max_results: Optional[] = None)

```

Searches email messages given a query string and the maximum number of results requested by the user Returns: List of relevant message objects up to the maximum number of results.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`query` |  The user's query |  _required_  
`max_results` |  `Optional[int]` |  The maximum number of search results |  `None`  
Source code in `llama_index/tools/google/gmail/base.py`
```
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
```
| ```
def search_messages(self, query: str, max_results: Optional[int] = None):
"""
    Searches email messages given a query string and the maximum number
    of results requested by the user
       Returns: List of relevant message objects up to the maximum number of results.

    Args:
        query (str): The user's query
        max_results (Optional[int]): The maximum number of search results
        to return.

    """
    if not max_results:
        max_results = self.max_results

    self._cache_service()

    messages = (
        self.service.users()
        .messages()
        .list(userId="me", q=query or None, maxResults=int(max_results))
        .execute()
        .get("messages", [])
    )

    results = []
    try:
        for message in messages:
            message_data = self.get_message_data(message)
            text = message_data.pop("body")
            metadata = message_data
            results.append(Document(text=text, metadata=metadata))
    except Exception as e:
        raise Exception("Can't get message data" + str(e))

    return results

```
  
---|---  
###  create_draft [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GmailToolSpec.create_draft "Permanent link")
```
create_draft(to: Optional[[]] = None, subject: Optional[] = None, message: Optional[] = None) -> 

```

Create and insert a draft email. Print the returned draft's message and id. Returns: Draft object, including draft id and message meta data.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`Optional[str]` |  The email addresses to send the message to |  `None`  
`subject` |  `Optional[str]` |  The subject for the event |  `None`  
`message` |  `Optional[str]` |  The message for the event |  `None`  
Source code in `llama_index/tools/google/gmail/base.py`
```
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
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
```
| ```
def create_draft(
    self,
    to: Optional[List[str]] = None,
    subject: Optional[str] = None,
    message: Optional[str] = None,
) -> str:
"""
    Create and insert a draft email.
       Print the returned draft's message and id.
       Returns: Draft object, including draft id and message meta data.

    Args:
        to (Optional[str]): The email addresses to send the message to
        subject (Optional[str]): The subject for the event
        message (Optional[str]): The message for the event

    """
    self._cache_service()
    service = self.service

    return (
        service.users()
        .drafts()
        .create(userId="me", body=self._build_draft(to, subject, message))
        .execute()
    )

```
  
---|---  
###  update_draft [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GmailToolSpec.update_draft "Permanent link")
```
update_draft(to: Optional[[]] = None, subject: Optional[] = None, message: Optional[] = None, draft_id:  = None) -> 

```

Update a draft email. Print the returned draft's message and id. This function is required to be passed a draft_id that is obtained when creating messages Returns: Draft object, including draft id and message meta data.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`Optional[str]` |  The email addresses to send the message to |  `None`  
`subject` |  `Optional[str]` |  The subject for the event |  `None`  
`message` |  `Optional[str]` |  The message for the event |  `None`  
`draft_id` |  the id of the draft to be updated |  `None`  
Source code in `llama_index/tools/google/gmail/base.py`
```
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
```
| ```
def update_draft(
    self,
    to: Optional[List[str]] = None,
    subject: Optional[str] = None,
    message: Optional[str] = None,
    draft_id: str = None,
) -> str:
"""
    Update a draft email.
       Print the returned draft's message and id.
       This function is required to be passed a draft_id that is obtained when creating messages
       Returns: Draft object, including draft id and message meta data.

    Args:
        to (Optional[str]): The email addresses to send the message to
        subject (Optional[str]): The subject for the event
        message (Optional[str]): The message for the event
        draft_id (str): the id of the draft to be updated

    """
    self._cache_service()
    service = self.service

    if draft_id is None:
        return (
            "You did not provide a draft id when calling this function. If you"
            " previously created or retrieved the draft, the id is available in"
            " context"
        )

    draft = self.get_draft(draft_id)
    headers = draft["message"]["payload"]["headers"]
    for header in headers:
        if header["name"] == "To" and not to:
            to = header["value"]
        elif header["name"] == "Subject" and not subject:
            subject = header["value"]

    return (
        service.users()
        .drafts()
        .update(
            userId="me", id=draft_id, body=self._build_draft(to, subject, message)
        )
        .execute()
    )

```
  
---|---  
###  get_draft [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GmailToolSpec.get_draft "Permanent link")
```
get_draft(draft_id:  = None) -> 

```

Get a draft email. Print the returned draft's message and id. Returns: Draft object, including draft id and message meta data.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`draft_id` |  the id of the draft to be updated |  `None`  
Source code in `llama_index/tools/google/gmail/base.py`
```
273
274
275
276
277
278
279
280
281
282
283
284
285
```
| ```
def get_draft(self, draft_id: str = None) -> str:
"""
    Get a draft email.
       Print the returned draft's message and id.
       Returns: Draft object, including draft id and message meta data.

    Args:
        draft_id (str): the id of the draft to be updated

    """
    self._cache_service()
    service = self.service
    return service.users().drafts().get(userId="me", id=draft_id).execute()

```
  
---|---  
###  send_draft [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GmailToolSpec.send_draft "Permanent link")
```
send_draft(draft_id:  = None) -> 

```

Sends a draft email. Print the returned draft's message and id. Returns: Draft object, including draft id and message meta data.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`draft_id` |  the id of the draft to be updated |  `None`  
Source code in `llama_index/tools/google/gmail/base.py`
```
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
```
| ```
def send_draft(self, draft_id: str = None) -> str:
"""
    Sends a draft email.
       Print the returned draft's message and id.
       Returns: Draft object, including draft id and message meta data.

    Args:
        draft_id (str): the id of the draft to be updated

    """
    self._cache_service()
    service = self.service
    return (
        service.users().drafts().send(userId="me", body={"id": draft_id}).execute()
    )

```
  
---|---  
##  GoogleSearchToolSpec [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GoogleSearchToolSpec "Permanent link")
Bases: 
Google Search tool spec.
Source code in `llama_index/tools/google/search/base.py`
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
```
| ```
class GoogleSearchToolSpec(BaseToolSpec):
"""Google Search tool spec."""

    spec_functions = [("google_search", "agoogle_search")]

    def __init__(self, key: str, engine: str, num: Optional[int] = None) -> None:
"""Initialize with parameters."""
        self.key = key
        self.engine = engine
        self.num = num

    def _get_url(self, query: str) -> str:
        url = QUERY_URL_TMPL.format(
            key=self.key, engine=self.engine, query=urllib.parse.quote_plus(query)
        )

        if self.num is not None:
            if not 1 <= self.num <= 10:
                raise ValueError("num should be an integer between 1 and 10, inclusive")
            url += f"&num={self.num}"

        return url

    def _parse_results(self, results: List[Dict]) -> Union[List[Dict], str]:
        cleaned_results = []
        if len(results) == 0:
            return "No search results available"

        for result in results:
            if "snippet" in result:
                cleaned_results.append(
                    {
                        "title": result["title"],
                        "link": result["link"],
                        "snippet": result["snippet"],
                    }
                )

        return cleaned_results

    def google_search(self, query: str):
"""
        Make a query to the Google search engine to receive a list of results.

        Args:
            query (str): The query to be passed to Google search.
            num (int, optional): The number of search results to return. Defaults to None.

        Raises:
            ValueError: If the 'num' is not an integer between 1 and 10.

        """
        url = self._get_url(query)

        with httpx.Client() as client:
            response = client.get(url)

        results = json.loads(response.text).get("items", [])

        return self._parse_results(results)

    async def agoogle_search(self, query: str):
"""
        Make a query to the Google search engine to receive a list of results.

        Args:
            query (str): The query to be passed to Google search.
            num (int, optional): The number of search results to return. Defaults to None.

        Raises:
            ValueError: If the 'num' is not an integer between 1 and 10.

        """
        url = self._get_url(query)

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        results = json.loads(response.text).get("items", [])

        return self._parse_results(results)

```
  
---|---  
###  google_search [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GoogleSearchToolSpec.google_search "Permanent link")
```
google_search(query: )

```

Make a query to the Google search engine to receive a list of results.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`query` |  The query to be passed to Google search. |  _required_  
`num` |  The number of search results to return. Defaults to None. |  _required_  
Raises:
Type | Description  
---|---  
`ValueError` |  If the 'num' is not an integer between 1 and 10.  
Source code in `llama_index/tools/google/search/base.py`
```
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
```
| ```
def google_search(self, query: str):
"""
    Make a query to the Google search engine to receive a list of results.

    Args:
        query (str): The query to be passed to Google search.
        num (int, optional): The number of search results to return. Defaults to None.

    Raises:
        ValueError: If the 'num' is not an integer between 1 and 10.

    """
    url = self._get_url(query)

    with httpx.Client() as client:
        response = client.get(url)

    results = json.loads(response.text).get("items", [])

    return self._parse_results(results)

```
  
---|---  
###  agoogle_search `async` [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/google/#llama_index.tools.google.GoogleSearchToolSpec.agoogle_search "Permanent link")
```
agoogle_search(query: )

```

Make a query to the Google search engine to receive a list of results.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`query` |  The query to be passed to Google search. |  _required_  
`num` |  The number of search results to return. Defaults to None. |  _required_  
Raises:
Type | Description  
---|---  
`ValueError` |  If the 'num' is not an integer between 1 and 10.  
Source code in `llama_index/tools/google/search/base.py`
```
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
```
| ```
async def agoogle_search(self, query: str):
"""
    Make a query to the Google search engine to receive a list of results.

    Args:
        query (str): The query to be passed to Google search.
        num (int, optional): The number of search results to return. Defaults to None.

    Raises:
        ValueError: If the 'num' is not an integer between 1 and 10.

    """
    url = self._get_url(query)

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    results = json.loads(response.text).get("items", [])

    return self._parse_results(results)

```
  
---|---  
options: members: - GmailToolSpec - GoogleCalendarToolSpec - GoogleSearchToolSpec
