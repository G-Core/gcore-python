# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StreamCreateClipParams"]


class StreamCreateClipParams(TypedDict, total=False):
    duration: Required[int]
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

    expiration: int
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

    start: int
    """Starting point of the segment to cut.

    Unix timestamp in seconds, absolute value. Example:
    `24.05.2024 14:00:00 (GMT) is Unix timestamp = 1716559200`

    If a value from the past is specified, it is used as the starting point for the
    segment to cut. If the value is omitted, then clip will start from now.
    """

    vod_required: bool
    """Indicates if video needs to be stored also as permanent VOD"""
