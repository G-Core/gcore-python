# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapAccountFirewallRule", "Action", "ActionBlock", "Condition", "ConditionIP", "ConditionIPRange", "Domain"]


class ActionBlock(BaseModel):
    """
    WAAP block action behavior could be configured with response status code and action duration.
    """

    action_duration: Optional[str] = None
    """How long a rule's block action will apply to subsequent requests.

    Can be specified in seconds or by using a numeral followed by 's', 'm', 'h', or
    'd' to represent time format (seconds, minutes, hours, or days). Empty time
    intervals are not allowed.
    """

    status_code: Optional[Literal[403, 405, 418, 429]] = None
    """A custom HTTP status code that the WAAP returns if a rule blocks a request"""


class Action(BaseModel):
    """The action that the rule takes when triggered"""

    allow: Optional[Dict[str, object]] = None
    """The WAAP allows the request"""

    block: Optional[ActionBlock] = None
    """
    WAAP block action behavior could be configured with response status code and
    action duration.
    """


class ConditionIP(BaseModel):
    """Match the incoming request against a single IP address"""

    ip_address: str
    """A single IPv4 or IPv6 address"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionIPRange(BaseModel):
    """Match the incoming request against an IP range"""

    lower_bound: str
    """The lower bound IPv4 or IPv6 address to match against"""

    upper_bound: str
    """The upper bound IPv4 or IPv6 address to match against"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class Condition(BaseModel):
    """
    The criteria of an incoming web request and the models of the various values those criteria can take
    """

    ip: Optional[ConditionIP] = None
    """Match the incoming request against a single IP address"""

    ip_range: Optional[ConditionIPRange] = None
    """Match the incoming request against an IP range"""


class Domain(BaseModel):
    """The domain this firewall rule belongs to"""

    id: int
    """The domain ID"""

    name: str
    """The domain name"""


class WaapAccountFirewallRule(BaseModel):
    """Firewall rule response for account-level queries with domain information"""

    id: int
    """The unique identifier of the rule"""

    action: Action
    """The action that the rule takes when triggered"""

    conditions: List[Condition]
    """The condition required for the WAAP engine to trigger the rule."""

    domain: Domain
    """The domain this firewall rule belongs to"""

    enabled: bool
    """Whether or not the rule is enabled"""

    name: str
    """The name assigned to the rule"""

    description: Optional[str] = None
    """The description assigned to the rule"""
