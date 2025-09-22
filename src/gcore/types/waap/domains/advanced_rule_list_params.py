# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AdvancedRuleListParams"]


class AdvancedRuleListParams(TypedDict, total=False):
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
        Literal[
            "id",
            "name",
            "description",
            "enabled",
            "action",
            "phase",
            "-id",
            "-name",
            "-description",
            "-enabled",
            "-action",
            "-phase",
        ]
    ]
    """Determine the field to order results by"""

    phase: Literal["access", "header_filter", "body_filter"]
    """Filter rules based on the WAAP request/response phase for applying the rule.

    The "access" phase is responsible for modifying the request before it is sent to
    the origin server.

    The "`header_filter`" phase is responsible for modifying the HTTP headers of a
    response before they are sent back to the client.

    The "`body_filter`" phase is responsible for modifying the body of a response
    before it is sent back to the client.
    """
