# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .ai_contentmoderation_nsfw import AIContentmoderationNsfw
from .ai_contentmoderation_sport import AIContentmoderationSport
from .ai_contentmoderation_hardnudity import AIContentmoderationHardnudity
from .ai_contentmoderation_softnudity import AIContentmoderationSoftnudity

__all__ = ["AITask", "TaskData", "TaskDataAITranscribe"]


class TaskDataAITranscribe(BaseModel):
    task_name: Literal["transcription"]
    """Name of the task to be performed"""

    url: str
    """URL to the MP4 file to analyse.

    File must be publicly accessible via HTTP/HTTPS.
    """

    audio_language: Optional[str] = None
    """Language in original audio (transcription only).

    This value is used to determine the language from which to transcribe.

    If this is not set, the system will run auto language identification and the
    subtitles will be in the detected language. The method also works based on AI
    analysis. It's fairly accurate, but if it's wrong, then set the language
    explicitly.

    Additionally, when this is not set, we also support recognition of alternate
    languages in the video (language code-switching).

    Language is set by 3-letter language code according to ISO-639-2 (bibliographic
    code).

    We can process languages:

    - 'afr': Afrikaans
    - 'alb': Albanian
    - 'amh': Amharic
    - 'ara': Arabic
    - 'arm': Armenian
    - 'asm': Assamese
    - 'aze': Azerbaijani
    - 'bak': Bashkir
    - 'baq': Basque
    - 'bel': Belarusian
    - 'ben': Bengali
    - 'bos': Bosnian
    - 'bre': Breton
    - 'bul': Bulgarian
    - 'bur': Myanmar
    - 'cat': Catalan
    - 'chi': Chinese
    - 'cze': Czech
    - 'dan': Danish
    - 'dut': Nynorsk
    - 'eng': English
    - 'est': Estonian
    - 'fao': Faroese
    - 'fin': Finnish
    - 'fre': French
    - 'geo': Georgian
    - 'ger': German
    - 'glg': Galician
    - 'gre': Greek
    - 'guj': Gujarati
    - 'hat': Haitian creole
    - 'hau': Hausa
    - 'haw': Hawaiian
    - 'heb': Hebrew
    - 'hin': Hindi
    - 'hrv': Croatian
    - 'hun': Hungarian
    - 'ice': Icelandic
    - 'ind': Indonesian
    - 'ita': Italian
    - 'jav': Javanese
    - 'jpn': Japanese
    - 'kan': Kannada
    - 'kaz': Kazakh
    - 'khm': Khmer
    - 'kor': Korean
    - 'lao': Lao
    - 'lat': Latin
    - 'lav': Latvian
    - 'lin': Lingala
    - 'lit': Lithuanian
    - 'ltz': Luxembourgish
    - 'mac': Macedonian
    - 'mal': Malayalam
    - 'mao': Maori
    - 'mar': Marathi
    - 'may': Malay
    - 'mlg': Malagasy
    - 'mlt': Maltese
    - 'mon': Mongolian
    - 'nep': Nepali
    - 'dut': Dutch
    - 'nor': Norwegian
    - 'oci': Occitan
    - 'pan': Punjabi
    - 'per': Persian
    - 'pol': Polish
    - 'por': Portuguese
    - 'pus': Pashto
    - 'rum': Romanian
    - 'rus': Russian
    - 'san': Sanskrit
    - 'sin': Sinhala
    - 'slo': Slovak
    - 'slv': Slovenian
    - 'sna': Shona
    - 'snd': Sindhi
    - 'som': Somali
    - 'spa': Spanish
    - 'srp': Serbian
    - 'sun': Sundanese
    - 'swa': Swahili
    - 'swe': Swedish
    - 'tam': Tamil
    - 'tat': Tatar
    - 'tel': Telugu
    - 'tgk': Tajik
    - 'tgl': Tagalog
    - 'tha': Thai
    - 'tib': Tibetan
    - 'tuk': Turkmen
    - 'tur': Turkish
    - 'ukr': Ukrainian
    - 'urd': Urdu
    - 'uzb': Uzbek
    - 'vie': Vietnamese
    - 'wel': Welsh
    - 'yid': Yiddish
    - 'yor': Yoruba
    """

    client_entity_data: Optional[str] = None
    """
    Meta parameter, designed to store your own extra information about a video
    entity: video source, video id, etc. It is not used in any way in video
    processing.

    For example, if an AI-task was created automatically when you uploaded a video
    with the AI auto-processing option (transcribing, translationing), then the ID
    of the associated video for which the task was performed will be explicitly
    indicated here.
    """

    client_user_id: Optional[str] = None
    """Meta parameter, designed to store your own identifier.

    Can be used by you to tag requests from different end-users. It is not used in
    any way in video processing.
    """

    subtitles_language: Optional[str] = None
    """
    Indicates which language it is clearly necessary to translate into. If this is
    not set, the original language will be used from attribute "`audio_language`".

    Please note that:

    - transcription into the original language is a free procedure,
    - and translation from the original language into any other languages is a
      "translation" procedure and is paid. More details in
      [POST /streaming/ai/tasks#transcribe](/docs/api-reference/streaming/ai/create-ai-asr-task).
      Language is set by 3-letter language code according to ISO-639-2
      (bibliographic code).
    """


TaskData: TypeAlias = Union[
    TaskDataAITranscribe,
    AIContentmoderationNsfw,
    AIContentmoderationHardnudity,
    AIContentmoderationSoftnudity,
    AIContentmoderationSport,
]


class AITask(BaseModel):
    progress: Optional[int] = None
    """Percentage of task completed.

    A value greater than 0 means that it has been taken into operation and is being
    processed.
    """

    status: Optional[Literal["PENDING", "STARTED", "SUCCESS", "FAILURE", "REVOKED", "RETRY"]] = None
    """Status of processing the AI task. See GET /ai/results method for description."""

    task_data: Optional[TaskData] = None
    """
    The object will correspond to the task type that was specified in the original
    request. There will be one object for transcription, another for searching for
    nudity, and so on.
    """

    task_id: Optional[str] = None
    """ID of the AI task"""

    task_name: Optional[Literal["content-moderation", "transcription"]] = None
    """Type of AI task"""
