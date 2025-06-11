# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AdvancedRuleCreateParams", "Action", "ActionBlock", "ActionTag"]


class AdvancedRuleCreateParams(TypedDict, total=False):
    action: Required[Action]
    """The action that a WAAP rule takes when triggered"""

    enabled: Required[bool]
    """Whether or not the rule is enabled"""

    name: Required[str]
    """The name assigned to the rule"""

    source: Required[str]
    """A CEL syntax expression that contains the rule's conditions.

    Allowed objects are: request, whois, session, response, tags,
    `user_defined_tags`, `user_agent`, `client_data`. More info can be found here:
    https://gcore.com/docs/waap/waap-rules/advanced-rules
    """

    description: Optional[str]
    """The description assigned to the rule"""

    phase: Optional[Literal["access", "header_filter", "body_filter"]]
    """The WAAP request/response phase for applying the rule.

    Default is "access". The "access" phase is responsible for modifying the request
    before it is sent to the origin server. The "`header_filter`" phase is
    responsible for modifying the HTTP headers of a response before they are sent
    back to the client. The "`body_filter`" phase is responsible for modifying the
    body of a response before it is sent back to the client.
    """


class ActionBlock(TypedDict, total=False):
    action_duration: Optional[str]
    """How long a rule's block action will apply to subsequent requests.

    Can be specified in seconds or by using a numeral followed by 's', 'm', 'h', or
    'd' to represent time format (seconds, minutes, hours, or days)
    """

    status_code: Optional[Literal[403, 405, 418, 429]]
    """Designates the HTTP status code to deliver when a request is blocked."""


class ActionTag(TypedDict, total=False):
    tags: Required[List[str]]
    """The list of user defined tags to tag the request with"""


class Action(TypedDict, total=False):
    allow: Optional[object]
    """The WAAP allowed the request"""

    block: Optional[ActionBlock]
    """
    WAAP block action behavior could be configured with response status code and
    action duration.
    """

    captcha: Optional[object]
    """The WAAP presented the user with a captcha"""

    handshake: Optional[object]
    """The WAAP performed automatic browser validation"""

    monitor: Optional[object]
    """The WAAP monitored the request but took no action"""

    tag: Optional[ActionTag]
    """WAAP tag action gets a list of tags to tag the request scope with"""
