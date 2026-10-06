# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["WaapOwaspTopThreatsTarget", "Policy"]


class Policy(BaseModel):
    """The parent policy this rule is grouped under, if any"""

    id: int
    """The parent policy's ID"""

    name: str
    """The parent policy's name"""


class WaapOwaspTopThreatsTarget(BaseModel):
    """
    A default OWASP Top Threats target that can be selected as the target of a
    policy override, so this specific managed detection stops blocking matching
    traffic while the rest of OWASP Top Threats protection stays unchanged.
    """

    id: int
    """The rule's ID; use this as a `target_id` when creating a policy override"""

    action: str
    """The action this rule takes when it triggers"""

    name: str
    """The rule's display name"""

    policy: Optional[Policy] = None
    """The parent policy this rule is grouped under, if any"""
