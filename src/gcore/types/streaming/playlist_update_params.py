# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["PlaylistUpdateParams"]


class PlaylistUpdateParams(TypedDict, total=False):
    active: bool
    """Enables/Disables playlist. Has two possible values:

    - true – Playlist can be played.
    - false – Playlist is disabled. No broadcast while it's disabled.
    """

    ad_id: int
    """The advertisement ID that will be inserted into the video"""

    client_user_id: int
    """Custom field where you can specify user ID in your system"""

    countdown: bool
    """Enables countdown before playlist start with `playlist_type: live`"""

    loop: bool
    """Enables/Disables playlist loop"""

    name: str
    """Playlist name"""

    player_id: int
    """The player ID with which the video will be played"""

    playlist_type: Literal["live", "vod"]
    """Determines whether the playlist:

    - `live` - playlist for live-streaming
    - `vod` - playlist is for video on demand access
    """

    start_time: str
    """Playlist start time.

    Playlist won't be available before the specified time. Datetime in ISO 8601
    format.
    """

    video_ids: Iterable[int]
    """A list of VOD IDs included in the playlist.

    Order of videos in a playlist reflects the order of IDs in the array.

    Maximum video limit = 128.
    """
