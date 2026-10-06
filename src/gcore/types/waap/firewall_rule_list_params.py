# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FirewallRuleListParams"]


class FirewallRuleListParams(TypedDict, total=False):
    action: Literal["allow", "block"]
    """Filter by action type"""

    description: str
    """Filter rules by description (supports wildcards)"""

    domain_ids: Iterable[int]
    """Filter by domain IDs (can specify multiple)"""

    enabled: bool
    """Filter by enabled status"""

    limit: int
    """Number of items to return"""

    name: str
    """Filter rules by name (supports wildcards)"""

    offset: int
    """Number of items to skip"""

    ordering: Optional[
        Literal["id", "name", "description", "enabled", "action", "-id", "-name", "-description", "-enabled", "-action"]
    ]
    """Order results by field (prefix with - for descending)"""
