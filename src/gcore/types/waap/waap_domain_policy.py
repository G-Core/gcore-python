# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .waap_policy_action import WaapPolicyAction

__all__ = ["WaapDomainPolicy"]


class WaapDomainPolicy(BaseModel):
    id: str
    """Unique identifier for the security rule"""

    action: WaapPolicyAction
    """The action taken by the WAAP upon rule activation."""

    description: str
    """Detailed description of the security rule"""

    group: str
    """The rule set group name to which the rule belongs"""

    mode: bool
    """Indicates if the security rule is active"""

    name: str
    """Name of the security rule"""

    rule_set_id: int
    """Identifier of the rule set to which the rule belongs"""
