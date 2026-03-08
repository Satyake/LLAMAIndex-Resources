# Typecast
##  TypecastToolSpec [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/typecast/#llama_index.tools.typecast.TypecastToolSpec "Permanent link")
Bases: 
Typecast tool spec for text-to-speech synthesis with emotion control.
Source code in `llama_index/tools/typecast/base.py`
```



 10
 11
 12
 13
 14
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
```
| ```
class TypecastToolSpec(BaseToolSpec):
"""Typecast tool spec for text-to-speech synthesis with emotion control."""

    spec_functions = ["get_voices", "text_to_speech"]

    def __init__(self, api_key: str, host: Optional[str] = None) -> None:
"""
        Initialize with parameters.

        Args:
            api_key (str): Your Typecast API key
            host (Optional[str]): The base url of Typecast API (default: https://api.typecast.ai)

        """
        self.api_key = api_key
        self.host = host

    def get_voices(self, model: Optional[str] = None) -> List[dict]:
"""
        Get list of available voices from Typecast.

        Args:
            model (Optional[str]): Filter by model name (e.g., "ssfm-v21")

        Returns:
            List[dict]: List of available voices with their details

        Raises:
            Exception: If API request fails

        """
        try:
            from typecast.client import Typecast

            # Create the client
            client = Typecast(host=self.host, api_key=self.api_key)

            # Get the voices
            response = client.voices(model=model)

            # Return the dumped voice models as dict
            return [voice.model_dump() for voice in response]
        except Exception as e:
            raise Exception(f"Failed to get voices from Typecast API: {e!s}")

    def text_to_speech(
        self,
        text: str,
        voice_id: str,
        output_path: str,
        model: str = "ssfm-v21",
        language: Optional[str] = None,
        emotion_preset: Optional[str] = "normal",
        emotion_intensity: Optional[float] = 1.0,
        volume: Optional[int] = 100,
        audio_pitch: Optional[int] = 0,
        audio_tempo: Optional[float] = 1.0,
        audio_format: Optional[str] = "wav",
    ) -> str:
"""
        Convert text to speech using Typecast API.

        Args:
            text (str): The text to convert to speech
            voice_id (str): The voice ID to use (e.g., "tc_62a8975e695ad26f7fb514d1")
            output_path (str): Path to save the audio file
            model (str): Voice model name (default: "ssfm-v21")
            language (Optional[str]): Language code (ISO 639-3, e.g., "eng", "kor")
            emotion_preset (Optional[str]): Emotion preset (normal, happy, sad, angry)
            emotion_intensity (Optional[float]): Emotion intensity (0.0 to 2.0)
            volume (Optional[int]): Volume (0 to 200, default: 100)
            audio_pitch (Optional[int]): Audio pitch (-12 to 12, default: 0)
            audio_tempo (Optional[float]): Audio tempo (0.5 to 2.0, default: 1.0)
            audio_format (Optional[str]): Audio format (wav or mp3, default: wav)

        Returns:
            str: Path to the generated audio file

        Raises:
            ValueError: If parameters are invalid
            Exception: If API request fails or file save fails

        """
        try:
            from typecast.client import Typecast
            from typecast.models import TTSRequest, Prompt, Output
            from typecast.exceptions import (
                TypecastError,
                PaymentRequiredError,
                UnauthorizedError,
            )

            # Validate parameters
            if not text or not text.strip():
                raise ValueError("Text cannot be empty")
            if not voice_id:
                raise ValueError("Voice ID is required")
            if not output_path:
                raise ValueError("Output path is required")

            # Create client
            client = Typecast(host=self.host, api_key=self.api_key)

            # Build the request
            request = TTSRequest(
                voice_id=voice_id,
                text=text,
                model=model,
                language=language,
                prompt=Prompt(
                    emotion_preset=emotion_preset,
                    emotion_intensity=emotion_intensity,
                ),
                output=Output(
                    volume=volume,
                    audio_pitch=audio_pitch,
                    audio_tempo=audio_tempo,
                    audio_format=audio_format,
                ),
            )

            # Generate audio
            try:
                response = client.text_to_speech(request)
            except PaymentRequiredError:
                raise Exception(
                    "Typecast API quota exceeded. Please check your account balance."
                )
            except UnauthorizedError:
                raise Exception(
                    "Typecast API authentication failed. Please check your API key."
                )
            except TypecastError as e:
                raise Exception(f"Typecast API error: {e!s}")

            # Save the audio
            try:
                with open(output_path, "wb") as fp:
                    fp.write(response.audio_data)
            except IOError as e:
                raise Exception(f"Failed to save audio file to {output_path}: {e!s}")

            # Return the save location
            return output_path

        except ValueError:
            raise
        except Exception as e:
            if "Typecast API" in str(e) or "quota" in str(e).lower():
                raise
            raise Exception(f"Failed to generate speech: {e!s}")

```
  
---|---  
###  get_voices [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/typecast/#llama_index.tools.typecast.TypecastToolSpec.get_voices "Permanent link")
```
get_voices(model: Optional[] = None) -> []

```

Get list of available voices from Typecast.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`model` |  `Optional[str]` |  Filter by model name (e.g., "ssfm-v21") |  `None`  
Returns:
Type | Description  
---|---  
`List[dict]` |  List[dict]: List of available voices with their details  
Raises:
Type | Description  
---|---  
`Exception` |  If API request fails  
Source code in `llama_index/tools/typecast/base.py`
```
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
```
| ```
def get_voices(self, model: Optional[str] = None) -> List[dict]:
"""
    Get list of available voices from Typecast.

    Args:
        model (Optional[str]): Filter by model name (e.g., "ssfm-v21")

    Returns:
        List[dict]: List of available voices with their details

    Raises:
        Exception: If API request fails

    """
    try:
        from typecast.client import Typecast

        # Create the client
        client = Typecast(host=self.host, api_key=self.api_key)

        # Get the voices
        response = client.voices(model=model)

        # Return the dumped voice models as dict
        return [voice.model_dump() for voice in response]
    except Exception as e:
        raise Exception(f"Failed to get voices from Typecast API: {e!s}")

```
  
