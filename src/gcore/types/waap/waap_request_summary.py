# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapRequestSummary", "PolicyOverride"]


class PolicyOverride(BaseModel):
    """An override that applied to a request, with its match metadata."""

    id: int
    """ID of the policy override applied to this request."""

    matched: Dict[str, object]
    """Match evidence keyed by target reference, such as 'ID861'.

    For legacy records, evidence is retained only for the first matched target;
    subsequent matched targets have empty objects.
    """

    t: Literal["waf_rule", "static_rule_template"]
    """
    Type of target affected by the override: 'waf_rule' for a detector or
    'static_rule_template' for a rule.
    """


class WaapRequestSummary(BaseModel):
    """Request summary used when displaying a list of requests"""

    id: str
    """Request's unique id"""

    action: str
    """Action of the triggered rule"""

    client_ip: str
    """Client's IP address."""

    country: str
    """Country code"""

    decision: Literal["passed", "allowed", "monitored", "blocked", ""]
    """The decision made for processing the request through the WAAP."""

    domain: str
    """Domain name"""

    domain_id: int
    """Domain ID"""

    method: str
    """HTTP method"""

    optional_action: Literal["captcha", "challenge", ""]
    """An optional action that may be applied in addition to the primary decision."""

    organization: str
    """Organization"""

    path: str
    """Request path"""

    reference_id: str
    """The reference ID to a sanction that was given to a user."""

    request_time: int
    """The UNIX timestamp in ms of the date a set of traffic counters was recorded"""

    result: Literal["passed", "blocked", "suppressed", ""]

    rule_id: str
    """The ID of the triggered rule."""

    rule_name: str
    """Name of the triggered rule"""

    status_code: int
    """Status code for http request"""

    traffic_types: str
    """Comma separated list of traffic types."""

    user_agent: str
    """User agent"""

    user_agent_client: str
    """Client from parsed User agent header"""

    http_version: Optional[str] = None
    """HTTP version of request"""

    ja3: Optional[str] = None
    """
    JA3 TLS client fingerprint as a 32-character lowercase hexadecimal MD5 hash, or
    an empty string when the record has no JA3 value.
    """

    policy_override: Optional[List[PolicyOverride]] = None
    """Applied overrides with id, t, and matched metadata keyed by target ID.

    Does not replace the final decision.
    """

    scheme: Optional[str] = None
    """The URI scheme of the request that generated an event"""

    session_id: Optional[str] = None
    """The session ID associated with the request."""
