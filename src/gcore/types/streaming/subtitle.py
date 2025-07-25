# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .subtitle_base import SubtitleBase

__all__ = ["Subtitle"]


class Subtitle(SubtitleBase):
    id: Optional[int] = None
    """ID of subtitle file"""
