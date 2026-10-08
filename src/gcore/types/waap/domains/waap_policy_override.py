# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "WaapPolicyOverride",
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
    "Target",
    "TargetSnapshot",
]


class ConditionCountry(BaseModel):
    """Match the country that the request originated from"""

    country_code: List[str]
    """
    A list of ISO 3166-1 alpha-2 formatted strings representing the countries to
    match against
    """

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHeader(BaseModel):
    """Match an incoming request header"""

    header: str
    """The request header name"""

    value: str
    """The request header value"""

    match_type: Optional[Literal["Exact", "Contains"]] = None
    """The type of matching condition for header and value."""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHeaderExists(BaseModel):
    """Match when an incoming request header is present"""

    header: str
    """The request header name"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionHTTPMethod(BaseModel):
    """Match the incoming HTTP method"""

    http_method: Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]
    """HTTP methods of a request"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


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


class ConditionJa3(BaseModel):
    """Match the JA3 TLS client fingerprint of the request"""

    ja3_fingerprints: List[str]
    """A list of JA3 TLS client fingerprints to match against the request"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionJa4(BaseModel):
    """Match the JA4 TLS client fingerprint of the request"""

    ja4_fingerprints: List[str]
    """A list of JA4 TLS client fingerprints to match against the request"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionOrganization(BaseModel):
    """
    Match the organization the request originated from, as determined by a WHOIS lookup of the requesting IP
    """

    organization: str
    """The organization to match against"""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionURL(BaseModel):
    """Match the incoming request URL"""

    url: str
    """
    The pattern to match against the request URL. Constraints depend on
    `match_type`:

    - **Exact/Contains**: plain text matching (e.g., `/admin`, must comply with
      `^[\\ww!\\$$~:#\\[[\\]]@\\((\\))*\\++,=\\//\\--\\..\\%%]+$`).
    - **Regex**: a valid regular expression (e.g., `^/upload(/\\dd+)?/\\ww+`).
      Lookahead/lookbehind constructs are forbidden.
    """

    match_type: Optional[Literal["Exact", "Contains", "Regex"]] = None
    """The type of matching condition."""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class ConditionUserAgent(BaseModel):
    """Match the user agent making the request"""

    user_agent: str
    """The user agent value to match"""

    match_type: Optional[Literal["Exact", "Contains"]] = None
    """The type of matching condition."""

    negation: Optional[bool] = None
    """Whether or not to apply a boolean NOT operation to the rule's condition"""


class Condition(BaseModel):
    """A single policy override condition. Only one of the fields below may be set.

    Limited to the subset of `CustomRuleConditionScope` scopes that policy overrides
    support (Lime wire-format translation is reused from Custom Rules' own
    `app.models.customer_rules.lime_translation.ConditionMapper`).
    """

    country: Optional[ConditionCountry] = None
    """Match the country that the request originated from"""

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

    ja3: Optional[ConditionJa3] = None
    """Match the JA3 TLS client fingerprint of the request"""

    ja4: Optional[ConditionJa4] = None
    """Match the JA4 TLS client fingerprint of the request"""

    organization: Optional[ConditionOrganization] = None
    """
    Match the organization the request originated from, as determined by a WHOIS
    lookup of the requesting IP
    """

    url: Optional[ConditionURL] = None
    """Match the incoming request URL"""

    user_agent: Optional[ConditionUserAgent] = None
    """Match the user agent making the request"""


class TargetSnapshot(BaseModel):
    """
    A point-in-time record of the target's details, retained for display after the linked object is deleted
    """

    name: str
    """The target's display name when it was linked"""

    action: Optional[str] = None
    """The action the target took when it triggered, if `target_type` is rule"""

    attack_type: Optional[str] = None
    """The attack category the target detected, if `target_type` is rule"""

    category: Optional[str] = None
    """The target's rule category (policy or template), if `target_type` is rule"""


class Target(BaseModel):
    id: int
    """The policy override target's ID"""

    ref: str
    """The stable reference edge uses to match this target"""

    snapshot: TargetSnapshot
    """
    A point-in-time record of the target's details, retained for display after the
    linked object is deleted
    """

    detector_id: Optional[int] = None
    """The linked detector's ID, if `target_type` is detector"""

    rule_id: Optional[int] = None
    """The linked rule's ID, if `target_type` is rule"""


class WaapPolicyOverride(BaseModel):
    id: int
    """The policy override's ID"""

    conditions: List[Condition]
    """The conditions required for the override to apply.

    Empty means the override applies to every request on the owning domain that hits
    a linked target.
    """

    created_at: datetime
    """When the override was created"""

    domain_id: int
    """The domain this override belongs to"""

    enabled: bool
    """Whether the override is active"""

    name: str
    """The policy override's display name"""

    stale: bool
    """Whether a linked target has been deleted, disabled, or otherwise become invalid.

    A stale override is not published and does not suppress anything until it's
    edited.
    """

    target_type: Literal["detector", "rule"]
    """Whether targets are detectors or rules"""

    targets: List[Target]
    """The detectors or rules this override suppresses"""

    updated_at: datetime
    """When the override was last updated"""

    description: Optional[str] = None
    """An optional note explaining the override"""
