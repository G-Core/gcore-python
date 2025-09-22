# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AITaskCreateParams"]


class AITaskCreateParams(TypedDict, total=False):
    task_name: Required[Literal["transcription", "content-moderation"]]
    """Name of the task to be performed"""

    url: Required[str]
    """URL to the MP4 file to analyse.

    File must be publicly accessible via HTTP/HTTPS.
    """

    audio_language: str
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

    category: Literal["sport", "nsfw", "hard_nudity", "soft_nudity"]
    """Model for analysis (content-moderation only).

    Determines what exactly needs to be found in the video.
    """

    client_entity_data: str
    """
    Meta parameter, designed to store your own extra information about a video
    entity: video source, video id, etc. It is not used in any way in video
    processing.

    For example, if an AI-task was created automatically when you uploaded a video
    with the AI auto-processing option (nudity detection, etc), then the ID of the
    associated video for which the task was performed will be explicitly indicated
    here.
    """

    client_user_id: str
    """Meta parameter, designed to store your own identifier.

    Can be used by you to tag requests from different end-users. It is not used in
    any way in video processing.
    """

    subtitles_language: str
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
