# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .playlist import Playlist

__all__ = ["PlaylistCreated"]


class PlaylistCreated(Playlist):
    id: Optional[int] = None
    """Playlist ID"""
