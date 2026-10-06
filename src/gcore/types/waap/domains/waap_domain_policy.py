# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WaapDomainPolicy"]


class WaapDomainPolicy(BaseModel):
    """Represents a configurable WAAP security rule, also known as a policy."""

    id: str
    """Unique identifier for the security rule"""

    action: Literal["Allow", "Block", "Captcha", "Gateway", "Handshake", "Monitor", "Composite"]
    """Specifies the action taken by the WAAP upon rule activation"""

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
