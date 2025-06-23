# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CustomRuleUpdateParams",
    "Action",
    "ActionBlock",
    "ActionTag",
    "Condition",
    "ConditionContentType",
    "ConditionCountry",
    "ConditionFileExtension",
    "ConditionHeader",
    "ConditionHeaderExists",
    "ConditionHTTPMethod",
    "ConditionIP",
    "ConditionIPRange",
    "ConditionOrganization",
    "ConditionOwnerTypes",
    "ConditionRequestRate",
    "ConditionResponseHeader",
    "ConditionResponseHeaderExists",
    "ConditionSessionRequestCount",
    "ConditionTags",
    "ConditionURL",
    "ConditionUserAgent",
    "ConditionUserDefinedTags",
]


class CustomRuleUpdateParams(TypedDict, total=False):
    domain_id: Required[int]
    """The domain ID"""

    action: Optional[Action]
    """The action that a WAAP rule takes when triggered"""

    conditions: Optional[Iterable[Condition]]
    """The conditions required for the WAAP engine to trigger the rule.

    Rules may have between 1 and 5 conditions. All conditions must pass for the rule
    to trigger
    """

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


class ConditionContentType(TypedDict, total=False):
    content_type: Required[List[str]]
    """The list of content types to match against"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionCountry(TypedDict, total=False):
    country_code: Required[List[str]]
    """
    A list of ISO 3166-1 alpha-2 formatted strings representing the countries to
    match against
    """

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionFileExtension(TypedDict, total=False):
    file_extension: Required[List[str]]
    """The list of file extensions to match against"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHeader(TypedDict, total=False):
    header: Required[str]
    """The request header name"""

    value: Required[str]
    """The request header value"""

    match_type: Literal["Exact", "Contains"]
    """The type of matching condition for header and value."""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHeaderExists(TypedDict, total=False):
    header: Required[str]
    """The request header name"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHTTPMethod(TypedDict, total=False):
    http_method: Required[Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
    """HTTP methods and descriptions Methods from the following RFCs are all observed:

    - RFC 7231: Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616
    - RFC 5789: PATCH Method for HTTP
    """

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


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


class ConditionOrganization(TypedDict, total=False):
    organization: Required[str]
    """The organization to match against"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionOwnerTypes(TypedDict, total=False):
    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""

    owner_types: List[
        Literal[
            "COMMERCIAL",
            "EDUCATIONAL",
            "GOVERNMENT",
            "HOSTING_SERVICES",
            "ISP",
            "MOBILE_NETWORK",
            "NETWORK",
            "RESERVED",
        ]
    ]
    """
    Match the type of organization that owns the IP address making an incoming
    request
    """


class ConditionRequestRate(TypedDict, total=False):
    path_pattern: Required[str]
    """A regular expression matching the URL path of the incoming request"""

    requests: Required[int]
    """
    The number of incoming requests over the given time that can trigger a request
    rate condition
    """

    time: Required[int]
    """
    The number of seconds that the WAAP measures incoming requests over before
    triggering a request rate condition
    """

    http_methods: Optional[
        List[Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
    ]
    """Possible HTTP request methods that can trigger a request rate condition"""

    ips: Optional[List[str]]
    """A list of source IPs that can trigger a request rate condition"""

    user_defined_tag: Optional[str]
    """
    A user-defined tag that can be included in incoming requests and used to trigger
    a request rate condition
    """


class ConditionResponseHeader(TypedDict, total=False):
    header: Required[str]
    """The response header name"""

    value: Required[str]
    """The response header value"""

    match_type: Literal["Exact", "Contains"]
    """The type of matching condition for header and value."""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionResponseHeaderExists(TypedDict, total=False):
    header: Required[str]
    """The response header name"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionSessionRequestCount(TypedDict, total=False):
    request_count: Required[int]
    """The number of dynamic requests in the session"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionTags(TypedDict, total=False):
    tags: Required[List[str]]
    """A list of tags to match against the request tags"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionURL(TypedDict, total=False):
    url: Required[str]
    """
    The pattern to match against the request URL. Constraints depend on
    `match_type`:

    - **Exact/Contains**: plain text matching (e.g., `/admin`).
    - **Regex**: a valid regular expression (must comply with
      `^[\\ww!\\$$~:#\\[[\\]]@\\((\\))\\*\\++,=\\//\\--\\..\\%%]+$`). Lookahead/lookbehind constructs are
      forbidden.
    """

    match_type: Literal["Exact", "Contains", "Regex"]
    """The type of matching condition."""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionUserAgent(TypedDict, total=False):
    user_agent: Required[str]
    """The user agent value to match"""

    match_type: Literal["Exact", "Contains"]
    """The type of matching condition."""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionUserDefinedTags(TypedDict, total=False):
    tags: Required[List[str]]
    """A list of user-defined tags to match against the request tags"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class Condition(TypedDict, total=False):
    content_type: Optional[ConditionContentType]
    """Match the requested Content-Type"""

    country: Optional[ConditionCountry]
    """Match the country that the request originated from"""

    file_extension: Optional[ConditionFileExtension]
    """Match the incoming file extension"""

    header: Optional[ConditionHeader]
    """Match an incoming request header"""

    header_exists: Optional[ConditionHeaderExists]
    """Match when an incoming request header is present"""

    http_method: Optional[ConditionHTTPMethod]
    """Match the incoming HTTP method"""

    ip: Optional[ConditionIP]
    """Match the incoming request against a single IP address"""

    ip_range: Optional[ConditionIPRange]
    """Match the incoming request against an IP range"""

    organization: Optional[ConditionOrganization]
    """
    Match the organization the request originated from, as determined by a WHOIS
    lookup of the requesting IP
    """

    owner_types: Optional[ConditionOwnerTypes]
    """
    Match the type of organization that owns the IP address making an incoming
    request
    """

    request_rate: Optional[ConditionRequestRate]
    """Match the rate at which requests come in that match certain conditions"""

    response_header: Optional[ConditionResponseHeader]
    """Match a response header"""

    response_header_exists: Optional[ConditionResponseHeaderExists]
    """Match when a response header is present"""

    session_request_count: Optional[ConditionSessionRequestCount]
    """Match the number of dynamic page requests made in a WAAP session"""

    tags: Optional[ConditionTags]
    """Matches requests based on specified tags"""

    url: Optional[ConditionURL]
    """Match the incoming request URL"""

    user_agent: Optional[ConditionUserAgent]
    """Match the user agent making the request"""

    user_defined_tags: Optional[ConditionUserDefinedTags]
    """Matches requests based on user-defined tags"""