---|---  
###  text_to_speech [#](https://developers.llamaindex.ai/python/framework-api-reference/tools/typecast/#llama_index.tools.typecast.TypecastToolSpec.text_to_speech "Permanent link")
```
text_to_speech(text: , voice_id: , output_path: , model:  = 'ssfm-v21', language: Optional[] = None, emotion_preset: Optional[] = 'normal', emotion_intensity: Optional[float] = 1.0, volume: Optional[] = 100, audio_pitch: Optional[] = 0, audio_tempo: Optional[float] = 1.0, audio_format: Optional[] = 'wav') -> 

```

Convert text to speech using Typecast API.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`text` |  The text to convert to speech |  _required_  
`voice_id` |  The voice ID to use (e.g., "tc_62a8975e695ad26f7fb514d1") |  _required_  
`output_path` |  Path to save the audio file |  _required_  
`model` |  Voice model name (default: "ssfm-v21") |  `'ssfm-v21'`  
`language` |  `Optional[str]` |  Language code (ISO 639-3, e.g., "eng", "kor") |  `None`  
`emotion_preset` |  `Optional[str]` |  Emotion preset (normal, happy, sad, angry) |  `'normal'`  
`emotion_intensity` |  `Optional[float]` |  Emotion intensity (0.0 to 2.0) |  `1.0`  
`volume` |  `Optional[int]` |  Volume (0 to 200, default: 100) |  `100`  
`audio_pitch` |  `Optional[int]` |  Audio pitch (-12 to 12, default: 0)  
`audio_tempo` |  `Optional[float]` |  Audio tempo (0.5 to 2.0, default: 1.0) |  `1.0`  
`audio_format` |  `Optional[str]` |  Audio format (wav or mp3, default: wav) |  `'wav'`  
Returns:
Name | Type | Description  
---|---|---  
`str` |  Path to the generated audio file  
Raises:
Type | Description  
---|---  
`ValueError` |  If parameters are invalid  
`Exception` |  If API request fails or file save fails  
Source code in `llama_index/tools/typecast/base.py`
```
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
```
| ```
def text_to_speech(
    self,
    text: str,
    voice_id: str,
    output_path: str,
    model: str = "ssfm-v21",
    language: Optional[str] = None,
    emotion_preset: Optional[str] = "normal",
    emotion_intensity: Optional[float] = 1.0,
    volume: Optional[int] = 100,
    audio_pitch: Optional[int] = 0,
    audio_tempo: Optional[float] = 1.0,
    audio_format: Optional[str] = "wav",
) -> str:
"""
    Convert text to speech using Typecast API.

    Args:
        text (str): The text to convert to speech
        voice_id (str): The voice ID to use (e.g., "tc_62a8975e695ad26f7fb514d1")
        output_path (str): Path to save the audio file
        model (str): Voice model name (default: "ssfm-v21")
        language (Optional[str]): Language code (ISO 639-3, e.g., "eng", "kor")
        emotion_preset (Optional[str]): Emotion preset (normal, happy, sad, angry)
        emotion_intensity (Optional[float]): Emotion intensity (0.0 to 2.0)
        volume (Optional[int]): Volume (0 to 200, default: 100)
        audio_pitch (Optional[int]): Audio pitch (-12 to 12, default: 0)
        audio_tempo (Optional[float]): Audio tempo (0.5 to 2.0, default: 1.0)
        audio_format (Optional[str]): Audio format (wav or mp3, default: wav)

    Returns:
        str: Path to the generated audio file

    Raises:
        ValueError: If parameters are invalid
        Exception: If API request fails or file save fails

    """
    try:
        from typecast.client import Typecast
        from typecast.models import TTSRequest, Prompt, Output
        from typecast.exceptions import (
            TypecastError,
            PaymentRequiredError,
            UnauthorizedError,
        )

        # Validate parameters
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        if not voice_id:
            raise ValueError("Voice ID is required")
        if not output_path:
            raise ValueError("Output path is required")

        # Create client
        client = Typecast(host=self.host, api_key=self.api_key)

        # Build the request
        request = TTSRequest(
            voice_id=voice_id,
            text=text,
            model=model,
            language=language,
            prompt=Prompt(
                emotion_preset=emotion_preset,
                emotion_intensity=emotion_intensity,
            ),
            output=Output(
                volume=volume,
                audio_pitch=audio_pitch,
                audio_tempo=audio_tempo,
                audio_format=audio_format,
            ),
        )

        # Generate audio
        try:
            response = client.text_to_speech(request)
        except PaymentRequiredError:
            raise Exception(
                "Typecast API quota exceeded. Please check your account balance."
            )
        except UnauthorizedError:
            raise Exception(
                "Typecast API authentication failed. Please check your API key."
            )
        except TypecastError as e:
            raise Exception(f"Typecast API error: {e!s}")

        # Save the audio
        try:
            with open(output_path, "wb") as fp:
                fp.write(response.audio_data)
        except IOError as e:
            raise Exception(f"Failed to save audio file to {output_path}: {e!s}")

        # Return the save location
        return output_path

    except ValueError:
        raise
    except Exception as e:
        if "Typecast API" in str(e) or "quota" in str(e).lower():
            raise
        raise Exception(f"Failed to generate speech: {e!s}")

```
  
---|---  
options: members: - TypecastToolSpec
