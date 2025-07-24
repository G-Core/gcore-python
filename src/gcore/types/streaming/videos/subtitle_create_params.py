# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..subtitle_base_param import SubtitleBaseParam

__all__ = ["SubtitleCreateParams", "Body"]


class SubtitleCreateParams(TypedDict, total=False):
    body: Required[Body]


class Body(SubtitleBaseParam, total=False):
    pass
