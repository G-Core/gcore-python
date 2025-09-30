# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ResourcePrefetchParams"]


class ResourcePrefetchParams(TypedDict, total=False):
    paths: Required[SequenceNotStr[str]]
    """Paths to files that should be pre-populated to the CDN.

    Paths to the files should be specified without a domain name.
    """
