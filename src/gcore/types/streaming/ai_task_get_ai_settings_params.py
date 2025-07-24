# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AITaskGetAISettingsParams"]


class AITaskGetAISettingsParams(TypedDict, total=False):
    type: Required[Literal["language_support"]]
    """The parameters section for which parameters are requested"""

    audio_language: str
    """The source language from which the audio will be transcribed.

    Required when `type=language_support`. Value is 3-letter language code according
    to ISO-639-2 (bibliographic code), (e.g., fre for French).
    """

    subtitles_language: str
    """The target language the text will be translated into.

    If omitted, the API will return whether the `audio_language` is supported for
    transcription only, instead of translation. Value is 3-letter language code
    according to ISO-639-2 (bibliographic code), (e.g., fre for French).
    """
