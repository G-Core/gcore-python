# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AccessKeyCreateParams"]


class AccessKeyCreateParams(TypedDict, total=False):
    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    ISO 8601 timestamp (RFC3339) after which the key is deleted from the backend and
    the cache. Must be in the future and within the next 5 minutes. A key created
    with an expiry is hidden from the access-key list and does not count toward the
    per-storage limit, so it is suited to short-lived browser/file-manager use. Omit
    for a key that never expires.
    """

    read_only: bool
    """Request a key scoped to read-only data access.

    Only supported for Standard storages; a Fast storage rejects true. Defaults to
    false (full read-write) when omitted.
    """

    accept_language: Annotated[str, PropertyInfo(alias="Accept-Language")]
