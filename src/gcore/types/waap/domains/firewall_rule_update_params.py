# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FirewallRuleUpdateParams", "Action", "ActionBlock", "Condition", "ConditionIP", "ConditionIPRange"]


class FirewallRuleUpdateParams(TypedDict, total=False):
    domain_id: Required[int]
    """The domain ID"""

    action: Optional[Action]
    """The action that a firewall rule takes when triggered"""

    conditions: Optional[Iterable[Condition]]
    """The condition required for the WAAP engine to trigger the rule."""

    description: Optional[str]
    """The description assigned to the rule"""

    enabled: Optional[bool]
    """Whether or not the rule is enabled"""

    name: Optional[str]
    """The name assigned to the rule"""


class ActionBlock(TypedDict, total=False):
    action_duration: Optional[str]
    """How long a rule's block action will apply to subsequent requests.

    Can be specified in seconds or by using a numeral followed by 's', 'm', 'h', or
    'd' to represent time format (seconds, minutes, hours, or days)
    """

    status_code: Optional[Literal[403, 405, 418, 429]]
    """Designates the HTTP status code to deliver when a request is blocked."""


class Action(TypedDict, total=False):
    allow: Optional[object]
    """The WAAP allowed the request"""

    block: Optional[ActionBlock]
    """
    WAAP block action behavior could be configured with response status code and
    action duration.
    """


class ConditionIP(TypedDict, total=False):
    ip_address: Required[str]
    """A single IPv4 or IPv6 address"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionIPRange(TypedDict, total=False):
    lower_bound: Required[str]
    """The lower bound IPv4 or IPv6 address to match against"""

    upper_bound: Required[str]
    """The upper bound IPv4 or IPv6 address to match against"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class Condition(TypedDict, total=False):
    ip: Optional[ConditionIP]
    """Match the incoming request against a single IP address"""

    ip_range: Optional[ConditionIPRange]
    """Match the incoming request against an IP range"""
