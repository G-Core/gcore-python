# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .create_video_param import CreateVideoParam
from .subtitle_base_param import SubtitleBaseParam

__all__ = ["VideoCreateMultipleParams", "Video"]


class VideoCreateMultipleParams(TypedDict, total=False):
    fields: str
    """
    Restriction to return only the specified attributes, instead of the entire
    dataset. Specify, if you need to get short response. The following fields are
    available for specifying: id, name, duration, status, `created_at`,
    `updated_at`, `hls_url`, screenshots, `converted_videos`, priority. Example,
    ?fields=id,name,`hls_url`
    """

    videos: Iterable[Video]


class Video(CreateVideoParam, total=False):
    subtitles: Iterable[SubtitleBaseParam]
