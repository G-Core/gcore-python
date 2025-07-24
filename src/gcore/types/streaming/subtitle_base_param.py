# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SubtitleBaseParam"]


class SubtitleBaseParam(TypedDict, total=False):
    language: str
    """3-letter language code according to ISO-639-2 (bibliographic code)"""

    name: str
    """Name of subtitle file"""

    vtt: str
    """Full text of subtitles/captions, with escaped "\n" ("\r") symbol of new line"""
