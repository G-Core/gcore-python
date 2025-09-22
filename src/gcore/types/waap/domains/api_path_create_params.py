# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["APIPathCreateParams"]


class APIPathCreateParams(TypedDict, total=False):
    http_scheme: Required[Literal["HTTP", "HTTPS"]]
    """The different HTTP schemes an API path can have"""

    method: Required[Literal["GET", "POST", "PUT", "PATCH", "DELETE", "TRACE", "HEAD", "OPTIONS"]]
    """The different methods an API path can have"""

    path: Required[str]
    """
    The API path, locations that are saved for resource IDs will be put in curly
    brackets
    """

    api_groups: SequenceNotStr[str]

    api_version: str

    tags: SequenceNotStr[str]
