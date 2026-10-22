# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapEventSummary", "PolicyOverride"]


class PolicyOverride(BaseModel):
    """An override that applied to a request, with its match metadata."""

    id: int
    """ID of the policy override applied to this request."""

    matched: Dict[str, object]
    """
    Match evidence keyed by target reference: a detector ID such as 'ID861', or a
    rule ID such as '94'. A detector entry holds 'field' and 'pattern_found'. A rule
    entry holds the rule's metadata, such as 'action' and 'rule_name', and for a
    rule based on a detector result also that match's 'field' and 'pattern_found'.
    'pattern_found' is empty when the matched content is hidden. For legacy records,
    evidence is retained only for the first matched target; subsequent matched
    targets have empty objects.
    """

    t: Literal["waf_rule", "static_rule_template"]
    """
    Type of target affected by the override: 'waf_rule' for a detector or
    'static_rule_template' for a rule.
    """


class WaapEventSummary(BaseModel):
    """Event record summary used when displaying a list of events"""

    id: str
    """Request's unique id"""

    action: str
    """Action of the triggered rule"""

    client_ip: str
    """Client's IP address."""

    country: str
    """Country code"""

    decision: Literal["blocked", "monitored", "allowed", "passed", ""]
    """The decision made for processing the request through the WAAP.

    Empty when no decision was recorded.
    """

    domain: str
    """Domain name"""

    domain_id: int
    """Domain ID"""

    method: str
    """HTTP method"""

    optional_action: Literal["captcha", "challenge", ""]
    """An optional action that may be applied in addition to the primary decision.

    Empty when none applies.
    """

    path: str
    """Request path"""

    policy_override_allowed: bool
    """Whether a Policy Override can be created for this request."""

    request_time: int
    """The UNIX timestamp in ms of the date a set of traffic counters was recorded"""

    result: Literal["passed", "blocked", "suppressed", ""]
    """The result of a request"""

    rule_id: str
    """The ID of the triggered rule."""

    rule_name: str
    """Name of the triggered rule"""

    status_code: int
    """Status code for http request"""

    policy_override: Optional[List[PolicyOverride]] = None
    """Applied overrides with id, t, and matched metadata keyed by target ID.

    Does not replace the final decision.
    """

    scheme: Optional[str] = None
    """The URI scheme of the request that generated an event"""
