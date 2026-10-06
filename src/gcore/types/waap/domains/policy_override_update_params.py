# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "PolicyOverrideUpdateParams",
    "Condition",
    "ConditionCountry",
    "ConditionHeader",
    "ConditionHeaderExists",
    "ConditionHTTPMethod",
    "ConditionIP",
    "ConditionIPRange",
    "ConditionJa3",
    "ConditionJa4",
    "ConditionOrganization",
    "ConditionURL",
    "ConditionUserAgent",
]


class PolicyOverrideUpdateParams(TypedDict, total=False):
    domain_id: Required[int]
    """The domain ID"""

    conditions: Optional[Iterable[Condition]]
    """The conditions required for the override to apply.

    An override may have up to 5 conditions; all must pass for the override to
    apply. Without conditions the override applies to every request on the owning
    domain that hits a linked target.
    """

    description: Optional[str]
    """An optional note explaining the override"""

    enabled: Optional[bool]
    """Whether the override is active"""

    name: Optional[str]
    """The policy override's display name"""


class ConditionCountry(TypedDict, total=False):
    """Match the country that the request originated from"""

    country_code: Required[SequenceNotStr[str]]
    """
    A list of ISO 3166-1 alpha-2 formatted strings representing the countries to
    match against
    """

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHeader(TypedDict, total=False):
    """Match an incoming request header"""

    header: Required[str]
    """The request header name"""

    value: Required[str]
    """The request header value"""

    match_type: Literal["Exact", "Contains"]
    """The type of matching condition for header and value."""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHeaderExists(TypedDict, total=False):
    """Match when an incoming request header is present"""

    header: Required[str]
    """The request header name"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHTTPMethod(TypedDict, total=False):
    """Match the incoming HTTP method"""

    http_method: Required[Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]]
    """HTTP methods of a request"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionIP(TypedDict, total=False):
    """Match the incoming request against a single IP address"""

    ip_address: Required[str]
    """A single IPv4 or IPv6 address"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionIPRange(TypedDict, total=False):
    """Match the incoming request against an IP range"""

    lower_bound: Required[str]
    """The lower bound IPv4 or IPv6 address to match against"""

    upper_bound: Required[str]
    """The upper bound IPv4 or IPv6 address to match against"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionJa3(TypedDict, total=False):
    """Match the JA3 TLS client fingerprint of the request"""

    ja3_fingerprints: Required[SequenceNotStr[str]]
    """A list of JA3 TLS client fingerprints to match against the request"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionJa4(TypedDict, total=False):
    """Match the JA4 TLS client fingerprint of the request"""

    ja4_fingerprints: Required[SequenceNotStr[str]]
    """A list of JA4 TLS client fingerprints to match against the request"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionOrganization(TypedDict, total=False):
    """
    Match the organization the request originated from, as determined by a WHOIS lookup of the requesting IP
    """

    organization: Required[str]
    """The organization to match against"""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionURL(TypedDict, total=False):
    """Match the incoming request URL"""

    url: Required[str]
    """
    The pattern to match against the request URL. Constraints depend on
    `match_type`:

    - **Exact/Contains**: plain text matching (e.g., `/admin`, must comply with
      `^[\\ww!\\$$~:#\\[[\\]]@\\((\\))*\\++,=\\//\\--\\..\\%%]+$`).
    - **Regex**: a valid regular expression (e.g., `^/upload(/\\dd+)?/\\ww+`).
      Lookahead/lookbehind constructs are forbidden.
    """

    match_type: Literal["Exact", "Contains", "Regex"]
    """The type of matching condition."""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionUserAgent(TypedDict, total=False):
    """Match the user agent making the request"""

    user_agent: Required[str]
    """The user agent value to match"""

    match_type: Literal["Exact", "Contains"]
    """The type of matching condition."""

    negation: bool
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class Condition(TypedDict, total=False):
    """A single policy override condition. Only one of the fields below may be set.

    Limited to the subset of `CustomRuleConditionScope` scopes that policy overrides
    support (Lime wire-format translation is reused from Custom Rules' own
    `app.models.customer_rules.lime_translation.ConditionMapper`).
    """

    country: ConditionCountry
    """Match the country that the request originated from"""

    header: ConditionHeader
    """Match an incoming request header"""

    header_exists: ConditionHeaderExists
    """Match when an incoming request header is present"""

    http_method: ConditionHTTPMethod
    """Match the incoming HTTP method"""

    ip: ConditionIP
    """Match the incoming request against a single IP address"""

    ip_range: ConditionIPRange
    """Match the incoming request against an IP range"""

    ja3: ConditionJa3
    """Match the JA3 TLS client fingerprint of the request"""

    ja4: ConditionJa4
    """Match the JA4 TLS client fingerprint of the request"""

    organization: ConditionOrganization
    """
    Match the organization the request originated from, as determined by a WHOIS
    lookup of the requesting IP
    """

    url: ConditionURL
    """Match the incoming request URL"""

    user_agent: ConditionUserAgent
    """Match the user agent making the request"""
