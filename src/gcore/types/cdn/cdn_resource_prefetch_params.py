# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CDNResourcePrefetchParams"]


class CDNResourcePrefetchParams(TypedDict, total=False):
    paths: Required[SequenceNotStr[str]]
    """Paths to files that should be pre-populated to the CDN.

    Paths to the files should be specified without a domain name.

    Control characters, such as line breaks, are not allowed inside a path, and a
    space in the query string must be encoded as %20. Outside the query string,
    every % must start a percent-encoded character such as %20.
    """
