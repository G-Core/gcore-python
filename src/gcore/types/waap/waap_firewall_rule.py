# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapFirewallRule", "Action", "ActionBlock", "Condition", "ConditionIP", "ConditionIPRange"]


class ActionBlock(BaseModel):
    action_duration: Optional[str] = None
    """How long a rule's block action will apply to subsequent requests.

    Can be specified in seconds or by using a numeral followed by 's', 'm', 'h', or
    'd' to represent time format (seconds, minutes, hours, or days)
    """

    status_code: Optional[Literal[403, 405, 418, 429]] = None
    """Designates the HTTP status code to deliver when a request is blocked."""


class Action(BaseModel):
    allow: Optional[object] = None
    """The WAAP allowed the request"""

    block: Optional[ActionBlock] = None
    """
    WAAP block action behavior could be configured with response status code and
    action duration.
    """


class ConditionIP(BaseModel):
    ip_address: str
    """A single IPv4 or IPv6 address"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionIPRange(BaseModel):
    lower_bound: str
    """The lower bound IPv4 or IPv6 address to match against"""

    upper_bound: str
    """The upper bound IPv4 or IPv6 address to match against"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class Condition(BaseModel):
    ip: Optional[ConditionIP] = None
    """Match the incoming request against a single IP address"""

    ip_range: Optional[ConditionIPRange] = None
    """Match the incoming request against an IP range"""


class WaapFirewallRule(BaseModel):
    id: int
    """The unique identifier of the rule"""

    action: Action
    """The action that a firewall rule takes when triggered"""

    conditions: List[Condition]
    """The condition required for the WAAP engine to trigger the rule."""

    enabled: bool
    """Whether or not the rule is enabled"""

    name: str
    """The name assigned to the rule"""

    description: Optional[str] = None
    """The description assigned to the rule"""
