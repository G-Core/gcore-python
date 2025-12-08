# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapRuleSet", "Tag", "Rule"]


class Tag(BaseModel):
    """A single tag associated with a rule set."""

    id: int
    """Identifier of the tag."""

    description: str
    """Detailed description of the tag."""

    name: str
    """Name of the tag."""


class Rule(BaseModel):
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


class WaapRuleSet(BaseModel):
    """Represents a custom rule set."""

    id: int
    """Identifier of the rule set."""

    description: str
    """Detailed description of the rule set."""

    is_active: bool
    """Indicates if the rule set is currently active."""

    name: str
    """Name of the rule set."""

    tags: List[Tag]
    """Collection of tags associated with the rule set."""

    resource_slug: Optional[str] = None
    """The resource slug associated with the rule set."""

    rules: Optional[List[Rule]] = None
