# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .waap_domain_status import WaapDomainStatus

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    ids: Iterable[int]
    """Filter domains based on their IDs"""

    limit: int
    """Number of items to return"""

    name: str
    """Filter domains based on the domain name. Supports '\\**' as a wildcard character"""

    offset: int
    """Number of items to skip"""

    ordering: Literal["id", "name", "status", "created_at", "-id", "-name", "-status", "-created_at"]
    """Sort the response by given field."""

    status: WaapDomainStatus
    """The different statuses a domain can have"""
