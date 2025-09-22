# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Clip"]


class Clip(BaseModel):
    id: str
    """ID of the clip"""

    duration: int
    """Requested segment duration in seconds to be cut.

    Please, note that cutting is based on the idea of instantly creating a clip,
    instead of precise timing. So final segment may be:

    - Less than the specified value if there is less data in the DVR than the
      requested segment.
    - Greater than the specified value, because segment is aligned to the first and
      last key frames of already stored fragment in DVR, this way -1 and +1 chunks
      can be added to left and right.

    Duration of cutted segment cannot be greater than DVR duration for this stream.
    Therefore, to change the maximum, use "`dvr_duration`" parameter of this stream.
    """

    created_at: Optional[str] = None
    """Creation date and time. Format is date time in ISO 8601"""

    expiration: Optional[int] = None
    """Expire time of the clip via a public link.

    Unix timestamp in seconds, absolute value.

    This is the time how long the instant clip will be stored in the server memory
    and can be accessed via public HLS/MP4 links. Download and/or use the instant
    clip before this time expires.

    After the time has expired, the clip is deleted from memory and is no longer
    available via the link. You need to create a new segment, or use
    `vod_required: true` attribute.

    If value is omitted, then expiration is counted as +3600 seconds (1 hour) to the
    end of the clip (i.e. `unix timestamp = <start> + <duration> + 3600`).

    Allowed range: 1m <= expiration <= 4h.

    Example:
    `24.05.2024 14:00:00 (GMT) + 60 seconds of duration + 3600 seconds of expiration = 24.05.2024 15:01:00 (GMT) is Unix timestamp = 1716562860`
    """

    hls_master: Optional[str] = None
    """Link to HLS .m3u8 with immediate clip.

    The link retains same adaptive bitrate as in the stream for end viewers. For
    additional restrictions, see the description of parameter "`mp4_master`".
    """

    mp4_master: Optional[str] = None
    """Link to MP4 with immediate clip.

    The link points to max rendition quality. Request of the URL can return:

    - 200 OK – if the clip exists.
    - 404 Not found – if the clip did not exist or has already ceased to exist.
    - 425 Too early – if recording is on-going now. The file is incomplete and will
      be accessible after start+duration time will come.
    """

    renditions: Optional[List[str]] = None
    """List of available rendition heights"""

    start: Optional[int] = None
    """Starting point of the segment to cut.

    Unix timestamp in seconds, absolute value. Example:
    `24.05.2024 14:00:00 (GMT) is Unix timestamp = 1716559200`

    If a value from the past is specified, it is used as the starting point for the
    segment to cut. If the value is omitted, then clip will start from now.
    """

    video_id: Optional[int] = None
    """ID of the created video if `vod_required`=true"""

    vod_required: Optional[bool] = None
    """Indicates if video needs to be stored as VOD"""
