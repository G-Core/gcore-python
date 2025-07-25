# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .create_video_param import CreateVideoParam

__all__ = ["VideoCreateParams"]


class VideoCreateParams(TypedDict, total=False):
    video: CreateVideoParam
