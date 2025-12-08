# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WaapAdvancedRule", "Action", "ActionBlock", "ActionTag"]


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


class ActionTag(BaseModel):
    """WAAP tag action gets a list of tags to tag the request scope with"""

    tags: List[str]
    """The list of user defined tags to tag the request with"""


class Action(BaseModel):
    """The action that the rule takes when triggered.

    Only one action can be set per rule.
    """

    allow: Optional[object] = None
    """The WAAP allowed the request"""

    block: Optional[ActionBlock] = None
    """
    WAAP block action behavior could be configured with response status code and
    action duration.
    """

    captcha: Optional[object] = None
    """The WAAP presented the user with a captcha"""

    handshake: Optional[object] = None
    """The WAAP performed automatic browser validation"""

    monitor: Optional[object] = None
    """The WAAP monitored the request but took no action"""

    tag: Optional[ActionTag] = None
    """WAAP tag action gets a list of tags to tag the request scope with"""


class WaapAdvancedRule(BaseModel):
    """An advanced WAAP rule applied to a domain"""

    id: int
    """The unique identifier for the rule"""

    action: Action
    """The action that the rule takes when triggered.

    Only one action can be set per rule.
    """

    enabled: bool
    """Whether or not the rule is enabled"""

    name: str
    """The name assigned to the rule"""

    source: str
    """A CEL syntax expression that contains the rule's conditions.

    Allowed objects are: request, whois, session, response, tags,
    `user_defined_tags`, `user_agent`, `client_data`.

    More info can be found here:
    https://gcore.com/docs/waap/waap-rules/advanced-rules
    """

    description: Optional[str] = None
    """The description assigned to the rule"""

    phase: Optional[Literal["access", "header_filter", "body_filter"]] = None
    """The WAAP request/response phase for applying the rule. Default is "access".

    The "access" phase is responsible for modifying the request before it is sent to
    the origin server.

    The "`header_filter`" phase is responsible for modifying the HTTP headers of a
    response before they are sent back to the client.

    The "`body_filter`" phase is responsible for modifying the body of a response
    before it is sent back to the client.
    """
