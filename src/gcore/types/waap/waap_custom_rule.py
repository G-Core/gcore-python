# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "WaapCustomRule",
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


class ActionBlock(BaseModel):
    action_duration: Optional[str] = None
    """How long a rule's block action will apply to subsequent requests.

    Can be specified in seconds or by using a numeral followed by 's', 'm', 'h', or
    'd' to represent time format (seconds, minutes, hours, or days)
    """

    status_code: Optional[Literal[403, 405, 418, 429]] = None
    """Designates the HTTP status code to deliver when a request is blocked."""


class ActionTag(BaseModel):
    tags: List[str]
    """The list of user defined tags to tag the request with"""


class Action(BaseModel):
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


class ConditionContentType(BaseModel):
    content_type: List[str]
    """The list of content types to match against"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionCountry(BaseModel):
    country_code: List[str]
    """
    A list of ISO 3166-1 alpha-2 formatted strings representing the countries to
    match against
    """

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionFileExtension(BaseModel):
    file_extension: List[str]
    """The list of file extensions to match against"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHeader(BaseModel):
    header: str
    """The request header name"""

    value: str
    """The request header value"""

    match_type: Optional[Literal["Exact", "Contains"]] = None
    """The type of matching condition for header and value."""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHeaderExists(BaseModel):
    header: str
    """The request header name"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHTTPMethod(BaseModel):
    http_method: Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]
    """HTTP methods and descriptions Methods from the following RFCs are all observed:

    - RFC 7231: Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616
    - RFC 5789: PATCH Method for HTTP
    """

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


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


class ConditionOrganization(BaseModel):
    organization: str
    """The organization to match against"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionOwnerTypes(BaseModel):
    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""

    owner_types: Optional[
        List[
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
    ] = None
    """
    Match the type of organization that owns the IP address making an incoming
    request
    """


class ConditionRequestRate(BaseModel):
    path_pattern: str
    """A regular expression matching the URL path of the incoming request"""

    requests: int
    """
    The number of incoming requests over the given time that can trigger a request
    rate condition
    """

    time: int
    """
    The number of seconds that the WAAP measures incoming requests over before
    triggering a request rate condition
    """

    http_methods: Optional[
        List[Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
    ] = None
    """Possible HTTP request methods that can trigger a request rate condition"""

    ips: Optional[List[str]] = None
    """A list of source IPs that can trigger a request rate condition"""

    user_defined_tag: Optional[str] = None
    """
    A user-defined tag that can be included in incoming requests and used to trigger
    a request rate condition
    """


class ConditionResponseHeader(BaseModel):
    header: str
    """The response header name"""

    value: str
    """The response header value"""

    match_type: Optional[Literal["Exact", "Contains"]] = None
    """The type of matching condition for header and value."""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionResponseHeaderExists(BaseModel):
    header: str
    """The response header name"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionSessionRequestCount(BaseModel):
    request_count: int
    """The number of dynamic requests in the session"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionTags(BaseModel):
    tags: List[str]
    """A list of tags to match against the request tags"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionURL(BaseModel):
    url: str
    """
    The pattern to match against the request URL. Constraints depend on
    `match_type`:

    - **Exact/Contains**: plain text matching (e.g., `/admin`).
    - **Regex**: a valid regular expression (must comply with
      `^[\\ww!\\$$~:#\\[[\\]]@\\((\\))\\*\\++,=\\//\\--\\..\\%%]+$`). Lookahead/lookbehind constructs are
      forbidden.
    """

    match_type: Optional[Literal["Exact", "Contains", "Regex"]] = None
    """The type of matching condition."""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionUserAgent(BaseModel):
    user_agent: str
    """The user agent value to match"""

    match_type: Optional[Literal["Exact", "Contains"]] = None
    """The type of matching condition."""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionUserDefinedTags(BaseModel):
    tags: List[str]
    """A list of user-defined tags to match against the request tags"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class Condition(BaseModel):
    content_type: Optional[ConditionContentType] = None
    """Match the requested Content-Type"""

    country: Optional[ConditionCountry] = None
    """Match the country that the request originated from"""

    file_extension: Optional[ConditionFileExtension] = None
    """Match the incoming file extension"""

    header: Optional[ConditionHeader] = None
    """Match an incoming request header"""

    header_exists: Optional[ConditionHeaderExists] = None
    """Match when an incoming request header is present"""

    http_method: Optional[ConditionHTTPMethod] = None
    """Match the incoming HTTP method"""

    ip: Optional[ConditionIP] = None
    """Match the incoming request against a single IP address"""

    ip_range: Optional[ConditionIPRange] = None
    """Match the incoming request against an IP range"""

    organization: Optional[ConditionOrganization] = None
    """
    Match the organization the request originated from, as determined by a WHOIS
    lookup of the requesting IP
    """

    owner_types: Optional[ConditionOwnerTypes] = None
    """
    Match the type of organization that owns the IP address making an incoming
    request
    """

    request_rate: Optional[ConditionRequestRate] = None
    """Match the rate at which requests come in that match certain conditions"""

    response_header: Optional[ConditionResponseHeader] = None
    """Match a response header"""

    response_header_exists: Optional[ConditionResponseHeaderExists] = None
    """Match when a response header is present"""

    session_request_count: Optional[ConditionSessionRequestCount] = None
    """Match the number of dynamic page requests made in a WAAP session"""

    tags: Optional[ConditionTags] = None
    """Matches requests based on specified tags"""

    url: Optional[ConditionURL] = None
    """Match the incoming request URL"""

    user_agent: Optional[ConditionUserAgent] = None
    """Match the user agent making the request"""

    user_defined_tags: Optional[ConditionUserDefinedTags] = None
    """Matches requests based on user-defined tags"""


class WaapCustomRule(BaseModel):
    id: int
    """The unique identifier for the rule"""

    action: Action
    """The action that a WAAP rule takes when triggered"""

    conditions: List[Condition]
    """The conditions required for the WAAP engine to trigger the rule.

    Rules may have between 1 and 5 conditions. All conditions must pass for the rule
    to trigger
    """

    enabled: bool
    """Whether or not the rule is enabled"""

    name: str
    """The name assigned to the rule"""

    description: Optional[str] = None
    """The description assigned to the rule"""
