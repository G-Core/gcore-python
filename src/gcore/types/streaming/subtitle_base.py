# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SubtitleBase"]


class SubtitleBase(BaseModel):
    language: Optional[str] = None
    """3-letter language code according to ISO-639-2 (bibliographic code)"""

    name: Optional[str] = None
    """Name of subtitle file"""

    vtt: Optional[str] = None
    """Full text of subtitles/captions, with escaped "\n" ("\r") symbol of new line"""
