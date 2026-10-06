# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["IPReputationClearLocalTagsParams", "Item"]


class IPReputationClearLocalTagsParams(TypedDict, total=False):
    items: Required[Iterable[Item]]


class Item(TypedDict, total=False):
    """Request model for deleting local IP tags."""

    domain_id: Required[int]
    """The domain ID to delete tags for"""

    ip: Required[str]
    """The IP address to delete tags for"""
