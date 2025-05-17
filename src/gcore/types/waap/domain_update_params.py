# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DomainUpdateParams"]


class DomainUpdateParams(TypedDict, total=False):
    status: Literal["active", "monitor"]
    """Domain statuses that can be used when updating a domain"""
