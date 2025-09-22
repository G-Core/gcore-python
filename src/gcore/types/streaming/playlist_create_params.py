# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["PlaylistCreateParams"]


class PlaylistCreateParams(TypedDict, total=False):
    active: bool
    """Enables/Disables playlist. Has two possible values:

    - true – Playlist can be played.
    - false – Playlist is disabled. No broadcast while it's desabled.
    """

    ad_id: int
    """The advertisement ID that will be inserted into the video"""

    client_id: int
    """Current playlist client ID"""

    client_user_id: int
    """Custom field where you can specify user ID in your system"""

    countdown: bool
    """Enables countdown before playlist start with `playlist_type: live`"""

    hls_cmaf_url: str
    """A URL to a master playlist HLS (master-cmaf.m3u8) with CMAF-based chunks.

    Chunks are in fMP4 container.

    It is possible to use the same suffix-options as described in the "`hls_url`"
    attribute.

    Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
    and intended for your use. Any additional internal manifests, sub-manifests,
    parameters, chunk names, file extensions, and related components are internal
    infrastructure entities. These may undergo modifications without prior notice,
    in any manner or form. It is strongly advised not to store them in your database
    or cache them on your end.
    """

    hls_url: str
    """A URL to a master playlist HLS (master.m3u8) with MPEG TS container.

    This URL is a link to the main manifest. But you can also manually specify
    suffix-options that will allow you to change the manifest to your request:
    `/playlists/{client_id}_{playlist_id}/master[-cmaf][-min-N][-max-N][-img][-(h264|hevc|av1)].m3u8`
    Please see the details in `hls_url` attribute of /videos/{id} method.

    Caution. Solely master.m3u8 (and master[-options].m3u8) is officially documented
    and intended for your use. Any additional internal manifests, sub-manifests,
    parameters, chunk names, file extensions, and related components are internal
    infrastructure entities. These may undergo modifications without prior notice,
    in any manner or form. It is strongly advised not to store them in your database
    or cache them on your end.
    """

    iframe_url: str
    """A URL to a built-in HTML video player with the video inside.

    It can be inserted into an iframe on your website and the video will
    automatically play in all browsers.

    The player can be opened or shared via this direct link. Also the video player
    can be integrated into your web pages using the Iframe tag.

    Please see the details in `iframe_url` attribute of /videos/{id} method.
    """

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
