# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccessKeyCreateParams"]


class AccessKeyCreateParams(TypedDict, total=False):
    read_only: bool
    """Request a key scoped to read-only data access.

    Only supported for Standard storages; a Fast storage rejects true. Defaults to
    false (full read-write) when omitted.
    """
