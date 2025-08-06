# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["CustomRuleListParams"]


class CustomRuleListParams(TypedDict, total=False):
    action: Literal["allow", "block", "captcha", "handshake", "monitor", "tag"]
    """Filter to refine results by specific actions"""

    description: str
    """Filter rules based on their description. Supports '\\**' as a wildcard character."""

    enabled: bool
    """Filter rules based on their active status"""

    limit: int
    """Number of items to return"""

    name: str
    """Filter rules based on their name. Supports '\\**' as a wildcard character."""

    offset: int
    """Number of items to skip"""

    ordering: Optional[
        Literal["id", "name", "description", "enabled", "action", "-id", "-name", "-description", "-enabled", "-action"]
    ]
    """Determine the field to order results by"""
